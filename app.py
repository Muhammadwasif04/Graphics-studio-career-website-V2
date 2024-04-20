from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Karachi, Pakistan'    
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Lahore, Pakistan'    
    },
    {
        'id': 3,
        'title': 'Data Engineer',
        'location': 'Hyderabad, Pakistan'    
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', job=jobs)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(jobs)