import web
from web.contrib.template import render_jinja


db = web.database(dbn='mysql', db='discussion', user='root', pw='abc123')

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
    results = db.query("SELECT * FROM profile")
    halo = results[0]
    return render.index(halo=halo)

if __name__ == "__main__":
  app.run()
