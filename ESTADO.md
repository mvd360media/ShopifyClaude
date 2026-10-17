# Estado del proyecto — Ojo Con Ese Detalle

- Tienda: ccdf97-s7.myshopify.com
- Dominio: ojoconesedetalle.es (DNS apuntado a Shopify, verificación en curso)
- Carpeta del tema: tema/ (este repositorio)
- Tema base: Dawn (Shopify/dawn main, commit 258f00f 2026-08-10)
- Entorno: Node v22.22.0, Shopify CLI 4.9.4 — OK
- Tema de trabajo: "Ojo Con Ese Detalle (Claude)" #211921994119 (sin publicar)
  - Vista previa: https://ccdf97-s7.myshopify.com?preview_theme_id=211921994119
  - Editor: https://ccdf97-s7.myshopify.com/admin/themes/211921994119/editor
- Tema activo actual: Helio #211593757063 (no tocar)
- Última publicación: 2026-10-17 portada y plantilla de producto (sin publicar)

## Conexión (entorno en la nube)
- Dominios permitidos añadidos por el usuario: accounts/admin/partners.shopify.com,
  ccdf97-s7.myshopify.com, cdn.shopify.com, monorail-edge.shopifysvc.com.
- Ejecutar el CLI con NODE_USE_ENV_PROXY=1 (Node no usa el proxy por defecto).
- Login del tema: flujo con código (el usuario abre el enlace).
- store auth: redirige a 127.0.0.1; el usuario pega la URL de error y se entrega con curl local.
- Producto: la tienda NO tiene productos todavía (2026-10-17).

## Fases completadas
- [x] 0 Entorno
- [x] 1 Conexión (tema + datos de la tienda)
- [x] 2 Proyecto (Dawn subido como tema sin publicar)
- [x] 3 Diseño (estilo aprobado por el usuario)
- [x] 4 Construcción (portada)
- [ ] 5 Páginas
- [ ] 6 Publicación

## Decisiones de diseño
- Prefijo propio: oc- (Ojo Con). CSS en assets/oc-styles.css, JS en assets/oc-scripts.js.
- Paleta: fondo #FBF8F4, alt #F3ECE3, tinta #1E1B2E, coral #FF5A4E, temporada (Navidad) #1F5E4A.
- Tipografía: Bricolage Grotesque (titulares, Google Fonts en layout/theme.liquid) + DM Sans (texto; dm_sans en ajustes del tema).
- Botones píldora, esquinas 16–32px, ojo animado como elemento de marca.
- Sin reseñas inventadas: se añadirán cuando haya reseñas reales.
- Imágenes con IA: aprobadas por el usuario; clave pendiente (variable de entorno OPENAI_API_KEY).
- Textos en imágenes de producto en inglés: traducir o regenerar en español.
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
  - Opción "Autonomía por carga": "1,5–2 h" (29,90 €) y "30–40 min" (39,90 €) — según imágenes del proveedor. OJO: la de más autonomía es la más barata → confirmar precios con el usuario.
  - Imágenes con texto en inglés a rehacer en español: MediaImage 77748808515975 (Multi-effect care), 77748808548743 (Wireless operation), 77748808614279 (400mAh 1.5-2h No box), 77748808647047 (400mAh 30-40min No box). Las dos últimas son imágenes de variante.
- Calendario de Adviento — gid://shopify/Product/16649471754631 — plantilla "oc"
  - Quitada imagen con marca de agua de otra tienda. Descripción reescrita (coincide con las fotos). Título sin "2026".
  - Opción "Diseño": "Merry Christmas" / "Advent (texto en alemán)". Opción "Size" eliminada.
  - Imagen con texto en inglés a rehacer: MediaImage 77756163391879 ("Back Details / Wood Rod").
  - Stock 1 unidad por variante (revisar sincronización de DSers).
- compareAtPrice borrado en ambos (DSers ponía el coste del proveedor).
- Ninguno publicado en el canal Tienda online (publishedAt null).

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
- [ ] Clave OpenAI válida (en esta sesión la variable tiene una clave recortada; el valor nuevo se aplica en sesión nueva)
- [ ] Rehacer en español las 5 imágenes con texto en inglés (lista arriba) y sustituirlas conservando el orden y la imagen de variante
- [ ] Generar imágenes de portada: hero, 4 tarjetas "regalos por persona", favicon/logo con el ojo
- [ ] Publicar productos en Tienda online (con write_publications o el usuario a mano)
- [ ] Crear colecciones (Drop de Navidad, Para ella, Para él, Amigo invisible, Menos de 20 €), publicarlas y enlazarlas en la portada (oc-drop.coleccion y URLs de oc-regalos)
- [ ] Confirmar precios de las variantes de la máscara
- [ ] Políticas legales, plazos de entrega reales tras ver tiempos del proveedor
