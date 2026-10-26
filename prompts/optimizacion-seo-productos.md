# PROMPT: Optimización SEO y organización de 3 productos en Shopify – Ojoconesedetalle

Actúa como especialista SEO en Shopify para el mercado de España, con acceso de administración a mi tienda «Ojoconesedetalle» (ccdf97-s7.myshopify.com). Vas a dejar perfectamente optimizadas, organizadas y vinculadas tres fichas de producto. Todo el contenido final ya está decidido y aparece abajo: tu trabajo es aplicarlo con exactitud, no reescribirlo.

## REGLAS OBLIGATORIAS

1. **No inventes datos.** Usa solo los textos de este prompt. Si algo no está, escribe [PENDIENTE: ...] en tu informe y no lo publiques.
2. **Pide confirmación antes de cualquier acción irreversible:** borrar imágenes, borrar valores de variantes, borrar productos, cambiar el estado de un producto, instalar una app o modificar el menú. Muéstrame primero la lista exacta de lo que vas a borrar o cambiar.
3. **Variantes: renombra, no recrees.** Las variantes están enlazadas a artículos del proveedor de AliExpress mediante una app de importación. No borres ni vuelvas a crear las variantes que se conservan: solo cambia el nombre de opciones y valores. Elimina solo los valores indicados.
4. **Todo en español de España.** No dejes textos en inglés visibles para el cliente (títulos, opciones, variantes, textos alternativos, nombres de archivo).
5. **Sin imágenes externas en las descripciones.** Elimina cualquier `<img>` que cargue desde aliexpress-media.com u otros dominios externos.
6. **Trabaja producto por producto** y al terminar cada uno dame un informe: hecho, pendiente y bloqueado (con el motivo).
7. **Si no puedes hacer algo** (por ejemplo, instalar una app o renombrar un archivo), no lo simules: explícame el paso exacto que tengo que hacer yo.

---

## FASE 1 – CONFIGURACIÓN GLOBAL DE LA TIENDA

### 1.1 Definiciones de metacampos de producto
Ruta: Configuración > Metacampos y metaobjetos > Productos. Créalas si no existen; si existen, no las dupliques. En todas: **un solo valor** y **acceso de la tienda online (Storefronts) activado**. Fija (pin) las que se usen.

| Nombre | Espacio de nombres y clave | Tipo |
|---|---|---|
| Subtítulo | custom.subtitulo | Texto de una sola línea |
| Colores de luz | custom.colores_luz | Número entero |
| Longitudes de onda | custom.longitudes_onda | Texto de una sola línea |
| Batería | custom.bateria | Texto de una sola línea |
| Número de bolsillos | custom.numero_bolsillos | Número entero |
| Material | custom.material | Texto de una sola línea |
| Medida del colgante | custom.medida_colgante | Texto de una sola línea |

Validaciones: ninguna. Las claves van sin tildes ni espacios.

### 1.2 Colecciones (manuales)
Crea las que no existan, cada una con título, descripción breve en español y URL limpia:

| Colección | URL |
|---|---|
| Cuidado facial | cuidado-facial |
| Navidad | navidad |
| Regalos personalizados | regalos-personalizados |
| Mascotas | mascotas |
| Joyería | joyeria |

Propón (sin aplicarlo hasta que lo confirme) cómo añadir estas colecciones al menú principal (Tienda online > Navegación).

### 1.3 Tema: mostrar el subtítulo
En Tienda online > Personalizar > plantilla de Productos, añade un bloque «Texto» debajo del título, conectado mediante origen dinámico a **custom.subtitulo**. Si el tema no lo permite, indícamelo.

---

## FASE 2 – REGLAS COMUNES DE IMÁGENES

**Conservar:** imágenes del producto real, limpias, sin promesas.

