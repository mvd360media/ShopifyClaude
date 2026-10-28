# Estado del proyecto — Ojo Con Ese Detalle

- Tienda: ccdf97-s7.myshopify.com
- Dominio: ojoconesedetalle.es (DNS apuntado a Shopify, verificación en curso)
- Carpeta del tema: tema/ (este repositorio)
- Tema base: Dawn (Shopify/dawn main, commit 258f00f 2026-08-10)
- Entorno: Node v22.22.0, Shopify CLI 4.9.4 — OK (reinstalado 2026-10-17, sesión 2)
- Tema de trabajo: "Ojo Con Ese Detalle (Claude)" #211921994119 (sin publicar)
  - Vista previa: https://ccdf97-s7.myshopify.com?preview_theme_id=211921994119
  - Editor: https://ccdf97-s7.myshopify.com/admin/themes/211921994119/editor
- Tema ACTIVO desde ~2026-10-27: "Ojo Con Ese Detalle (Claude)" #211921994119 (lo publicó la usuaria). Helio queda sin publicar. Antes de subir, comparar con el tema vivo (shopify theme pull) por si hay cambios del editor.
- Última publicación: 2026-10-17 (sesión 3) estructura SEO, menús, blog, campaña Black Friday (tema sin publicar)

## Conexión (entorno en la nube)
- Dominios permitidos añadidos por el usuario: accounts/admin/partners.shopify.com,
  ccdf97-s7.myshopify.com, cdn.shopify.com, monorail-edge.shopifysvc.com.
- Ejecutar el CLI con NODE_USE_ENV_PROXY=1 (Node no usa el proxy por defecto).
- Login del tema: flujo con código (el usuario abre el enlace).
- store auth: redirige a 127.0.0.1; el usuario pega la URL de error y se entrega con curl local.
- La tienda está ABIERTA al público (sin contraseña): todo lo publicado en Tienda online se puede comprar.
- store auth (sesión 3) añade: read/write_online_store_navigation, read/write_legal_policies, read/write_discounts, read_inventory.

## Fases completadas
- [x] 0 Entorno
- [x] 1 Conexión (tema + datos de la tienda)
- [x] 2 Proyecto (Dawn subido como tema sin publicar)
- [x] 3 Diseño (estilo aprobado por el usuario)
- [x] 4 Construcción (portada)
- [x] 5 Páginas (falta aviso legal y privacidad: datos del titular)
- [ ] 6 Publicación

## Decisiones de diseño
- Prefijo propio: oc- (Ojo Con). CSS en assets/oc-styles.css, JS en assets/oc-scripts.js.
- Paleta: fondo #FBF8F4, alt #F3ECE3, tinta #1E1B2E, coral #FF5A4E, temporada (Navidad) #1F5E4A.
- Tipografía: Bricolage Grotesque (titulares, Google Fonts en layout/theme.liquid) + DM Sans (texto; dm_sans en ajustes del tema).
- Botones píldora, esquinas 16–32px, ojo animado como elemento de marca.
- Sin reseñas inventadas: se añadirán cuando haya reseñas reales.
- Imágenes con IA: aprobadas por el usuario. La variable OPENAI_API_KEY de la sesión 2 seguía recortada; la usuaria pegó una clave nueva en el chat (guardada solo en el scratchpad, nunca en el repo). Recomendado: revocarla en OpenAI y crear otra al terminar.
- Textos en imágenes de producto en inglés: traducir o regenerar en español.
- Vocabulario: NO usar "drop" en textos visibles; usar "colección de temporada" / "Especial X".
- Marca: Ojo Con Ese Detalle. Tono cercano, emocional, tipo "OhMyGift".
- Modelo: colecciones de temporada (drops) + productos fijos. Primera campaña: Black Friday / Navidad / Reyes.

