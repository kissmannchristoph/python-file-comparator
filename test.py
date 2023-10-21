import array
import json
from aiohttp import web
import socketio
from sqlitemodel import SQL
from src.database.model.SyncFolderModel import SyncFolder
import pickle
from json import JSONEncoder
from src.shared.types_pb2 import *
from src.shared.network_pb2 import ListSyncFoldersResponse
from google.protobuf.json_format import MessageToJson

sio = socketio.AsyncServer(cors_allowed_origins='*')
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

class test():
    def __init__(self):
        self.a = "asdasd"

    def toJSON(self):
            return json.dumps(self, default=lambda o: o.__dict__, 
                sort_keys=True, indent=4)

def default_serializer(obj):
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    # Für andere Datentypen, die nicht serialisiert werden können, 
    # können Sie eine benutzerdefinierte Logik hinzufügen oder 
    # einfach TypeError werfen.
    raise TypeError(f"Type {type(obj)} not serializable")

@sio.event
async def ListSyncFolders(sid, data = None):
   folders = []
   
   for f in SyncFolder().select(SQL()):
    folders.append(SharedSyncFolder(name=f.name, targetFolder=f.targetFolder, originFolder=f.originFolder))

   response = ListSyncFoldersResponse(syncFolders=folders)
   await sio.emit("ListSyncFolders", MessageToJson(response))

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

app.router.add_static('/assets', 'web/dist/assets')
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)