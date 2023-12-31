from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': "Benglaru, India",
  'salary': 'Rs, 10,00,000'
}, {
  'id': 2,
  'title': 'Data Analyst',
  'location': "Delhi, India",
  'salary': 'Rs, 15,00,000'
}, {
  'id': 3,
  'title': 'Front End Engineer',
  'location': "Remote",
  'salary': 'Rs, 12,00,000'
}, {
  'id': 4,
  'title': 'Back End Engineer',
  'location': "San Francisco",
  'salary': '$120,000'
}]


@app.route("/")
def hello_jovian():
  return render_template("home.html", jobs=JOBS)


@app.route('/api/jobs')
def get_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
