# -*- coding:utf-8 -*-

import os
from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(body=text.encode('utf-8'))

app = web.Application()
app.router.add_route('GET', '/{name}', handle)
port = int(os.environ['PORT'])
web.run_app(app, port=port)
