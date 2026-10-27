# Aplica las fichas de docs/seo/fichas_p3_p6.py: textos, SEO, URL con redirección, organización, metacampos,
# colecciones y nombres de opciones. No borra variantes ni fotos.
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs', 'seo'))
from gql import run
from fichas_p3_p6 import FICHAS

cols = {c['handle']: c['id'] for c in run('{collections(first:50){nodes{id handle}}}', mutate=False)['collections']['nodes']}
solo = sys.argv[1:] or list(FICHAS)
for clave in solo:
    f = FICHAS[clave]
    pid = "gid://shopify/Product/" + f['id']
    antes = run('{product(id:"%s"){handle options{id name optionValues{id name}}}}' % pid, mutate=False)['product']
    assert len(f['titulo']) <= 75 and len(f['seo_t']) <= 60 and len(f['seo_d']) <= 160, (clave, len(f['titulo']), len(f['seo_t']), len(f['seo_d']))
    mf = [{"namespace": "custom", "key": k, "type": "single_line_text_field", "value": v} for k, v in f['meta'].items()]
    mf += [{"namespace": "custom", "key": "para_quien", "type": "list.single_line_text_field", "value": json.dumps(f['para_quien'], ensure_ascii=False)},
           {"namespace": "custom", "key": "ocasion", "type": "list.single_line_text_field", "value": json.dumps(f['ocasion'], ensure_ascii=False)}]
    inp = {"id": pid, "title": f['titulo'], "handle": f['url'], "descriptionHtml": f['desc'], "vendor": "Ojoconesedetalle",
           "productType": f['tipo'], "category": "gid://shopify/TaxonomyCategory/" + f['categoria'], "tags": f['etiquetas'],
           "templateSuffix": f['plantilla'], "seo": {"title": f['seo_t'], "description": f['seo_d']}, "metafields": mf}
    r = run('mutation($i:ProductInput!){productUpdate(input:$i){product{handle} userErrors{field message}}}', {"i": inp})
    print(clave, 'ficha', r['productUpdate']['userErrors'] or 'ok')
    if antes['handle'] != f['url']:
        r = run('mutation($r:UrlRedirectInput!){urlRedirectCreate(urlRedirect:$r){userErrors{message}}}',
                {"r": {"path": "/products/" + antes['handle'], "target": "/products/" + f['url']}})
        print(clave, 'redirección', r['urlRedirectCreate']['userErrors'] or 'ok')
    for h in f['colecciones']:
        r = run('mutation($id:ID!,$p:[ID!]!){collectionAddProducts(id:$id,productIds:$p){userErrors{message}}}', {"id": cols[h], "p": [pid]})
        print(clave, 'colección', h, r['collectionAddProducts']['userErrors'] or 'ok')
    for o in antes['options']:
        if o['name'] not in f['opciones']:
            continue
        nombre, valores = f['opciones'][o['name']]
        upd = [{"id": v['id'], "name": valores[v['name']]} for v in o['optionValues'] if v['name'] in valores]
        r = run('''mutation($p:ID!,$o:OptionUpdateInput!,$v:[OptionValueUpdateInput!]){productOptionUpdate(productId:$p,option:$o,optionValuesToUpdate:$v,variantStrategy:LEAVE_AS_IS){userErrors{field message}}}''',
                {"p": pid, "o": {"id": o['id'], "name": nombre}, "v": upd})
        print(clave, 'opción', nombre, r['productOptionUpdate']['userErrors'] or 'ok')