**Eliminar:**
- antes/después;
- porcentajes o resultados no verificables (por ejemplo «-31,15 %», «+34,3 %»);
- infografías en inglés con beneficios o afirmaciones;
- imágenes con especificaciones que contradicen la ficha (otras autonomías, «No box»);
- imágenes que muestran variantes que no se venden (por ejemplo, varios colgantes cuando solo se vende uno);
- duplicados.

**Orden:** la primera imagen es la principal (producto solo, fondo limpio).

**Nombre de archivo:** minúsculas, sin tildes, con guiones y empezando por la keyword principal del producto. Si Shopify no permite renombrar, descarga la imagen, renómbrala, súbela de nuevo y elimina la antigua.

**Texto alternativo:** describe lo que se ve en español, con la keyword principal de forma natural y en menos de 125 caracteres. Nada de «imagen de…» ni listas de palabras clave.

**Antes de borrar,** muéstrame una tabla con cada imagen (posición + descripción breve de lo que se ve) y tu decisión: conservar o eliminar, nuevo nombre de archivo y texto alternativo.

---

## FASE 3 – PRODUCTO 1: MÁSCARA LED FACIAL

**Título:**
Máscara LED Facial 7 Colores – Inalámbrica y Recargable

**Descripción** (sustituye todo el HTML):
```html
<p><strong>Máscara LED facial de 7 colores, inalámbrica y recargable: incorpora la luz LED a tu rutina de cuidado facial en casa.</strong></p>
<p>Esta <strong>máscara de luz LED para la cara</strong> reúne <strong>7 colores de luz</strong> en un solo dispositivo, sin cables y con un solo botón. Te la pones, eliges el color y la usas mientras lees o te relajas, sin pedir cita ni desplazarte a un centro de estética.</p>

<h2>¿Para qué sirve la máscara LED facial?</h2>
<p>La luz LED se utiliza en estética facial como complemento de la rutina de cuidado de la piel. Cada color corresponde a una longitud de onda distinta y se asocia a un objetivo diferente:</p>
<ul>
<li><strong>Rutina antiedad:</strong> la luz roja es la más utilizada en el cuidado de la piel madura.</li>
<li><strong>Piel con imperfecciones:</strong> la luz azul es la más habitual en rutinas para piel grasa o con tendencia acneica.</li>
<li><strong>Comodidad:</strong> sin cables y con carga USB-C, para usarla en cualquier rincón de casa.</li>
</ul>

<h2>Los 7 colores de la máscara LED</h2>
<p>Longitudes de onda y usos indicados por el fabricante:</p>
<ul>
<li><strong>Luz roja (630 nm):</strong> rutina antiedad.</li>
<li><strong>Luz azul (470 nm):</strong> piel grasa o con imperfecciones.</li>
<li><strong>Luz verde (520 nm):</strong> piel con tono irregular.</li>
<li><strong>Luz amarilla (630 + 520 nm):</strong> piel apagada.</li>
<li><strong>Luz morada (630 + 470 nm):</strong> combina la luz roja y la azul.</li>
<li><strong>Luz cian (470 + 520 nm):</strong> piel sensible.</li>
<li><strong>Luz blanca (470 + 520 + 630 nm):</strong> combina las tres longitudes de onda.</li>
</ul>

<h2>Cómo usar la máscara LED</h2>
<ol>
<li>Limpia y seca el rostro, sin maquillaje.</li>
<li>Colócate la máscara y ajusta la cinta.</li>
<li>Pulsa el botón para encenderla y elige el color.</li>
<li>Mantén los ojos cerrados durante la sesión.</li>
<li>Al terminar, aplica tu sérum o crema habitual.</li>
</ol>
<p>El fabricante recomienda sesiones de 10 a 30 minutos al día.</p>

<h2>Características (según el fabricante)</h2>
<ul>
<li><strong>Colores de luz:</strong> 7</li>
<li><strong>LEDs:</strong> 60 con chip RGB</li>
<li><strong>Longitudes de onda:</strong> 470 nm, 520 nm y 630 nm</li>
<li><strong>Batería:</strong> recargable de 400 mAh</li>
<li><strong>Carga:</strong> USB tipo C</li>
<li><strong>Manejo:</strong> un solo botón</li>
<li><strong>Material:</strong> polipropileno (PP)</li>
</ul>

<h2>Precauciones de uso</h2>
<ul>
<li>No uses la máscara mientras se está cargando.</li>
<li>Consulta con tu médico antes de usarla si estás embarazada, tienes epilepsia o fotosensibilidad, tomas medicación fotosensibilizante o tienes alguna enfermedad ocular o de la piel.</li>
<li>Uso exclusivo para adultos.</li>
<li>No sustituye a ningún tratamiento médico ni dermatológico.</li>
</ul>

<h2>Preguntas frecuentes</h2>
<p><strong>¿Para qué sirve la máscara LED facial?</strong><br>Para incorporar la luz LED a tu rutina de cuidado facial en casa, eligiendo el color según tu objetivo.</p>
<p><strong>¿Cuánto tiempo hay que usarla?</strong><br>El fabricante recomienda sesiones de 10 a 30 minutos al día.</p>
<p><strong>¿Funciona la máscara LED?</strong><br>Los resultados dependen de cada piel y de la constancia de uso, por lo que no podemos garantizar resultados concretos.</p>
<p><strong>¿Tiene contraindicaciones?</strong><br>Consulta el apartado «Precauciones de uso» y, ante cualquier duda, pregunta a tu médico.</p>
<p><strong>¿Tiene garantía?</strong><br>Sí, 3 años de garantía legal y 14 días para desistir de la compra.</p>

<p><strong>Añádela al carrito y empieza tu rutina de luz LED en casa.</strong></p>
```

