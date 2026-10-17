# Crea los artículos del blog "Ideas de regalo" (ejecutar con python3 docs/blog/articulos.py).
import json,sys,os; sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","..","herramientas"))
from gql import run
BLOG="gid://shopify/Blog/135166329223"; CDN="https://cdn.shopify.com/s/files/1/1107/0472/2311/files/"
B="Ojo Con Ese Detalle"
A=[]
A.append(dict(title="Calendario de adviento de tela: 24 ideas para rellenarlo",handle="ideas-para-rellenar-calendario-adviento",
img=("oc-t-menos20.jpg","Calendario de adviento de tela con bolsillos para rellenar y chocolate caliente"),
tags=["Navidad","Calendario de adviento"],
seo=(f"24 ideas para rellenar un calendario de adviento | {B}","Ideas para rellenar un calendario de adviento de tela: dulces, detalles, actividades y sorpresas para niños, parejas y adultos."),
summary="<p>Un calendario de adviento de tela se reutiliza cada año y lo rellenas a tu gusto. Te dejamos 24 ideas, una por día, para niños, parejas y adultos.</p>",
body="""<p>Los calendarios de adviento de tela tienen una gran ventaja frente a los de cartón: <strong>los rellenas tú</strong> y sirven para muchos años. Eso sí, llenar 24 bolsillos da para pensar. Aquí tienes ideas para todos los gustos y presupuestos.</p>
<h2>Ideas dulces (las clásicas que nunca fallan)</h2>
<ol><li>Bombones o chocolatinas individuales.</li><li>Galletas de jengibre caseras.</li><li>Caramelos de su sabor favorito.</li><li>Turrón en porciones pequeñas.</li><li>Una bolsita de chocolate a la taza para preparar juntos.</li></ol>
<h2>Detalles pequeños que hacen ilusión</h2>
<ol start="6"><li>Pegatinas o tatuajes temporales.</li><li>Un llavero curioso.</li><li>Calcetines navideños enrollados.</li><li>Una vela pequeña aromática.</li><li>Un bálsamo labial.</li><li>Una mini figura o adorno para el árbol.</li><li>Pinzas o gomas para el pelo.</li></ol>
<h2>Planes y actividades (cero gasto, mucho recuerdo)</h2>
<ol start="13"><li>Vale por una noche de película con palomitas.</li><li>Vale por un desayuno en la cama.</li><li>Salir a ver las luces de Navidad.</li><li>Hacer juntos galletas o un roscón.</li><li>Escribir la carta a los Reyes Magos.</li><li>Decorar el árbol o el belén.</li><li>Una tarde de juegos de mesa.</li></ol>
<h2>Para parejas y adultos</h2>
<ol start="20"><li>Una nota con un recuerdo bonito de este año.</li><li>Vale por un masaje.</li><li>Una mini botella de licor o un té especial.</li><li>Una lista de canciones hecha a medida.</li><li>Para el día 24: una pista que lleve al regalo grande.</li></ol>
<h2>Trucos para que quede bonito</h2>
<ul><li>Envuelve los detalles en papel de seda: así no se adivina lo que hay dentro.</li><li>Alterna días dulces con días de planes para que no se haga repetitivo.</li><li>Guarda los regalos más especiales para los fines de semana.</li><li>Si es para niños, deja preparado el bolsillo del día la noche anterior.</li></ul>
<p>¿Aún no tienes calendario? Nuestro <a href="/products/calendario-adviento-tela-24-bolsillos">calendario de adviento de tela de 24 bolsillos</a> se cuelga en la pared y se rellena año tras año. Encuéntralo en la <a href="/collections/navidad">colección de Navidad</a>.</p>"""))
A.append(dict(title="Ideas para el amigo invisible por menos de 20 €",handle="ideas-amigo-invisible-menos-de-20",
img=("oc-t-amigo.jpg","Regalos pequeños envueltos para el amigo invisible con una etiqueta misteriosa"),
tags=["Navidad","Amigo invisible","Menos de 20 €"],
seo=(f"Ideas para el amigo invisible por menos de 20 € | {B}","Ideas de regalo para el amigo invisible por menos de 20 €: detalles originales para la oficina, la familia o los amigos que siempre aciertan."),
summary="<p>¿Te ha tocado alguien a quien casi no conoces? Estas ideas para el amigo invisible por menos de 20 € aciertan en la oficina, en la familia y con los amigos.</p>",
body="""<p>El amigo invisible tiene una regla de oro: <strong>presupuesto ajustado y regalo que no parezca de compromiso</strong>. Y casi siempre te toca la persona que menos conoces. Estas ideas funcionan aunque no sepas mucho de quien te ha tocado.</p>
<h2>Si es de la oficina</h2>
<ul><li><strong>Algo para el escritorio:</strong> una libreta bonita, un organizador o una taza original.</li><li><strong>Un detalle para la pausa del café:</strong> un té especial o chocolate de calidad.</li><li><strong>Algo útil para el día a día:</strong> un cargador portátil pequeño o una botella térmica.</li></ul>
<h2>Si es de la familia</h2>
<ul><li><strong>Decoración navideña:</strong> un adorno especial o un <a href="/products/calendario-adviento-tela-24-bolsillos">calendario de adviento de tela para rellenar</a>, que además sirve para todos los años.</li><li><strong>Algo para casa:</strong> una vela aromática o una manta pequeña.</li><li><strong>Un juego de mesa rápido</strong> para la sobremesa de Navidad.</li></ul>
<h2>Si es de tu grupo de amigos</h2>
<ul><li><strong>Algo con humor:</strong> un regalo que haga referencia a una anécdota compartida.</li><li><strong>Un capricho:</strong> un producto de cuidado personal o unos calcetines originales.</li><li><strong>Una experiencia pequeña:</strong> entradas de cine o un vale para un café.</li></ul>
<h2>Cuatro reglas para no fallar</h2>
<ol><li><strong>Respeta el presupuesto.</strong> Pasarse incomoda tanto como quedarse corto.</li><li><strong>Mejor útil que decorativo</strong> si no conoces sus gustos.</li><li><strong>Cuida el envoltorio:</strong> un buen papel y un lazo hacen que el regalo parezca más.</li><li><strong>Incluye el tique regalo</strong> por si quiere cambiarlo.</li></ol>
<p>Hemos reunido nuestras ideas en dos colecciones: <a href="/collections/amigo-invisible">Amigo invisible</a> y <a href="/collections/menos-de-20">Regalos de menos de 20 €</a>. Recuerda pedir antes del 1 de diciembre si el intercambio es antes de Navidad.</p>"""))
A.append(dict(title="Máscara LED facial: qué es, cómo se usa y qué esperar",handle="mascara-led-facial-que-es-como-se-usa",
img=("oc-h-blackfriday.jpg","Máscara LED facial blanca encendida en luz roja"),
tags=["Belleza","Black Friday","Para ella"],
seo=(f"Máscara LED facial: qué es y cómo usarla en casa | {B}","Qué es una máscara LED facial, qué significa cada color de luz, cómo usarla en casa paso a paso y qué precauciones tener."),
summary="<p>Las máscaras LED faciales se han convertido en uno de los regalos de belleza más buscados. Te contamos qué son, cómo se usan y qué precauciones tener.</p>",
body="""<p>Las máscaras LED faciales llevan años en los centros de estética y ahora se pueden usar en casa. Son uno de los regalos de belleza más buscados, pero conviene saber qué son y cómo se usan antes de comprar una.</p>
<h2>¿Qué es una máscara LED facial?</h2>
<p>Es una máscara que cubre el rostro y lleva diodos LED en su interior. Emite luz de distintos colores (longitudes de onda) que se utilizan en estética como <strong>complemento de la rutina de cuidado de la piel</strong>. No sustituye a ningún tratamiento médico ni dermatológico.</p>
<h2>Qué significa cada color</h2>
<ul><li><strong>Luz roja (630 nm):</strong> la más usada en rutinas antiedad y para piel madura.</li><li><strong>Luz azul (470 nm):</strong> habitual en rutinas para piel grasa o con imperfecciones.</li><li><strong>Luz verde (520 nm):</strong> asociada a pieles con tono irregular.</li><li><strong>Colores combinados</strong> (amarillo, morado, cian, blanco): mezclan las anteriores.</li></ul>
<h2>Cómo usarla paso a paso</h2>
<ol><li>Limpia y seca bien la cara, sin maquillaje.</li><li>Colócate la máscara y ajusta la cinta.</li><li>Enciéndela y elige el color.</li><li>Mantén los ojos cerrados durante la sesión.</li><li>Al terminar, aplica tu sérum o crema habitual.</li></ol>
<p>Los fabricantes suelen recomendar <strong>sesiones de 10 a 30 minutos</strong>, varias veces por semana. La constancia es más importante que la duración de cada sesión.</p>
<h2>Precauciones</h2>
<ul><li>No la uses mientras se está cargando.</li><li>Consulta con tu médico antes de usarla si estás embarazada, tienes epilepsia o fotosensibilidad, tomas medicación fotosensibilizante o tienes alguna enfermedad ocular o de la piel.</li><li>Uso exclusivo para adultos.</li></ul>
<h2>Qué mirar antes de comprar</h2>
<ul><li><strong>Inalámbrica o con cable:</strong> sin cables puedes moverte por casa durante la sesión.</li><li><strong>Batería:</strong> fíjate en la autonomía por carga.</li><li><strong>Número de colores y de LED:</strong> más LED reparten mejor la luz por todo el rostro.</li></ul>
<p>Nuestra <a href="/products/mascara-led-facial-7-colores">máscara LED facial inalámbrica de 7 colores</a> tiene 60 LED, carga por USB-C y dos versiones de batería. Del 20 al 30 de noviembre la encontrarás con 5 € menos en la <a href="/collections/black-friday">colección Black Friday</a>.</p>"""))
m='''mutation($a:ArticleCreateInput!){articleCreate(article:$a){article{id handle} userErrors{field message}}}'''
for a in A:
  inp={"blogId":BLOG,"title":a["title"],"handle":a["handle"],"body":a["body"],"summary":a["summary"],"tags":a["tags"],"isPublished":True,
       "author":{"name":B},"image":{"url":CDN+a["img"][0],"altText":a["img"][1]},
       "metafields":[{"namespace":"global","key":"title_tag","type":"single_line_text_field","value":a["seo"][0]},{"namespace":"global","key":"description_tag","type":"single_line_text_field","value":a["seo"][1]}]}
  print(json.dumps(run(m,{"a":inp}),ensure_ascii=False))
