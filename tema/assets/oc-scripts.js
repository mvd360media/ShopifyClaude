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
      var principal = g.querySelector('.oc-galeria__principal img');
      g.querySelectorAll('.oc-galeria__miniaturas button').forEach(function (b) {
        b.addEventListener('click', function () {
          principal.src = b.getAttribute('data-src');
          principal.srcset = '';
          principal.alt = b.getAttribute('data-alt') || '';
          g.querySelectorAll('.oc-galeria__miniaturas button').forEach(function (x) { x.setAttribute('aria-current', 'false'); });
          b.setAttribute('aria-current', 'true');
        });
      });
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

  function init() { initReveal(); initCuentaAtras(); initGaleria(); initVariantes(); initPersonalizacion(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
  document.addEventListener('shopify:section:load', init);
})();