**Imágenes:**

| Posición actual | Contenido | Acción | Nombre de archivo | Texto alternativo |
|---|---|---|---|---|
| 1 | Máscara blanca encendida en luz roja | Conservar (principal) | mascara-led-facial-7-colores.jpg | Máscara LED facial de 7 colores encendida en luz roja |
| 2 | Mujer con porcentajes de mejora | Eliminar | — | — |
| 3 | Cuadro de colores en inglés | Eliminar | — | — |
| 4 | «Multi-effect care», máscara con luz roja sobre fondo oscuro | Conservar | mascara-luz-led-facial.jpg | Máscara de luz LED facial inalámbrica |
| 5 | «Wireless operation», mano pulsando el botón | Conservar | mascara-led-inalambrica-un-boton.jpg | Máscara LED inalámbrica con un solo botón |
| 6 | Antes/después de la piel | Eliminar | — | — |
| 7 | 400mAh / «Use 1.5-2 hour» / «No box» | Eliminar | — | — |
| 8 | 400mAh / «Use 30-40 min» / «No box», con accesorios | Eliminar | — | — |

**Organización:**
- **Categoría:** Salud y belleza > Cuidado personal > Cosméticos > Herramientas de cosmética > Herramientas para el cuidado de la piel. Si existe una subcategoría de dispositivos de luz o LED, elígela. **No** uses «Máscaras y peelings» ni «Kits y sets».
- **Metacampos de categoría:**
  - Acepta: Grupo de edad = Adultos; Área del cuerpo/cara = Rostro; Material = Polipropileno (PP).
  - Opcional: Contra el envejecimiento.
  - Rechaza: Calmante y cualquier otro beneficio no verificado.
- **Tipo:** Máscara LED facial
- **Proveedor:** Ojoconesedetalle
- **Colección:** Cuidado facial
- **Etiquetas:** máscara led, mascarilla led facial, máscara led facial, luz led facial, 7 colores, cuidado facial, aparato de belleza, inalámbrica

**SEO:**
- **Título de la página:** Máscara LED Facial 7 Colores Inalámbrica | Ojoconesedetalle
- **Meta descripción:** Máscara de luz LED facial de 7 colores, inalámbrica y recargable por USB-C. Luz roja, azul y 5 colores más para tu rutina de cuidado facial en casa.
- **URL:** mascara-led-facial-7-colores (con redirección 301 desde la URL anterior)

