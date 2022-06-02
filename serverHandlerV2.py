import tornado.ioloop
import tornado.web
import os
from weatherWidget import openWeatherMapAPI

# this entire .py file was just to figure out the StaticFileHandler,


class templateHandler(tornado.web.RequestHandler):
    def get(self):
        n = str(self.get_argument("n"))
        r = openWeatherMapAPI.return_weather(n)
        self.render("template.html", r=r)


class webApp(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/city", templateHandler)
        ]

        settings = {
            "static_path": os.path.join(os.path.dirname(__file__), "static")}
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    print("STARTING SERVER")
    app = webApp()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
