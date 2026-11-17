(function(){
  var b=document.querySelector('.burger'),n=document.getElementById('nav');
  if(b&&n){b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)});}
  document.querySelectorAll('.ba').forEach(function(el){var r=el.querySelector('.ba-range');if(r)r.addEventListener('input',function(){el.style.setProperty('--pos',r.value+'%')});});
  document.querySelectorAll('.calc').forEach(function(c){
    var m=c.querySelector('#calc-m2'),f=c.querySelector('#calc-fin'),t=c.querySelector('#calc-teinte'),j=c.querySelector('#calc-joints'),o=c.querySelector('#calc-out'),res=c.querySelector('#calc-res');
    function up(){var s=+m.value,p=+f.value+(t.checked?12:0)+(j.checked?8:0);o.textContent=s;res.textContent=(s*p).toLocaleString('fr-FR')+' €';}
    [m,f,t,j].forEach(function(x){x.addEventListener('input',up);x.addEventListener('change',up)});up();
  });
  // Suivi des conversions (si GA4 configuré)
  function ev(name,p){if(window.gtag)gtag('event',name,p||{});}
  document.querySelectorAll('a[href^="tel:"]').forEach(function(a){a.addEventListener('click',function(){ev('clic_telephone')})});
  document.querySelectorAll('form.form').forEach(function(f){f.addEventListener('submit',function(){ev('generate_lead',{form:'devis'})})});
})();
