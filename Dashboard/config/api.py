
import os

#urlaplocal = "http://127.0.0.1:8000"
url_heroku = "https://newappeurocopa.herokuapp.com"
urlheroku =  os.getenv("HEROKU_URL") or url_heroku