## Secciones creadas
- oc-hero: portada principal (texto + imagen, sello, 2 botones)
- oc-marquesina: banda en movimiento con frases
- oc-drop: colección de temporada con cuenta atrás hasta la fecha de fin real
- oc-regalos: tarjetas "regalos por persona" (bloques)
- oc-ventajas: por qué comprarnos (bloques con iconos)
- oc-faq: preguntas frecuentes (bloques)
- oc-cta: llamada final
- oc-producto: página de producto (galería, variantes, compra, plazo de entrega, garantías)
- templates/index.json (portada) y templates/product.oc.json (plantilla de producto "oc")
- Footer y barra de anuncios configurados en español

## Productos (revisados 2026-10-17)
- Máscara LED — gid://shopify/Product/16649284485511 — plantilla "oc"
  - Quitadas imágenes con claims médicos / antes-después. Descripción sin imágenes de AliExpress (incluían un anuncio de otra tienda); añadidas autonomía y "se envía sin caja original".
  - Opción "Autonomía por carga": "1,5–2 h" 44,90 € y "30–40 min" 34,90 € desde 2026-10-17 (antes 39,90/29,90 unas horas).
  - Black Friday: descuento automático "Black Friday 2026 – 5 € menos" (DiscountAutomaticNode/2432608698759), colección black-friday, 20–30 nov 2026 (hora de Madrid) → 39,90 / 29,90.
  - LEGAL (Omnibus): NO bajar el precio entre el 21 oct y el 19 nov; el precio tachado debe ser el más bajo de los 30 días previos al 20 nov.
  - Imágenes en español (gpt-image-2, 2026-10-17), sustituyen a las de inglés en el mismo orden: 77762749989255 (Cuidado completo), 77762770403719 (Sin cables), 77762783445383 (var. 1,5–2 h), 77762796814727 (var. 30–40 min). Las dos últimas vinculadas a su variante.
- Calendario de Adviento — gid://shopify/Product/16649471754631 — plantilla "oc"
  - Quitada imagen con marca de agua de otra tienda. Descripción reescrita (coincide con las fotos). Título sin "2026".
  - Opción "Diseño": "Merry Christmas" / "Advent (texto en alemán)". Opción "Size" eliminada.
  - "Parte trasera / Varilla de madera" en español: 77762798584199 (posición 3). Orden nuevo: portada Merry Christmas primero (antes salía la parte trasera como foto principal).
  - Stock 1 unidad por variante (revisar sincronización de DSers).
- compareAtPrice borrado en ambos (DSers ponía el coste del proveedor).
- Ambos publicados en Tienda online (2026-10-17 21:59 UTC).

## Imágenes de la tienda (Contenido → Archivos)
- oc-favicon.png (ojo de marca, dibujado, no IA) → ajuste favicon del tema.
- oc-h-hero.jpg (high) → oc-hero.imagen. oc-t-ella / oc-t-el / oc-t-amigo / oc-t-menos20 (medium) → tarjetas de oc-regalos.
- Todas las imágenes de producto y de portada tienen texto alternativo en español.
- Gasto aproximado en OpenAI: ~0,9 $ (9 medium + 1 high, con referencias).
- Herramienta: herramientas/subir.py (subir_archivo, subir_media_producto).

## Colecciones
- REGLA de la usuaria: cada producto va en la temporada que ella indica. Máscara = Black Friday. Calendario = Navidad. No mezclar.
- Black friday (black-friday): máscara. Sección de portada "black_friday" (fin 2026-12-01). Botón del hero y CTA apuntan aquí (temporada más próxima).
- Navidad (navidad): calendario. Sección de portada "drop" (fin 2027-01-06).
- Las secciones de temporada se ocultan solas al llegar su fecha de fin (ajuste ocultar_al_terminar). El 1 de diciembre hay que cambiar el botón del hero y el CTA a Navidad.
- Ambas con descripción y SEO (título y meta descripción).
- AUTOMÁTICAS por etiqueta: Para ella (etiqueta para-ella), Para él (para-el), Amigo invisible (amigo-invisible). Menos de 20 € automática por precio < 20 €. Al subir un producto, basta con ponerle la etiqueta.
- Etiquetas actuales: máscara = para-ella; calendario = para-ella, para-el, amigo-invisible.
- Todas con descripción y SEO.
- Todas publicadas en Tienda online y enlazadas en las tarjetas de oc-regalos.

