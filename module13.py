## exercise1
from flask import Flask, request,jsonify
from flask_cors import CORS
import mysql.connector
app = Flask(__name__)
CORS(app)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2,number):
        if number % i == 0:
          return False
    return True

@app.route('/prime_number/<int:number>')
def prime_or_not(number):
    prime = is_prime(number)
    response = {
        "Number": number,
        "IsPrime": prime
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

app = Flask(__name__)
CORS(app)
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='spy',
        password='spy',
        database='spy'
    )
    return connection
@app.route('/get_ICAO/<icao>',methods= ['GET'])
def get_icao_from_database(icao):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f" SELECT ident AS ICAO, name AS Name, municipality AS Location FROM airport WHERE ident = %s",
            (icao,))
    airport_data = cursor.fetchone()
    cursor.close()
    connection.close()

    if airport_data:
        return jsonify(airport_data)
    else:
        return jsonify({"error": "Country not found"}), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)