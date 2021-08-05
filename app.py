from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

import psycopg2
import psycopg2.extras



app = Flask(__name__)

conn = psycopg2.connect(dbname='sampledb', user='postgres', password='dba', host='localhost', port='5433')



@app.route("/")
def home():
    passhash = generate_password_hash('aq')
    print(passhash)
    return passhash

@app.route("/user")
def get_usre():
    try:
        id = request.args.get('id')
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if id:            
            cursor.execute("select * from useraccount where id=%s",id)
            row = cursor.fetchone()
            resp = jsonify(row)
            resp.status_code = 200
            return resp
        else:
            resp = jsonify('User "id" not found in query string')
            resp.status_code = 500
            return resp

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run()