## Páginas, políticas y blog (2026-10-17, sesión 3)
- Políticas de Shopify (se ven en el pago): Envíos (SHIPPING_POLICY), Devoluciones (REFUND_POLICY), Términos (TERMS_OF_SERVICE) con nuestros textos; Privacidad = la generada por Shopify. Aviso legal = política LEGAL_NOTICE (/policies/legal-notice) con titular, NIE y domicilio; /pages/aviso-legal redirige ahí y está en el menú del pie. Privacidad: gestionada automáticamente por Shopify (no se puede editar por API hasta que la usuaria desactive la gestión automática); le faltan nombre del titular y NIE y deja un hueco de teléfono.
- Páginas /pages/envios, /devoluciones, /terminos, /privacidad BORRADAS y redirigidas a /policies/... (evita contenido duplicado).
- Páginas nuevas: Quiénes somos (/pages/quienes-somos), Preguntas frecuentes (/pages/preguntas-frecuentes), con título y descripción SEO.
- Blog renombrado: "Ideas de regalo" (/blogs/ideas-de-regalo; /blogs/noticias redirige). Artículos (docs/blog/articulos.py): rellenar calendario de adviento, amigo invisible < 20 €, máscara LED qué es y cómo se usa.
- Menú principal: Inicio · Temporadas (Black Friday, Navidad y Reyes) · Regalos (Para ella, Para él, Amigo invisible, Menos de 20 €, Ver todos) · Ideas de regalo · Quiénes somos · Contacto.
- Menú pie (Ayuda): Preguntas frecuentes, Envíos, Devoluciones, Términos, Privacidad, Contacto, Buscar. Pie: marca · Tienda (menú principal) · Ayuda · Cómo funciona.
- Colección "Página de inicio" (frontpage, vacía) despublicada.

## SEO técnico del tema
- Título y descripción de la portada: Configuración del tema → "Ojo Con: SEO y campaña" (oc_seo_titulo_inicio, oc_seo_descripcion_inicio, oc_seo_imagen para redes).
- layout/theme.liquid: la marca no se repite en el título si ya está (comparación sin mayúsculas); "Página N" en español.
- header.liquid: el logo ya no es h1 en la portada (el h1 es el de oc-hero). Un solo h1 por página verificado en portada, producto, colección, artículo, página y política.
- Datos estructurados: producto (oc-producto), artículo, organización y web (header).
- Rebaja de campaña en el tema: snippets/oc-rebaja.liquid, usado en snippets/price.liquid (Dawn, tarjetas), oc-producto y oc-drop. Ajustes en "Ojo Con: SEO y campaña" (activa, colección, importe, primer y último día, etiqueta). Debe coincidir con el descuento automático.

## Páginas legales (antiguo script: docs/legales/paginas.py — ya sustituidas por políticas)
- Publicadas: Envíos y plazos (/pages/envios), Devoluciones (/pages/devoluciones), Términos (/pages/terminos).
- En borrador: Aviso legal (/pages/aviso-legal) y Privacidad (/pages/privacidad) — falta nombre/razón social, NIF y dirección ([PENDIENTE] en el texto). Al publicarlas, añadir sus enlaces al bloque "Información" del footer.
- Plazo de entrega prudente: 1–3 días de preparación, 7–15 días laborables en total. Fechas límite: Navidad 1 dic, Reyes 12 dic. Mismo texto en FAQ de portada, plantilla de producto y página de envíos.

