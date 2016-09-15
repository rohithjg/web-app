import tornado.ioloop
import tornado.httpserver
import tornado.web
import tornado.options
from tornado.options import *
from model.contact import engine
from model.contact import users

# Utility Libraries
import os.path

define("port", default=8889, help="run on the given port", type=int)


#Test Database Insert
ins = users.insert().values(id =1, firstname='ro', lastname='j', companyname='silicus', date='2016-09-15', notes='test')


# database connection using lazy initialization
connection=engine.connect()
result = connection.execute(ins)
result.close()

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("index.html")

class LoginHandler(BaseHandler):
    @tornado.gen.coroutine
    def get(self):
        incorrect = self.get_secure_cookie("incorrect")
        self.render("login.html")

    @tornado.gen.coroutine
    def post(self):
        incorrect = self.get_secure_cookie("incorrect")
        get_username = tornado.escape.xhtml_escape(self.get_argument("username"))
        get_password = tornado.escape.xhtml_escape(self.get_argument("password"))

        if "demo" == get_username and "demo" == get_password:
            self.set_secure_cookie("user", self.get_argument("username"))
            self.set_secure_cookie("incorrect", "0")
            self.redirect(self.reverse_url("main"))
            print self.reverse_url("main")
        else:
            self.write("""<center>
                Incorrect Login, Please Try Again <br />
                <a href="/">Go Home</a>
              </center>""")
            return

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect(self.get_argument("next", self.reverse_url("main")))
        print self.reverse_url("main")

class ContactHandler(BaseHandler):
    def post(self):
        self.write("Hello")
        return

class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self,[
        # r"/" == root website address
        tornado.web.url(r"/", MainHandler, name="main"),
        tornado.web.url(r'/login',LoginHandler, name="login"),
        tornado.web.url(r'/logout',LogoutHandler, name="logout"),
        tornado.web.url(r'/contact',ContactHandler, name="contact")
        ], **settings)


# Path for static files and templates, Instructs tornado from where to fetch information
settings = dict(
      cookie_secret = "srPsH0quSiq4VWfVZ/5UZTgXwKCCUUq4qkxVcRWpeQM=",
      login_url = "/login",
      template_path = os.path.join(os.path.dirname(__file__), "templates"),
      static_path = os.path.join(os.path.dirname(__file__), "static"),
      debug = True,
      xsrf_cookies = True,
)

# Start server from a dedicated port
if __name__ == "__main__":
  print 'Server running'
  Application().listen(options.port)
  tornado.options.parse_command_line()
  tornado.ioloop.IOLoop.instance().start()