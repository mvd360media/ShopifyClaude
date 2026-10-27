# Estado del proyecto — Ojo Con Ese Detalle

- Tienda: ccdf97-s7.myshopify.com
- Dominio: ojoconesedetalle.es (DNS apuntado a Shopify, verificación en curso)
- Carpeta del tema: tema/ (este repositorio)
- Tema base: Dawn (Shopify/dawn main, commit 258f00f 2026-08-10)
- Entorno: Node v22.22.0, Shopify CLI 4.9.4 — OK (reinstalado 2026-10-17, sesión 2)
- Tema de trabajo: "Ojo Con Ese Detalle (Claude)" #211921994119 (sin publicar)
  - Vista previa: https://ccdf97-s7.myshopify.com?preview_theme_id=211921994119
  - Editor: https://ccdf97-s7.myshopify.com/admin/themes/211921994119/editor
- Tema activo actual: Helio #211593757063 (no tocar)
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
- Decisiones de la usuaria: envío a toda España; IVA de importación del colgante NO incluido (puede haber cargos); devoluciones a Calle Colón, 1, 46016 Tavernes Blanques (CP deducido, confirmar), a cargo del cliente; cancelar personalizados en 2 h; respuesta en 48 h laborables; fotos borradas 30 días tras la entrega; transferencia a China por art. 49.1.b RGPD.
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

## Pendiente
- [ ] Confirmar qué producto es el "Colgante personalizado con foto de mascota" y adaptar su ficha (español, 20 mm, 40/45/50 cm, foto + texto 20 caracteres, fechas límite, precio de venta)
- [ ] Operativa: no enviar pedidos personalizados al fabricante hasta pasadas 2 h (plazo de cancelación)
- [ ] 1 dic 2026: hero (imagen oc-h-hero.jpg, textos y botón) + CTA + barra de anuncios → Navidad
- [ ] Dar de alta la tienda en Google Search Console y enviar el sitemap (la usuaria, con su cuenta de Google)
- [ ] Enero: cambiar la tarjeta "Amigo invisible" por la temporada siguiente (San Valentín)
- [ ] Revocar en OpenAI la clave pegada en el chat y crear otra (actualizar la variable de entorno)
- [ ] Datos del titular (nombre o razón social, NIF, dirección) → completar y publicar Aviso legal y Privacidad, y enlazarlas en el footer
- [ ] Confirmar plazos reales del proveedor (ahora prudentes: 7–15 días laborables)
- [ ] Publicar el tema como activo cuando la usuaria dé el visto bueno
- [x] 5 imágenes de producto rehechas en español
- [x] Imágenes de portada (hero + 4 tarjetas) y favicon
- [x] Productos publicados en Tienda online
- [x] Colecciones creadas, publicadas y enlazadas en portada
- [x] Precios de la máscara corregidos