**Metacampos:**

| Metacampo | Valor |
|---|---|
| custom.subtitulo | 7 colores de luz LED, sin cables y con un solo botón, para tu rutina facial en casa. |
| custom.colores_luz | 7 |
| custom.longitudes_onda | 470 nm · 520 nm · 630 nm |
| custom.bateria | 400 mAh, recargable por USB-C |

**Estado:** [DECIDIR] Recomendación: activo con inventario 0 y «Seguir vendiendo sin stock» desactivado hasta verificar el producto con el proveedor (certificado CE y muestra física).

---

## FASE 4 – PRODUCTO 2: CALENDARIO DE ADVIENTO DE TELA

**Título:**
Calendario de Adviento de Tela 2026 para Colgar – 24 Bolsillos para Rellenar

**Descripción** (sustituye todo el HTML):
```html
<p><strong>Calendario de adviento de tela 2026 para colgar, con 24 bolsillos para rellenar: cuenta los días hasta Navidad con una sorpresa cada día.</strong></p>
<p>Este <strong>calendario de adviento para rellenar</strong> convierte la cuenta atrás navideña en un pequeño ritual diario. Llena sus <strong>24 bolsillos</strong> con los detalles que tú elijas y, del 1 al 24 de diciembre, abrid uno cada día en familia. Además de <strong>calendario de Navidad</strong>, es un adorno que decora la casa durante todas las fiestas.</p>

<h2>Un calendario de adviento original que rellenas a tu manera</h2>
<ul>
<li><strong>Tú eliges las sorpresas:</strong> chocolatinas, notas, pequeños detalles o planes para hacer juntos.</li>
<li><strong>Para toda la familia:</strong> un calendario de adviento infantil para los peques o una sorpresa diaria para tu pareja.</li>
<li><strong>Reutilizable:</strong> al no venir relleno, puedes llenarlo de nuevo con lo que quieras.</li>
</ul>

<h2>Decoración navideña con diseño 2026</h2>
<p>El diseño combina el número <strong>2026</strong> con motivos navideños como copos de nieve y árboles de Navidad. Cuélgalo en el salón, el dormitorio o la entrada para llenar la casa de ambiente navideño.</p>

<h2>Un recuerdo de esta Navidad</h2>
<p>Según el fabricante, al terminar las fiestas puedes escribir en la parte trasera tus recuerdos de la Navidad de 2026 y guardarlo como recuerdo.</p>

<h2>Características (según el fabricante)</h2>
<ul>
<li><strong>Bolsillos:</strong> 24</li>
<li><strong>Material:</strong> tela</li>
<li><strong>Diseño:</strong> 2026 con árbol de Navidad y copos de nieve</li>
<li><strong>Formato:</strong> para colgar en la pared</li>
<li><strong>Contenido:</strong> 1 calendario</li>
<li><strong>Color:</strong> el de las imágenes. Puede variar ligeramente según la pantalla.</li>
</ul>

<h2>Preguntas frecuentes</h2>
<p><strong>¿El calendario incluye regalos?</strong><br>No. Se entrega vacío para que lo rellenes con las sorpresas que tú elijas.</p>
<p><strong>¿Se puede reutilizar?</strong><br>Sí, puedes rellenarlo tantas veces como quieras. Ten en cuenta que el diseño lleva el año 2026.</p>
<p><strong>¿Tiene garantía?</strong><br>Sí, 3 años de garantía legal y 14 días para desistir de la compra.</p>

<p><strong>Añádelo al carrito y prepara ya tu cuenta atrás para la Navidad.</strong></p>
```

**Imágenes:** aplica las reglas de la Fase 2. Patrón de texto alternativo: «Calendario de adviento de tela 2026 [lo que se ve]». Nombre de archivo de la principal: calendario-adviento-tela-24-bolsillos.jpg. Muéstrame la tabla antes de borrar nada.

