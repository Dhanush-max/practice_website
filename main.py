from flask import Flask , render_template , jsonify

app = Flask(__name__)

food = [
  {
    'id':1,
    'name':'eth',
    'price':'$4000'
  },
  {
    'id':2,
    'name':'polygon',
    'price':'$20'
  },
  {
    'id':3,
    'name':'shiba',
    'price':'$0.0123'
  },
  {
    'id':4,
    'name':'bitcoin',
    'price':'$21,200'
  }
]

@app.route("/")
def hello_World():
  return render_template('home.html',foods=food)

@app.route("/food")
def food_list():
  return jsonify(food)
if __name__ == "__main__":
  app.run(host='0.0.0.0' , debug=True)