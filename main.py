import cherrypy


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        print("hello-world")
        return "This is my app" 


if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld()) 