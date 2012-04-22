from database import database
db = database()

"""
definition:
  user (varchar(30))
  password md5(varchar(30))
"""

def getUser():
  result = db.query("SELECT * FROM profile")
  name = result[0].user
  return name
