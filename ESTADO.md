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
- Última publicación: 2026-10-17 primera subida de Dawn base

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
- [ ] 3 Diseño
- [ ] 4 Construcción
- [ ] 5 Páginas
- [ ] 6 Publicación

## Decisiones de diseño
- Marca: Ojo Con Ese Detalle. Tono cercano, emocional, tipo "OhMyGift".
- Modelo: colecciones de temporada (drops) + productos fijos. Primera campaña: Black Friday / Navidad / Reyes.

## Secciones creadas
(se rellena en la fase 4)