**Organización:**
- **Categoría:** Hogar y jardín > Decoración > Decoraciones de temporada y festivas > Calendarios de Adviento. Si no existe, usa el nivel superior. **No** uses Juguetes, Alimentación ni Cuidado personal.
- **Metacampos de categoría:** acepta solo los que sean hechos visibles (tema navideño, material tela). Rechaza los que no puedas comprobar.
- **Tipo:** Calendario de adviento
- **Proveedor:** Ojoconesedetalle
- **Colección:** Navidad
- **Etiquetas:** calendario de adviento, calendario adviento tela, calendario de navidad, calendario navideño, calendario de adviento para rellenar, decoración navideña, navidad 2026, 24 bolsillos

**SEO:**
- **Título de la página:** Calendario de Adviento de Tela 2026 | Ojoconesedetalle
- **Meta descripción:** Calendario de adviento de tela 2026 para colgar, con 24 bolsillos para rellenar con sorpresas. Decoración navideña para contar los días hasta Navidad.
- **URL:** calendario-adviento-tela-24-bolsillos (sin año, con redirección 301)

**Metacampos:**

| Metacampo | Valor |
|---|---|
| custom.subtitulo | 24 bolsillos para rellenar con tus sorpresas y contar los días hasta Navidad. |
| custom.numero_bolsillos | 24 |

**Pendiente** (no publicar sin el dato): medidas del calendario y de los bolsillos, composición del tejido, plazo de envío a España.

---

## FASE 5 – PRODUCTO 3: COLGANTE PERSONALIZADO CON FOTO DE MASCOTA

**Título:**
Colgante Personalizado con Foto de tu Mascota – Collar de Acero Inoxidable

**Descripción** (sustituye todo el HTML, incluidas las imágenes de AliExpress incrustadas):
```html
<p><strong>Colgante personalizado con la foto de tu mascota: lleva siempre contigo a tu perro o tu gato.</strong></p>
<p>Este <strong>collar personalizado con foto</strong> reproduce la imagen de tu mascota en un colgante redondo de <strong>acero inoxidable</strong>, junto con su nombre o un texto corto. Tú eliges la foto, el texto y el largo de la cadena. Es un <strong>regalo personalizado</strong> para cualquier amante de los animales, para una mamá perruna o para recordar a una mascota que ya no está.</p>

<h2>Cómo personalizar tu colgante</h2>
<ol>
<li>Elige el <strong>largo de la cadena</strong>: 40, 45 o 50 cm.</li>
<li><strong>Sube la foto</strong> de tu mascota (JPG o PNG, hasta 10 MB).</li>
<li>Escribe el <strong>nombre o texto</strong> que quieres (máximo 20 caracteres).</li>
<li>Añade el colgante al carrito y finaliza tu pedido.</li>
</ol>

<h2>Consejos para elegir la foto</h2>
<ul>
<li>Usa una foto <strong>nítida y con buena luz</strong>, mejor de día.</li>
<li>Elige una imagen en la que se vea bien la <strong>cara de tu mascota</strong>, de frente.</li>
<li>Sube el archivo original, sin capturas de pantalla ni filtros.</li>
<li>Solo se admiten fotos en <strong>JPG o PNG</strong>. Si usas iPhone y tu foto no se sube, ve a Ajustes &gt; Cámara &gt; Formatos y elige «Más compatible».</li>
</ul>
<p>El colgante mide 20 mm de diámetro, así que el resultado final depende de la calidad de la foto.</p>

<h2>Un regalo con mucho significado</h2>
<ul>
<li><strong>Para amantes de los perros y los gatos:</strong> un detalle único para cumpleaños, aniversarios o Navidad.</li>
<li><strong>Para una mamá perruna:</strong> el regalo perfecto para quien considera a su perro parte de la familia.</li>
<li><strong>En recuerdo de tu mascota:</strong> una forma de llevar cerca a quien te acompañó tantos años.</li>
</ul>

<h2>Características (según el fabricante)</h2>
<ul>
<li><strong>Material:</strong> acero inoxidable</li>
<li><strong>Colgante:</strong> redondo, 20 mm de diámetro</li>
<li><strong>Cadena:</strong> de eslabones</li>
<li><strong>Largos disponibles:</strong> 40, 45 o 50 cm</li>
<li><strong>Personalización:</strong> foto de tu mascota y texto de hasta 20 caracteres</li>
</ul>

<h2>Preguntas frecuentes</h2>
<p><strong>¿Puedo poner la foto de cualquier mascota?</strong><br>Sí: perro, gato o cualquier otra mascota. Te recomendamos una foto nítida y de frente.</p>
<p><strong>¿Qué texto puedo añadir?</strong><br>El nombre de tu mascota o un texto corto de hasta 20 caracteres, incluidos los espacios.</p>
<p><strong>¿Qué largo de cadena elijo?</strong><br>40 cm queda cerca de la base del cuello; 45 y 50 cm caen más abajo, sobre el pecho.</p>
<p><strong>¿Cuánto tarda en llegar?</strong><br>Lo fabricamos después de tu pedido. El plazo estimado de entrega es de 2 a 3 semanas.</p>
<p><strong>¿Puedo devolverlo?</strong><br>Al ser un producto personalizado, no se aplica el derecho de desistimiento de 14 días. Si llega defectuoso o dañado, tienes 3 años de garantía legal.</p>

<p><strong>Sube la foto de tu mascota y crea hoy tu colgante personalizado.</strong></p>
```

