from flask import Flask, render_template, jsonify
import json
app = Flask(__name__)
@app.route('/')
def index():
    with open('scan_results.json') as f:
        scan_results = json.load(f)
    return render_template('dashboard.html', scan_results=scan_results)

# @app.route('/api/scan_results')
# def api_scan_results():
#     with open('scan_results.json') as f:
#         scan_results = json.load(f)
#     return jsonify(scan_results)

if __name__ == '__main__':
    app.run(debug=True)
