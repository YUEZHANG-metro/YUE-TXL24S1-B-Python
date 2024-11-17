## exercise1
from flask import Flask, request,jsonify
app = Flask(__name__)

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
