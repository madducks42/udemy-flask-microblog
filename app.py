from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def first_page_html():
  return render_template("jinja_intro.html", name="Jane Doe", template_name="Flask")
