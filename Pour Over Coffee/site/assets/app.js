
/* Pour Over Coffee Knowledge Base — interactivity */
(function(){
  "use strict";
  var root=document.documentElement;

  /* theme */
  var saved=localStorage.getItem("pourover-theme");
  if(saved)root.setAttribute("data-theme",saved);
  var tg=document.getElementById("themeToggle");
  if(tg)tg.addEventListener("click",function(){
    var next=root.getAttribute("data-theme")==="dark"?"light":"dark";
    root.setAttribute("data-theme",next);
    localStorage.setItem("pourover-theme",next);
  });

  /* mobile drawer */
  var mt=document.getElementById("menuToggle"),
      scrim=document.getElementById("scrim");
  function closeNav(){document.body.classList.remove("nav-open");}
  if(mt)mt.addEventListener("click",function(){
    document.body.classList.toggle("nav-open");});
  if(scrim)scrim.addEventListener("click",closeNav);

  /* ---- search ---- */
  var modal=document.getElementById("searchModal"),
      input=document.getElementById("searchInput"),
      results=document.getElementById("searchResults"),
      openBtn=document.getElementById("searchOpen"),
      DATA=window.SEARCH_INDEX||[],sel=-1,rows=[];

  function openSearch(){
    if(!modal)return;
    modal.hidden=false;input.value="";render("");
    setTimeout(function(){input.focus();},30);
  }
  function closeSearch(){if(modal)modal.hidden=true;}
  function esc(s){return s.replace(/[&<>]/g,function(c){
    return{"&":"&amp;","<":"&lt;",">":"&gt;"}[c];});}
  function hl(text,q){
    if(!q)return esc(text);
    var i=text.toLowerCase().indexOf(q.toLowerCase());
    if(i<0)return esc(text);
    return esc(text.slice(0,i))+"<b>"+esc(text.slice(i,i+q.length))+
      "</b>"+esc(text.slice(i+q.length));
  }
  function score(p,q){
    var t=p.t.toLowerCase(),k=(p.k||"").toLowerCase(),
        s=(p.s||"").toLowerCase();
    if(t===q)return 100;
    if(t.indexOf(q)===0)return 80;
    if(t.indexOf(q)>=0)return 60;
    if(k.indexOf(q)>=0)return 40;
    if(s.indexOf(q)>=0)return 20;
    return 0;
  }
  function render(q){
    q=q.trim().toLowerCase();sel=-1;
    if(!q){
      results.innerHTML='<div class="sr-empty">Type to search '+
        DATA.length+' interlinked notes — try “bloom”, “V60”, '+
        '“extraction”, or a recipe name.</div>'+hint();
      rows=[];return;
    }
    var matched=[];
    DATA.forEach(function(p){
      var sc=score(p,q);if(sc>0)matched.push([sc,p]);
    });
    matched.sort(function(a,b){return b[0]-a[0];});
    matched=matched.slice(0,24);
    if(!matched.length){
      results.innerHTML='<div class="sr-empty">No notes match “'+
        esc(q)+'”.</div>';rows=[];return;
    }
    results.innerHTML=matched.map(function(m){
      var p=m[1];
      return '<a class="sr-item" href="'+p.u+'" style="--src:'+p.c+'">'+
        '<span class="sr-ic">'+p.i+'</span>'+
        '<span class="sr-main"><span class="sr-title">'+hl(p.t,q)+
        '</span><span class="sr-meta">'+esc(p.d)+'</span>'+
        '<span class="sr-snip">'+esc(p.s)+'</span></span></a>';
    }).join("")+hint();
    rows=Array.prototype.slice.call(
      results.querySelectorAll(".sr-item"));
  }
  function hint(){
    return '<div class="sr-hint"><span><kbd>&uarr;</kbd><kbd>&darr;</kbd>'+
      ' navigate</span><span><kbd>&crarr;</kbd> open</span>'+
      '<span><kbd>esc</kbd> close</span></div>';
  }
  function move(d){
    if(!rows.length)return;
    if(sel>=0)rows[sel].classList.remove("sel");
    sel=(sel+d+rows.length)%rows.length;
    rows[sel].classList.add("sel");
    rows[sel].scrollIntoView({block:"nearest"});
  }
  if(openBtn)openBtn.addEventListener("click",openSearch);
  if(input)input.addEventListener("input",function(){render(input.value);});
  document.addEventListener("keydown",function(e){
    if(e.key==="/"&&modal.hidden&&
       !/^(INPUT|TEXTAREA)$/.test(document.activeElement.tagName)){
      e.preventDefault();openSearch();
    }else if(e.key==="Escape"){closeSearch();closeNav();}
    else if(!modal.hidden){
      if(e.key==="ArrowDown"){e.preventDefault();move(1);}
      else if(e.key==="ArrowUp"){e.preventDefault();move(-1);}
      else if(e.key==="Enter"&&sel>=0){location.href=rows[sel].href;}
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