## Cómo retomar en una sesión nueva (entorno en la nube)
1. npm install -g @shopify/cli@latest
2. Crear stub de navegador: carpeta bin con un xdg-open que guarde la URL en un archivo; anteponerla al PATH.
3. Ejecutar todo con NODE_USE_ENV_PROXY=1.
4. Login del tema: `shopify theme list --store ccdf97-s7.myshopify.com` en segundo plano → pasar al usuario el enlace activate-with-code.
5. Datos: `shopify store auth --store ccdf97-s7.myshopify.com --scopes read_products,write_products,read_files,write_files,read_themes,read_content,write_content,read_online_store_pages,write_online_store_pages,read_publications,write_publications`
   → el usuario abre la URL, autoriza y pega la URL de error 127.0.0.1:PUERTO/auth/callback?...; entregarla con `curl --noproxy 127.0.0.1 "<url>"`.
6. Utilidades en herramientas/: gql.py (run(query, variables)), shot.mjs (capturas con Playwright + headless_shell), crop.py.
7. Comprobar OPENAI_API_KEY con GET https://api.openai.com/v1/models (200 = válida).

## Políticas (2026-10-26) — textos en docs/legales/politicas/
- Publicadas: Envío, Reembolso, Términos, Contacto (CONTACT_INFORMATION), Aviso legal. Todas con apartado "Productos personalizados".
- Decisiones de la usuaria: envío a toda España; IVA de importación y aduana del colgante los paga la usuaria (coste total 13,78 €); el cliente no paga nada al recibirlo; devoluciones a Calle Colón, 1, 46016 Tavernes Blanques (CP deducido, confirmar), a cargo del cliente; cancelar personalizados en 2 h; respuesta en 48 h laborables; fotos borradas 30 días tras la entrega; transferencia a China por art. 49.1.b RGPD.
- Plazos 2–3 semanas y fechas límite (Navidad 24 nov, Reyes 7 dic 2026) SOLO para el colgante personalizado.
- Privacidad: gestión automática DESACTIVADA por la usuaria (2026-10-26). Publicada = texto de Shopify + responsable + apartado de personalizados insertado antes del primer h2 (copia en privacidad-completa.html). Quitado el hueco "llámenos al ,". Si Shopify cambia su plantilla, ya no se actualiza sola.
- La tienda tiene 6 productos personalizados importados en inglés (sin publicar, precio = coste). Máscara y calendario pasaron a borrador.

## SEO productos personalizados (2026-10-26) — prompt de la usuaria, docs/seo/
- Metacampos de producto creados: custom.material, medida_colgante, personalizacion, plazo_entrega, aviso_fechas (subtitulo ya existía). Acceso tienda online.
- Colecciones: regalos-personalizados y mascotas (ya existían, publicadas; añadida descripción y SEO), recuerdo-mascotas y joyeria-personalizada (nuevas, SIN publicar). Productos asignados según la tabla; P2 añadido a navidad.
- P1 colgante (16661035155847): aplicados título, descripción aprobada, SEO, tipo, proveedor Ojoconesedetalle, categoría Joyería > Collares (aa-6-8), etiquetas, metacampos, nombres de opciones (Colgante / Largo de cadena; 1 colgante 20 mm; 40/45/50 cm). Redirección 301 ya existía.
- P1 variantes: la usuaria borró las sobrantes (queda «Double-sided custom», a borrar). Añadida opción Color (Rosado = variantes originales enlazadas a Rose gold; Dorado y Plateado = 6 variantes NUEVAS sin SKU, hay que enlazarlas en DSers a Gold/Steel). Precio 4,62 = coste, pendiente precio de venta. Descripción, meta y subtítulo mencionan el color.
- P1 pendiente: imágenes (las 4 muestran 2-3 colgantes; la 4 es una tabla de tipografías en inglés). El SKU del proveedor indica color Rose gold.
- Bloques de metacampos en la plantilla de producto de Helio (tema activo): BLOQUEADO (despliegue en producción); pasos manuales dados.
- Apps de personalización: ningún plan gratuito revisado cumple todo (EasyFlow, Easify, Globo, Ultimate Product Options sin subida de archivos en gratis; Uploadly gratis = 20 pedidos y 60 días).
- Recordatorios programados: 25/11 (aviso Reyes) y 8/12 (vaciar aviso) del colgante.
- P1: «Double-sided custom» borrado por la usuaria (verificado: 9 variantes). Largos ordenados 40/45/50. SKU legibles en las variantes nuevas (COLGANTE-FOTO-20MM-DORADO-40CM...).
- P2 APLICADO (2026-10-27): adorno de madera con forma de huella (no bola). Título, descripción (con 2 [PENDIENTE]: límite del nombre y plazo), SEO, URL adorno-navidad-personalizado-mascota + 301, tipo, categoría hg-3-58-7, etiquetas, metacampos, opción «Diseño» (Navideño/Sencillo/Alas de ángel · perro/gato), fotos ordenadas (principal = huella navideña sola), alt y nombres de archivo en español. Sin publicar.

