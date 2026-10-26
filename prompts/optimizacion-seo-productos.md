# PROMPT: Optimización SEO y organización de los productos personalizados – Ojoconesedetalle

Actúa como especialista SEO en Shopify para el mercado de España, con acceso de administración a mi tienda «Ojoconesedetalle» (ccdf97-s7.myshopify.com). Vas a optimizar, organizar y vincular **solo estos 6 productos**:

| # | Producto (título actual en Shopify) | Variantes actuales |
|---|---|---|
| P1 | Colgante Personalizado con Foto de tu Mascota – Collar de Acero Inoxidable | 32 |
| P2 | Personalized Christmas Baubles Custom Laser… | 6 |
| P3 | Sipuris Custom Name Necklace Personalized Gold… | 184 |
| P4 | UniCrena Engraved Dog Keychain - Custom Pet Pictu… | 1 |
| P5 | Custom Photo Projection Necklace with Picture Inside… | 75 |
| P6 | Pet Ashes Necklace for Dog, Engravable Memorial Hair… | 1 |

**No toques ningún otro producto.** La máscara LED y el calendario de adviento quedan fuera.

## REGLAS OBLIGATORIAS

1. **No inventes datos.** Usa solo la información que ya esté en cada ficha (especificaciones del proveedor) y lo que te doy aquí. Lo que no conste o se contradiga, márcalo [PENDIENTE: ...] y no lo publiques.
2. **Sin promesas no verificables:** nada de «hipoalergénico», «oro», «plata de ley», «acero quirúrgico 316L», «resistente al agua», «no se oscurece», «certificado», «calidad premium» ni plazos garantizados. Los colores dorado y oro rosa se llaman «dorado» y «rosado».
3. **Sin marcas de terceros:** elimina «Sipuris», «UniCrena» y cualquier otra marca del proveedor en títulos, descripciones, textos alternativos y etiquetas. El proveedor (vendor) de todos es «Ojoconesedetalle».
4. **Pide confirmación antes de cualquier acción irreversible:** borrar imágenes, borrar valores de variantes, cambiar el estado, publicar en canales, instalar apps o modificar menús. Muéstrame antes la lista exacta.
5. **Variantes: renombra, no recrees.** Están enlazadas a artículos de AliExpress mediante una app de importación. Solo cambia el nombre de opciones y valores, y elimina los valores que yo apruebe.
6. **Todo en español de España** y visible sin textos en inglés: título, opciones, variantes, descripción, textos alternativos y nombres de archivo.
7. **Sin imágenes externas en las descripciones:** elimina todo `<img>` que cargue de aliexpress-media.com u otros dominios.
8. **Trabaja producto por producto.** Para P2-P6, primero propónme el contenido (título, descripción, SEO, variantes, imágenes) y espera mi aprobación antes de aplicarlo. P1 ya está aprobado: aplícalo directamente.
9. **Si no puedes hacer algo,** no lo simules: dime el paso exacto que tengo que hacer yo.

---

## FASE 1 – CONFIGURACIÓN GLOBAL

### 1.1 Definiciones de metacampos de producto
Ruta: Configuración > Metacampos y metaobjetos > Productos. Créalas si no existen; si existen, no las dupliques. En todas: **un solo valor**, **acceso de la tienda online activado**, sin validaciones y con claves sin tildes.

| Nombre | Clave | Tipo | Uso |
|---|---|---|---|
| Subtítulo | custom.subtitulo | Texto de una sola línea | Frase bajo el título |
| Material | custom.material | Texto de una sola línea | Según el fabricante |
| Medida del colgante | custom.medida_colgante | Texto de una sola línea | Si consta |
| Personalización | custom.personalizacion | Texto de una sola línea | Qué aporta el cliente (foto, texto y límite) |
| Plazo de entrega | custom.plazo_entrega | Texto de una sola línea | Plazo propio del producto |
| Aviso de fechas límite | custom.aviso_fechas | Texto de una sola línea | Mensaje Navidad/Reyes de cada producto |

Si existen definiciones de la máscara o del calendario (colores_luz, longitudes_onda, bateria, numero_bolsillos), no las borres.

