from aiohttp import web
import socketio
from sqlitemodel import SQL
from src.database.model.SyncFolderModel import SyncFolder

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

async def index(request):
    """Serve the client-side application."""
    with open('web/dist/index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.event
def connect(sid, environ):
    print("connect ", sid)

@sio.event
async def chat_message(sid, data):
    print("message ", data)

@sio.event
async def ListSyncFolders(sid, data):
   return SyncFolder().select(SQL())

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

app.router.add_static('/assets', 'web/dist/assets')
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)