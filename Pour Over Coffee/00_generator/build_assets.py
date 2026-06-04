# -*- coding: utf-8 -*-
"""Design assets (CSS + JS) for the Pour Over Coffee Knowledge Base site."""

CSS = r"""
/* ============================================================
   Pour Over Coffee Knowledge Base — design system
   ============================================================ */
:root{
  --bg:#EDE3D2; --bg-grad:#E2D4BC;
  --surface:#F7F0E2; --surface-2:#EADFCB; --surface-3:#DFCFB2;
  --ink:#241A12; --ink-2:#4A3A2A; --ink-3:#7C6850;
  --border:#DCCBA9; --border-2:#C7B088;
  --accent:#7A4A24; --accent-2:#A66A38; --accent-deep:#5A3318;
  --accent-soft:#E6D0AC;
  --link:#8A4F23; --link-hover:#693914;
  --hop:#8C6E32; --hop-deep:#5E4A1F;
  --il-ink:#241A12; --il-paper:#F7EFDD; --il-foam:#FBF4E4;
  --il-glass:rgba(247,240,226,.55); --il-beer:#6F4A2A;
  --shadow:0 1px 2px rgba(40,25,8,.07),0 8px 24px -10px rgba(40,25,8,.18);
  --shadow-lg:0 4px 12px rgba(40,25,8,.12),0 30px 60px -24px rgba(40,25,8,.34);
  --radius:16px;
  --serif:"Fraunces",Georgia,"Times New Roman",serif;
  --sans:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  --mono:"Spline Sans Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  --maxw:1320px;
}
html[data-theme="dark"]{
  --bg:#0F0B07; --bg-grad:#17100A;
  --surface:#1A130C; --surface-2:#221910;
  --surface-3:#2C2014;
  --ink:#EFE3CE; --ink-2:#C6B091; --ink-3:#917A5C;
  --border:#332818; --border-2:#473A26;
  --accent:#C98A3E; --accent-2:#E0A552; --accent-deep:#E0A552;
  --accent-soft:#3E2C14;
  --link:#D89A4A; --link-hover:#ECB868;
  --hop:#C9A45E; --hop-deep:#E0C896;
  --il-ink:#EFE3CE; --il-paper:#D8C39A; --il-foam:#E6D6AE;
  --il-glass:rgba(239,227,206,.16); --il-beer:#7A4F2C;
  --shadow:0 1px 2px rgba(0,0,0,.45),0 10px 30px -12px rgba(0,0,0,.65);
  --shadow-lg:0 6px 18px rgba(0,0,0,.55),0 36px 70px -28px rgba(0,0,0,.82);
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:88px}
body{
  background:var(--bg);color:var(--ink);
  font-family:var(--sans);font-size:16px;line-height:1.65;
  -webkit-font-smoothing:antialiased;
  background-image:radial-gradient(900px 480px at 80% -8%,var(--bg-grad),transparent);
}
a{color:var(--link);text-decoration:none}
::selection{background:var(--accent-soft);color:var(--ink)}
img{max-width:100%}

/* ---------- top bar ---------- */
.topbar{
  position:sticky;top:0;z-index:60;display:flex;align-items:center;gap:18px;
  height:64px;padding:0 22px;
  background:color-mix(in srgb,var(--bg) 86%,transparent);
  backdrop-filter:saturate(1.4) blur(12px);
  border-bottom:1px solid var(--border);
}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);flex:none}
.logo-mark{width:30px;height:30px;color:var(--accent)}
.brand-name{font-family:var(--serif);font-size:1.12rem;letter-spacing:.01em}
.brand-name b{font-weight:600}
.searchbtn{
  display:flex;align-items:center;gap:9px;margin-left:6px;
  flex:1;max-width:420px;height:40px;padding:0 12px;cursor:pointer;
  background:var(--surface);border:1px solid var(--border);
  border-radius:11px;color:var(--ink-3);font-family:var(--sans);
  font-size:.9rem;transition:border-color .15s,box-shadow .15s;
}
.searchbtn:hover{border-color:var(--border-2);box-shadow:var(--shadow)}
.searchbtn svg{width:17px;height:17px;color:var(--ink-3);flex:none}
.searchbtn span{flex:1;text-align:left}
.searchbtn kbd,.search-input-row kbd{
  font-family:var(--mono);font-size:.7rem;padding:2px 7px;
  background:var(--surface-2);border:1px solid var(--border);
  border-radius:6px;color:var(--ink-3)
}
.topbar-right{display:flex;gap:8px;margin-left:auto;flex:none}
.iconbtn{
  width:40px;height:40px;display:grid;place-items:center;cursor:pointer;
  background:var(--surface);border:1px solid var(--border);
  border-radius:11px;color:var(--ink-2);transition:.15s;
}
.iconbtn:hover{border-color:var(--border-2);color:var(--accent)}
.iconbtn svg{width:19px;height:19px}
.ic-moon{display:none}
html[data-theme="dark"] .ic-sun{display:none}
html[data-theme="dark"] .ic-moon{display:block}
.menubtn{display:none}

/* ---------- layout ---------- */
.layout{display:flex;max-width:var(--maxw);margin:0 auto;
  align-items:flex-start}
.sidebar{
  position:sticky;top:64px;flex:none;width:286px;
  height:calc(100vh - 64px);overflow-y:auto;padding:22px 14px 60px;
  border-right:1px solid var(--border);
}
.sidebar::-webkit-scrollbar{width:9px}
.sidebar::-webkit-scrollbar-thumb{
  background:var(--border-2);border-radius:9px;
  border:3px solid var(--bg)}
.nav-group{margin-bottom:3px}
.nav-head{
  display:flex;align-items:center;gap:9px;padding:8px 10px;cursor:pointer;
  border-radius:10px;list-style:none;font-weight:600;font-size:.88rem;
  color:var(--ink-2);transition:background .12s;
}
.nav-head::-webkit-details-marker{display:none}
.nav-head:hover{background:var(--surface-2)}
.nav-icon{font-size:1rem;width:20px;text-align:center;
  filter:saturate(1.1)}
.nav-dname{flex:1}
.nav-caret{width:12px;height:12px;color:var(--ink-3);
  transition:transform .18s}
.nav-group[open] .nav-caret{transform:rotate(180deg)}
.nav-group[open] .nav-head{color:var(--dc)}
.nav-list{list-style:none;margin:2px 0 8px;padding-left:8px;
  border-left:1.5px solid var(--border)}
.nav-link{
  display:block;padding:5.5px 10px;font-size:.845rem;line-height:1.35;
  color:var(--ink-3);border-radius:8px;
  transition:color .12s,background .12s;
}
.nav-link:hover{color:var(--ink);background:var(--surface-2)}
.nav-moc{font-weight:600;color:var(--ink-2)}
.nav-parent{font-weight:600;color:var(--ink-2)}
.nav-link.nav-sub{margin-left:14px;padding-left:12px;font-size:.82rem;
  border-left:1.5px solid var(--border)}
.nav-link.nav-sub:hover{border-left-color:var(--border-2)}
.nav-link.nav-sub.current{border-left-color:var(--dc)}
.nav-link.current{
  color:var(--dc);background:color-mix(in srgb,var(--dc) 13%,transparent);
  font-weight:600;box-shadow:inset 2.5px 0 0 var(--dc);
}

/* ---------- main / content grid ---------- */
.main{flex:1;min-width:0}
.content-grid{
  display:grid;grid-template-columns:minmax(0,1fr) 232px;
  gap:48px;max-width:1010px;margin:0 auto;padding:36px 40px 80px;
}
.article{min-width:0}

/* ---------- page head ---------- */
.crumb{display:flex;flex-wrap:wrap;align-items:center;gap:7px;
  font-size:.8rem;color:var(--ink-3);margin-bottom:20px}
.crumb a{color:var(--ink-3)}
.crumb a:hover{color:var(--accent)}
.crumb-sep{opacity:.5}
.domain-chip{
  display:inline-flex;align-items:center;gap:7px;
  padding:5px 13px 5px 9px;border-radius:999px;
  font-size:.76rem;font-weight:600;letter-spacing:.02em;
  color:var(--dc);background:color-mix(in srgb,var(--dc) 13%,transparent);
  text-transform:uppercase;
}
.page-title{
  font-family:var(--serif);font-weight:560;
  font-size:clamp(2rem,1.3rem + 2.6vw,3rem);line-height:1.1;
  letter-spacing:-.012em;margin:14px 0 0;color:var(--ink);
}
.page-head{position:relative;padding-bottom:24px;margin-bottom:30px;
  border-bottom:1px solid var(--border)}
.page-head::after{content:"";position:absolute;left:0;bottom:-1px;
  width:64px;height:3px;border-radius:3px;background:var(--dc)}
.page-meta{display:flex;align-items:center;gap:8px;margin-top:12px;
  font-size:.82rem;color:var(--ink-3)}
.page-meta .dot{opacity:.5}
.readtime{color:var(--accent-deep);font-weight:600}
html[data-theme="dark"] .readtime{color:var(--accent-2)}
.tags{display:flex;flex-wrap:wrap;gap:6px;margin-top:14px}
.tag{font-size:.7rem;font-family:var(--mono);color:var(--ink-3);
  background:var(--surface-2);border:1px solid var(--border);
  padding:3px 9px;border-radius:6px}

/* ---------- prose ---------- */
.prose{font-size:1.045rem;color:var(--ink-2)}
.prose>*+*{margin-top:1.05em}
.prose h2,.prose h3,.prose h4{
  font-family:var(--serif);color:var(--ink);font-weight:560;
  line-height:1.25;letter-spacing:-.01em;scroll-margin-top:88px;position:relative}
.prose h2{font-size:1.62rem;margin-top:2.1em;padding-top:.2em}
.prose h3{font-size:1.24rem;margin-top:1.7em}
.prose h4{font-size:1.05rem;margin-top:1.4em;color:var(--ink-2)}
.prose h2+*,.prose h3+*{margin-top:.7em}
.anchor{
  position:absolute;left:-1.1em;top:.06em;width:1em;
  color:var(--accent);opacity:0;font-weight:400;
  text-decoration:none;transition:opacity .12s;
}
.prose h2:hover .anchor,.prose h3:hover .anchor{opacity:.55}
.prose p,.prose li{color:var(--ink-2)}
.prose strong{color:var(--ink);font-weight:650}
.prose em{font-style:italic}
.prose ul,.prose ol{padding-left:1.35em}
.prose li{margin:.34em 0}
.prose li::marker{color:var(--accent)}
.prose hr{border:0;height:1px;background:var(--border);margin:2.2em 0}

/* wikilinks */
.wlink{
  color:var(--link);font-weight:500;
  border-bottom:1.5px solid color-mix(in srgb,var(--link) 32%,transparent);
  transition:border-color .12s,color .12s;
}
.wlink:hover{color:var(--link-hover);
  border-bottom-color:var(--link-hover)}
.wlink-self{font-weight:600;color:var(--ink)}
.wlink-missing{color:var(--ink-3);
  border-bottom:1.5px dotted var(--border-2)}
.exlink{color:var(--link);border-bottom:1.5px solid transparent}
.exlink:hover{border-bottom-color:var(--link)}
.exlink::after{content:"\2197";font-size:.75em;vertical-align:.3em;
  margin-left:1px;opacity:.7}

/* code */
.prose code{
  font-family:var(--mono);font-size:.86em;
  background:var(--surface-2);border:1px solid var(--border);
  padding:.1em .38em;border-radius:6px;color:var(--accent-deep);
}
html[data-theme="dark"] .prose code{color:var(--accent-2)}
.codeblock{
  font-family:var(--mono);font-size:.84rem;line-height:1.6;
  background:var(--surface-2);border:1px solid var(--border);
  border-radius:12px;padding:16px 18px;overflow-x:auto;
}
.codeblock code{background:none;border:0;padding:0;color:var(--ink-2)}

/* blockquote */
blockquote{
  border-left:3px solid var(--accent);padding:2px 0 2px 18px;
  color:var(--ink-2);font-style:italic;
}

/* ---------- callouts ---------- */
.callout{
  border-radius:12px;padding:14px 16px;
  border:1px solid var(--cb,var(--border));
  background:var(--cs,var(--surface-2));
  --ci:var(--accent);
}
.callout-head{display:flex;align-items:center;gap:9px;
  font-weight:650;font-size:.93rem;color:var(--ink)}
.callout-icon{
  width:22px;height:22px;flex:none;display:grid;place-items:center;
  border-radius:7px;font-size:.8rem;color:#fff;background:var(--ci);
}
.callout-title{font-family:var(--sans)}
.callout-body{margin-top:7px;font-size:.96rem;color:var(--ink-2)}
.callout-body>*+*{margin-top:.6em}
.callout-body>:first-child{margin-top:0}
.callout-note{--ci:#3D7E96;
  --cb:color-mix(in srgb,#3D7E96 30%,var(--border));
  --cs:color-mix(in srgb,#3D7E96 8%,var(--surface))}
.callout-tip{--ci:var(--hop);
  --cb:color-mix(in srgb,var(--hop) 32%,var(--border));
  --cs:color-mix(in srgb,var(--hop) 9%,var(--surface))}
.callout-example{--ci:#8567A8;
  --cb:color-mix(in srgb,#8567A8 30%,var(--border));
  --cs:color-mix(in srgb,#8567A8 8%,var(--surface))}
.callout-warning{--ci:#C0682C;
  --cb:color-mix(in srgb,#C0682C 32%,var(--border));
  --cs:color-mix(in srgb,#C0682C 9%,var(--surface))}

/* ---------- tables ---------- */
.table-wrap{overflow-x:auto;border:1px solid var(--border);
  border-radius:13px;box-shadow:var(--shadow)}
table{border-collapse:collapse;width:100%;font-size:.91rem}
.datatable thead th{
  background:var(--surface-3);color:var(--ink);font-weight:650;
  text-align:left;padding:11px 14px;font-size:.78rem;
  text-transform:uppercase;letter-spacing:.03em;white-space:nowrap;
}
.datatable td{padding:10px 14px;border-top:1px solid var(--border);
  color:var(--ink-2);vertical-align:top}
.datatable tbody tr{background:var(--surface)}
.datatable tbody tr:nth-child(even){background:var(--surface-2)}
.datatable tbody tr:hover{background:color-mix(in srgb,var(--accent) 8%,var(--surface))}
.datatable td:first-child{font-weight:600;color:var(--ink)}
.kvtable{background:var(--surface)}
.kvtable td{padding:9px 15px;border-top:1px solid var(--border);
  color:var(--ink-2)}
.kvtable tr:first-child td{border-top:0}
.kvtable td:first-child{font-weight:650;color:var(--ink);
  width:38%;background:var(--surface-2)}

/* ---------- family-tree diagram ---------- */
.diagram{margin:1.6em 0}
.ftree{width:100%;height:auto;display:block;
  background:linear-gradient(180deg,var(--surface),var(--surface-2));
  border:1px solid var(--border);border-radius:16px;
  padding:14px;box-shadow:var(--shadow)}
.ft-line{fill:none;stroke:var(--border-2);stroke-width:2}
.ft-rect{fill:var(--surface);stroke:var(--border-2);stroke-width:1.5;
  transition:fill .14s,stroke .14s}
.ft-label{font-family:var(--sans);font-size:14px;font-weight:600;
  fill:var(--ink);text-anchor:middle;dominant-baseline:middle}
.ft-node{cursor:pointer}
.ft-node .ft-rect{filter:drop-shadow(0 2px 5px rgba(60,40,10,.10))}
.ft-node:hover .ft-rect{fill:var(--accent);stroke:var(--accent-deep)}
.ft-node:hover .ft-label{fill:#fff}
.ft-sub .ft-rect{fill:var(--surface-2)}
.ft-sub .ft-label{font-size:12.5px;font-weight:600}
.ft-root .ft-rect{fill:var(--accent-soft);stroke:var(--accent);
  stroke-dasharray:4 3}
.ft-root .ft-label{fill:var(--accent-deep);font-size:13px}
html[data-theme="dark"] .ft-root .ft-label{fill:var(--accent-2)}
.ft-era{font-family:var(--serif);font-style:italic;font-size:13px;
  fill:var(--ink-3);text-anchor:middle}
figcaption{margin-top:10px;font-size:.83rem;color:var(--ink-3);
  text-align:center;font-style:italic}

/* ---------- backlinks ---------- */
.backlinks{margin-top:3em;padding-top:1.6em;
  border-top:1px solid var(--border)}
.bl-head{font-family:var(--serif);font-size:1.05rem;font-weight:560;
  color:var(--ink);display:flex;align-items:center;gap:9px;
  margin-bottom:13px}
.bl-head span{font-family:var(--sans);font-size:.72rem;font-weight:700;
  color:var(--accent-deep);background:var(--accent-soft);
  padding:2px 8px;border-radius:999px}
html[data-theme="dark"] .bl-head span{color:#15110B}
.bl-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));
  gap:8px}
.bl-item{display:flex;align-items:center;gap:9px;padding:9px 12px;
  background:var(--surface);border:1px solid var(--border);
  border-radius:10px;font-size:.86rem;color:var(--ink-2);
  font-weight:500;transition:.14s}
.bl-item:hover{border-color:var(--accent);color:var(--ink);
  transform:translateY(-1px);box-shadow:var(--shadow)}
.bl-ic{font-size:.95rem;flex:none}

/* ---------- prev / next ---------- */
.pagenav{display:grid;grid-template-columns:1fr 1fr;gap:14px;
  margin-top:2.6em}
.pn-card{display:flex;flex-direction:column;gap:5px;padding:16px 18px;
  background:var(--surface);border:1px solid var(--border);
  border-radius:13px;transition:.16s}
.pn-card:hover{border-color:var(--accent);transform:translateY(-2px);
  box-shadow:var(--shadow-lg)}
.pn-next{text-align:right}
.pn-dir{font-size:.74rem;font-weight:700;letter-spacing:.04em;
  text-transform:uppercase;color:var(--accent-deep)}
html[data-theme="dark"] .pn-dir{color:var(--accent-2)}
.pn-title{font-family:var(--serif);font-size:1.04rem;color:var(--ink);
  font-weight:560;line-height:1.25}

/* ---------- TOC ---------- */
.toc{position:relative}
.toc-inner{position:sticky;top:88px}
.toc-head{font-size:.72rem;font-weight:700;letter-spacing:.07em;
  text-transform:uppercase;color:var(--ink-3);margin-bottom:10px;
  padding-left:12px}
.toc-link{display:block;padding:4px 12px;font-size:.83rem;
  color:var(--ink-3);border-left:2px solid var(--border);
  line-height:1.4;transition:.12s}
.toc-link:hover{color:var(--ink)}
.toc-l3{padding-left:24px;font-size:.79rem}
.toc-link.active{color:var(--accent-deep);font-weight:600;
  border-left-color:var(--accent)}
html[data-theme="dark"] .toc-link.active{color:var(--accent-2)}

/* ============================================================
   HOME
   ============================================================ */
.main-home{max-width:none}
.hero{position:relative;overflow:hidden;
  padding:84px 40px 70px;
  border-bottom:1px solid var(--border)}
.hero-inner{position:relative;max-width:760px;margin:0 auto}
.hero-eyebrow{display:inline-block;font-size:.78rem;font-weight:600;
  letter-spacing:.05em;text-transform:uppercase;color:var(--accent-deep);
  background:var(--accent-soft);padding:6px 14px;border-radius:999px;
  margin-bottom:22px}
html[data-theme="dark"] .hero-eyebrow{color:#15110B}
.hero-title{font-family:var(--serif);font-weight:560;
  font-size:clamp(2.7rem,1.6rem + 4.4vw,4.7rem);line-height:1.02;
  letter-spacing:-.022em;color:var(--ink)}
.hero-em{color:var(--accent);font-style:italic}
.hero-sub{margin-top:22px;font-size:1.12rem;line-height:1.62;
  color:var(--ink-2);max-width:620px}
.hero-actions{display:flex;flex-wrap:wrap;gap:13px;margin-top:30px}
.btn{display:inline-flex;align-items:center;padding:12px 22px;
  border-radius:11px;font-weight:600;font-size:.95rem;transition:.16s}
.btn-primary{background:var(--accent);color:#fff;
  box-shadow:0 8px 22px -8px var(--accent)}
.btn-primary:hover{background:var(--accent-deep);transform:translateY(-2px)}
html[data-theme="dark"] .btn-primary{color:#15110B}
.btn-ghost{background:var(--surface);color:var(--ink);
  border:1px solid var(--border-2)}
.btn-ghost:hover{border-color:var(--accent);color:var(--accent-deep);
  transform:translateY(-2px)}
html[data-theme="dark"] .btn-ghost:hover{color:var(--accent-2)}
.hero-stats{display:flex;flex-wrap:wrap;gap:34px;margin-top:42px;
  padding-top:28px;border-top:1px solid var(--border)}
.hstat b{display:block;font-family:var(--serif);font-size:2.1rem;
  font-weight:560;color:var(--accent-deep);line-height:1}
html[data-theme="dark"] .hstat b{color:var(--accent-2)}
.hstat span{font-size:.82rem;color:var(--ink-3)}

.home-sec{max-width:1080px;margin:0 auto;padding:64px 40px}
.home-sec-tint{max-width:none;background:var(--surface-2);
  border-block:1px solid var(--border)}
.home-sec-tint .sec-head,.home-sec-tint .lede{
  max-width:760px;margin-inline:auto}
.sec-head{margin-bottom:34px}
.sec-kicker{font-size:.76rem;font-weight:700;letter-spacing:.06em;
  text-transform:uppercase;color:var(--accent)}
.sec-head h2{font-family:var(--serif);font-weight:560;
  font-size:clamp(1.7rem,1.2rem + 1.8vw,2.4rem);
  letter-spacing:-.015em;color:var(--ink);margin-top:8px;line-height:1.12}
.sec-head p{margin-top:12px;color:var(--ink-2);max-width:560px;
  font-size:1.02rem}
.lede{font-size:1.16rem;line-height:1.66;color:var(--ink-2);
  font-family:var(--serif)}
.lede .wlink{font-family:var(--serif)}

.dcard-grid{display:grid;
  grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:18px}
.dcard{position:relative;display:flex;flex-direction:column;
  padding:24px 22px 20px;background:var(--surface);
  border:1px solid var(--border);border-radius:var(--radius);
  overflow:hidden;transition:.18s}
.dcard::before{content:"";position:absolute;inset:0 0 auto;height:4px;
  background:var(--dc)}
.dcard:hover{transform:translateY(-4px);box-shadow:var(--shadow-lg);
  border-color:color-mix(in srgb,var(--dc) 45%,var(--border))}
.dcard-top{display:flex;align-items:center;justify-content:space-between}
.dcard-icon{font-size:1.7rem;width:48px;height:48px;display:grid;
  place-items:center;border-radius:13px;
  background:color-mix(in srgb,var(--dc) 14%,transparent)}
.dcard-count{font-size:.74rem;font-weight:600;color:var(--ink-3);
  font-family:var(--mono)}
.dcard-name{font-family:var(--serif);font-size:1.32rem;font-weight:560;
  color:var(--ink);margin-top:16px}
.dcard-blurb{margin-top:7px;font-size:.92rem;color:var(--ink-2);
  flex:1;line-height:1.55}
.dcard-go{display:flex;align-items:center;gap:6px;margin-top:16px;
  font-size:.83rem;font-weight:650;color:var(--dc)}
.dcard-go svg{width:15px;height:15px;transition:transform .16s}
.dcard:hover .dcard-go svg{transform:translateX(4px)}

.path-grid{display:grid;
  grid-template-columns:repeat(auto-fill,minmax(248px,1fr));gap:16px}
.path-card{padding:22px 20px;background:var(--surface);
  border:1px solid var(--border);border-radius:14px;transition:.16s}
.path-card:hover{border-color:var(--border-2);box-shadow:var(--shadow)}
.path-icon{font-size:1.6rem}
.path-card h4{font-family:var(--serif);font-size:1.12rem;font-weight:560;
  color:var(--ink);margin-top:10px}
.path-card p{font-size:.88rem;color:var(--ink-2);margin-top:5px}
.path-links{display:flex;flex-direction:column;gap:4px;margin-top:13px}
.path-link{font-size:.88rem;font-weight:600;color:var(--link);
  padding:5px 0;border-top:1px solid var(--border)}
.path-link:hover{color:var(--link-hover)}

.site-footer{max-width:1080px;margin:0 auto;padding:50px 40px 70px;
  border-top:1px solid var(--border);color:var(--ink-3)}
.footer-mark{display:flex;align-items:center;gap:9px;
  font-family:var(--serif);font-size:1.1rem;color:var(--ink)}
.footer-mark .logo-mark{width:24px;height:24px}
.site-footer p{margin-top:10px;font-size:.9rem;max-width:520px}
.footer-fine{font-size:.82rem!important}

/* ---------- search modal ---------- */
.search-modal{position:fixed;inset:0;z-index:100;
  background:color-mix(in srgb,var(--ink) 45%,transparent);
  backdrop-filter:blur(4px);display:flex;justify-content:center;
  padding:11vh 20px 20px}
.search-modal[hidden]{display:none}
.search-box{width:100%;max-width:620px;height:max-content;
  max-height:74vh;display:flex;flex-direction:column;
  background:var(--surface);border:1px solid var(--border-2);
  border-radius:16px;box-shadow:var(--shadow-lg);overflow:hidden}
.search-input-row{display:flex;align-items:center;gap:11px;
  padding:16px 18px;border-bottom:1px solid var(--border)}
.search-ic{width:19px;height:19px;color:var(--ink-3);flex:none}
#searchInput{flex:1;border:0;background:none;outline:none;
  font-family:var(--sans);font-size:1.04rem;color:var(--ink)}
#searchInput::placeholder{color:var(--ink-3)}
.search-results{overflow-y:auto;padding:8px}
.sr-item{display:flex;gap:12px;padding:11px 13px;border-radius:10px;
  cursor:pointer}
.sr-item:hover,.sr-item.sel{background:var(--surface-2)}
.sr-ic{font-size:1.1rem;flex:none;width:34px;height:34px;display:grid;
  place-items:center;border-radius:9px;
  background:color-mix(in srgb,var(--src) 15%,transparent)}
.sr-main{min-width:0}
.sr-title{display:block;font-weight:600;color:var(--ink);font-size:.96rem}
.sr-title b{background:var(--accent-soft);color:var(--ink);
  border-radius:3px;padding:0 1px}
html[data-theme="dark"] .sr-title b{background:var(--accent);color:#15110B}
.sr-meta{display:block;font-size:.78rem;color:var(--src);font-weight:600;
  margin-top:2px}
.sr-snip{font-size:.81rem;color:var(--ink-3);margin-top:2px;
  display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;
  overflow:hidden}
.sr-empty{padding:34px;text-align:center;color:var(--ink-3);
  font-size:.92rem}
.sr-hint{padding:11px 14px;border-top:1px solid var(--border);
  font-size:.76rem;color:var(--ink-3);display:flex;gap:14px}
.sr-hint kbd{font-family:var(--mono);font-size:.72rem;
  background:var(--surface-2);border:1px solid var(--border);
  border-radius:5px;padding:1px 6px}

/* ---------- ask (Q&A) ---------- */
.search-body{display:flex;flex-direction:column;overflow-y:auto;min-height:0}
.search-results{overflow:visible}
.ask-panel{padding:16px 18px 8px;border-bottom:1px solid var(--border)}
.ask-panel[hidden]{display:none}
.ask-head{display:flex;align-items:center;gap:9px;margin-bottom:7px}
.ask-eyebrow{font-family:var(--mono);font-size:.7rem;letter-spacing:.14em;
  text-transform:uppercase;color:var(--ink-3)}
.ask-badge{font-family:var(--mono);font-size:.62rem;letter-spacing:.08em;
  text-transform:uppercase;color:var(--accent);
  background:color-mix(in srgb,var(--accent) 14%,transparent);
  border:1px solid color-mix(in srgb,var(--accent) 30%,transparent);
  border-radius:999px;padding:2px 8px}
.ask-q{font-family:var(--serif);font-size:1.06rem;color:var(--ink);
  line-height:1.32;margin-bottom:9px}
.ask-q::before{content:"\201C"}.ask-q::after{content:"\201D"}
.ask-answer{font-size:.95rem;line-height:1.6;color:var(--ink-2);
  white-space:pre-wrap;min-height:1.2em}
.ask-answer.streaming::after{content:"";display:inline-block;width:.46em;
  height:1.02em;margin-left:1px;vertical-align:-2px;background:var(--accent);
  border-radius:1px;animation:askblink 1s steps(2) infinite}
@keyframes askblink{50%{opacity:0}}
.ask-foot{margin-top:11px;font-size:.76rem;color:var(--ink-3);font-style:italic}
.ask-sources{margin-top:6px}
.ask-src-label,.sr-jump{font-family:var(--mono);font-size:.67rem;
  letter-spacing:.12em;text-transform:uppercase;color:var(--ink-3);
  padding:8px 13px 4px}
.ask-note{padding:14px 16px;border-radius:11px;font-size:.9rem;line-height:1.5;
  background:var(--surface-2);color:var(--ink-2)}
.ask-note-resting{border:1px solid color-mix(in srgb,var(--accent) 32%,transparent)}
.ask-note-error{border:1px solid color-mix(in srgb,#c0506a 38%,transparent)}
.sr-intro{padding:26px 22px 20px;text-align:center}
.sr-intro-h{font-family:var(--serif);font-size:1.18rem;color:var(--ink);
  margin-bottom:6px}
.sr-intro-p{font-size:.88rem;color:var(--ink-3);line-height:1.55;
  max-width:430px;margin:0 auto 16px}
.ask-chips{display:flex;flex-wrap:wrap;gap:8px;justify-content:center}
.ask-chip{font-family:var(--sans);font-size:.83rem;color:var(--ink-2);
  background:var(--surface-2);border:1px solid var(--border);border-radius:999px;
  padding:7px 13px;cursor:pointer;text-align:left;
  transition:border-color .15s,color .15s,background .15s}
.ask-chip:hover{color:var(--ink);border-color:var(--border-2);
  background:color-mix(in srgb,var(--accent) 9%,var(--surface-2))}

.scrim{position:fixed;inset:0;z-index:40;background:rgba(20,14,6,.5);
  display:none}

/* ---------- responsive ---------- */
@media(max-width:1080px){
  .content-grid{grid-template-columns:1fr;gap:0}
  .toc{display:none}
}
@media(max-width:860px){
  .menubtn{display:grid}
  .searchbtn span,.searchbtn kbd{display:none}
  .searchbtn{flex:none;width:40px;padding:0;justify-content:center}
  .sidebar{position:fixed;top:64px;left:0;z-index:50;
    width:300px;background:var(--bg);transform:translateX(-105%);
    transition:transform .22s ease;box-shadow:var(--shadow-lg)}
  body.nav-open .sidebar{transform:translateX(0)}
  body.nav-open .scrim{display:block}
  .content-grid{padding:26px 22px 70px}
  .hero,.home-sec,.site-footer{padding-inline:24px}
  .hero{padding-top:54px}
  .pagenav{grid-template-columns:1fr}
  .pn-next{text-align:left}
  .moc-grid{grid-template-columns:1fr!important;gap:14px}
  .moc-art{justify-self:start;width:60%!important}
  .vs-grid{grid-template-columns:1fr!important}
  .vs-glass-wrap{flex-direction:row!important;gap:14px;align-items:center}
  .vs-glass{width:90px!important}
  .ht-row{grid-template-columns:96px 28px 1fr!important}
  .ht-year{font-size:1rem!important}
}

/* ============================================================
   DOMAIN ILLUSTRATIONS
   ============================================================ */
.d-ill{width:100%;height:auto;display:block;
  filter:drop-shadow(0 2px 4px rgba(60,40,10,.08))}

/* ============================================================
   MOC BANNER  (illustrated domain landing)
   ============================================================ */
.moc-banner{
  position:relative;overflow:hidden;margin-bottom:34px;padding:24px 26px 28px;
  border-radius:20px;background:linear-gradient(135deg,
    color-mix(in srgb,var(--dc) 18%,var(--surface)) 0%,
    color-mix(in srgb,var(--dc) 6%,var(--surface)) 100%);
  border:1px solid color-mix(in srgb,var(--dc) 22%,var(--border));
  box-shadow:var(--shadow);
}
.moc-banner::before{content:"";position:absolute;left:0;top:0;width:4px;
  height:100%;background:var(--dc)}
.moc-banner .crumb{margin-bottom:18px}
.moc-grid{display:grid;grid-template-columns:1fr 280px;gap:32px;
  align-items:center}
.moc-text{min-width:0}
.moc-kicker{font-size:.74rem;font-weight:700;letter-spacing:.07em;
  text-transform:uppercase;color:var(--dc);font-family:var(--mono)}
.moc-title{font-family:var(--serif);font-weight:560;
  font-size:clamp(2rem,1.3rem + 2.8vw,3.1rem);line-height:1.06;
  letter-spacing:-.018em;color:var(--ink);margin-top:8px}
.moc-blurb{margin-top:14px;font-size:1.05rem;line-height:1.55;
  color:var(--ink-2);max-width:520px}
.moc-art{position:relative;width:280px;color:var(--dc)}
.moc-art .d-ill{filter:drop-shadow(0 6px 18px
  color-mix(in srgb,var(--dc) 40%,transparent))}

/* ============================================================
   HOME — illustrated domain cards
   ============================================================ */
.dcard{padding:0;overflow:hidden}
.dcard-art{position:relative;height:140px;display:flex;align-items:flex-end;
  justify-content:center;color:var(--dc);overflow:hidden;
  background:linear-gradient(180deg,
    color-mix(in srgb,var(--dc) 16%,var(--surface)),
    color-mix(in srgb,var(--dc) 6%,var(--surface)))}
.dcard-art::before{content:"";position:absolute;inset:0;
  background:radial-gradient(120% 80% at 50% 110%,
    color-mix(in srgb,var(--dc) 20%,transparent),transparent 70%)}
.dcard-art .d-ill{position:relative;width:86%;
  transform:translateY(8%);transition:transform .25s ease}
.dcard:hover .dcard-art .d-ill{transform:translateY(2%) scale(1.03)}
.dcard .dcard-top{padding:14px 20px 0;align-items:flex-start}
.dcard .dcard-icon{font-size:1.15rem;width:36px;height:36px;border-radius:10px;
  background:var(--surface);border:1px solid var(--border);
  box-shadow:var(--shadow);margin-top:-30px;z-index:1;position:relative}
.dcard-name,.dcard-blurb,.dcard-go{padding-inline:20px}
.dcard-name{margin-top:12px}
.dcard-go{padding-bottom:18px}

/* ============================================================
   COMMON DIAGRAM CHROME
   ============================================================ */
.diagram{margin:1.8em 0;padding:18px 18px 14px;
  background:linear-gradient(180deg,var(--surface) 0%,var(--surface-2) 100%);
  border:1px solid var(--border);border-radius:18px;
  box-shadow:var(--shadow)}
.diagram svg{width:100%;height:auto;display:block;max-width:100%}
.diagram figcaption{margin:14px 6px 4px;font-size:.85rem;color:var(--ink-3);
  text-align:center;font-style:italic;line-height:1.45}

/* ============================================================
   FAMILY TREE  (refined)
   ============================================================ */
.diagram-tree{padding:24px 18px 18px}
.ftree{background:transparent;border:0;padding:0;box-shadow:none;border-radius:0}
.ft-line{fill:none;stroke:var(--border-2);stroke-width:2;
  stroke-linecap:round}
.ft-line-dash{stroke-dasharray:4 4;opacity:.7}
.ft-rect{fill:var(--surface);stroke:var(--border-2);stroke-width:1.6;
  transition:fill .14s,stroke .14s,filter .14s;
  filter:drop-shadow(0 2px 6px rgba(60,40,10,.10))}
.ft-label{font-family:var(--sans);font-size:14px;font-weight:600;
  fill:var(--ink);text-anchor:middle;dominant-baseline:middle}
.ft-node{cursor:pointer}
.ft-node:hover .ft-rect{fill:var(--accent);stroke:var(--accent-deep)}
.ft-node:hover .ft-label{fill:#fff}
html[data-theme="dark"] .ft-node:hover .ft-label{fill:#15110B}
.ft-sub .ft-rect{fill:var(--surface-2)}
.ft-sub .ft-label{font-size:12.5px}
.ft-static{cursor:default}
.ft-static .ft-rect,.ft-static:hover .ft-rect{
  fill:color-mix(in srgb,var(--accent) 12%,var(--surface));stroke:var(--border-2)}
.ft-static .ft-label,.ft-static:hover .ft-label{fill:var(--ink-2)}
.ft-root .ft-rect{fill:color-mix(in srgb,var(--accent) 22%,var(--surface));
  stroke:var(--accent);stroke-dasharray:4 3}
.ft-root .ft-label{fill:var(--accent-deep);font-size:13px;font-weight:700;
  letter-spacing:.02em}
html[data-theme="dark"] .ft-root .ft-label{fill:var(--accent-2)}
.ft-era{font-family:var(--serif);font-style:italic;font-size:13px;
  fill:var(--ink-3);text-anchor:middle}

/* ============================================================
   BREWING PROCESS FLOW
   ============================================================ */
.bpflow{font-family:var(--sans)}
.bp-band{fill:none;stroke:var(--border);stroke-width:1.5;
  stroke-dasharray:3 5;opacity:.6}
.bp-band-hot{fill:color-mix(in srgb,#B5612E 8%,transparent)}
.bp-band-cold{fill:color-mix(in srgb,#3D7E96 8%,transparent)}
.bp-band-label{font-size:11px;font-weight:700;letter-spacing:.12em;
  text-anchor:middle;dominant-baseline:middle;fill:var(--ink-3);
  font-family:var(--mono)}
.bp-conn{stroke:var(--border-2);stroke-width:2.4;fill:none;
  stroke-linecap:round}
.bp-conn-curve{stroke-dasharray:6 4;opacity:.7}
.bp-arrow{fill:var(--border-2)}
.bp-step{cursor:pointer}
.bp-node-bg{fill:var(--surface);stroke:none;
  filter:drop-shadow(0 3px 8px rgba(60,40,10,.10))}
.bp-node-rim{fill:none;stroke:var(--border-2);stroke-width:2;
  transition:stroke .15s}
.bp-step:hover .bp-node-bg{fill:color-mix(in srgb,var(--accent) 12%,var(--surface))}
.bp-step:hover .bp-node-rim{stroke:var(--accent)}
.bp-glyph{color:var(--accent-deep)}
html[data-theme="dark"] .bp-glyph{color:var(--accent-2)}
.bp-step-num{font-size:10px;font-weight:700;letter-spacing:.12em;
  fill:var(--ink-3);text-anchor:middle;font-family:var(--mono)}
.bp-step-label{font-size:14px;font-weight:600;fill:var(--ink);
  text-anchor:middle}
.bp-step:hover .bp-step-label{fill:var(--accent-deep)}
html[data-theme="dark"] .bp-step:hover .bp-step-label{fill:var(--accent-2)}

/* ============================================================
   HOP TIMING — five-window infographic
   ============================================================ */
.hopline{font-family:var(--sans)}
.hl-band{fill:var(--surface);stroke:var(--border);stroke-width:1.4}
.hl-axis{font-size:11px;font-weight:700;letter-spacing:.08em;
  text-transform:uppercase;fill:var(--ink-3);font-family:var(--mono)}
.hl-zone{cursor:pointer}
.hl-zone-rect{fill:transparent;stroke:transparent;stroke-width:1.5;
  transition:.14s}
.hl-zone:hover .hl-zone-rect{fill:color-mix(in srgb,var(--accent) 12%,transparent);
  stroke:var(--accent)}
.hl-zone-label{font-size:13.5px;font-weight:650;fill:var(--ink);
  text-anchor:middle}
.hl-zone-meta{font-size:10.5px;fill:var(--ink-3);text-anchor:middle;
  font-family:var(--mono)}
.hl-zone-num{font-size:11px;font-weight:700;fill:var(--accent-deep);
  text-anchor:middle;font-family:var(--mono);letter-spacing:.1em}
html[data-theme="dark"] .hl-zone-num{fill:var(--accent-2)}
.hl-contrib{font-size:11px;font-weight:600;text-anchor:middle;
  font-family:var(--mono)}
.hl-contrib-bit{fill:var(--accent-deep)}
.hl-contrib-aro{fill:var(--hop-deep)}
html[data-theme="dark"] .hl-contrib-bit{fill:var(--accent-2)}
.hl-legend{font-size:11px;fill:var(--ink-3);dominant-baseline:middle}

/* ============================================================
   HISTORY TIMELINE
   ============================================================ */
.htimeline{padding:8px 4px 4px}
.ht-era{display:flex;align-items:center;gap:11px;
  padding:14px 4px 10px;margin-top:14px;
  border-top:1px solid color-mix(in srgb,var(--ec) 30%,var(--border))}
.ht-era:first-child{border-top:0;margin-top:0;padding-top:4px}
.ht-era-dot{width:10px;height:10px;border-radius:50%;background:var(--ec)}
.ht-era-label{font-family:var(--serif);font-size:1.04rem;font-weight:600;
  color:var(--ec);letter-spacing:.005em}
.ht-row{display:grid;grid-template-columns:140px 36px 1fr;
  align-items:start;padding:12px 4px;
  text-decoration:none;color:inherit;transition:.14s;border-radius:10px}
.ht-row:hover{background:color-mix(in srgb,var(--ec) 9%,transparent)}
.ht-year{font-family:var(--serif);font-size:1.18rem;font-weight:560;
  color:var(--ec);text-align:right;padding-right:14px;line-height:1.15}
.ht-spine{position:relative;display:flex;justify-content:center;
  padding-top:6px}
.ht-spine::before{content:"";position:absolute;left:50%;top:0;
  width:2px;height:calc(100% + 28px);
  background:color-mix(in srgb,var(--ec) 32%,var(--border));
  transform:translateX(-50%)}
.ht-dot{width:13px;height:13px;border-radius:50%;background:var(--surface);
  border:2.5px solid var(--ec);position:relative;z-index:1;
  transition:.14s}
.ht-row:hover .ht-dot{background:var(--ec);transform:scale(1.18)}
.ht-card{padding:2px 10px 8px 14px}
.ht-title{font-size:.99rem;font-weight:550;color:var(--ink);
  line-height:1.5}
.ht-go{margin-top:5px;font-size:.78rem;font-weight:600;
  color:var(--ec);opacity:0;transition:.14s}
.ht-row:hover .ht-go{opacity:1}
.ht-go span{margin-left:2px}

/* ============================================================
   FLAVOR WHEEL
   ============================================================ */
.fwheel{font-family:var(--sans)}
.fw-outer{fill:color-mix(in srgb,var(--fc) 18%,var(--surface));
  stroke:color-mix(in srgb,var(--fc) 30%,var(--border));stroke-width:1.2}
.fw-inner{fill:color-mix(in srgb,var(--fc) 38%,var(--surface));
  stroke:color-mix(in srgb,var(--fc) 55%,var(--border));stroke-width:1.6;
  transition:fill .14s}
.fw-class-link{cursor:pointer}
.fw-class-link:hover .fw-inner{fill:var(--fc)}
.fw-class{font-size:14px;font-weight:700;fill:var(--ink);
  text-anchor:middle;dominant-baseline:middle;letter-spacing:.04em;
  text-transform:uppercase;pointer-events:none}
.fw-class-link:hover .fw-class{fill:#fff}
html[data-theme="dark"] .fw-class-link:hover .fw-class{fill:#15110B}
.fw-desc{font-size:11.5px;font-weight:600;fill:var(--ink-2);
  text-anchor:middle;dominant-baseline:middle;font-family:var(--mono);
  pointer-events:none}
.fw-hub{fill:var(--surface);stroke:var(--border-2);stroke-width:2;
  filter:drop-shadow(0 4px 10px rgba(60,40,10,.18))}
.fw-hub-label{font-family:var(--serif);font-size:14px;font-weight:600;
  letter-spacing:.18em;fill:var(--ink);text-anchor:middle}
.fw-hub-sub{font-family:var(--serif);font-size:14px;font-weight:600;
  letter-spacing:.18em;fill:var(--ink-3);text-anchor:middle}

/* ============================================================
   STYLE MAP — clarity vs strength scatter
   ============================================================ */
.smap{font-family:var(--sans);background:var(--surface);
  border-radius:14px}
.sm-axis{stroke:var(--border-2);stroke-width:1.5}
.sm-grid{stroke:var(--border);stroke-width:1;stroke-dasharray:3 4;
  opacity:.7}
.sm-grid-mid{stroke-dasharray:none;opacity:.85}
.sm-tick{font-size:11px;fill:var(--ink-3);font-family:var(--mono)}
.sm-axis-label{font-size:11px;font-weight:600;fill:var(--ink-3);
  font-family:var(--mono);letter-spacing:.04em;text-transform:uppercase}
.sm-axis-title{font-size:11px;font-weight:700;fill:var(--ink-2);
  font-family:var(--mono);letter-spacing:.14em}
.sm-quad-a{fill:color-mix(in srgb,var(--accent) 5%,transparent)}
.sm-quad-b{fill:color-mix(in srgb,#B14A55 5%,transparent)}
.sm-quad-c{fill:color-mix(in srgb,var(--hop) 5%,transparent)}
.sm-quad-d{fill:color-mix(in srgb,#8567A8 5%,transparent)}
.sm-pt{cursor:pointer}
.sm-halo{fill:none;stroke:var(--border-2);stroke-width:0;transition:.14s}
.sm-pt:hover .sm-halo{stroke-width:6;
  stroke:color-mix(in srgb,var(--accent) 60%,transparent)}
.sm-dot{stroke:var(--ink);stroke-width:1.5;transition:transform .14s;
  transform-origin:center;transform-box:fill-box}
.sm-pt:hover .sm-dot{transform:scale(1.22)}
.sm-label{font-size:11.5px;font-weight:600;fill:var(--ink);
  dominant-baseline:middle;pointer-events:none}
.sm-pt:hover .sm-label{fill:var(--accent-deep);font-weight:700}
html[data-theme="dark"] .sm-pt:hover .sm-label{fill:var(--accent-2)}

/* ============================================================
   VITAL SIGNS PANEL (replaces "Quick stats" callout on styles)
   ============================================================ */
.vs-panel{margin:1.6em 0;padding:24px 26px 22px;border-radius:18px;
  background:linear-gradient(180deg,var(--surface),var(--surface-2));
  border:1px solid var(--border-2);box-shadow:var(--shadow);
  position:relative;overflow:hidden}
.vs-panel::before{content:"";position:absolute;left:0;top:0;
  width:3px;height:100%;
  background:linear-gradient(180deg,var(--accent),var(--hop))}
.vs-head{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;
  margin-bottom:18px;padding-bottom:14px;
  border-bottom:1px solid var(--border)}
.vs-kicker{font-family:var(--mono);font-size:.7rem;font-weight:700;
  letter-spacing:.14em;color:var(--accent-deep);
  background:var(--accent-soft);padding:4px 10px;border-radius:999px}
html[data-theme="dark"] .vs-kicker{color:#15110B;
  background:var(--accent-2)}
.vs-name{font-family:var(--serif);font-size:1.15rem;font-weight:560;
  color:var(--ink);margin:0}
.vs-grid{display:grid;grid-template-columns:160px 1fr;gap:30px;
  align-items:center}
.vs-glass-wrap{display:flex;flex-direction:column;align-items:center;
  gap:10px}
.vs-glass{width:128px;height:auto;display:block;
  filter:drop-shadow(0 6px 18px rgba(60,40,10,.16))}
.vs-color-label{display:flex;align-items:center;gap:8px;
  font-size:.78rem;color:var(--ink-3);text-align:center}
.vs-swatch{width:14px;height:14px;border-radius:4px;
  border:1.5px solid var(--border-2);flex:none}
.vs-gauges{display:flex;flex-direction:column;gap:16px;min-width:0}
.vs-gauge,.vs-haze{display:flex;flex-direction:column;gap:6px}
.vs-glabel{display:flex;justify-content:space-between;align-items:baseline;
  font-size:.78rem;font-weight:700;letter-spacing:.06em;
  text-transform:uppercase;color:var(--ink-3);font-family:var(--mono)}
.vs-glabel .vs-gval{font-family:var(--serif);font-size:1.04rem;
  font-weight:560;color:var(--ink);text-transform:none;letter-spacing:0}
.vs-gbody{position:relative;height:14px}
.vs-gtrack{position:absolute;inset:5px 0;border-radius:3px;
  background:var(--surface-3)}
.vs-gfill{position:absolute;top:4px;height:6px;border-radius:3px;
  background:linear-gradient(90deg,var(--accent),var(--accent-2));
  box-shadow:0 0 0 1px rgba(0,0,0,.05) inset}
.vs-gpin{position:absolute;top:0;width:3px;height:14px;
  border-radius:2px;background:var(--accent-deep);
  transform:translateX(-50%)}
html[data-theme="dark"] .vs-gpin{background:var(--accent-2)}
.vs-gmax{position:absolute;right:0;top:-18px;font-size:.7rem;
  color:var(--ink-3);font-family:var(--mono)}
.vs-haze .vs-hdots{display:flex;gap:5px}
.vs-hdot{width:18px;height:8px;border-radius:3px;
  background:var(--surface-3)}
.vs-hdot.on{background:linear-gradient(90deg,var(--accent),var(--hop))}
.vs-hscale{display:flex;justify-content:space-between;
  font-size:.7rem;color:var(--ink-3);font-family:var(--mono);
  letter-spacing:.05em}
.vs-foot{margin-top:18px;padding-top:14px;
  border-top:1px solid var(--border);display:flex;flex-direction:column;
  gap:8px}
.vs-foot-row{display:flex;gap:14px;align-items:baseline;flex-wrap:wrap}
.vs-foot-label{font-size:.72rem;font-weight:700;letter-spacing:.08em;
  text-transform:uppercase;color:var(--ink-3);font-family:var(--mono);
  min-width:90px}
.vs-foot-val{font-size:.95rem;color:var(--ink-2);flex:1;min-width:0}
.vs-foot-val .wlink{font-weight:600}
"""

JS = r"""
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
  var ASK_TOPIC="pour over";
  var ASK_GUIDE="pour-over";
  var ASK_EG=["What’s the best V60 recipe?",
              "Why does my coffee taste sour?",
              "How fine should I grind for pour over?"];

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
"""
