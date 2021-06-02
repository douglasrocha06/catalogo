import pymysql.cursors
import pymysql
from app import app
from flaskext.mysql import MySQL

mysql2 = MySQL()
app2.config['MYSQL_DATABASE_USER'] = 'admin'
app2.config['MYSQL_DATABASE_PASSWORD'] = '12345678'
app2.config['MYSQL_DATABASE_DB'] = 'api_produtos'
app2.config['MYSQL_DATABASE_HOST'] = 'djlbanco.cxycaymkd24m.us-east-1.rds.amazonaws.com'
mysql2.init_app(app2)
