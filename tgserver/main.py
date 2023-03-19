from aiohttp import web
import aiohttp_jinja2
import jinja2
import asyncio

from settings import config, BASE_DIR
from routes import setup_routes, setup_static_routes
from botapp import bot, bot_setup

async def main():
    print('starting')
    await bot.initialize()
    await bot.start()
    await bot.updater.start_polling()
    app = web.Application()
    setup_routes(app)
    app['config'] = config
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(BASE_DIR / 'tgserver' / 'templates')))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8000)
    await site.start()

    await bot.updater.stop()
    await bot.stop()
    await bot.shutdown()

def main2():
    app = web.Application()
    setup_routes(app)
    setup_static_routes(app)
    app['config'] = config
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(BASE_DIR / 'tgserver' / 'templates')))
    app.cleanup_ctx.append(bot_setup)
    web.run_app(app)

if __name__ == "__main__":
    # asyncio.run(main())
    main2()