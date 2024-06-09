from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Load scan_results.json
    with open('scan_results.json') as f:
        scan_results = json.load(f)
    
    # Load suricata.json
    with open('suricata.json') as f:
        suricata_results = json.load(f)
    
    # Load zap_results_new.json
    with open('zap_scan_results_new.json') as f:
        zap_results = json.load(f)
    
    # Combine all results into a single dictionary
    combined_results = {
        'scan_results': scan_results,
        'suricata_results': suricata_results,
        'zap_results': zap_results
    }
    
    return render_template('dashboard.html', combined_results=combined_results)

if __name__ == '__main__':
    app.run(debug=True)
