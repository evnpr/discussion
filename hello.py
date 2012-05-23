from main import *

class hello:
  def GET(self):
    password = db.query("SELECT * FROM profile")[0]
    halo = profile.getUser()
    return render.index(halo=halo, password = password)

