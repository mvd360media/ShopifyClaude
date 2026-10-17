import json,subprocess,sys,tempfile,os
def run(query, variables=None, mutate=True):
    qf=tempfile.NamedTemporaryFile('w',suffix='.graphql',delete=False); qf.write(query); qf.close()
    cmd=['shopify','store','execute','--store','ccdf97-s7.myshopify.com','--query-file',qf.name,'--json']
    if variables is not None:
        vf=tempfile.NamedTemporaryFile('w',suffix='.json',delete=False); json.dump(variables,vf,ensure_ascii=False); vf.close(); cmd+=['--variable-file',vf.name]
    if mutate: cmd.append('--allow-mutations')
    env=dict(os.environ,NODE_USE_ENV_PROXY='1',NODE_NO_WARNINGS='1')
    r=subprocess.run(cmd,capture_output=True,text=True,env=env,cwd='/home/user/ShopifyClaude')
    try: return json.loads(r.stdout)
    except Exception: return {'_raw':r.stdout[-1500:],'_err':r.stderr[-1500:]}
