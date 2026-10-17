import json,os,subprocess,time,mimetypes
from gql import run

def staged(path):
    """Sube un archivo local al almacén temporal de Shopify y devuelve su resourceUrl."""
    name=os.path.basename(path); mime=mimetypes.guess_type(path)[0] or 'image/jpeg'
    r=run('''mutation($i:[StagedUploadInput!]!){stagedUploadsCreate(input:$i){stagedTargets{url resourceUrl parameters{name value}} userErrors{field message}}}''',
          {"i":[{"filename":name,"mimeType":mime,"resource":"IMAGE","httpMethod":"POST","fileSize":str(os.path.getsize(path))}]})
    t=r['stagedUploadsCreate']['stagedTargets'][0]
    cmd=['curl','-s','-o','/dev/null','-w','%{http_code}']
    for p in t['parameters']: cmd+=['-F',f"{p['name']}={p['value']}"]
    cmd+=['-F',f'file=@{path};type={mime}',t['url']]
    code=subprocess.run(cmd,capture_output=True,text=True).stdout
    if not code.startswith('2'): raise RuntimeError(f'subida fallida HTTP {code}')
    return t['resourceUrl']

def subir_archivo(path,alt=''):
    """Sube una imagen a Contenido → Archivos. Devuelve 'shopify://shop_images/<nombre>'."""
    r=run('''mutation($f:[FileCreateInput!]!){fileCreate(files:$f){files{id fileStatus} userErrors{field message}}}''',
          {"f":[{"originalSource":staged(path),"contentType":"IMAGE","alt":alt,"filename":os.path.basename(path)}]})
    e=r['fileCreate']['userErrors']
    if e: raise RuntimeError(e)
    fid=r['fileCreate']['files'][0]['id']
    for _ in range(30):
        s=run('query($id:ID!){node(id:$id){... on MediaImage{fileStatus image{url}}}}',{"id":fid},mutate=False)['node']
        if s['fileStatus']=='READY':
            nombre=s['image']['url'].split('/files/')[-1].split('?')[0]
            return fid,'shopify://shop_images/'+nombre
        if s['fileStatus']=='FAILED': raise RuntimeError('procesado fallido')
        time.sleep(2)
    raise RuntimeError('tiempo de espera agotado')

def subir_media_producto(product_id,path,alt=''):
    """Añade una imagen a la galería del producto. Devuelve el id del nuevo media."""
    r=run('''mutation($p:ID!,$m:[CreateMediaInput!]!){productCreateMedia(productId:$p,media:$m){media{id} mediaUserErrors{field message}}}''',
          {"p":product_id,"m":[{"originalSource":staged(path),"mediaContentType":"IMAGE","alt":alt}]})
    e=r['productCreateMedia']['mediaUserErrors']
    if e: raise RuntimeError(e)
    mid=r['productCreateMedia']['media'][0]['id']
    for _ in range(30):
        s=run('query($id:ID!){node(id:$id){... on MediaImage{status}}}',{"id":mid},mutate=False)['node']
        if s['status']=='READY': return mid
        if s['status']=='FAILED': raise RuntimeError('procesado fallido')
        time.sleep(2)
    raise RuntimeError('tiempo de espera agotado')
