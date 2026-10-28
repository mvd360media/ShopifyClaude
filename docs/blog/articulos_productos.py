# Artículos del blog "Ideas de regalo" ligados a los productos personalizados (ejecutar con python3 docs/blog/articulos_productos.py).
# Solo datos del fabricante y de las políticas de la tienda. Enlaces internos a productos, colecciones y la guía de fotos.
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "herramientas"))
from gql import run

BLOG = "gid://shopify/Blog/135166329223"
B = "Ojoconesedetalle"
POR = json.load(open('/tmp/claude-0/portadas.json')) if os.path.exists('/tmp/claude-0/portadas.json') else {}
U = {"P1": "/products/colgante-personalizado-foto-mascota", "P2": "/products/adorno-navidad-personalizado-mascota",
     "P3": "/products/collar-nombre-personalizado", "P4": "/products/llavero-personalizado-foto-mascota",
     "P5": "/products/collar-foto-proyeccion", "P6": "/products/colgante-cenizas-mascota"}
GUIA = '<a href="/pages/como-elegir-la-foto">cómo elegir la foto perfecta</a>'

A = [
dict(handle="regalos-para-amantes-de-los-perros-y-gatos", img="P1", tags=["Mascotas", "Regalos personalizados"],
 title="Regalos para amantes de los perros y los gatos: ideas personalizadas que emocionan",
 seo=(f"Regalos para amantes de perros y gatos | {B}", "Ideas de regalos personalizados para amantes de los perros y los gatos: colgantes, llaveros y adornos con la foto o el nombre de su mascota."),
 summary="<p>Si alguien de tu entorno habla de su perro o su gato como de un miembro más de la familia, un regalo con su mascota siempre acierta. Te dejamos ideas para todos los presupuestos.</p>",
 body=f"""<p>Para quien quiere a su mascota como a uno más de la familia, el mejor regalo es el que la incluye. Un detalle con la <strong>foto o el nombre de su perro o su gato</strong> se recuerda mucho más que cualquier regalo genérico. Estas son nuestras ideas.</p>
<h2>1. Un colgante con la foto de su mascota</h2>
<p>El <a href="{U['P1']}">colgante personalizado con foto de mascota</a> lleva grabada la imagen de su perro o su gato en un colgante redondo de acero inoxidable de 20 mm, con su nombre o un texto corto. Puedes elegir entre rosado, dorado o plateado y tres largos de cadena. Es el regalo ideal para una «mamá perruna».</p>
<h2>2. Un llavero para llevarla a todas partes</h2>
<p>Si buscas algo práctico, el <a href="{U['P4']}">llavero personalizado con foto de mascota</a> lleva la foto grabada en un corazón de acero de 30 × 30 mm y, por detrás, su nombre, una frase o una fecha. Un regalo que usará cada día.</p>
<h2>3. Un adorno para que tenga su sitio en el árbol</h2>
<p>En Navidad, el <a href="{U['P2']}">adorno de Navidad personalizado</a> es una huella de madera de 8 cm con el nombre de la mascota recortado. Hay tres diseños y huella de perro o de gato. Perfecto también para el amigo invisible.</p>
<h2>4. Un recuerdo para una mascota que ya no está</h2>
<p>Cuando la mascota ha fallecido, el <a href="{U['P6']}">colgante para cenizas de mascota</a> es una forma delicada de acompañar el duelo: un corazón con su foto y su nombre que guarda un poco de sus cenizas o de su pelo. Tienes más ideas en nuestra colección <a href="/collections/recuerdo-mascotas">Recuerdo de mascotas</a>.</p>
<h2>Cómo acertar con un regalo personalizado</h2>
<ul>
<li><strong>Consigue una buena foto:</strong> nítida, de frente y con buena luz. Te explicamos {GUIA}.</li>
<li><strong>Revisa el texto dos veces:</strong> se graba tal y como lo escribes.</li>
<li><strong>Pide con tiempo:</strong> se fabrican bajo pedido. En cada producto verás la fecha límite para recibirlo antes de Navidad o de Reyes.</li>
</ul>
<p>Encuentra todas las ideas en nuestra colección <a href="/collections/mascotas">Regalos para amantes de las mascotas</a>.</p>"""),
dict(handle="colgante-para-cenizas-de-mascota", img="P6", tags=["Recuerdo de mascotas", "Mascotas"],
 title="Colgante para cenizas de mascota: qué es, cómo se rellena y cómo elegirlo",
 seo=(f"Colgante para cenizas de mascota: guía | {B}", "Qué es un colgante para cenizas de mascota, cómo se rellena paso a paso, qué se puede guardar dentro y cómo personalizarlo con su foto y su nombre."),
 summary="<p>Perder a una mascota duele. Un colgante para cenizas permite llevar una pequeña parte de ella siempre cerca. Te explicamos cómo funciona y cómo elegirlo.</p>",
 body=f"""<p>Despedirse de una mascota es de las cosas más difíciles. Muchas personas buscan una forma de <strong>tenerla cerca</strong> después de su marcha, y el colgante para cenizas es una de las más discretas y bonitas.</p>
<h2>¿Qué es un colgante para cenizas?</h2>
<p>Es una joya con un pequeño compartimento interior donde se guarda una cantidad mínima de cenizas o un poco de pelo de la mascota. Por fuera parece un colgante normal; solo tú sabes lo que lleva dentro.</p>
<h2>Cómo se rellena</h2>
<ol>
<li>Abre el compartimento: en nuestro <a href="{U['P6']}">colgante para cenizas de mascota</a>, la parte superior del corazón se abre girándola.</li>
<li>Con el kit de relleno que incluye, introduce con cuidado una pequeña cantidad de cenizas o de pelo.</li>
<li>Vuelve a cerrar girando la pieza hasta el final.</li>
</ol>
<p>Hazlo despacio, sobre una superficie lisa y con buena luz.</p>
<h2>Cómo personalizarlo</h2>
<ul>
<li><strong>Por delante:</strong> su foto grabada con láser y su nombre.</li>
<li><strong>Por detrás:</strong> hasta tres frases cortas (menos de 15 caracteres cada una), como «Siempre conmigo» o una fecha.</li>
</ul>
<p>Para que el grabado salga bien, elige una foto donde se vea bien su cara. Te ayudamos con {GUIA}.</p>
<h2>Qué tener en cuenta al elegirlo</h2>
<ul>
<li><strong>Material:</strong> el nuestro es de acero inoxidable.</li>
<li><strong>Tamaño:</strong> el corazón mide 2,5 × 2 cm y la cadena, 50 cm.</li>
<li><strong>Si es un regalo:</strong> es un detalle de apoyo muy agradecido para alguien que acaba de perder a su mascota.</li>
</ul>
<p>Más ideas en nuestra colección <a href="/collections/recuerdo-mascotas">Recuerdo de mascotas</a>.</p>"""),
dict(handle="collar-con-nombre-personalizado-como-elegir", img="P3", tags=["Joyería personalizada", "Para ella"],
 title="Collar con nombre personalizado: cómo elegir tipografía, color y largo de cadena",
 seo=(f"Collar con nombre: elige letra y largo | {B}", "Guía para elegir tu collar con nombre personalizado: qué tipografía escoger, plateado o dorado, qué largo de cadena queda mejor y qué nombre poner."),
 summary="<p>Un collar con nombre es de esos regalos que no fallan. Para que quede perfecto, te contamos cómo elegir la letra, el color y el largo de la cadena.</p>",
 body=f"""<p>El <a href="{U['P3']}">collar con nombre personalizado</a> es un clásico que nunca pasa de moda: el nombre recortado en acero inoxidable, colgando de una cadena fina. Estas son las tres decisiones que lo hacen único.</p>
<h2>1. La tipografía</h2>
<p>Tenemos 23 tipografías. Al elegir una en la ficha verás una muestra con un nombre de ejemplo.</p>
<ul>
<li><strong>Si el nombre es largo,</strong> elige una letra cursiva fina: se lee mejor.</li>
<li><strong>Si es corto,</strong> una letra más gruesa o con adornos destaca más.</li>
<li><strong>Para dos nombres,</strong> están las tipografías «Dos nombres» e «Infinito».</li>
</ul>
<h2>2. El color</h2>
<p>Puedes elegirlo en <strong>plateado o dorado</strong>. El plateado combina con todo y es más discreto; el dorado llama más la atención y queda muy bien con ropa de colores cálidos.</p>
<h2>3. El largo de la cadena</h2>
<ul>
<li><strong>40 cm:</strong> queda cerca de la base del cuello, visible con casi cualquier escote.</li>
<li><strong>45 cm:</strong> el más habitual; cae un poco más abajo.</li>
<li><strong>50 cm:</strong> cae sobre el pecho; ideal para llevarlo por encima de un jersey.</li>
</ul>
<h2>Qué nombre poner</h2>
<p>El tuyo, el de tu pareja, el de tus hijos… o el de tu mascota. Escríbelo con cuidado: lo cortamos tal y como lo escribes, con sus mayúsculas, minúsculas y tildes.</p>
<h2>Cuánto tarda</h2>
<p>Se fabrica bajo pedido: el plazo estimado de entrega es de 3 a 4 semanas. Mira la fecha límite para Navidad junto al botón de compra.</p>
<p>Más ideas en <a href="/collections/joyeria-personalizada">Joyería personalizada</a> y <a href="/collections/para-ella">Regalos para ella</a>.</p>"""),
dict(handle="collar-con-foto-dentro-como-funciona", img="P5", tags=["Joyería personalizada", "San Valentín", "Para ella"],
 title="Collar con foto dentro: cómo funciona el colgante de proyección y cómo se ve la foto",
 seo=(f"Collar con foto dentro: cómo funciona | {B}", "Cómo funciona un collar con foto dentro (de proyección): dónde va la foto, cómo se ve, qué plantilla elegir y qué foto funciona mejor."),
 summary="<p>Parece un colgante normal, pero esconde una foto que solo aparece al mirar a través de la piedra. Así funciona el collar de proyección.</p>",
 body=f"""<p>El <a href="{U['P5']}">collar con foto dentro</a> (también llamado collar de proyección) guarda una foto dentro de una pequeña piedra. A simple vista es un colgante bonito; cuando acercas la piedra al ojo, aparece la imagen.</p>
<h2>¿Cómo se ve la foto?</h2>
<ol>
<li>Acerca la piedra al ojo, a pocos centímetros.</li>
<li>Busca una fuente de luz detrás, como una ventana o una lámpara.</li>
<li>Mira a través de la piedra: verás la foto.</li>
</ol>
<h2>Las tres plantillas</h2>
<ul>
<li><strong>A:</strong> solo la foto.</li>
<li><strong>B:</strong> la foto rodeada de «te quiero» en 100 idiomas.</li>
<li><strong>C:</strong> la foto dentro de un corazón con «te quiero» en varios idiomas.</li>
</ul>
<h2>Qué foto funciona mejor</h2>
<p>La imagen se ve en pequeño, así que funcionan mejor las fotos <strong>sencillas, con pocas personas y buena luz</strong>. Una foto de pareja o de dos personas de cerca es ideal. Más consejos en {GUIA}.</p>
<h2>A quién regalarlo</h2>
<ul>
<li><strong>A tu pareja:</strong> por San Valentín o vuestro aniversario.</li>
<li><strong>A tu madre:</strong> con una foto de la familia.</li>
<li><strong>A tu mejor amiga:</strong> un recuerdo secreto que solo vosotras conocéis.</li>
</ul>
<p>Elige entre muchos modelos (corazón, huella, luna, estrella…) y tres colores: plateado, dorado o rosado. Lo tienes en <a href="/collections/joyeria-personalizada">Joyería personalizada</a>.</p>"""),
dict(handle="frases-para-grabar-colgante-llavero-mascota", img="P4", tags=["Mascotas", "Ideas"],
 title="40 frases cortas para grabar en el colgante o el llavero de tu mascota",
 seo=(f"Frases cortas para grabar con tu mascota | {B}", "Ideas de frases cortas para grabar en un colgante, llavero o adorno con la foto o el nombre de tu mascota: cariñosas, divertidas y de recuerdo."),
 summary="<p>¿No sabes qué poner junto a la foto de tu mascota? Te dejamos frases cortas que caben en un colgante, un llavero o un adorno.</p>",
 body=f"""<p>En una joya o un llavero el espacio es pequeño, así que la frase tiene que ser <strong>corta y con significado</strong>. Antes de elegir, mira el límite de caracteres de cada producto: el <a href="{U['P1']}">colgante con foto</a> admite 20, las frases del <a href="{U['P6']}">colgante para cenizas</a> menos de 15 y el reverso del <a href="{U['P4']}">llavero con foto</a> 40.</p>
<h2>Cariñosas</h2>
<ul><li>Mi mejor amigo</li><li>Mi persona favorita</li><li>Amor de cuatro patas</li><li>Mi compañero</li><li>Contigo siempre</li><li>Mi peludo</li><li>Mi niña</li><li>Mi bebé peludo</li><li>Te quiero</li><li>Mi familia</li></ul>
<h2>Divertidas</h2>
<ul><li>Jefe de la casa</li><li>Ladrón de sofás</li><li>Experto en siestas</li><li>Pide galletas</li><li>Rey del barrio</li><li>Guau</li><li>Miau</li><li>Mal ejemplo</li><li>Cero obediencia</li><li>Pura energía</li></ul>
<h2>De recuerdo</h2>
<ul><li>Siempre conmigo</li><li>Nunca olvidado</li><li>Siempre amado</li><li>Para siempre</li><li>En mi corazón</li><li>Gracias por todo</li><li>Hasta pronto</li><li>Mi ángel</li><li>Te echo de menos</li><li>Inolvidable</li></ul>
<h2>Con fechas</h2>
<ul><li>Su nombre y el año en que llegó (por ejemplo, «Lila 2019»)</li><li>Fecha de nacimiento y despedida</li><li>«Desde 2020»</li><li>«2012 – 2026»</li><li>El día que os conocisteis</li><li>Su cumpleaños</li><li>Las iniciales y el año</li><li>«Mi primer perro»</li><li>«Mi primer gato»</li><li>«Mi familia desde 2018»</li></ul>
<h2>Consejos antes de grabar</h2>
<ul>
<li>Cuenta los espacios: también son caracteres.</li>
<li>Revisa tildes, mayúsculas y minúsculas: se graba tal cual.</li>
<li>Combina una frase corta con una buena foto. Te explicamos {GUIA}.</li>
</ul>
<p>Encuentra todos los regalos en <a href="/collections/mascotas">Regalos para amantes de las mascotas</a>.</p>"""),
dict(handle="regalos-personalizados-navidad-fechas-limite", img="P2", tags=["Navidad", "Regalos personalizados"],
 title="Regalos personalizados para Navidad y Reyes 2026: fechas límite para recibirlos a tiempo",
 seo=(f"Regalos personalizados Navidad 2026 | {B}", "Ideas de regalos personalizados para Navidad y Reyes 2026 y la fecha límite de cada uno para recibirlo a tiempo. Se fabrican bajo pedido."),
 summary="<p>Los regalos personalizados se fabrican bajo pedido, así que hay que pedirlos con tiempo. Aquí tienes las fechas límite de cada uno para Navidad y Reyes.</p>",
 body=f"""<p>Un regalo personalizado se hace <strong>a medida cuando haces el pedido</strong>. Por eso, en Navidad conviene pedirlo antes que cualquier otro regalo. Estas son las fechas límite de esta temporada: son el último día para pedir y aumentan las posibilidades de recibirlo a tiempo, aunque no garantizan una fecha concreta.</p>
<h2>Fechas límite por producto</h2>
<ul>
<li><a href="{U['P3']}"><strong>Collar con nombre personalizado</strong></a>: Navidad, hasta el 15 de noviembre; Reyes, hasta el 28 de noviembre.</li>
<li><a href="{U['P1']}"><strong>Colgante con foto de mascota</strong></a>: Navidad, hasta el 24 de noviembre; Reyes, hasta el 7 de diciembre.</li>
<li><a href="{U['P5']}"><strong>Collar con foto dentro</strong></a>: Navidad, hasta el 24 de noviembre; Reyes, hasta el 7 de diciembre.</li>
<li><a href="{U['P6']}"><strong>Colgante para cenizas de mascota</strong></a>: Navidad, hasta el 27 de noviembre; Reyes, hasta el 10 de diciembre.</li>
<li><a href="{U['P4']}"><strong>Llavero con foto de mascota</strong></a>: Navidad, hasta el 28 de noviembre; Reyes, hasta el 11 de diciembre.</li>
<li><a href="{U['P2']}"><strong>Adorno de Navidad personalizado</strong></a>: Navidad, hasta el 29 de noviembre; Reyes, hasta el 12 de diciembre.</li>
</ul>
<p>En cada producto, junto al botón de compra, verás siempre la fecha que toca.</p>
<h2>Ideas según a quién se lo regales</h2>
<ul>
<li><strong>Para ella:</strong> un collar con su nombre o con una foto dentro. Mira <a href="/collections/para-ella">Regalos para ella</a>.</li>
<li><strong>Para él:</strong> un llavero con la foto de su perro. Mira <a href="/collections/para-el">Regalos para él</a>.</li>
<li><strong>Para el amigo invisible:</strong> el adorno de Navidad con el nombre de su mascota. Mira <a href="/collections/amigo-invisible">Amigo invisible</a>.</li>
<li><strong>Para quien perdió a su mascota este año:</strong> un recuerdo con su foto. Mira <a href="/collections/recuerdo-mascotas">Recuerdo de mascotas</a>.</li>
</ul>
<h2>Tres consejos para que llegue perfecto</h2>
<ol>
<li>Ten la foto preparada antes de pedir: te contamos {GUIA}.</li>
<li>Revisa el nombre o la frase antes de pagar.</li>
<li>Si te equivocas, tienes 2 horas desde la compra para cancelar un pedido personalizado.</li>
</ol>
<p>Todos los regalos de la temporada están en nuestra colección <a href="/collections/navidad">Especial Navidad</a>.</p>"""),
]

ya = {a['handle'] for a in run('{blog(id:"%s"){articles(first:100){nodes{handle}}}}' % BLOG, mutate=False)['blog']['articles']['nodes']}
m = '''mutation($a:ArticleCreateInput!){articleCreate(article:$a){article{handle} userErrors{field message}}}'''
for a in A:
    if a['handle'] in ya:
        print('ya existe', a['handle']); continue
    assert len(a['seo'][0]) <= 60 and len(a['seo'][1]) <= 160, (a['handle'], len(a['seo'][0]), len(a['seo'][1]))
    inp = {"blogId": BLOG, "title": a['title'], "handle": a['handle'], "body": a['body'], "summary": a['summary'], "tags": a['tags'],
           "isPublished": False, "author": {"name": "Ojo Con Ese Detalle"},
           "metafields": [{"namespace": "global", "key": "title_tag", "type": "single_line_text_field", "value": a['seo'][0]},
                          {"namespace": "global", "key": "description_tag", "type": "single_line_text_field", "value": a['seo'][1]}]}
    if a['img'] in POR:
        inp["image"] = {"url": POR[a['img']]['image']['url'], "altText": POR[a['img']]['alt'] or a['title']}
    print(json.dumps(run(m, {"a": inp}), ensure_ascii=False))
