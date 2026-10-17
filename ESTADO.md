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

## Pendiente
- [ ] Clave de OpenAI → generar imágenes (la variable OPENAI_API_KEY existe pero la clave es inválida: parece copiada recortada)
- [x] Productos importados (2): plantilla "oc" asignada y vendor "Ojo Con Ese Detalle" (2026-10-17)
  - Máscara LED (gid://shopify/Product/16649284485511): imágenes 2,3,6 con claims médicos y antes/después; 4,5,7,8 con texto en inglés; variantes "400mah no box"/"No Box" confusas; ambas sin caja
  - Calendario adviento (gid://shopify/Product/16649471754631): imagen 1 con marca de agua de otra tienda; 2 con texto en inglés; 6 en alemán (¿variante A2?); descripción habla de diseño "2026" que no coincide con las fotos; stock 1 unidad
  - compareAtPrice menor que el precio en ambos (parece el coste del proveedor): revisar regla de precios de DSers
  - Productos NO publicados en el canal Tienda online (publishedAt null) → no se ven en la web
- [ ] Crear colecciones (Drop Navidad, Para ella, Para él, Amigo invisible, Menos de 20 €) y enlazarlas
- [x] Nombre de la tienda: Ojo con ese detalle
- [ ] Políticas legales, plazos de entrega reales tras ver tiempos del proveedor
