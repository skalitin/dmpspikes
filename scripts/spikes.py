import requests
import asyncio
import aiohttp
import adal
import json
import datetime

api = "http://localhost:8080/api"

project_data = {'name': 'New Project',
                'description': 'Something here...',
                'type': 'activedirectory'}

project_id = 'new-project-1'
r_new_proj1 = requests.post(api + "/projects/%s" % project_id, data=project_data)

#Delete all collections
response = requests.get(api + "/collections")
data = json.loads(response.text)
for h in data['hits']['hits']:
    coll_id = h['_id']
    requests.delete(api + "/collections/" + coll_id)

#Sync backups
#for i in range(1,3):
i = 1
data = dict(
    title="New Backup %s" % i,
    when=datetime.datetime.now().isoformat(),
    users=42 + i,
    projectId='new-project-1',
    tenantId='tenant2',
   # collections='["tenant2"]',
    connectionId='AVRxAJKbplFxrm2a1RZO')
res = requests.post(api + "/backups/backup%s" % i, data=data)
print(res.text)

res = requests.post(api + "/collections/tenant2/backups",data=data)
print(res.text)

    #connectionId = 'AVRwti3HmB7CB6pk7BZW'