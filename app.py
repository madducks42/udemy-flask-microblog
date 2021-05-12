from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def first_page_html():
  return render_template("jinja_intro.html", name="Jane Doe", template_name="Flask")

@app.route("/expressions/")
def expressions():

  #interpolation
  color = "brown"
  animal_one = "fox"
  animal_two = "dog"

  #addition and subtraction
  orange_amount = 10
  apple_amount = 20
  donate_amount = 15

  #string concatenation
  first_name = "Captain"
  last_name = "Marvel"

  kwargs = {
    "color": color, 
    "animal_one": animal_one, "animal_two": animal_two, "orange_amount": orange_amount, "apple_amount": apple_amount, "donate_amount": donate_amount, 
    "first_name": first_name, "last_name": last_name
  }

  return render_template("expressions.html", **kwargs )