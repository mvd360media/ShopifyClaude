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
- Última publicación: 2026-10-17 (sesión 2) enlaces de colecciones, plazos, footer legal (tema sin publicar)

## Conexión (entorno en la nube)
- Dominios permitidos añadidos por el usuario: accounts/admin/partners.shopify.com,
  ccdf97-s7.myshopify.com, cdn.shopify.com, monorail-edge.shopifysvc.com.
- Ejecutar el CLI con NODE_USE_ENV_PROXY=1 (Node no usa el proxy por defecto).
- Login del tema: flujo con código (el usuario abre el enlace).
- store auth: redirige a 127.0.0.1; el usuario pega la URL de error y se entrega con curl local.
- La tienda está ABIERTA al público (sin contraseña): todo lo publicado en Tienda online se puede comprar.
- Sin permisos para menús (navegación) ni políticas legales de Shopify: enlaces legales van en un bloque de texto del footer.

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
  - Opción "Autonomía por carga": "1,5–2 h" (39,90 €) y "30–40 min" (29,90 €) — precios intercambiados por indicación de la usuaria (2026-10-17).
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
- Para ella (para-ella): máscara + calendario. Para él (para-el): calendario. Amigo invisible (amigo-invisible): calendario. Menos de 20 € (menos-de-20): automática, precio de variante < 20.
- Todas publicadas en Tienda online y enlazadas en las tarjetas de oc-regalos.

## Páginas legales (script: docs/legales/paginas.py)
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

## Pendiente
- [ ] 1 dic 2026: hero (botón) + CTA + barra de anuncios → Navidad
- [ ] Decidir con la usuaria: menú por temporadas, hero de marca vs campaña, colecciones por persona automáticas por etiqueta
- [ ] Revocar en OpenAI la clave pegada en el chat y crear otra (actualizar la variable de entorno)
- [ ] Datos del titular (nombre o razón social, NIF, dirección) → completar y publicar Aviso legal y Privacidad, y enlazarlas en el footer
- [ ] Confirmar plazos reales del proveedor (ahora prudentes: 7–15 días laborables)
- [ ] Publicar el tema como activo cuando la usuaria dé el visto bueno
- [x] 5 imágenes de producto rehechas en español
- [x] Imágenes de portada (hero + 4 tarjetas) y favicon
- [x] Productos publicados en Tienda online
- [x] Colecciones creadas, publicadas y enlazadas en portada
- [x] Precios de la máscara corregidos
