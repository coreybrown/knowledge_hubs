
/* IPA Knowledge Base — interactivity */
(function(){
  "use strict";
  var root=document.documentElement;

  /* theme */
  var saved=localStorage.getItem("ipa-theme");
  if(saved)root.setAttribute("data-theme",saved);
  var tg=document.getElementById("themeToggle");
  if(tg)tg.addEventListener("click",function(){
    var next=root.getAttribute("data-theme")==="dark"?"light":"dark";
    root.setAttribute("data-theme",next);
    localStorage.setItem("ipa-theme",next);
  });

  /* mobile drawer */
  var mt=document.getElementById("menuToggle"),
      scrim=document.getElementById("scrim");
  function closeNav(){document.body.classList.remove("nav-open");}
  if(mt)mt.addEventListener("click",function(){
    document.body.classList.toggle("nav-open");});
  if(scrim)scrim.addEventListener("click",closeNav);

  /* ---- search + ask ---- */
  var modal=document.getElementById("searchModal"),
      input=document.getElementById("searchInput"),
      results=document.getElementById("searchResults"),
      panel=document.getElementById("askPanel"),
      openBtn=document.getElementById("searchOpen"),
      DATA=window.SEARCH_INDEX||[],sel=-1,rows=[],asking=false;

  /* Preview by default (local stub: real keyword retrieval + simulated stream).
     Append ?ask=live to any page URL to exercise the real /api/ask backend;
     change this to `true` to enable the live backend for everyone. The UI
     (streaming, sources, states) is identical either way.
     Dev: type ":resting" or ":error" as the question to preview those states. */
  var ASK_ENABLED=(location.search.indexOf("ask=live")>=0);
  var ASK_TOPIC="IPAs";
  var ASK_GUIDE="ipas";
  var ASK_EG=["What sets a West Coast IPA apart from a hazy one?",
              "Why do IPAs go stale so fast?",
              "Which hops give citrus and tropical aromas?"];

  function openSearch(){
    if(!modal)return;
    modal.hidden=false;input.value="";resetAsk();render("");
    setTimeout(function(){input.focus();},30);
  }
  function closeSearch(){if(modal)modal.hidden=true;}
  function resetAsk(){asking=false;if(panel){panel.hidden=true;panel.innerHTML="";}}
  function esc(s){return s.replace(/[&<>]/g,function(c){
    return{"&":"&amp;","<":"&lt;",">":"&gt;"}[c];});}
  function hl(text,q){
    if(!q)return esc(text);
    var i=text.toLowerCase().indexOf(q.toLowerCase());
    if(i<0)return esc(text);
    return esc(text.slice(0,i))+"<b>"+esc(text.slice(i,i+q.length))+
      "</b>"+esc(text.slice(i+q.length));
  }
  var ASK_STOP={the:1,a:1,an:1,is:1,are:1,of:1,for:1,to:1,and:1,or:1,in:1,on:1,
    with:1,vs:1,it:1,this:1,that:1,can:1,should:1,do:1,does:1,did:1,my:1,me:1,
    i:1,you:1,what:1,whats:1,how:1,why:1,when:1,which:1,who:1,was:1,be:1};
  function askTokens(q){
    return q.toLowerCase().split(/[^a-z0-9]+/).filter(function(t){
      return t.length>2 && !ASK_STOP[t];});
  }
  function score(p,q){
    q=(q||"").trim().toLowerCase();if(!q)return 0;
    var t=p.t.toLowerCase(),k=(p.k||"").toLowerCase(),s=(p.s||"").toLowerCase();
    if(t===q)return 1000;
    if(t.indexOf(q)===0)return 200;
    var toks=askTokens(q);
    if(!toks.length){            // 1–2 char query: whole-string fallback
      if(t.indexOf(q)>=0)return 60;
      if(k.indexOf(q)>=0)return 40;
      if(s.indexOf(q)>=0)return 20;
      return 0;
    }
    var sc=0;                    // multi-term: sum per-token field hits
    toks.forEach(function(w){
      if(t.indexOf(w)>=0)sc+=6;
      else if(k.indexOf(w)>=0)sc+=3;
      else if(s.indexOf(w)>=0)sc+=1;
    });
    return sc;
  }
  function topMatches(q,n){
    q=(q||"").trim().toLowerCase();if(!q)return [];
    var m=[];DATA.forEach(function(p){var sc=score(p,q);if(sc>0)m.push([sc,p]);});
    m.sort(function(a,b){return b[0]-a[0];});
    return m.slice(0,n).map(function(x){return x[1];});
  }
  function srcCard(p){
    return '<a class="sr-item" href="'+p.u+'" style="--src:'+p.c+'">'+
      '<span class="sr-ic">'+p.i+'</span>'+
      '<span class="sr-main"><span class="sr-title">'+esc(p.t)+'</span>'+
      '<span class="sr-meta">'+esc(p.d)+'</span></span></a>';
  }
  function chipsHTML(){
    return '<div class="ask-chips">'+ASK_EG.map(function(q){
      return '<button type="button" class="ask-chip" data-q="'+esc(q)+'">'+
        esc(q)+'</button>';}).join("")+'</div>';
  }
  function render(q){
    q=q.trim().toLowerCase();sel=-1;
    if(!q){
      results.innerHTML='<div class="sr-intro"><div class="sr-intro-h">'+
        'Ask anything about '+esc(ASK_TOPIC)+'</div><div class="sr-intro-p">'+
        'Get a short, sourced answer drawn from the guide — or keep typing to '+
        'jump straight to a note.</div>'+chipsHTML()+'</div>'+hint();
      rows=[];bindChips();return;
    }
    var matched=[];
    DATA.forEach(function(p){var sc=score(p,q);if(sc>0)matched.push([sc,p]);});
    matched.sort(function(a,b){return b[0]-a[0];});
    matched=matched.slice(0,24);
    if(!matched.length){
      results.innerHTML='<div class="sr-empty">No notes match “'+esc(q)+
        '”. Press <kbd>&crarr;</kbd> to ask instead.</div>';rows=[];return;
    }
    results.innerHTML='<div class="sr-jump">Jump to a note</div>'+
      matched.map(function(m){
      var p=m[1];
      return '<a class="sr-item" href="'+p.u+'" style="--src:'+p.c+'">'+
        '<span class="sr-ic">'+p.i+'</span>'+
        '<span class="sr-main"><span class="sr-title">'+hl(p.t,q)+
        '</span><span class="sr-meta">'+esc(p.d)+'</span>'+
        '<span class="sr-snip">'+esc(p.s)+'</span></span></a>';
    }).join("")+hint();
    rows=Array.prototype.slice.call(results.querySelectorAll(".sr-item"));
  }
  function hint(){
    return '<div class="sr-hint"><span><kbd>&crarr;</kbd> ask</span>'+
      '<span><kbd>&uarr;</kbd><kbd>&darr;</kbd> browse</span>'+
      '<span><kbd>esc</kbd> close</span></div>';
  }
  function bindChips(){
    Array.prototype.slice.call(results.querySelectorAll(".ask-chip"))
      .forEach(function(b){b.addEventListener("click",function(){
        var q=b.getAttribute("data-q");input.value=q;render(q);ask(q);});});
  }
  function move(d){
    if(!rows.length)return;
    if(sel>=0)rows[sel].classList.remove("sel");
    sel=(sel+d+rows.length)%rows.length;
    rows[sel].classList.add("sel");
    rows[sel].scrollIntoView({block:"nearest"});
  }

  /* ---- ask flow (preview until /api/ask is live) ---- */
  function ask(q){
    q=(q||"").trim();if(!q||asking||!panel)return;
    asking=true;sel=-1;panel.hidden=false;
    if(!ASK_ENABLED&&q===":resting")return askState("resting");
    if(!ASK_ENABLED&&q===":error")return askState("error");
    var sources=topMatches(q,3);
    panel.innerHTML='<div class="ask-head"><span class="ask-eyebrow">Answer'+
      '</span>'+(ASK_ENABLED?'':'<span class="ask-badge">Preview</span>')+
      '</div><div class="ask-q">'+esc(q)+'</div>'+
      '<div class="ask-answer streaming" id="askAnswer"></div>'+
      '<div class="ask-sources" id="askSources"></div>';
    var ans=document.getElementById("askAnswer");
    render(q);   // refresh the "jump to a note" list under the answer
    if(ASK_ENABLED)streamReal(q,ans,sources);else streamMock(q,ans,sources);
  }
  function askState(kind){
    var msg=kind==="resting"
      ? "The assistant is resting — it’s reached today’s question limit. Keyword search still works below."
      : "Couldn’t reach the assistant just now. Try again, or use keyword search below.";
    panel.innerHTML='<div class="ask-note ask-note-'+kind+'">'+esc(msg)+'</div>';
    asking=false;
  }
  function renderSources(sources){
    var el=document.getElementById("askSources");
    if(!el||!sources.length)return;
    el.innerHTML='<div class="ask-src-label">Go deeper</div>'+
      sources.map(srcCard).join("");
  }
  function streamMock(q,ans,sources){
    var text;
    if(sources.length){
      var top=sources[0],snip=(top.s||"").trim();
      if(snip&&!/[.!?…]$/.test(snip))snip+="…";
      text="Here’s what the guide covers. The most relevant note is “"+top.t+"”"+
        (sources.length>1?", with more in “"+sources[1].t+"”":"")+". "+snip;
    }else{
      text="This guide doesn’t appear to cover that. Try rephrasing, or browse the notes below.";
    }
    typeOut(ans,text,function(){
      ans.classList.remove("streaming");renderSources(sources);
      if(!ASK_ENABLED){
        var s=document.getElementById("askSources");
        if(s&&s.parentNode){var f=document.createElement("div");
          f.className="ask-foot";
          f.textContent="Preview answer — live AI responses arrive once the backend is connected.";
          s.parentNode.insertBefore(f,s);}
      }
      asking=false;
    });
  }
  function typeOut(el,text,done){
    var w=text.split(/(\s+)/),i=0;el.textContent="";
    var t=setInterval(function(){
      if(!el.isConnected){clearInterval(t);return;}
      if(i>=w.length){clearInterval(t);if(done)done();return;}
      el.textContent+=w[i++];if(panel)panel.scrollTop=panel.scrollHeight;
    },22);
  }
  function bySlug(slug){
    var u=slug+".html";
    for(var i=0;i<DATA.length;i++)if(DATA[i].u===u)return DATA[i];
    return null;
  }
  function streamReal(q,ans,sources){
    fetch("/api/ask",{method:"POST",headers:{"Content-Type":"application/json"},
      body:JSON.stringify({guide:ASK_GUIDE,q:q})}).then(function(r){
      if(r.status===429)return askState("resting");
      if(!r.ok||!r.body)return askState("error");
      var hdr=r.headers.get("X-Ask-Sources");   // slugs the server actually used
      if(hdr){try{var mp=JSON.parse(hdr).map(bySlug).filter(Boolean);
        if(mp.length)sources=mp;}catch(e){}}
      var rd=r.body.getReader(),dec=new TextDecoder();ans.textContent="";
      (function pump(){return rd.read().then(function(res){
        if(res.done){ans.classList.remove("streaming");renderSources(sources);
          asking=false;return;}
        ans.textContent+=dec.decode(res.value,{stream:true});
        if(panel)panel.scrollTop=panel.scrollHeight;return pump();});})();
    }).catch(function(){askState("error");});
  }

  if(openBtn)openBtn.addEventListener("click",openSearch);
  if(input)input.addEventListener("input",function(){
    if(asking)resetAsk();render(input.value);});
  document.addEventListener("keydown",function(e){
    if(e.key==="/"&&modal.hidden&&
       !/^(INPUT|TEXTAREA)$/.test(document.activeElement.tagName)){
      e.preventDefault();openSearch();
    }else if(e.key==="Escape"){closeSearch();closeNav();}
    else if(!modal.hidden){
      if(e.key==="ArrowDown"){e.preventDefault();move(1);}
      else if(e.key==="ArrowUp"){e.preventDefault();move(-1);}
      else if(e.key==="Enter"){
        if(sel>=0)location.href=rows[sel].href;
        else{e.preventDefault();ask(input.value);}
      }
    }
  });
  if(modal)modal.addEventListener("click",function(e){
    if(e.target===modal)closeSearch();});

  /* ---- TOC scrollspy ---- */
  var tocLinks=Array.prototype.slice.call(
    document.querySelectorAll(".toc-link"));
  if(tocLinks.length){
    var heads=tocLinks.map(function(l){
      return document.getElementById(l.getAttribute("href").slice(1));
    });
    var obs=new IntersectionObserver(function(){
      var top=window.scrollY+100,cur=0;
      heads.forEach(function(h,i){
        if(h&&h.offsetTop<=top)cur=i;
      });
      tocLinks.forEach(function(l,i){
        l.classList.toggle("active",i===cur);
      });
    },{rootMargin:"-80px 0px -70% 0px",threshold:0});
    heads.forEach(function(h){if(h)obs.observe(h);});
  }
})();
