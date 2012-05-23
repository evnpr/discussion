import web

def database():
  db = web.database(dbn='mysql', db='discussion', user='root', pw='')
  return db