**Variantes** (renombra, no recrees):
- Opción «Main Stone Color» → renombrar a **Colgante**. Conservar solo «1 pendant 20mm», renombrado a **1 colgante 20 mm**. Eliminar: NO carving, 1 pendant 15mm, 2/3/4 pendant 15mm y 2/3/4 pendant 20mm.
- Opción «Length» → renombrar a **Largo de cadena**. Valores **40 cm**, **45 cm** y **50 cm**. Eliminar «Double-sided custom».
- Resultado: 3 variantes con precio.
- Después, comprueba en la app de importación (DSers u otra) que cada variante sigue enlazada a «1 pendant 20mm» + el largo correspondiente del proveedor. Si se ha roto algún enlace, avísame.
- No añadas opción de color hasta que el proveedor confirme qué colores envía.

**Imágenes:** aplica la Fase 2. Elimina las que muestren 2, 3 o 4 colgantes o el colgante de 15 mm. La principal debe mostrar **un único colgante**. Patrón de texto alternativo: «Colgante personalizado con foto de mascota – [lo que se ve]». Nombre de archivo de la principal: colgante-personalizado-foto-mascota.jpg. Muéstrame la tabla antes de borrar nada.

**Organización:**
- **Categoría:** Ropa y accesorios > Joyería > Collares
- **Metacampos de categoría:** acepta solo los verificados (material: acero inoxidable; tipo: colgante). No aceptes color, piedras ni metales preciosos.
- **Tipo:** Colgante personalizado
- **Proveedor:** Ojoconesedetalle
- **Colecciones:** Regalos personalizados, Mascotas, Joyería
- **Etiquetas:** colgante personalizado, collar personalizado con foto, colgante foto mascota, collar foto perro, regalo personalizado, regalo amantes de perros, mamá perruna, recuerdo mascota, acero inoxidable

**SEO:**
- **Título de la página:** Colgante con Foto de tu Mascota | Ojoconesedetalle
- **Meta descripción:** Colgante personalizado con la foto de tu perro o gato, en acero inoxidable. Elige el largo de la cadena. Un regalo único para amantes de las mascotas.
- **URL:** colgante-personalizado-foto-mascota (con redirección 301)

