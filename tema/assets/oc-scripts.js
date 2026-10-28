/* Ojo Con Ese Detalle — interacciones propias */
(function () {
  function initReveal() {
    var els = document.querySelectorAll('.oc-reveal:not(.oc-visible)');
    if (!els.length) return;
    if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      els.forEach(function (el) { el.classList.add('oc-visible'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('oc-visible'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    els.forEach(function (el) { io.observe(el); });
  }

  function initCuentaAtras() {
    document.querySelectorAll('[data-oc-fin]').forEach(function (el) {
      var fin = new Date(el.getAttribute('data-oc-fin') + 'T23:59:59');
      var out = el.querySelector('b');
      if (isNaN(fin) || !out) return;
      var tick = function () {
        var ms = fin - new Date();
        if (ms <= 0) { out.textContent = el.getAttribute('data-oc-terminado') || 'Terminado'; return; }
        var d = Math.floor(ms / 864e5), h = Math.floor(ms / 36e5) % 24, m = Math.floor(ms / 6e4) % 60;
        out.textContent = d + ' d ' + h + ' h ' + m + ' min';
      };
      tick();
      setInterval(tick, 30000);
    });
  }

  function initGaleria() {
    document.querySelectorAll('[data-oc-galeria]').forEach(function (g) {
      if (g.dataset.ocListo) return;
      g.dataset.ocListo = '1';
      var principal = g.querySelector('.oc-galeria__principal img');
      var botones = Array.prototype.slice.call(g.querySelectorAll('.oc-galeria__miniaturas button'));
      var contador = g.querySelector('[data-oc-contador-fotos]');
      if (!principal || !botones.length) return;
      var actual = Math.max(0, botones.findIndex(function (b) { return b.getAttribute('aria-current') === 'true'; }));
      var mostrar = function (i, desplazar) {
        actual = (i + botones.length) % botones.length;
        var b = botones[actual];
        principal.src = b.getAttribute('data-src');
        principal.srcset = '';
        principal.alt = b.getAttribute('data-alt') || '';
        botones.forEach(function (x) { x.setAttribute('aria-current', 'false'); });
        b.setAttribute('aria-current', 'true');
        if (contador) contador.textContent = (actual + 1) + ' / ' + botones.length;
        if (desplazar !== false) b.scrollIntoView({ block: 'nearest', inline: 'nearest' });
      };
      botones.forEach(function (b, i) { b.addEventListener('click', function () { mostrar(i); }); });
      var ant = g.querySelector('[data-oc-ant]'), sig = g.querySelector('[data-oc-sig]');
      if (ant) ant.addEventListener('click', function () { mostrar(actual - 1); });
      if (sig) sig.addEventListener('click', function () { mostrar(actual + 1); });
      g.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowLeft') mostrar(actual - 1);
        if (e.key === 'ArrowRight') mostrar(actual + 1);
      });
      // permite que las variantes muestren su foto
      g.ocMostrarMedia = function (id) {
        var i = botones.findIndex(function (b) { return b.getAttribute('data-media-id') === String(id); });
        if (i > -1) mostrar(i);
      };
      if (contador) contador.textContent = (actual + 1) + ' / ' + botones.length;
    });
  }

  function initVariantes() {
    document.querySelectorAll('[data-oc-producto]').forEach(function (root) {
      var data = root.querySelector('script[data-oc-variantes]');
      if (!data) return;
      var variantes = JSON.parse(data.textContent);
      var input = root.querySelector('input[name="id"]');
      var boton = root.querySelector('.oc-compra__boton');
      var precio = root.querySelector('[data-oc-precio]');
      var tachado = root.querySelector('[data-oc-tachado]');
      var formato = root.getAttribute('data-oc-moneda') || '{{amount_with_comma_separator}} €';
      var dinero = function (c) {
        var n = (c / 100).toFixed(2).split('.');
        return formato.replace(/\{\{\s*amount_with_comma_separator\s*\}\}/, n[0].replace(/\B(?=(\d{3})+(?!\d))/g, '.') + ',' + n[1])
          .replace(/\{\{\s*amount\s*\}\}/, n[0] + '.' + n[1]);
      };
      var actualizar = function () {
        var sel = Array.prototype.map.call(root.querySelectorAll('.oc-opcion'), function (f) {
          var c = f.querySelector('input:checked');
          return c ? c.value : null;
        });
        var v = variantes.find(function (x) { return x.options.every(function (o, i) { return o === sel[i]; }); });
        if (!v) { boton.disabled = true; boton.textContent = boton.getAttribute('data-no-disponible'); return; }
        input.value = v.id;
        var galeria = document.querySelector('[data-oc-galeria]');
        if (v.media && galeria && galeria.ocMostrarMedia) galeria.ocMostrarMedia(v.media);
        precio.textContent = dinero(v.price);
        if (tachado) {
          tachado.textContent = v.compare_at_price > v.price ? dinero(v.compare_at_price) : '';
        }
        boton.disabled = !v.available;
        boton.textContent = v.available ? boton.getAttribute('data-texto') : boton.getAttribute('data-agotado');
        var url = new URL(window.location.href);
        url.searchParams.set('variant', v.id);
        window.history.replaceState({}, '', url.toString());
      };
      root.querySelectorAll('.oc-opcion input').forEach(function (i) { i.addEventListener('change', actualizar); });
    });
  }


  function initPersonalizacion() {
    document.querySelectorAll('[data-oc-pers]').forEach(function (pers) {
      if (pers.dataset.ocListo) return;
      pers.dataset.ocListo = '1';
      var form = pers.closest('form');
      var error = pers.querySelector('[data-oc-error]');
      pers.querySelectorAll('[data-oc-contador]').forEach(function (texto) {
        var cuenta = texto.parentNode.querySelector('[data-oc-cuenta]');
        if (!cuenta) return;
        var contar = function () { cuenta.textContent = Array.from(texto.value).length; };
        texto.addEventListener('input', contar);
        contar();
      });
      var fallo = function (campo, mensaje) {
        error.textContent = mensaje;
        error.hidden = false;
        if (campo) { campo.setAttribute('aria-invalid', 'true'); campo.focus(); }
        return false;
      };
      var validar = function () {
        pers.querySelectorAll('[aria-invalid]').forEach(function (c) { c.removeAttribute('aria-invalid'); });
        error.hidden = true;
        var campos = pers.querySelectorAll('input, select');
        for (var i = 0; i < campos.length; i++) {
          var c = campos[i];
          var nombre = c.getAttribute('data-oc-nombre') || (c.labels && c.labels[0] ? c.labels[0].textContent.replace('*', '').trim() : '');
          if (c.type === 'file') {
            var f = c.files[0];
            if (!f) { if (c.hasAttribute('data-oc-obligatorio')) return fallo(c, 'Sube la foto para continuar.'); continue; }
            if (!/\.(jpe?g|png)$/i.test(f.name)) return fallo(c, 'La foto tiene que ser JPG o PNG.');
            var max = parseFloat(c.getAttribute('data-oc-max-mb')) || 10;
            if (f.size > max * 1024 * 1024) return fallo(c, 'La foto pesa más de ' + max + ' MB. Prueba con otra o redúcela.');
          } else if (c.type === 'checkbox') {
            if (c.hasAttribute('data-oc-obligatorio') && !c.checked) return fallo(c, 'Marca la casilla para confirmar que has revisado tus datos.');
          } else {
            var valor = c.value.trim();
            if (c.hasAttribute('data-oc-obligatorio') && !valor) return fallo(c, 'Completa «' + nombre + '» para continuar.');
            var lim = parseInt(c.getAttribute('maxlength'), 10);
            if (lim && Array.from(valor).length > lim) return fallo(c, '«' + nombre + '» admite como máximo ' + lim + ' caracteres.');
          }
        }
        return true;
      };
      var fichero = pers.querySelector('[data-oc-fichero]');
      var foto = pers.querySelector('input[type=file]');
      if (foto && fichero) foto.addEventListener('change', function () { fichero.textContent = foto.files[0] ? foto.files[0].name : 'Ninguna foto elegida'; });
      pers.querySelectorAll('input, select').forEach(function (c) { c.addEventListener('change', function () { if (!error.hidden) validar(); }); });
      if (form) form.addEventListener('submit', function (e) { if (!validar()) e.preventDefault(); });
    });
  }


  function initCarritoEmergente() {
    document.querySelectorAll('[data-oc-producto][data-oc-ajax]').forEach(function (root) {
      if (root.dataset.ocAjaxListo) return;
      root.dataset.ocAjaxListo = '1';
      var form = root.querySelector('form[action*="/cart/add"]');
      var dialogo = root.parentNode.querySelector('[data-oc-emergente]') || document.querySelector('[data-oc-emergente]');
      if (!form || !dialogo || typeof dialogo.showModal !== 'function') return;
      var boton = form.querySelector('[type="submit"]');
      var error = form.querySelector('[data-oc-error]');
      dialogo.querySelectorAll('[data-oc-cerrar]').forEach(function (b) { b.addEventListener('click', function () { dialogo.close(); }); });
      dialogo.addEventListener('click', function (e) { if (e.target === dialogo) dialogo.close(); });
      form.addEventListener('submit', function (e) {
        if (e.defaultPrevented) return;
        e.preventDefault();
        var texto = boton ? boton.textContent : '';
        if (boton) { boton.disabled = true; boton.textContent = 'Añadiendo…'; }
        fetch(window.Shopify && Shopify.routes ? Shopify.routes.root + 'cart/add.js' : '/cart/add.js', {
          method: 'POST', body: new FormData(form), headers: { 'X-Requested-With': 'XMLHttpRequest', 'Accept': 'application/json' }
        }).then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
          .then(function (res) {
            if (boton) { boton.disabled = false; boton.textContent = texto; }
            if (!res.ok) {
              if (error) { error.textContent = res.j.description || 'No se ha podido añadir. Inténtalo de nuevo.'; error.hidden = false; }
              return;
            }
            var it = res.j;
            var img = it.image ? '<img src="' + it.image + '" alt="" width="72" height="72">' : '';
            var precio = it.final_line_price !== undefined ? (it.final_line_price / 100).toFixed(2).replace('.', ',') + ' €' : '';
            dialogo.querySelector('[data-oc-emergente-producto]').innerHTML = img + '<div><strong>' + it.product_title + '</strong><span>' +
              (it.variant_title && it.variant_title !== 'Default Title' ? it.variant_title : '') + '</span><span>' + precio + '</span></div>';
            dialogo.querySelectorAll('.oc-reveal').forEach(function (x) { x.classList.add('oc-visible'); });
            dialogo.showModal();
            fetch('/?sections=cart-icon-bubble').then(function (r) { return r.json(); }).then(function (s) {
              var b = document.getElementById('cart-icon-bubble');
              if (b && s['cart-icon-bubble']) {
                var tmp = document.createElement('div'); tmp.innerHTML = s['cart-icon-bubble'];
                var nuevo = tmp.querySelector('.shopify-section') || tmp;
                b.innerHTML = nuevo.innerHTML;
              }
            }).catch(function () {});
          })
          .catch(function () { if (boton) { boton.disabled = false; boton.textContent = texto; } form.submit(); });
      });
    });
  }

  function init() { initReveal(); initCuentaAtras(); initGaleria(); initVariantes(); initPersonalizacion(); initCarritoEmergente(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
  document.addEventListener('shopify:section:load', init);
})();