### 1.2 Tema
En Tienda online > Personalizar > plantilla de Productos, añade bajo el título tres bloques «Texto» conectados con origen dinámico a **custom.subtitulo**, **custom.aviso_fechas** y **custom.plazo_entrega**. Así cada producto muestra solo sus propios plazos; si el metacampo está vacío, el bloque no muestra nada. Compruébalo en un producto sin valor.

### 1.3 Colecciones manuales
Crea las que no existan, con título, descripción breve en español y URL limpia:

| Colección | URL | Productos |
|---|---|---|
| Regalos personalizados | regalos-personalizados | P1-P6 |
| Mascotas | mascotas | P1, P4, P5 si se anuncia con mascotas, P6 |
| Recuerdo de mascotas | recuerdo-mascotas | P1, P4, P6 |
| Joyería personalizada | joyeria-personalizada | P1, P3, P5, P6 |
| Navidad | navidad | P2 |

Propón (sin aplicarlo) cómo enlazarlas en el menú principal.

### 1.4 Canales de venta
Los 6 productos tienen **0 canales**: no se ven en la tienda online. Al final de cada producto aprobado, pídeme confirmación para publicarlo en el canal **Tienda online**.

---

## FASE 2 – KEYWORD PRINCIPAL POR PRODUCTO (evitar canibalización)

Cada producto apunta a una búsqueda distinta. Usa la keyword principal en el título, en el título SEO, en la URL, en el primer párrafo y en el texto alternativo de la imagen principal. Estas keywords **no están validadas** con Google Ads: si te doy datos del Planificador, sustitúyelas.

| Producto | Keyword principal | Secundarias | URL |
|---|---|---|---|
| P1 | colgante personalizado con foto de mascota | collar con foto de perro, regalo mamá perruna | colgante-personalizado-foto-mascota |
| P2 | bolas de Navidad personalizadas | adorno navideño personalizado, bola de Navidad con nombre | bolas-navidad-personalizadas |
| P3 | collar con nombre personalizado | colgante con nombre, collar nombre acero | collar-nombre-personalizado |
| P4 | llavero personalizado con foto de mascota | llavero foto perro, llavero grabado mascota | llavero-personalizado-foto-mascota |
| P5 | collar con foto dentro (proyección) | colgante con foto proyectada, collar foto oculta | collar-foto-proyeccion |
| P6 | colgante para cenizas de mascota | colgante urna mascota, recuerdo mascota fallecida | colgante-cenizas-mascota |

Todas las URL con redirección 301 desde la anterior.

---

## FASE 3 – PLANTILLA DE CONTENIDO (P2-P6)

**Título:** keyword principal + diferenciador + material o formato, en un máximo de 75 caracteres. Sin marcas.

**Descripción** (solo HTML básico: p, h2, ol, ul, li, strong, br), con esta estructura:
1. Párrafo inicial en negrita con la keyword principal y el beneficio emocional.
2. Párrafo con la keyword y las secundarias, de forma natural.
3. `<h2>Cómo personalizar tu [producto]</h2>`: pasos numerados con los campos exactos de la Fase 5.
4. `<h2>Consejos para la foto</h2>` (solo si se sube foto): nítida, de frente, JPG/PNG y el aviso para iPhone.
5. `<h2>Un regalo con significado</h2>`: ocasiones. En P6, tono respetuoso y sin humor.
6. `<h2>Características (según el fabricante)</h2>`: solo datos que consten y no se contradigan.
7. `<h2>Preguntas frecuentes</h2>`: qué puedo personalizar, medidas o largos, cuánto tarda («[PENDIENTE]» si no hay plazo) y devoluciones: «Al ser un producto personalizado, no se aplica el derecho de desistimiento de 14 días. Si llega defectuoso o dañado, tienes 3 años de garantía legal.»
8. Llamada a la acción final en negrita.

**SEO:** título de la página como «[Keyword principal] | Ojoconesedetalle», de 60 caracteres como máximo. Meta descripción de 160 caracteres como máximo, con la keyword y un motivo de compra. Nada sin verificar.

