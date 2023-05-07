from flask import Flask , render_template , jsonify

app = Flask(__name__)

food = [
  {
    'id':1,
    'name':'Dosa',
    'Rating':'9/10'
  },
  {
    'id':2,
    'name':'idly',
    'Rating':'6/10'
  },
  {
    'id':3,
    'name':'Rice',
    'Rating':'7/10'
  },
  {
    'id':4,
    'name':'Biriyani',
    'Rating':'9.5/10'
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