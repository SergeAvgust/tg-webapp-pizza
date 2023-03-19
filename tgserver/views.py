from aiohttp import web
import aiosqlite
import aiohttp_jinja2
from settings import BASE_DIR

@aiohttp_jinja2.template('webapp.html')
async def webapp(request):
    async with aiosqlite.connect(str(BASE_DIR / "server.db")) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT * FROM pizza;") as cursor:
            pizzas = [{k: item[k]  for k in item.keys()} for item in await cursor.fetchall()]
            return {"pizzas": pizzas} # id, name, img, price

@aiohttp_jinja2.template('index.html')
async def index(request):
    async with aiosqlite.connect(str(BASE_DIR / "server.db")) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT * FROM pizza;") as cursor:
        #    pizzas = cursor
        #    pizzas2 = await pizzas.fetchall()
        #    print(pizzas2[0]['id'])
            pizzas = [{k: item[k]  for k in item.keys()} for item in await cursor.fetchall()]
        async with db.execute("""
            SELECT id
                , user
                , group_concat(pizzas) AS total_pizzas
                , money
            FROM (
                SELECT o.id, o.user, (p.name || ": " || op.pizza_amount) AS pizzas, o.money
                FROM orders AS o
                JOIN ordered_pizza AS op ON op.order_id = o.id
                JOIN pizza AS p ON p.id = op.pizza_id
                )
            ORDER BY id;
            """) as cursor:
            orders = [{k: item[k]  for k in item.keys()} for item in await cursor.fetchall()]
        #pizzas = [dict(p) for p in pizzas]
        return {"pizzas": pizzas,
                "orders": orders}
        


