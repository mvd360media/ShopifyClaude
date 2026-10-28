# Contenido de las fichas P3-P6 (datos solo del fabricante). Lo aplica herramientas/aplicar_fichas.py.
B = "Ojoconesedetalle"
DEV = "<p><strong>¿Puedo devolverlo?</strong><br>Al ser un producto personalizado, no se aplica el derecho de desistimiento de 14 días. Si llega defectuoso o dañado, tienes 3 años de garantía legal.</p>"
PAGO = "<p><strong>¿Tendré que pagar algo al recibirlo?</strong><br>No. El precio que ves es el precio final del producto.</p>"
FOTO = """<h2>Consejos para la foto</h2>
<ul>
<li>Usa una foto <strong>nítida y con buena luz</strong>, mejor de día.</li>
<li>Elige una imagen en la que se vea bien la <strong>cara</strong>, de frente.</li>
<li>Sube el archivo original, sin capturas de pantalla ni filtros.</li>
<li>Solo se admiten fotos en <strong>JPG o PNG</strong>. Si usas iPhone y tu foto no se sube, ve a Ajustes &gt; Cámara &gt; Formatos y elige «Más compatible».</li>
</ul>
<p>Más ideas en nuestra guía <a href="/pages/como-elegir-la-foto">Cómo elegir la foto perfecta</a>.</p>"""