- 2026-10-27: colgante a 34,90 € (coste total 13,78 € con IVA, envío e importación, lo paga la usuaria). Opciones en orden Colgante → Largo de cadena → Color. FAQ «¿Tendré que pagar algo al recibirlo? No».
- Adorno: coste 11,76 € (5,69 + 6,07 importación, envío gratis), con cordel, personalización por «nota al vendedor» sin límite de caracteres conocido. Plazo 2–3 semanas; fechas límite Navidad 29/11 y Reyes 12/12 (1 + 15 + 7 días). Recordatorios programados 30/11 y 13/12. Precio de venta pendiente.
- Política de envío: apartado de personalizados ahora cubre colgante y adorno (plazos, fechas y aduana incluida).
- Metacampos de categoría (color con muestras, material): sin permisos de metaobjetos; la usuaria los pone a mano.
- Reseñas: la usuaria quiere Judge.me (importar de AliExpress); no tengo acceso a la app. Obligación legal de indicar el origen de las reseñas.

## Personalización gratis en el tema (2026-10-27)
- snippets/oc-personalizacion.liquid + bloque "Personalización" en sections/oc-producto.liquid: foto (JPG/PNG, tamaño máx.), texto (límite), tipografía (lista), casilla de confirmación. Se envían como propiedades del artículo (formulario multipart a /cart/add); validación en assets/oc-scripts.js (initPersonalizacion). Botón propio «Elegir foto».
- oc-producto muestra metacampos: subtítulo, aviso de fechas (encima del botón) y plazo de entrega; muestras de color si la opción tiene swatch.
- Plantillas: product.colgante-foto (foto 10 MB + texto 20 + tipografía F.1–F.16) y product.adorno-nombre (nombre 12). Garantía mostrada: «Garantía legal de 3 años». Antetítulo «Hecho a medida bajo pedido» (no «a mano»: no verificable).
- Probado en vista previa: formulario multipart, campos visibles, errores (vacío, formato, límite). NO probado el añadir al carrito (producto sin publicar) → hacer pedido de prueba al publicar.
- Colgante: fotos nuevas de la usuaria (un colgante por cadena) → principal = tres colores; todas las variantes con esa foto; nombres de archivo en español. Imagen de tipografías rehecha en español (la antigua borrada). Fotos 1-3 (varios colgantes / persona): propuestas para borrar, sin confirmar.
- Colores enlazados al metacampo de categoría por la usuaria; el valor «Rosa» debería llamarse «Rosado»; las muestras no tienen color (metaobjetos sin código de color; sin permisos para leerlos).
- Adorno a 24,90 €. Fichas sin «aduana»; política de envío sin «China» (solo «fuera de la UE»); privacidad mantiene China (obligatorio).

