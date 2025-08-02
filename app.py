
from flask import Flask, render_template, request, redirect, url_for
from static.data.clustering import predict_investor_cluster, predict_owner_cluster
import json

app = Flask(__name__)

# Fake data store
with open('static/data/properties.json', encoding='utf-8') as f:
    properties_data = json.load(f)

with open('static/data/investors.json', encoding='utf-8') as f:
    investors_data = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/investor', methods=['GET', 'POST'])
def investor():
    if request.method == 'POST':
        form = request.form
        data = {
            'investor_city': form['city'],
            'interest_type': form['type'],
            'experience': form['experience'],
            'risk': form['risk'],
            'duration': form['duration'],
            'goal': form['goal'],
            'budget': int(form['budget'])
                }

        cluster = predict_investor_cluster(data)
        matches = [p for p in properties_data if p['cluster'] == cluster]
        return render_template('investor_dashboard.html', properties=matches)
    return render_template('investor_form.html')

@app.route('/owner', methods=['GET', 'POST'])
def owner():
    if request.method == 'POST':
        form = request.form
        data = {
            'location': form['location'],
            'type': form['type'],
            'price': int(form['price'])
        }
        cluster = predict_owner_cluster(data)
        matches = [inv for inv in investors_data if inv['cluster'] == cluster]
        
        owners = [data] 

        return render_template('owner_dashboard.html', investors=matches,owners=owners)
    return render_template('owner_form.html')

if __name__ == '__main__':
    app.run(debug=True)
