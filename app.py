import tornado.ioloop
import tornado.web
from mathw import MathWork

from config import Config


class MainHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "content-type")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PATCH, PUT')
        # HEADERS!
        self.set_header("Access-Control-Allow-Headers", "access-control-allow-origin,authorization,content-type")

    def options(self, *args):
        self.set_status(204)
        self.finish()

    def get(self):
        series = self.get_argument('series')
        level = self.get_argument('level')
        MathWork(series=series.capitalize(),
                 level=level,
                 outputName=Config().get_file_path(series, level)).go()
        self.finish({'status': 1})


class MathWorkApp(object):

    def __init__(self):
        self._app = tornado.web.Application([
            (r"/", MainHandler),
        ])

    @staticmethod
    def _init_cache():
        c = Config()
        if not c.front_path.exists():
            c.front_path.mkdir()
        if not c.cache_path.exists():
            c.cache_path.mkdir()

    def run(self):
        self._init_cache()
        self._app.listen(8888)
        tornado.ioloop.IOLoop.current().start()


