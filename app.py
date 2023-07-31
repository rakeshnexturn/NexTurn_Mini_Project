import time
from flask import Flask, render_template
from prometheus_client import start_http_server, Counter

app = Flask(__name__)

# Create a counter metric to track the number of log events
log_events_counter = Counter('python_app_log_events', 'Number of log events processed')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/click_here', methods=['GET'])
def click_here():
    generate_log()
    # Increment the log events counter for each log event processed
    log_events_counter.inc()
    return 'Button clicked!'

def generate_log():
    with open('log.txt', 'a') as log_file:
        log_file.write(f'Button clicked at: {time.strftime("%Y-%m-%d %H:%M:%S")}\n')

if __name__ == '__main__':
    # Start the Prometheus HTTP server on port 8080
    start_http_server(8080)

    # Start the Flask application on host '0.0.0.0' and port 5000
    app.run(host='0.0.0.0', port=5000)
