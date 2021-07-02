from flask import Flask, render_template, request, make_response, redirect, url_for
from replit import db



app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

# Index page and Rendering Basic Templates
@app.route('/', methods = ['GET', 'POST'])
def index():
  if request.method == "POST":
    plat = request.form.get('platform')
    passw = request.form.get('password')
    db[plat] = passw
    return db[plat]
  return render_template("index.html")
  


# Redirects
@app.route('/passwords')
def passwords():
  passwords = ""
  keys = db.keys()
  for i in keys:
    passwords = str(i) + " " + str(db[i]) + "\n" + passwords
  return passwords



if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
