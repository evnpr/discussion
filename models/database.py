import web

def database():
  db = web.database(dbn='mysql', db='discussion', user='root', pw='abc123')
  return db