## Fichas P3–P6 y estructura (2026-10-27, tarde)
- Fichas P3 collar con nombre, P4 llavero, P5 collar con foto dentro, P6 colgante para cenizas: contenido en docs/seo/fichas_p3_p6.py, aplicado con herramientas/aplicar_fichas.py (textos, SEO, URL + 301, tipo, categoría, etiquetas, metacampos, plantilla, colecciones, nombres de opciones). Sin borrar variantes ni fotos.
- Metacampos de filtro: custom.para_quien y custom.ocasion (listas) en los 6 productos.
- Fotos: P3 23 imágenes de tipografía con «Tipografía X» en vez del texto en inglés + medidas en español; P5 3 infografías traducidas; P4 y P6 rehechas con IA sin la marca UniCrena y en español. Originales en docs/imagenes-originales/. Sustitución con fileUpdate originalSource (mismo media, misma variante).
- Tema: snippets oc-tarjeta, oc-etiquetas (Personalizable / Llega antes de Navidad / Llega para Reyes, también en tarjetas de Dawn), oc-whatsapp; secciones oc-pasos, oc-complementos, oc-carrito-sugerencias; bloques texto_extra y @app en oc-producto; oc-drop se oculta si su colección está vacía.
- Plantillas de producto: colgante-foto, adorno-nombre, collar-nombre, llavero-foto, collar-proyeccion, colgante-cenizas (ficha + cómo funciona + ventajas + completa tu regalo + marquesina).
- Portada: regalos personalizados en general + campaña mascotas; sin sección Black Friday. Carrito con sugerencias de «Regalos personalizados». Colecciones con segunda foto al pasar el ratón.
- Página nueva: /pages/como-elegir-la-foto.

## Precios, plazos y fechas (2026-10-27, noche)
- Precios: colgante 34,90 (coste 13,78) · adorno 24,90 (11,76) · collar nombre 29,90 (11,60–12,96) · llavero 29,90 (14,05) · collar proyección 34,90 (15,62–16) · colgante cenizas 39,90 (19,44).
- Todas las variantes de los 6 productos: «seguir vendiendo sin stock» (CONTINUE).
- Fechas límite automáticas: metacampos custom.fecha_navidad / custom.fecha_reyes + snippets/oc-aviso.liquid (texto junto al botón y etiqueta de tarjeta; cambian solos). Fórmula: 1 día + peor caso del proveedor + 7 días, contando desde el 22/12 y el 4/1.
  Colgante 24/11 y 7/12 · Adorno 29/11 y 12/12 · Collar nombre 15/11 y 28/11 · Llavero 28/11 y 11/12 · Proyección 24/11 y 7/12 · Cenizas 27/11 y 10/12. Recordatorios manuales cancelados (ya no hacen falta).
- Plazos: collar con nombre 3–4 semanas (peor caso ~30 días: en el límite legal), resto 2–3 semanas.
- Nombre comercial Movida 360 delante en las políticas; la titular (nombre y NIE) se mantiene en aviso legal, contacto y privacidad (obligatorio por la LSSI).
- Política de envío: apartado de personalizados con los 6 productos, plazos y fechas; IVA de importación incluido en todos (confirmar con la usuaria para P3–P6).
- Menú: Inicio · Regalos personalizados (Joyería, Mascotas, Recuerdo de mascotas, Navidad, Ver todos) · Para quién (Para ella, Para él, Para mascotas, Amigo invisible) · Ideas de regalo · Cómo elegir la foto · Quiénes somos · Contacto. Colección nueva Para mascotas (etiqueta para-mascotas). Publicadas: para-mascotas, recuerdo-mascotas, joyeria-personalizada. Recordatorio el 8/1/2027 para quitar Amigo invisible.
- WhatsApp: 34603603668 (botón flotante).
- Blog: 6 artículos nuevos EN BORRADOR (docs/blog/articulos_productos.py) — publicar junto con los productos. Fichas enlazan a sus artículos («Te puede interesar»).
- Collar de proyección: quedan 21 modelos con nombre en español. Foto «Fotos de compradores» traducida (decisión de la usuaria: se queda).
- Máscara y calendario vuelven a estar activos y publicados.

