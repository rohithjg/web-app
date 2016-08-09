import tornado.ioloop
import tornado.web

# Utility Libraries
import os.path


class MainHandler(tornado.web.RequestHandler):

  def get(self):
    self.write("WELCOME TO HANDS ON LEARNING")
    self.render("login.html")

# Path for static files and templates
# Instructs tornado from where to fetch information
settings = dict(
      template_path = os.path.join(os.path.dirname(__file__), "templates"),
      static_path = os.path.join(os.path.dirname(__file__), "static"),
      debug = True
)

# r"/" == root website address
application =  tornado.web.Application([
    (r"/", MainHandler)
],**settings)


# Start server from a dedicated port
if __name__ == "__main__":
  print 'Server running'

  application.listen(8889)
  tornado.ioloop.IOLoop.instance().start()

