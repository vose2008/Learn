import web
from config import settings

render = settings.render

class index:
    def GET(self):
        return render.index()
