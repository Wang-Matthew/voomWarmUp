import tornado.ioloop
import tornado.web
from weatherWidget import openWeatherMapAPI

# MainHandler class and make_app function are from Tornado doc
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello matt!")


class queryStringRequestHandler(tornado.web.RequestHandler):
    def get(self):
        n = str(self.get_argument("n"))
        r = openWeatherMapAPI.return_weather(n)
        self.write(r)

class blogRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("serverHandler.html")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", MainHandler),
        (r"/city", queryStringRequestHandler),
        (r"/blog", blogRequestHandler)
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()