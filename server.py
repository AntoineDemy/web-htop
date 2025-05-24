from flask import Flask, jsonify, send_from_directory
import psutil

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/system')
def system_info():
    cpu = psutil.cpu_percent(percpu=True)
    memory = psutil.virtual_memory()._asdict()
    return jsonify({
        'cpu_percent': cpu,
        'memory': memory
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
