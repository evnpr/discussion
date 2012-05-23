import web
from web.contrib.template import render_jinja
from models import profile, database
from hello import *


def index():
    db = database.database()
    urls = (
                '/', 'hello'
                        )
    render = render_jinja(
                  'templates',                 # Set template directory.
                   encoding = 'utf-8',         # Encoding.
                           )


app = web.application(urls, globals())

if __name__ == "__main__":
  app.run()
