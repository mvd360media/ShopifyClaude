# Crea las páginas legales en la tienda (ejecutar desde la raíz del proyecto).
# NOTA (2026-10-17): estas páginas se sustituyeron por las políticas de Shopify; se conserva como referencia.
import sys,json; sys.path.insert(0,'herramientas'); from gql import run
EMAIL="pedidos@ojoconesedetalle.es"
PEND='<strong>[PENDIENTE: nombre o razón social, NIF y dirección del titular]</strong>'
paginas=[
("Envíos y plazos","envios",True,f"""
<p>Enviamos a toda España peninsular y Baleares. Si vives en Canarias, Ceuta o Melilla, escríbenos antes de comprar.</p>
<h2>¿Cuánto tarda?</h2>
<ul><li><strong>Preparación:</strong> 1–3 días laborables desde que haces el pedido.</li>
<li><strong>Plazo total de entrega:</strong> entre 7 y 15 días laborables (sin contar fines de semana ni festivos).</li></ul>
<p>Cuando tu pedido salga, te enviaremos por email el número de seguimiento.</p>
<h2>Fechas señaladas</h2>
<p>Para Navidad, pide antes del 1 de diciembre. Para Reyes, antes del 12 de diciembre. Después de esas fechas no podemos garantizar la entrega a tiempo.</p>
<h2>Gastos de envío</h2>
<p>Los gastos de envío se muestran antes de pagar, en la pantalla de finalizar compra.</p>
<h2>Retrasos o incidencias</h2>
<p>Si tu pedido supera los 15 días laborables o llega dañado, escríbenos a <a href="mailto:{EMAIL}">{EMAIL}</a> con tu número de pedido y lo solucionamos.</p>
<p>Algunos productos pueden llegar en envíos separados o sin la caja original del fabricante; cuando sea así, lo indicamos en la ficha del producto.</p>"""),
("Devoluciones","devoluciones",True,f"""
<p>Tienes <strong>14 días naturales</strong> desde que recibes tu pedido para devolverlo sin dar explicaciones (derecho de desistimiento).</p>
<h2>Cómo devolver un producto</h2>
<ol><li>Escríbenos a <a href="mailto:{EMAIL}">{EMAIL}</a> con tu número de pedido e indica qué quieres devolver.</li>
<li>Te responderemos con la dirección y las instrucciones de envío.</li>
<li>Envía el producto en buen estado, sin usar y, si es posible, con su embalaje.</li></ol>
<h2>Reembolso</h2>
<p>Te devolvemos el importe pagado, incluidos los gastos de envío estándar, en un máximo de 14 días desde que nos comunicas la devolución. Podemos esperar a recibir el producto (o la prueba de que lo has enviado) antes de hacer el reembolso. Lo haremos por el mismo método de pago que usaste.</p>
<p>Los gastos de devolver el producto corren a tu cargo, salvo que el producto esté defectuoso o no corresponda con lo que pediste.</p>
<h2>Productos defectuosos</h2>
<p>Si un producto llega roto o no funciona, escríbenos con una foto en un plazo de 14 días. Te enviamos uno nuevo o te devolvemos el dinero, sin coste para ti. Además, tienes la garantía legal de 3 años para productos nuevos.</p>
<h2>Excepciones</h2>
<p>Por higiene, no se aceptan devoluciones de productos de cuidado personal que se hayan desprecintado, salvo que estén defectuosos.</p>"""),
("Términos y condiciones","terminos",True,f"""
<p>Estas condiciones regulan las compras en ojoconesedetalle.es. Al hacer un pedido, las aceptas.</p>
<h2>Quiénes somos</h2>
<p>La tienda pertenece al titular indicado en nuestro <a href="/pages/aviso-legal">Aviso legal</a>. Puedes contactarnos en <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Precios y pago</h2>
<p>Los precios incluyen IVA. Los gastos de envío se muestran antes de pagar. El pago se realiza de forma segura en la pantalla de finalizar compra con los métodos disponibles.</p>
<h2>Pedidos</h2>
<p>Recibirás un email de confirmación tras tu compra. Si un producto se agota después de tu pedido, te avisaremos y te devolveremos el importe íntegro.</p>
<h2>Envíos</h2>
<p>Consulta plazos y condiciones en <a href="/pages/envios">Envíos y plazos</a>.</p>
<h2>Devoluciones y garantía</h2>
<p>Tienes 14 días para devolver tu pedido y la garantía legal de 3 años. Más información en <a href="/pages/devoluciones">Devoluciones</a>.</p>
<h2>Fotos y descripciones</h2>
<p>Intentamos que las fotos y descripciones sean fieles al producto. Puede haber pequeñas diferencias de color o acabado.</p>
<h2>Ley aplicable</h2>
<p>Estas condiciones se rigen por la ley española. Como consumidor, puedes acudir a los tribunales de tu domicilio.</p>"""),
("Aviso legal","aviso-legal",False,f"""
<p>En cumplimiento de la Ley 34/2002 de Servicios de la Sociedad de la Información (LSSI), te informamos de que este sitio web pertenece a:</p>
<ul><li><strong>Titular:</strong> {PEND}</li><li><strong>Email:</strong> {EMAIL}</li></ul>
<h2>Uso del sitio</h2>
<p>Al navegar por esta web aceptas usarla de forma lícita. Los textos, imágenes y diseño son propiedad del titular o se usan con permiso, y no pueden copiarse sin autorización.</p>
<h2>Responsabilidad</h2>
<p>Hacemos lo posible para que la información sea correcta y esté actualizada, pero no nos hacemos responsables de errores puntuales ni del contenido de webs externas enlazadas.</p>"""),
("Política de privacidad","privacidad",False,f"""
<p><strong>Responsable del tratamiento:</strong> {PEND}. Email: {EMAIL}.</p>
<h2>Qué datos usamos y para qué</h2>
<p>Usamos tu nombre, email, teléfono y dirección para gestionar tus pedidos, envíos y devoluciones y para atender tus consultas. Si te suscribes, también para enviarte novedades (puedes darte de baja en cualquier momento).</p>
<h2>Base legal</h2>
<p>La ejecución del contrato de compra, el cumplimiento de obligaciones legales (por ejemplo, fiscales) y tu consentimiento en el caso de las comunicaciones comerciales.</p>
<h2>Con quién los compartimos</h2>
<p>Con los proveedores necesarios para que la tienda funcione: la plataforma de la tienda y el pago (Shopify), las empresas de transporte y nuestros proveedores de producto para el envío. No vendemos tus datos.</p>
<h2>Cuánto tiempo</h2>
<p>Mientras sea necesario para tu pedido y durante los plazos que exige la ley.</p>
<h2>Tus derechos</h2>
<p>Puedes pedir acceso, rectificación, supresión, oposición, limitación y portabilidad escribiendo a {EMAIL}. Si crees que no hemos tratado bien tus datos, puedes reclamar ante la Agencia Española de Protección de Datos (aepd.es).</p>"""),
]
m='''mutation($p:PageCreateInput!){pageCreate(page:$p){page{id handle isPublished} userErrors{field message}}}'''
for title,handle,pub,body in paginas:
    print(json.dumps(run(m,{"p":{"title":title,"handle":handle,"isPublished":pub,"body":body.strip()}}),ensure_ascii=False))
