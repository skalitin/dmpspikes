import requests

import asyncio
import aiohttp
import adal

api = "http://localhost:8080/api/"

project_data = {'name': 'New Project',
                'description': 'Something here...',
                'type': 'activedirectory'}

project_id = 'new-project-1'
r_new_proj1 = requests.post(api + "projects/%s" % project_id, data=project_data)

project_data = {'name': 'Another Project', 'description': 'Something here...'}
project_id = 'new-project-2'
r_new_proj2 = requests.post(api + "projects/%s" % project_id, data=project_data)


response = requests.get("http://localhost:8080/api/projects")
print(response)



#Register connection berigy callback

data= {"pattern": "/api/connections/:id/verify", "method": "POST", "url": "http://localhost:5000/verify"}
requests.post(api + "callbacks", data=data)


data= {"pattern": "/api/connections", "method": "POST", "url": "http://localhost:5000/connections"}
requests.post(api + "callbacks", data=data)

collection = {
    "name": "test-two",
    "connectionId": "AVRnnRvvNUK6k1Qv_hLB",
    "projectId": "AVRnHPfRE94xB12-0ehn"
}
r = aiohttp.post("http://localhost:8080/api/collections", data=collection)


token_response = adal.acquire_token_with_client_credentials(
    "https://login.microsoftonline.com/397f39d7-9019-461f-ac09-d338c247f3ea",
    "b12cd57a-f0b1-4461-9bc9-ec0cb8db0692",
    "UntPnHdeQXxVmkT9qG9fhHC4v8itA4XZ3RTdDzUj5yM="
)