**Metacampos:**

| Metacampo | Valor |
|---|---|
| custom.subtitulo | Con la foto de tu perro o gato, en acero inoxidable. Elige el largo de la cadena. |
| custom.material | Acero inoxidable |
| custom.medida_colgante | 20 mm de diámetro |

### 5.1 App gratuita de personalización (subida de foto + texto limitado)

**Requisitos obligatorios de la app:**
1. Plan gratuito permanente, no solo de prueba, que incluya todo lo de esta lista. Verifícalo en la ficha de la app en la Shopify App Store.
2. Campo de **subida de archivo** con restricción de formato (JPG, PNG) y de tamaño (10 MB).
3. Campo de **texto** con **límite de caracteres** (20).
4. Ambos campos **obligatorios**: sin ellos no se puede añadir al carrito.
5. Asignable **solo a este producto**.
6. Los datos aparecen en el pedido como propiedades del artículo y la foto se puede descargar desde el pedido.
7. Compatible con el tema actual y con etiquetas en español.

**Pasos:**
1. Busca en la App Store («product options file upload», «personalización producto subir foto») y propónme 2 o 3 apps que cumplan todos los requisitos, indicando qué incluye su plan gratuito.
2. Yo apruebo e instalo la elegida. No la instales sin mi confirmación.
3. Configura los campos:

| Campo | Tipo | Obligatorio | Restricción | Texto de ayuda |
|---|---|---|---|---|
| Foto de tu mascota | Subida de archivo | Sí | JPG, PNG · máx. 10 MB | Foto nítida y de frente. JPG o PNG, hasta 10 MB. |
| Nombre o texto | Texto de una línea | Sí | Máx. 20 caracteres | Ej.: Kira · Máximo 20 caracteres, incluidos espacios. |

4. Asígnalos solo al producto «Colgante Personalizado con Foto de tu Mascota».
5. **Prueba de funcionamiento:**
   - sin foto, no deja añadir al carrito;
   - con más de 20 caracteres, no deja añadir al carrito;
   - un archivo HEIC o de más de 10 MB se rechaza;
   - en un pedido de prueba (modo de prueba o pedido preliminar) aparecen la foto descargable y el texto.

   Infórmame del resultado de cada comprobación.

### 5.2 Mensaje de plazos (solo este producto)
Añade en la plantilla de producto un bloque de texto, visible solo en este producto (con una plantilla de producto propia o con un metacampo), con el mensaje según la fecha:
- Hasta el 24/11/2026: «🎄 Pide antes del 24 de noviembre para recibirlo antes de Navidad.»
- Del 25/11 al 7/12/2026: «👑 ¿Es para Reyes? Pide antes del 7 de diciembre para recibirlo a tiempo.»
- Desde el 8/12/2026: «Producto personalizado: lo fabricamos después de tu pedido. Plazo estimado de entrega: 2-3 semanas.»

Este plazo es solo de este producto: no lo pongas en la barra de anuncios global ni en otros productos.

---

## FASE 6 – COMPROBACIÓN FINAL

Para cada producto, verifica y marca ✅ o ❌:
- título, descripción, título SEO (≤ 60 caracteres), meta descripción (≤ 160 caracteres) y URL con redirección;
- categoría correcta y metacampos de categoría revisados;
- tipo, proveedor, colecciones y etiquetas;
- metacampos personalizados rellenados y subtítulo visible en la página;
- imágenes: ninguna eliminable restante, principal correcta, todas con texto alternativo y nombre de archivo en español;
- ninguna imagen externa en la descripción;
- vista previa en móvil sin textos en inglés;
- variantes en español y enlazadas al proveedor (colgante);
- app de personalización funcionando (colgante).

Termina con:
1. Tabla resumen por producto: hecho / pendiente / bloqueado.
2. Lista de todos los [PENDIENTE] y [DECIDIR].
3. Pasos que tengo que hacer yo manualmente.
