import web
from web.contrib.template import render_jinja

urls = (
            '/', 'hello'
                    )

app = web.application(urls, globals())
render = render_jinja(
              'templates',                 # Set template directory.
               encoding = 'utf-8',         # Encoding.
                       )

class hello:
  def GET(self):
    halo = 'Hello world!!'
    return render.index(halo=halo)

if __name__ == "__main__":
  app.run()