## Galería y colecciones (2026-10-27, noche)
- Galería de oc-producto rehecha: foto inicial = foto principal del producto (o la de la variante si viene ?variant=); al elegir variante muestra su foto; flechas, contador «n / total» y teclado; en ordenador miniaturas en columna a la izquierda, siempre visibles. Probado en el collar con nombre.
- Collar con nombre: foto principal = varios collares en mano; tipografías ordenadas B01…B18 y luego por nombre. Collar de proyección: 2.ª foto = la de la mascota.
- Navidad: los 6 personalizados. Mascotas: + collar de proyección. Amigo invisible: etiqueta en los 6.
- Configuración leída: plan Basic; impuestos incluidos; IVA en envíos DESACTIVADO; envía a ~40 países (debería ser solo España); zona España incluye Canarias, Ceuta y Melilla; tarifas Estándar 6,99 € y 0 €; sin pasarela de pago. Sin permisos para cambiar envíos, mercados ni pagos.

## Carrito y ventana emergente (2026-10-28)
- Las sugerencias del carrito no se veían: las tarjetas usan la animación oc-reveal y la página del carrito no cargaba oc-scripts.js. Ahora oc-carrito-sugerencias, oc-complementos y oc-pasos cargan el script.
- Ventana emergente al añadir al carrito (oc-producto, ajuste «emergente», colección de sugerencias, por defecto Regalos personalizados): envío por /cart/add.js con FormData (la foto se sube igual; probado en el llavero), actualiza la burbuja del carrito y muestra 3 sugerencias.
- Envío gratis preparado en el tema (Configuración del tema → Ojo Con → «Anunciar envío gratis»), APAGADO hasta que la tarifa de España sea 0 €. Hoy: España 6,99 € (gratis desde 55 €), además zonas UE (8,99 €) e Internacional (12,99 €) que hay que borrar.
- Quitado «(según el fabricante)» de fichas, artículos y colección de joyería (la usuaria ha comprobado las muestras).
- Collar de proyección: marca «YILI» tapada en 8 fotos. Llavero: opción «Default Title» → «Modelo: Corazón con huellas».
- Quiénes somos y artículo del amigo invisible sin enlace a «Menos de 20 €». Colecciones «Menos de 20 €» y «Black Friday» despublicadas con 301 (a Amigo invisible y Regalos personalizados).

## Pendiente
- [ ] Pasarela de pago, envíos solo a España (decidir Canarias/Ceuta/Melilla), IVA en envíos, facturas, email de dominio (la usuaria; pasos en el chat)
- [x] 2026-10-27: PUBLICADOS los 6 productos personalizados y los 6 artículos. Prueba real de carrito OK: foto subida a cdn.shopify.com/.../uploads, texto y tipografía como propiedades; sugerencias del carrito y WhatsApp visibles.
- [x] Pedido de prueba #1001 (28/10): foto y texto visibles en el pedido (ordenador y app). Pendiente: email de confirmación, mapping DSers (variantes desenlazadas), cancelar #1001
- [x] Máscara y calendario en BORRADOR (ya no se venden). Redirecciones 301: máscara → /collections/regalos-personalizados, calendario → /collections/navidad (también las direcciones antiguas en inglés). Artículo de la máscara en borrador con 301 al blog. Enlaces al calendario cambiados por el adorno. Descuento automático de Black Friday BORRADO y rebaja de campaña del tema desactivada (oc_camp_activa=false).
- [x] Search & Discovery: filtros comprobados en la tienda (Disponibilidad, Precio, Tipo, Color, Para quién, Ocasión). Ojo: el filtro Color usa la opción «Color» (colgante y collar de proyección); el collar con nombre la tiene como «Color y largo».
- [ ] Judge.me, Search & Discovery (filtros), canales de Google y Meta, Search Console (la usuaria)
- [x] IVA de importación P3–P6 lo paga la usuaria (confirmado)
- Reseñas: aviso «Opiniones de compradores de este mismo producto en AliExpress» encima de los bloques de app (ajuste resenas_aviso de oc-producto); estrellas activadas en las colecciones. Judge.me (Reviews + Importer) instalado por la usuaria. Search & Discovery instalado.