**Organización:**
- Tipo: Colgante personalizado / Collar personalizado / Llavero personalizado / Adorno navideño personalizado.
- Categoría de la taxonomía de Shopify: P1, P3, P5 y P6 en Joyería > Collares; P4 en Llaveros; P2 en Decoraciones de temporada y festivas > adornos de Navidad.
- Metacampos de categoría: acepta solo los hechos verificables (material, tipo). No aceptes metales preciosos, piedras ni beneficios.
- Etiquetas: entre 6 y 10, en minúsculas, con la keyword principal y las secundarias.

**Variantes:** propón un conjunto reducido y vendible (por ejemplo, colores × largos reales), muestra la tabla de antes y después con los valores a eliminar, y espera mi aprobación. Las opciones se llaman Color, Largo de cadena, Tamaño o Número de colgantes, según corresponda. En P3 (184 variantes) y P5 (75), explica qué combinaciones conservas y por qué.

---

## FASE 4 – IMÁGENES (todos los productos)

**Eliminar:**
- imágenes con marcas de terceros o logotipos de otras tiendas;
- textos en inglés con promesas;
- porcentajes o «antes/después»;
- especificaciones que contradigan la ficha;
- variantes que no se venden;
- duplicados;
- fotos de personas que parezcan sacadas de redes sociales.

**Principal:** el producto solo, la variante más representativa y fondo limpio.

**Nombre de archivo:** keyword en minúsculas, sin tildes y con guiones (por ejemplo, colgante-personalizado-foto-mascota.jpg). Si no se puede renombrar, descarga la imagen, renómbrala, súbela y borra la antigua.

**Texto alternativo:** describe lo que se ve, con la keyword principal en la imagen 1, en menos de 125 caracteres.

**Variantes:** asigna a cada variante la imagen de su color.

Antes de borrar, enséñame una tabla por producto: posición, qué se ve, conservar o eliminar, nombre nuevo y texto alternativo.

---

## FASE 5 – APP GRATUITA DE PERSONALIZACIÓN (los 6 productos)

**Requisitos:**
1. Plan gratuito permanente que incluya todo lo de esta lista.
2. Campo de subida de archivo con restricción de formato (JPG, PNG) y de tamaño.
3. Campo de texto con límite de caracteres.
4. Campos obligatorios: sin ellos no se puede añadir al carrito.
5. Conjuntos de campos distintos por producto.
6. Los datos aparecen en el pedido y la foto se puede descargar.
7. Compatible con el tema actual y con etiquetas en español.

**Pasos:**
1. Propónme 2 o 3 apps de la Shopify App Store que cumplan todo, con lo que incluye su plan gratuito. No instales nada sin mi confirmación.
2. Una vez instalada, configura un conjunto de campos por producto.

**Campos por producto.** Deben coincidir exactamente con el formulario «Personalizar ahora» de cada proveedor en AliExpress. Yo te daré lo que falta:

| Producto | Foto (formato, tamaño) | Texto (límite) | Otros campos | Estado |
|---|---|---|---|---|
| P1 | Obligatoria · JPG/PNG · 10 MB · «Foto de tu mascota» | Obligatorio · 20 caracteres · «Nombre o texto» | — | Confirmado |
| P2 | [PENDIENTE] | [PENDIENTE] | [PENDIENTE] | Pedir datos |
| P3 | [PENDIENTE] | [PENDIENTE] | [PENDIENTE: tipografía] | Pedir datos |
| P4 | [PENDIENTE] | [PENDIENTE] | [PENDIENTE] | Pedir datos |
| P5 | [PENDIENTE] | [PENDIENTE] | [PENDIENTE] | Pedir datos |
| P6 | [PENDIENTE] | [PENDIENTE] | [PENDIENTE] | Pedir datos |

No configures los campos de un producto hasta que su fila esté completa.

**Pruebas por producto:**
- sin los campos obligatorios no deja añadir al carrito;
- el texto que supera el límite se bloquea;
- los formatos no permitidos se rechazan;
- en un pedido de prueba aparecen la foto descargable y el texto.

