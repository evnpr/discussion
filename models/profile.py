from database import database
db = database()

"""
definition:
  id (int, primary_key, auto_int)
  user (varchar(30))
  password md5(varchar(30))
"""

def getUser():
  result = db.query("SELECT * FROM profile")
  name = result[0].user
  return name
