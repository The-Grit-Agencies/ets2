from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

def get_ets2_data():
    response = requests.get('http://localhost:25555/api/ets2/telemetry')
    if response.status_code == 200:
        data = response.json()
        return {
            'speed': data['truck']['speed'],
            'truck_type': data['truck']['make'],
            'fuel': data['truck']['fuel'],
            'pressure': data['truck']['oilPressure'],
            'condition': data['truck']['damage'],
            'job_type': data['job']['cargo'],
            'remaining_time': data['navigation']['estimatedTime']
        }
    return {}

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/data')
def data():
    return jsonify(get_ets2_data())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

