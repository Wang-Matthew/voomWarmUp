import tornado.ioloop
import tornado.web
import os
from weatherWidget import openWeatherMapAPI

# MainHandler class and make_app function are from Tornado doc

print("STARTING SERVER")


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello matt! Test")


# this is to handle the weather widget
class queryStringRequestHandler(tornado.web.RequestHandler):
    def get(self):
        n = str(self.get_argument("n")).title()
        r = openWeatherMapAPI.return_weather(n)
        self.render("template.html", r=r)


class blogRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("serverHandler.html")


class webApp(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/city", queryStringRequestHandler),
            (r"/blog", blogRequestHandler)
        ]

        settings = {
            "static_path": os.path.join(os.path.dirname(__file__), "static")}
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    app = webApp()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
