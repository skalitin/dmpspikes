import json
import logging
import adal

format = ' '.join(
    ['%(asctime)s',
     '%(levelname)s',
     '%(module)s',
     '%(funcName)s',
     'L%(lineno)s',
     '%(message)s'])

logging.basicConfig(format=format, level=logging.INFO)

import asyncio
import aiohttp
from aiohttp import web


async def create_collection(request):
    response = await request.read()
    data = json.loads(response.decode())

    if not (data["data"].__contains__("draft") & data["data"]["draft"]):
        collection = {
            "name": data["data"]["name"],
            "connectionId": data["id"],
            "projectId": data["data"]["projectId"]
        }

        logging.info("Creating collection %s..." % collection["name"])
        response = await aiohttp.post("http://localhost:8080/api/collections", data=collection)
        logging.info(response)

    return web.Response(body=b"{}")


async def test_connection(request):
    response = await request.read()
    data = json.loads(response.decode())

    connection_data = data["data"]
    connection_id = data["id"]

    if connection_data.__contains__("draft") & connection_data["draft"]:
        tenant_id = connection_data["tenantId"]
        client_id = connection_data["clientId"]
        client_secret = connection_data["clientSecret"]

        try:
            logging.error("Getting token for tenant %s and client id %s..." % (tenant_id, client_id))
            token_response = adal.acquire_token_with_client_credentials(
                "https://login.microsoftonline.com/%s" % tenant_id,
                client_id,
                client_secret)

            logging.info("Access token acquired")
            response = await aiohttp.patch("http://localhost:8080/api/connections/%s" % connection_id,
                                           data={"verified": "true"})
        except Exception as ex:
            logging.error("Error getting token: %s" % ex)
            response = await aiohttp.patch("http://localhost:8080/api/connections/%s" % connection_id,
                                           data={"verified": "false", "verificationError": ex})

    return web.Response(body=b"{}")


if __name__ == "__main__":
    app = web.Application()
    app.router.add_route("POST", "/verify", test_connection)
    app.router.add_route("POST", "/connections", create_collection)

    loop = asyncio.get_event_loop()
    handler = app.make_handler()

    f = loop.create_server(handler, '0.0.0.0', 5000)
    logging.info("Listening...")
    loop.run_until_complete(f)

    loop.run_forever()
