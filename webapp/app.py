import tornado.ioloop
import tornado.httpserver
import tornado.web
import tornado.options
from tornado.options import *
from model.contact import *
from model.register import stakeholders


# Utility Libraries
import os.path

define("port", default=8889, help="run on the given port", type=int)

#Test Database Insert
# ins = users.insert().values(id ='1', firstname='hi', lastname='j', companyname='silicus', date='2016-09-15', notes='test')

# database connection using lazy initialization
# connection=engine.connect()
# result = connection.execute(ins)
# result.close()


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
        print get_username
        print get_password
        print stakeholders.c.username
        #if stakeholders.c.username == get_username and stakeholders.c.password == get_password:
        #    print 'hello'
        if "demo" == get_username and "demo" == get_password:
            self.set_secure_cookie("user", self.get_argument("username"))
            self.set_secure_cookie("incorrect", "0")
            self.redirect(self.reverse_url("main"))
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
    @tornado.gen.coroutine
    def post(self):
        self.write('Record Created Successfully')
        get_id = tornado.escape.xhtml_escape(self.get_argument("id"))
        get_companyname = tornado.escape.xhtml_escape(self.get_argument("companyname"))
        get_date = tornado.escape.xhtml_escape(self.get_argument("date"))
        get_notes = tornado.escape.xhtml_escape(self.get_argument("notes"))
        # database connection using lazy initialization
        connection = engine.connect()
        #data write query
        ins = users.insert().values(id=get_id,companyname=get_companyname, date=get_date, notes=get_notes)
        # query execution
        result = connection.execute(ins)
        # database connection close
        result.close()
        return


class RegistrationHandler(BaseHandler):
    @tornado.gen.coroutine
    def get(self):
        self.render("registration.html")

    @tornado.gen.coroutine
    def post(self):
        self.write('Hurray!! Registration Successful')
        get_firstname = tornado.escape.xhtml_escape(self.get_argument("firstname"))
        get_lastname = tornado.escape.xhtml_escape(self.get_argument("lastname"))
        get_email = tornado.escape.xhtml_escape(self.get_argument("email"))
        get_sex = tornado.escape.xhtml_escape(self.get_argument("sex"))
        new_user = tornado.escape.xhtml_escape(self.get_argument("username"))
        new_pwd = tornado.escape.xhtml_escape(self.get_argument("password"))
        # database connection using lazy initialization
        connection = engine.connect()
        duc = stakeholders.insert().values(firstname=get_firstname, lastname=get_lastname, email=get_email,
                                    sex=get_sex, username=new_user,
                                    password=new_pwd)
        result = connection.execute(duc)
        result.close()
        return

class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self,[
        # r"/" == root website address
        tornado.web.url(r"/", MainHandler, name="main"),
        tornado.web.url(r'/login',LoginHandler, name="login"),
        tornado.web.url(r'/logout',LogoutHandler, name="logout"),
        tornado.web.url(r'/contact',ContactHandler, name="contact"),
        tornado.web.url(r'/register', RegistrationHandler, name="register")
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