FICHAS = {
"P3": dict(
 id="16661129953671", plantilla="collar-nombre", categoria="aa-6-8", tipo="Collar personalizado",
 titulo="Collar con Nombre Personalizado – Acero Inoxidable Plateado o Dorado",
 url="collar-nombre-personalizado",
 seo_t=f"Collar con Nombre Personalizado | {B}",
 seo_d="Collar con nombre personalizado en acero inoxidable, plateado o dorado. Elige entre 23 tipografías y el largo de la cadena. Un regalo único para ella.",
 etiquetas=["collar con nombre personalizado","colgante con nombre","collar nombre acero","collar personalizado","regalo personalizado","regalo para ella","joyería personalizada","acero inoxidable","para-ella"],
 meta=dict(subtitulo="Tu nombre recortado en acero inoxidable, con 23 tipografías para elegir.", material="Acero inoxidable", medida_colgante="Aprox. 51,7 × 20,3 mm (varía según el nombre)", personalizacion="Nombre y tipografía"),
 para_quien=["Ella","Pareja"], ocasion=["Cumpleaños","Navidad","San Valentín","Aniversario"],
 colecciones=["regalos-personalizados","joyeria-personalizada"],
 desc=f"""<p><strong>Collar con nombre personalizado: el nombre que más quieres, siempre contigo.</strong></p>
<p>Este <strong>collar con nombre</strong> lleva recortado en <strong>acero inoxidable</strong> el nombre que tú elijas: el tuyo, el de tu pareja, el de tu hijo o el de tu mascota. Es un <strong>colgante con nombre</strong> de línea fina que se lleva a diario y un regalo personalizado que no falla.</p>
<h2>Cómo personalizar tu collar</h2>
<ol>
<li>Elige la <strong>tipografía</strong>: tienes 23 modelos de letra (al elegir una, verás su muestra en las fotos).</li>
<li>Elige el <strong>color y el largo</strong> de la cadena.</li>
<li>Escribe el <strong>nombre</strong> que quieres. Revisa bien la ortografía: lo cortamos tal y como lo escribes.</li>
<li>Añade el collar al carrito y finaliza tu pedido.</li>
</ol>
<h2>Un regalo con significado</h2>
<ul>
<li><strong>Para ella:</strong> su nombre o el de alguien especial, para cumpleaños, aniversarios o Navidad.</li>
<li><strong>Para parejas:</strong> con las tipografías «Dos nombres» o «Infinito» caben los nombres de los dos.</li>
<li><strong>Para mamá:</strong> con el nombre de sus hijos.</li>
</ul>
<h2>Características</h2>
<ul>
<li><strong>Material:</strong> acero inoxidable</li>
<li><strong>Colores:</strong> plateado o dorado</li>
<li><strong>Colgante:</strong> aprox. 51,7 × 20,3 mm; el tamaño final se ajusta al nombre</li>
<li><strong>Peso:</strong> 4,5 g</li>
<li><strong>Cadena:</strong> de eslabones</li>
<li><strong>Tipografías:</strong> 23 modelos</li>
</ul>
<h2>Preguntas frecuentes</h2>
<p><strong>¿Qué puedo personalizar?</strong><br>El nombre, la tipografía, el color y el largo de la cadena.</p>
<p><strong>¿Puedo poner dos nombres?</strong><br>Sí, con las tipografías «Dos nombres» e «Infinito».</p>
<p><strong>¿Cuánto tarda en llegar?</strong><br>Lo fabricamos después de tu pedido. El plazo estimado de entrega es de 3 a 4 semanas. Junto al botón de compra verás la fecha límite para recibirlo antes de Navidad o de Reyes.</p>
{PAGO}
{DEV}
<p><strong>Elige tu tipografía, escribe el nombre y crea hoy tu collar.</strong></p>
<p><strong>Te puede interesar:</strong> <a href="/blogs/ideas-de-regalo/collar-con-nombre-personalizado-como-elegir">Cómo elegir tipografía, color y largo de tu collar con nombre</a></p>""",
 pers=dict(titulo="Personaliza tu collar", foto_activa=False, texto_activo=True, texto_etiqueta="Nombre", texto_obligatorio=True, texto_max=15,
           texto_ayuda="Revisa bien la ortografía: lo cortamos tal y como lo escribes. Para dos nombres, elige la tipografía «Dos nombres» o «Infinito».",
           tipo_activa=False, confirmacion_texto="He revisado el nombre. Sé que los productos personalizados no se pueden devolver por desistimiento."),
 extras=[],
 opciones={"Metal Color":("Tipografía",{"Two name font":"Dos nombres","Infinite font":"Infinito"}),
           "Length":("Color y largo",{"Silver and 35cm":"Plateado · 35 cm","Silver and 40cm":"Plateado · 40 cm","Silver and 45cm":"Plateado · 45 cm","Silver and 50cm":"Plateado · 50 cm","Silver and 60cm":"Plateado · 60 cm","Gold and 35cm":"Dorado · 35 cm","Gold and 40cm":"Dorado · 40 cm","Gold and 45cm":"Dorado · 45 cm"})},
),
"P4": dict(
 id="16661067465095", plantilla="llavero-foto", categoria="aa-4-1", tipo="Llavero personalizado",
 titulo="Llavero Personalizado con Foto de tu Mascota – Corazón de Acero Grabado",
 url="llavero-personalizado-foto-mascota",
 seo_t=f"Llavero con Foto de tu Mascota | {B}",
 seo_d="Llavero personalizado con la foto de tu perro o gato grabada en un corazón de acero inoxidable, con nombre, frase o fecha por detrás. Un regalo único.",
 etiquetas=["llavero personalizado con foto de mascota","llavero foto perro","llavero grabado mascota","llavero personalizado","regalo amantes de perros","recuerdo mascota","regalo personalizado","acero inoxidable","para-el"],
 meta=dict(subtitulo="Tu mascota grabada en un corazón de acero, con nombre o frase por detrás.", material="Acero inoxidable 304", medida_colgante="30 × 30 mm", personalizacion="Foto de tu mascota (JPG o PNG) y texto para el reverso"),
 para_quien=["Amantes de las mascotas","Él","Ella"], ocasion=["Cumpleaños","Navidad","Recuerdo"],
 colecciones=["regalos-personalizados","mascotas","recuerdo-mascotas"],
 desc=f"""<p><strong>Llavero personalizado con la foto de tu mascota: llévala contigo cada vez que coges las llaves.</strong></p>
<p>Este <strong>llavero con foto de tu perro o gato</strong> lleva la imagen de tu mascota <strong>grabada con láser</strong> en un corazón de acero inoxidable con huellas recortadas. Por detrás puedes grabar su nombre, una frase o una fecha. Un <strong>llavero grabado</strong> para el día a día o para recordar a una mascota que ya no está.</p>
<h2>Cómo personalizar tu llavero</h2>
<ol>
<li><strong>Sube la foto</strong> de tu mascota (JPG o PNG, hasta 10 MB).</li>
<li>Escribe, si quieres, el <strong>texto para el reverso</strong>: su nombre, una frase o una fecha.</li>
<li>Añade el llavero al carrito y finaliza tu pedido.</li>
</ol>
{FOTO}
<p>El corazón mide 30 × 30 mm, así que el resultado final depende de la calidad de la foto. La foto se graba en tonos grises, no en color.</p>
<h2>Un regalo con significado</h2>
<ul>
<li><strong>Para amantes de los perros y los gatos:</strong> un detalle para cumpleaños o Navidad.</li>
<li><strong>Para él:</strong> un regalo práctico que va a usar todos los días.</li>
<li><strong>En recuerdo de tu mascota:</strong> una forma de llevarla siempre cerca.</li>
</ul>
<h2>Características</h2>
<ul>
<li><strong>Material:</strong> acero inoxidable 304</li>
<li><strong>Forma:</strong> corazón con huellas recortadas</li>
<li><strong>Medida:</strong> 30 × 30 mm</li>
<li><strong>Grabado:</strong> láser; foto por delante y texto por detrás</li>
<li><strong>Uso:</strong> para llaves o bolsos</li>
</ul>
<h2>Preguntas frecuentes</h2>
<p><strong>¿Qué puedo personalizar?</strong><br>La foto de tu mascota por delante y un texto corto por detrás.</p>
<p><strong>¿Sale la foto en color?</strong><br>No: se graba con láser sobre el acero, en tonos grises.</p>
<p><strong>¿Cuánto tarda en llegar?</strong><br>Lo fabricamos después de tu pedido. El plazo estimado de entrega es de 2 a 3 semanas. Junto al botón de compra verás la fecha límite para recibirlo antes de Navidad o de Reyes.</p>
{PAGO}
{DEV}
<p><strong>Sube la foto de tu mascota y crea hoy tu llavero.</strong></p>
<p><strong>Te puede interesar:</strong> <a href="/blogs/ideas-de-regalo/frases-para-grabar-colgante-llavero-mascota">40 frases cortas para grabar en el llavero</a> · <a href="/blogs/ideas-de-regalo/regalos-para-amantes-de-los-perros-y-gatos">Regalos para amantes de los perros y los gatos</a></p>""",
 pers=dict(titulo="Personaliza tu llavero", foto_activa=True, foto_etiqueta="Foto de tu mascota", foto_obligatoria=True, foto_max_mb=10,
           foto_ayuda="JPG o PNG, hasta 10 MB. Mejor una foto nítida, de frente y con buena luz.",
           texto_activo=True, texto_etiqueta="Texto para el reverso", texto_obligatorio=False, texto_max=40,
           texto_ayuda="Opcional: nombre, frase o fecha. Revísalo bien: lo grabamos tal y como lo escribes.",
           tipo_activa=False, confirmacion_texto="He revisado la foto y el texto. Sé que los productos personalizados no se pueden devolver por desistimiento."),
 extras=[], opciones={},
),
"P5": dict(
 id="16661046067591", plantilla="collar-proyeccion", categoria="aa-6-8", tipo="Collar personalizado",
 titulo="Collar con Foto Dentro – Colgante de Proyección Personalizado",
 url="collar-foto-proyeccion",
 seo_t=f"Collar con Foto Dentro (Proyección) | {B}",
 seo_d="Collar con foto dentro: mira a través de la piedra y verás tu foto. Elige modelo, color y plantilla «Te quiero» en 100 idiomas. Un regalo para tu pareja.",
 etiquetas=["collar con foto dentro","colgante con foto proyectada","collar foto oculta","collar proyección","te quiero en 100 idiomas","regalo para ella","regalo san valentín","regalo personalizado","para-ella"],
 meta=dict(subtitulo="Mira a través de la piedra y aparece tu foto.", material="Acero inoxidable y cobre", personalizacion="Foto (JPG o PNG) y plantilla A, B o C"),
 para_quien=["Ella","Pareja"], ocasion=["San Valentín","Aniversario","Navidad","Cumpleaños"],
 colecciones=["regalos-personalizados","joyeria-personalizada"],
 desc=f"""<p><strong>Collar con foto dentro: un recuerdo secreto que solo aparece cuando miras a través de la piedra.</strong></p>
<p>Este <strong>colgante con foto proyectada</strong> guarda tu foto favorita dentro de una pequeña piedra. A simple vista parece un colgante normal; al acercar la piedra al ojo, aparece la foto. Es un <strong>collar con foto oculta</strong> para regalar a tu pareja, a tu madre o a tu mejor amiga.</p>
<h2>Cómo personalizar tu collar</h2>
<ol>
<li>Elige el <strong>modelo</strong> y el <strong>color</strong>.</li>
<li>Elige la <strong>plantilla</strong>: A (solo la foto), B (la foto rodeada de «te quiero» en 100 idiomas) o C (la foto dentro de un corazón con «te quiero» en varios idiomas).</li>
<li><strong>Sube la foto</strong> (JPG o PNG, hasta 15 MB).</li>
<li>Añade el collar al carrito y finaliza tu pedido.</li>
</ol>
{FOTO}
<h2>Un regalo con significado</h2>
<ul>
<li><strong>Para tu pareja:</strong> vuestra foto, para San Valentín o vuestro aniversario.</li>
<li><strong>Para mamá:</strong> una foto de la familia que puede llevar siempre.</li>
<li><strong>Para tu mejor amiga:</strong> un recuerdo que solo vosotras sabéis que está ahí.</li>
</ul>
<h2>Características</h2>
<ul>
<li><strong>Material:</strong> acero inoxidable y cobre</li>
<li><strong>Colores:</strong> plateado, dorado o rosado</li>
<li><strong>Foto:</strong> micrograbada dentro de la piedra</li>
<li><strong>Plantillas:</strong> 3 (A, B y C)</li>
</ul>
<h2>Preguntas frecuentes</h2>
<p><strong>¿Cómo se ve la foto?</strong><br>Acerca la piedra al ojo, mejor con luz, y mira a través de ella.</p>
<p><strong>¿Qué puedo personalizar?</strong><br>La foto, la plantilla, el modelo y el color.</p>
<p><strong>¿Cuánto tarda en llegar?</strong><br>Lo fabricamos después de tu pedido. El plazo estimado de entrega es de 2 a 3 semanas. Junto al botón de compra verás la fecha límite para recibirlo antes de Navidad o de Reyes.</p>
{PAGO}
{DEV}
<p><strong>Elige tu foto favorita y guárdala para siempre en un collar.</strong></p>
<p><strong>Te puede interesar:</strong> <a href="/blogs/ideas-de-regalo/collar-con-foto-dentro-como-funciona">Cómo funciona el collar con foto dentro</a></p>""",
 pers=dict(titulo="Personaliza tu collar", foto_activa=True, foto_etiqueta="Foto", foto_obligatoria=True, foto_max_mb=15,
           foto_ayuda="JPG o PNG, hasta 15 MB. Mejor una foto nítida y con buena luz.",
           texto_activo=False, texto_etiqueta="Texto", texto_obligatorio=False, texto_max=20, texto_ayuda="",
           tipo_activa=True, tipo_etiqueta="Plantilla", tipo_opciones="A · Solo la foto, B · Foto con «te quiero» en 100 idiomas, C · Foto en un corazón con «te quiero»",
           tipo_ayuda="Mira las tres plantillas en las fotos del producto.",
           confirmacion_texto="He revisado la foto y la plantilla. Sé que los productos personalizados no se pueden devolver por desistimiento."),
 extras=[],
 opciones={"Metal Color":("Modelo",{"custom photo-1":"Corazón","custom photo-23":"Huella","custom photo-7":"Candado","custom photo-8":"Redondo","custom photo-20":"Corazón «mom»"}),
           "Main Stone Color":("Color",{"Rose gold":"Rosado","Silver":"Plateado","Gold":"Dorado"})},
),
"P6": dict(
 id="16661036564871", plantilla="colgante-cenizas", categoria="aa-6-8", tipo="Colgante personalizado",
 titulo="Colgante para Cenizas de Mascota – Corazón Grabado con Foto y Nombre",
 url="colgante-cenizas-mascota",
 seo_t=f"Colgante para Cenizas de Mascota | {B}",
 seo_d="Colgante para cenizas de mascota en forma de corazón de acero inoxidable, grabado con su foto y su nombre. Guarda un poco de sus cenizas o de su pelo.",
 etiquetas=["colgante para cenizas de mascota","colgante urna mascota","recuerdo mascota fallecida","colgante cenizas perro","colgante cenizas gato","recuerdo mascota","colgante personalizado","acero inoxidable"],
 meta=dict(subtitulo="Un corazón con su foto y su nombre para llevar siempre una parte de tu mascota.", material="Acero inoxidable", medida_colgante="2,5 × 2 cm", personalizacion="Foto, nombre y hasta 3 frases cortas por detrás"),
 para_quien=["Amantes de las mascotas"], ocasion=["Recuerdo"],
 colecciones=["regalos-personalizados","mascotas","recuerdo-mascotas","joyeria-personalizada"],
 desc=f"""<p><strong>Colgante para cenizas de mascota: una forma de llevar siempre cerca a quien te acompañó tantos años.</strong></p>
<p>Este <strong>colgante urna para mascota</strong> tiene forma de corazón y es de <strong>acero inoxidable</strong>. Por delante lleva grabados su foto y su nombre; por detrás, hasta tres frases cortas. La parte de arriba se abre girándola y deja un pequeño hueco para guardar un poco de sus cenizas o de su pelo.</p>
<h2>Cómo personalizar tu colgante</h2>
<ol>
<li><strong>Sube la foto</strong> de tu mascota (JPG o PNG, hasta 10 MB).</li>
<li>Escribe su <strong>nombre</strong>.</li>
<li>Si quieres, añade hasta <strong>tres frases cortas</strong> para la parte de atrás (menos de 15 caracteres cada una).</li>
<li>Añade el colgante al carrito y finaliza tu pedido.</li>
</ol>
{FOTO}
<h2>Un recuerdo con significado</h2>
<ul>
<li><strong>Para ti:</strong> para llevar cerca una parte de tu mascota.</li>
<li><strong>Para alguien que ha perdido a su mascota:</strong> un detalle de apoyo que se agradece.</li>
</ul>
<h2>Características</h2>
<ul>
<li><strong>Material:</strong> acero inoxidable</li>
<li><strong>Colgante:</strong> corazón de 2,5 × 2 cm</li>
<li><strong>Cadena:</strong> tipo caja, 50 cm</li>
<li><strong>Compartimento:</strong> se abre girando la parte superior</li>
<li><strong>Incluye:</strong> kit de relleno</li>
<li><strong>Grabado:</strong> láser; foto y nombre por delante, hasta 3 frases por detrás</li>
</ul>
<h2>Preguntas frecuentes</h2>
<p><strong>¿Qué puedo guardar dentro?</strong><br>Una pequeña cantidad de cenizas o un poco de pelo.</p>
<p><strong>¿Qué puedo personalizar?</strong><br>La foto y el nombre por delante, y hasta tres frases cortas por detrás.</p>
<p><strong>¿Cuánto tarda en llegar?</strong><br>Lo fabricamos después de tu pedido. El plazo estimado de entrega es de 2 a 3 semanas. Junto al botón de compra verás la fecha límite para recibirlo antes de Navidad o de Reyes.</p>
{PAGO}
{DEV}
<p><strong>Sube su foto y crea un recuerdo para llevarlo siempre contigo.</strong></p>
<p><strong>Te puede interesar:</strong> <a href="/blogs/ideas-de-regalo/colgante-para-cenizas-de-mascota">Colgante para cenizas: qué es y cómo se rellena</a> · <a href="/blogs/ideas-de-regalo/frases-para-grabar-colgante-llavero-mascota">Frases cortas de recuerdo para grabar</a></p>""",
 pers=dict(titulo="Personaliza tu colgante", foto_activa=True, foto_etiqueta="Foto de tu mascota", foto_obligatoria=True, foto_max_mb=10,
           foto_ayuda="JPG o PNG, hasta 10 MB. Mejor una foto con la cara bien visible y buena luz.",
           texto_activo=True, texto_etiqueta="Nombre de tu mascota", texto_obligatorio=True, texto_max=15,
           texto_ayuda="Se graba por delante, bajo la foto.",
           tipo_activa=False, confirmacion_texto="He revisado la foto y los textos. Sé que los productos personalizados no se pueden devolver por desistimiento."),
 extras=[dict(etiqueta="Frase 1 (detrás)", obligatorio=False, max=14, ayuda="Por ejemplo: Siempre conmigo."),
         dict(etiqueta="Frase 2 (detrás)", obligatorio=False, max=14, ayuda=""),
         dict(etiqueta="Frase 3 (detrás)", obligatorio=False, max=14, ayuda="")],
 opciones={"Metal Color":("Modelo",{"Pet Ashes Necklace":"Corazón para cenizas"})},
),
}
