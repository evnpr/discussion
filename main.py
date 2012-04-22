import web
from web.contrib.template import render_jinja
from models import profile, database
db = database.database()

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
    password = db.query("SELECT * FROM profile")[0]
    halo = profile.getUser()
    return render.index(halo=halo, password = password)

if __name__ == "__main__":
  app.run()