## Envíos y email de confirmación (2026-10-28)
- Envíos comprobados: una sola zona «España» sin Canarias, Ceuta ni Melilla (península + Baleares). Zonas UE e Internacional borradas. Tarifas: Estándar 6,99 € y gratis desde 55 €.
- Textos «toda España» → «península y Baleares»: política de envío, FAQ, Quiénes somos (publicados) y tema (confianza + marquesina; pendiente de publicar si el inicio de sesión del CLI caducó).
- Email de confirmación corregido en docs/emails/email-confirmacion-corregido.liquid: mensaje propio en la rama de envío normal (estaba en la de recogida dividida), aviso de 2 h para corregir la personalización, y foto/texto visibles en todas las líneas (antes solo en tarjetas regalo).
- Recomendación: envío gratis siempre durante el lanzamiento (el coste de envío ya va incluido en el coste del proveedor). IVA en envíos sigue DESACTIVADO: si se cobra envío, hay que activarlo.

## Revisión general (2026-10-28, tarde)
- Envío: tarifa Estándar gratis (dos tarifas: 1 € sin condición y 0 € desde 1 €; en el pago solo sale GRATIS). IVA en envíos ACTIVADO. Pago: tarjeta, PayPal, Shop Pay y Google Pay visibles en el pago (probado con carrito real, sin pagar).
- Tema: aviso «Envío gratis a península y Baleares» activado (ficha, confianza y marquesina). Política de envío y FAQ actualizadas.
- Problemas vistos en el pago: casilla «Enviarme novedades» PREMARCADA (RGPD: debe ir desmarcada); el envío dice «Se envía el siguiente día hábil» (falso para productos bajo pedido; también sale una fecha estimada en el email).
- Canales: solo Tienda online, Point of Sale y Shop. Productos publicados solo en Tienda online. Falta instalar Google & YouTube y Facebook & Instagram.
- Sin acceso para comprobar: carritos abandonados, Shopify Payments, facturas.

## Revisión completa y logo (2026-10-28, noche)
- Logo: docs/marca/ (original, horizontal transparente, icono, icono transparente, compartir 1200x628, logo-email). Subidos a Archivos: oc-logo-horizontal.png (cabecera, 220 px), oc-icono.png (favicon), oc-icono-transparente.png (pie), oc-compartir.jpg (imagen al compartir).
- Colores: coral #FF5A4E → terracota del logo #B9532E (contraste 4,8 con blanco); hover #9E4526.
- Corregido: código PRUEBA100% desactivado; email de todas las políticas → pedidos@; FAQ (plazos 2–4 semanas, fechas límite por producto, quitada pregunta de Black Friday); Quiénes somos (48 h, garantía 3 años en vez de 14 días); colecciones Navidad/Para ella/Para él/Amigo invisible con textos y SEO de regalos personalizados; artículo amigo invisible (adorno 24,90 €); menú sin «Para mascotas» (vacía); pie con texto nuevo; «Colecciones» y «Tu carrito está vacío».
- DSers vuelve a escribir compareAtPrice con el coste del proveedor: borrados otra vez (196 variantes). Hay que desactivar en DSers la sincronización de precio de comparación.
- Pendiente usuaria: formato de moneda «34,90 €», logo en emails y en el pago, quitar «Se envía el siguiente día hábil».
- Manual de gestión para la persona que lleve los pedidos: Claude Docs https://claude.ai/artifact/DqVs7f3Aw41wUMfNcHk4cx (rutina diaria, paso a paso DSers/AliExpress, chat con proveedor, plantillas, productos, problemas, calendario).
- Manual solo de pedidos (para la pareja de la usuaria): https://claude.ai/artifact/FydAWSTEamLymnJ1W9FEdn
- Tarea programada: revisión semanal los lunes 10:17 (Madrid), id trig_01XSYCYqY77hHQo8XfvfQVBS, vuelve a esta sesión.
