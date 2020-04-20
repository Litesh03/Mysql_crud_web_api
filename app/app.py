from flask import Flask, render_template, request, g, jsonify, redirect, abort
import json
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'          #host
app.config['MYSQL_USER'] = 'root'               #user
app.config['MYSQL_PASSWORD'] = 'xxxxxxxx'     #password
app.config['MYSQL_DB'] = 'database'            #database_name

mysql = MySQL(app)


@app.before_request
def before_request():
    """
        Connect to database and create table at initialization
        You can create your own table with different primary key
        and field names as per your requirement
    """
    g.db = mysql.connection.cursor()
    g.db.execute('CREATE TABLE IF NOT EXISTS monthly_data \
    	(Sr INT PRIMARY KEY AUTO_INCREMENT, Name TEXT,id TEXT, Item TEXT, Date TEXT, Price REAL)')


@app.route('/api/v1.0/store_data',methods=['POST', 'GET'])
def storeData():
    """
        API to store the data into database
        This API accepts data in JSON format
    """
    if request.method == 'POST':
        incomingData = request.data
        d = json.loads(incomingData)

        try:
            g.db.execute("INSERT INTO monthly_data(name,id,item,date,price) VALUES(%s,%s,%s,%s,%s)"\
                ,(d['name'].capitalize(),d['id'],d['item'],d['date'],d['price']))
            mysql.connection.commit()

        except ValueError:
            print('Failed Pushing Data to Database')
            return False
    return jsonify(d)


@app.route('/api/v1.0/get_data',methods=['POST', 'GET'])
def return_expenses():
    """
       This API gives out all the rows in the table
       It gives JSON output
    """
    g.db.execute("SELECT * FROM monthly_data ORDER BY Sr")
    rows = g.db.fetchall()
    data = []
    for x in rows:
        data.append({'sr':x[0],'name':x[1], 'id':x[2], 'item':x[3], 'price':x[5], 'date':x[4]})
    return jsonify(data)


@app.route('/api/v1.0/delete_row', methods=['POST', 'GET'])
def delete_row():
    """
        API to delete a row in the table
        It accepts 'sr' as primary key and delete the corresponding row
    """
    if request.method == 'POST':
        d = json.loads(request.data)
        data = (d['sr'],)
        g.db.execute("DELETE FROM monthly_data WHERE Sr = %s", data)
        mysql.connection.commit()
        return d
    else:
        pass

@app.route('/api/v1.0/update_row', methods=['POST', 'GET'])
def update_exp():
    """
        This API accepts data along with 'sr' as primary key
        and updates the data at the corresponding location
    """
    if request.method == 'POST':
        d = json.loads(request.data)
        data = (d['name'].capitalize(), d['id'], d['item'], d['date'], d['price'],d['sr'],)
        g.db.execute("UPDATE monthly_data SET Name = %s, id = %s, Item = %s, date = %s, price = %s \
         WHERE Sr = %s", data)
        mysql.connection.commit()
        return d
    else:
        return None


if __name__ == '__main__':
    app.run()