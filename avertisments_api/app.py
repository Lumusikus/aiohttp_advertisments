from aiohttp import web
import asyncio
import json
from db import init_db, create_ad, get_ad, get_all_ads, update_ad, delete_ad
from models import Advertisement

from aiohttp_swagger import setup_swagger

routes = web.RouteTableDef()

# создать объявление
@routes.post('/ads')
async def create_ad_handler(request):
    data = await request.json()
    ad_id = await create_ad(data['title'], data['description'], data['owner'])
    return web.json_response({'id': ad_id})

# получить все объявления
@routes.get('/ads')
async def get_ads_handler(request):
    rows = await get_all_ads()
    ads = [
        {'id': row[0], 'title': row[1], 'description': row[2], 'created_at': row[3], 'owner': row[4]}
        for row in rows
    ]
    return web.json_response(ads)

# получить одно объявление
@routes.get('/ads/{id}')
async def get_ad_handler(request):
    ad_id = int(request.match_info['id'])
    row = await get_ad(ad_id)
    if row:
        ad = {'id': row[0], 'title': row[1], 'description': row[2], 'created_at': row[3], 'owner': row[4]}
        return web.json_response(ad)
    return web.HTTPNotFound(text="Ad not found")

# редактировать объявление
@routes.put('/ads/{id}')
async def update_ad_handler(request):
    ad_id = int(request.match_info['id'])
    data = await request.json()
    await update_ad(ad_id, data['title'], data['description'], data['owner'])
    return web.json_response({'status': 'updated'})

# удалить объявление
@routes.delete('/ads/{id}')
async def delete_ad_handler(request):
    ad_id = int(request.match_info['id'])
    await delete_ad(ad_id)
    return web.json_response({'status': 'deleted'})

# запуск сервера
async def init_app():
    await init_db()
    app = web.Application()
    app.add_routes(routes)
    setup_swagger(app, swagger_url="/api/doc", ui_version=3)
    return app

if __name__ == '__main__':
    web.run_app(init_app(), host='127.0.0.1', port=8080)
