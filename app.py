from flask import Flask, render_template

app = Flask(
    __name__
)  # If you run a Python file directly (e.g., python app.py), Python sets __name__ to "__main__"
# __name__ is passed to the Flask class to indicate the location of the current module
# Flask(__name__) registers it as a WSGI application so it can communicate with web servers

# this is an imitation of the database structure we are going to use
JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Remote',
    'salary': '$50,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Remote',
    'salary': '$100,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Montreal, Canada',
    'salary': '$50,000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$100,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)  # This runs only if the script is executed directly (e.g., python app.py)
