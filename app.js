(function(){
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var yr = document.getElementById('yr');
  if(yr) yr.textContent = new Date().getFullYear();

  /* ---- mobile navigation ---- */
  (function nav(){
    var burger = document.getElementById('burger');
    var menu = document.getElementById('menu');
    if(!burger || !menu) return;
    function close(){
      burger.setAttribute('aria-expanded','false');
      menu.classList.remove('open');
      document.body.classList.remove('nav-open');
    }
    function open(){
      burger.setAttribute('aria-expanded','true');
      menu.classList.add('open');
      document.body.classList.add('nav-open');
    }
    burger.addEventListener('click', function(){
      burger.getAttribute('aria-expanded') === 'true' ? close() : open();
    });
    menu.addEventListener('click', function(e){ if(e.target.closest('a')) close(); });
    document.addEventListener('keydown', function(e){ if(e.key === 'Escape') close(); });
    addEventListener('resize', function(){ if(innerWidth > 1000) close(); }, {passive:true});
  })();

  /* ---- optional photos: hide cleanly if absent ---- */
  document.querySelectorAll('.slot img, .portrait img').forEach(function(img){
    function miss(){ img.setAttribute('data-missing',''); }
    img.addEventListener('error', miss);
    if(img.complete && img.naturalWidth === 0) miss();
  });

  /* ---- reveal on scroll ---- */
  var els = document.querySelectorAll('.rise, .stat, .strata');
  if(!('IntersectionObserver' in window)){
    els.forEach(function(e){ e.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function(en){
      en.forEach(function(x){ if(x.isIntersecting){ x.target.classList.add('in'); io.unobserve(x.target); } });
    },{threshold:.08,rootMargin:'0px 0px -6% 0px'});
    els.forEach(function(el,i){ el.style.transitionDelay = (Math.min(i%5,4)*60)+'ms'; io.observe(el); });
  }

  /* ---- count up ---- */
  var nums = document.querySelectorAll('[data-count]');
  function countUp(el){
    var target = +el.dataset.count, suf = el.dataset.suffix || '', t0 = null, dur = 1300;
    if(reduce){ el.textContent = target.toLocaleString('en-US') + suf; return; }
    function step(t){
      if(!t0) t0 = t;
      var p = Math.min((t-t0)/dur,1), e = 1-Math.pow(1-p,3);
      el.textContent = Math.round(target*e).toLocaleString('en-US') + suf;
      if(p<1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if('IntersectionObserver' in window){
    var io2 = new IntersectionObserver(function(en){
      en.forEach(function(x){ if(x.isIntersecting){ countUp(x.target); io2.unobserve(x.target); } });
    },{threshold:.4});
    nums.forEach(function(n){ io2.observe(n); });
  } else { nums.forEach(countUp); }

  /* ---- scroll progress + band parallax ---- */
  var prog = document.getElementById('prog'), ticking = false;
  var bands = Array.prototype.slice.call(document.querySelectorAll('.band img'));
  function onScroll(){
    if(ticking) return; ticking = true;
    requestAnimationFrame(function(){
      if(prog){
        var h = document.documentElement.scrollHeight - innerHeight;
        prog.style.width = (h>0 ? (scrollY/h)*100 : 0) + '%';
      }
      if(!reduce){
        for(var i=0;i<bands.length;i++){
          var b = bands[i], r = b.parentNode.getBoundingClientRect();
          if(r.bottom > 0 && r.top < innerHeight){
            var p = (r.top + r.height/2 - innerHeight/2) / innerHeight;
            b.style.transform = 'translate3d(0,' + (p * -8) + '%,0)';
          }
        }
      }
      ticking = false;
    });
  }
  addEventListener('scroll', onScroll, {passive:true}); onScroll();

  /* ---- card glow follows pointer (desktop only) ---- */
  if(matchMedia('(hover:hover)').matches){
    document.querySelectorAll('.card').forEach(function(c){
      c.addEventListener('pointermove', function(e){
        var r = c.getBoundingClientRect();
        c.style.setProperty('--mx',(e.clientX-r.left)+'px');
        c.style.setProperty('--my',(e.clientY-r.top)+'px');
      });
    });
  }

  /* ---- HERO: wireframe terrain with subsurface copper anomaly ---- */
  (function terrain(){
    var cv = document.getElementById('terrain');
    if(!cv) return;
    var ctx = cv.getContext('2d'), W = cv.width, H = cv.height;
    var COLS = 46, ROWS = 30;
    var HORIZON = -43, SPREAD = W*0.70, DEPTH = 483, EV = 110;
    var ANOM = {x:0.10, z:0.44}, LIFT = -118;
    var t = 0, raf = null, running = false;

    function elev(x, z, time){
      var e = Math.sin(x*2.6 + time*0.22) * 0.30
            + Math.sin(z*3.1 - time*0.16) * 0.24
            + Math.sin((x+z)*4.4 + time*0.12) * 0.14
            + Math.sin(x*7.3 - z*5.1) * 0.07;
      e += Math.exp(-Math.pow((x + z*0.55 + 0.15)*2.4, 2)) * 0.42;
      return e;
    }
    function proj(x, z, time, lift){
      var s = 1 / (1 + z*2.15);
      var e = elev(x, z, time);
      return { x: W/2 + x*SPREAD*s, y: HORIZON + DEPTH*s - (e*EV + (lift||0))*s, s: s, e: e };
    }
    function draw(){
      ctx.clearRect(0,0,W,H);
      var a = proj(ANOM.x, ANOM.z, t, LIFT);
      var pulse = 0.62 + Math.sin(t*1.5)*0.20;
      var r = 155 * a.s * (1 + Math.sin(t*1.5)*0.05);
      var g = ctx.createRadialGradient(a.x, a.y, 0, a.x, a.y, r);
      g.addColorStop(0,   'rgba(255,214,170,'+(0.60*pulse)+')');
      g.addColorStop(0.35,'rgba(240,168,104,'+(0.32*pulse)+')');
      g.addColorStop(0.7, 'rgba(200,117,51,'+(0.13*pulse)+')');
      g.addColorStop(1,   'rgba(200,117,51,0)');
      ctx.save(); ctx.translate(a.x, a.y); ctx.scale(1, 0.60);
      ctx.fillStyle = g;
      ctx.beginPath(); ctx.arc(0, 0, r, 0, 6.283); ctx.fill();
      ctx.restore();

      ctx.lineWidth = 1;
      for(var k=1;k<=3;k++){
        ctx.strokeStyle = 'rgba(240,168,104,'+(0.22/k*pulse)+')';
        ctx.beginPath();
        ctx.ellipse(a.x, a.y, r*0.30*k, r*0.19*k, 0, 0, 6.283);
        ctx.stroke();
      }
      for(var j=ROWS; j>=0; j--){
        var z = j/ROWS;
        var fade = 0.10 + (1-z)*0.62;
        ctx.beginPath();
        for(var i=0;i<=COLS;i++){
          var x = (i/COLS - 0.5)*2;
          var p = proj(x, z, t);
          i ? ctx.lineTo(p.x,p.y) : ctx.moveTo(p.x,p.y);
        }
        var near = Math.exp(-Math.pow((z-ANOM.z)*3.4,2));
        ctx.strokeStyle = 'rgba('+Math.round(150+105*near)+','+Math.round(170-40*near)+','+Math.round(190-110*near)+','+ fade +')';
        ctx.lineWidth = 0.6 + (1-z)*0.9;
        ctx.stroke();
      }
      for(var i2=0;i2<=COLS;i2+=3){
        var x2 = (i2/COLS - 0.5)*2;
        ctx.beginPath();
        for(var j2=0;j2<=ROWS;j2++){
          var p2 = proj(x2, j2/ROWS, t);
          j2 ? ctx.lineTo(p2.x,p2.y) : ctx.moveTo(p2.x,p2.y);
        }
        ctx.strokeStyle = 'rgba(140,160,190,0.13)';
        ctx.lineWidth = 0.6;
        ctx.stroke();
      }
      var top = proj(ANOM.x, ANOM.z, t);
      var prog2 = (Math.sin(t*0.55 - 1.57)+1)/2;
      var bitY = top.y + (a.y - top.y) * prog2;
      ctx.setLineDash([5,5]);
      ctx.strokeStyle = 'rgba(79,191,168,.55)'; ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.moveTo(top.x, top.y); ctx.lineTo(top.x, a.y + 10); ctx.stroke();
      ctx.setLineDash([]);
      ctx.strokeStyle = 'rgba(240,168,104,.95)'; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(top.x, top.y); ctx.lineTo(top.x, bitY); ctx.stroke();
      ctx.fillStyle = '#ffe3c4';
      ctx.beginPath(); ctx.arc(top.x, bitY, 3.4, 0, 6.283); ctx.fill();
      ctx.strokeStyle = 'rgba(255,227,196,.35)';
      ctx.beginPath(); ctx.arc(top.x, bitY, 8+4*Math.sin(t*3), 0, 6.283); ctx.stroke();
      ctx.strokeStyle = 'rgba(79,191,168,.9)'; ctx.lineWidth = 1.4;
      ctx.beginPath(); ctx.moveTo(top.x-9, top.y); ctx.lineTo(top.x+9, top.y); ctx.stroke();

      var hz = ctx.createLinearGradient(0, 0, 0, 96);
      hz.addColorStop(0,'rgba(7,10,14,.92)');
      hz.addColorStop(1,'rgba(7,10,14,0)');
      ctx.fillStyle = hz; ctx.fillRect(0,0,W,96);
    }
    function loop(){ t += 0.016; draw(); raf = requestAnimationFrame(loop); }
    function start(){ if(!running && !reduce){ running = true; loop(); } }
    function stop(){ running = false; cancelAnimationFrame(raf); }
    draw();
    if(reduce) return;
    if('IntersectionObserver' in window){
      new IntersectionObserver(function(en){ en[0].isIntersecting ? start() : stop(); },{threshold:.05}).observe(cv);
    } else start();
    document.addEventListener('visibilitychange',function(){ document.hidden ? stop() : start(); });
  })();

  /* ---- copper dust particles ---- */
  var cv = document.getElementById('dust');
  if(!cv) return;
  if(reduce){ cv.style.display='none'; return; }
  var ctx = cv.getContext('2d'), dpr = Math.min(devicePixelRatio||1, 1.5), ps = [], W, H, raf, visible = true;
  function size(){
    W = cv.width  = innerWidth*dpr; H = cv.height = innerHeight*dpr;
    cv.style.width = innerWidth+'px'; cv.style.height = innerHeight+'px';
    var n = innerWidth < 700 ? 18 : 40;
    ps = []; for(var i=0;i<n;i++) ps.push({
      x:Math.random()*W, y:Math.random()*H,
      r:(Math.random()*1.5+.4)*dpr,
      vx:(Math.random()-.5)*.12*dpr, vy:(-Math.random()*.22-.05)*dpr,
      a:Math.random()*.5+.15
    });
  }
  function drawDust(){
    ctx.clearRect(0,0,W,H);
    for(var i=0;i<ps.length;i++){
      var p = ps[i];
      p.x += p.vx; p.y += p.vy;
      if(p.y < -10){ p.y = H+10; p.x = Math.random()*W; }
      if(p.x < -10) p.x = W+10; else if(p.x > W+10) p.x = -10;
      ctx.beginPath(); ctx.arc(p.x,p.y,p.r,0,6.283);
      ctx.fillStyle = 'rgba(240,168,104,'+p.a+')'; ctx.fill();
    }
    raf = requestAnimationFrame(drawDust);
  }
  var rt; addEventListener('resize',function(){ clearTimeout(rt); rt = setTimeout(size,200); },{passive:true});
  document.addEventListener('visibilitychange',function(){
    if(document.hidden){ cancelAnimationFrame(raf); visible=false; }
    else if(!visible){ visible=true; drawDust(); }
  });
  size(); drawDust();
})();
