from flask import Flask, jsonify


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def hello_world():
    return 'Flask Dockerized'


@app.route('/api')
def index():
  return jsonify({
    "message": 'Flask Dockerized'
  })


if __name__ == '__main__':
  app.run(host='0.0.0.0')
