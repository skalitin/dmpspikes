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

#delete all objects
response = requests.get(api + "/objects")
data = json.loads(response.text)
for h in data['hits']['hits']:
    id = h['_id']
    requests.delete(api + "/objects/" + id)

#Delete all collections
response = requests.get(api + "/collections")
data = json.loads(response.text)
for h in data['hits']['hits']:
    id = h['_id']
    requests.delete(api + "/collections/" + id)

#Sync backups to collection
collection_id = 'tenant2'
for i in range(1,3):
    data = dict(
        title="New backup %s" % i,
        when=datetime.datetime.now().isoformat(),
        users=5000 + i,
        projectId='new-project-1',
        tenantId='tenant2')
    res = requests.post("%s/collections/%s/backups" % (api, collection_id), data=data)
    print(res.text)

#Create objects
collection_id = 'tenant2'
for i in range(0,3):
    data = dict(
        displayName="User %s" % i,
        mail="mail %s" % i,
        name="Name %s" % i,
        location="location %s" % i,
        projectId='new-project-1',
        backupDate=datetime.datetime.now().isoformat(),
        tenantId='tenant2')
    res = requests.post("%s/collections/%s/objects" % (api, collection_id), data=data)
    print(res.text)

