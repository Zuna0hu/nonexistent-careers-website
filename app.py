from flask import Flask, render_template

app = Flask(
    __name__
)  # If you run a Python file directly (e.g., python app.py), Python sets __name__ to "__main__"
# __name__ is passed to the Flask class to indicate the location of the current module
# Flask(__name__) registers it as a WSGI application so it can communicate with web servers


@app.route("/")
def hello_world():
  return render_template('home.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)  # This runs only if the script is executed directly (e.g., python app.py)