---

## FASE 6 – P1 YA APROBADO (aplicar tal cual)

**Título:**
Colgante Personalizado con Foto de tu Mascota – Collar de Acero Inoxidable

**Descripción:**
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

**Variantes:** tiene 32 y deben quedar 3.
- Opción «Main Stone Color» (o equivalente) → renombrar a **Colgante**. Conservar solo «1 pendant 20mm», renombrado a **1 colgante 20 mm**.
- Opción «Length» → renombrar a **Largo de cadena**. Valores **40 cm**, **45 cm** y **50 cm**. Eliminar «Double-sided custom» y «NO carving».
- Si las 32 variantes incluyen otra opción (por ejemplo, color), enséñamela antes de tocarla.
- Después, comprueba el enlace de cada variante con el proveedor en la app de importación.

**Imágenes:** la principal debe mostrar **un solo colgante**. Elimina las de 2, 3 o 4 colgantes y las de 15 mm.

**Organización:**
- Categoría: Joyería > Collares (actualmente «Colgantes», válida si cuelga de Collares).
- Tipo: Colgante personalizado
- Colecciones: Regalos personalizados, Mascotas, Recuerdo de mascotas, Joyería personalizada
- Etiquetas: colgante personalizado, collar personalizado con foto, colgante foto mascota, collar foto perro, regalo personalizado, regalo amantes de perros, mamá perruna, recuerdo mascota, acero inoxidable

**SEO:**
- Título de la página: Colgante con Foto de tu Mascota | Ojoconesedetalle
- Meta descripción: Colgante personalizado con la foto de tu perro o gato, en acero inoxidable. Elige el largo de la cadena. Un regalo único para amantes de las mascotas.
- URL: colgante-personalizado-foto-mascota

**Metacampos:**

| Metacampo | Valor |
|---|---|
| custom.subtitulo | Con la foto de tu perro o gato, en acero inoxidable. Elige el largo de la cadena. |
| custom.material | Acero inoxidable |
| custom.medida_colgante | 20 mm de diámetro |
| custom.personalizacion | Foto de tu mascota (JPG o PNG) y texto de hasta 20 caracteres |
| custom.plazo_entrega | Producto personalizado: plazo estimado de entrega de 2 a 3 semanas. |
| custom.aviso_fechas | 🎄 Pide antes del 24 de noviembre para recibirlo antes de Navidad. |

Recuérdame cambiar custom.aviso_fechas:
- el 25/11/2026 por «👑 ¿Es para Reyes? Pide antes del 7 de diciembre para recibirlo a tiempo.»;
- el 8/12/2026, vaciarlo.

**Fechas límite de P2-P6:** se calculan con su plazo real de AliExpress («Envío: X-Y»), así: 1 día de gestión + peor caso del proveedor + 7 días de margen, contando hacia atrás desde el 22/12 (Navidad) y el 4/1 (Reyes). Si no tienes el plazo, deja custom.aviso_fechas vacío y márcalo [PENDIENTE]. P2 (bolas de Navidad) es urgente: después de Navidad pierde casi todo su interés.

---

## FASE 7 – COMPROBACIÓN FINAL

Para cada producto, marca ✅ o ❌:
- título sin marcas y en español; descripción aprobada; título SEO de 60 caracteres o menos; meta descripción de 160 o menos; URL con redirección;
- categoría, metacampos de categoría revisados, tipo, proveedor, colecciones y etiquetas;
- metacampos personalizados y bloques visibles en la página (y ocultos cuando están vacíos);
- imágenes limpias, principal correcta, textos alternativos y nombres de archivo en español, sin imágenes externas en la descripción;
- variantes reducidas, en español y enlazadas al proveedor;
- app de personalización configurada y probada (o [PENDIENTE] con el motivo);
- publicado en el canal Tienda online (tras mi confirmación);
- vista previa en móvil correcta.

Termina con:
1. Tabla resumen por producto: hecho / pendiente / bloqueado.
2. Lista de todos los [PENDIENTE].
3. Pasos que tengo que hacer yo manualmente.
