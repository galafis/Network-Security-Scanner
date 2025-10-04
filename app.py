import os
from flask import Flask, render_template, jsonify, request
from network_scanner import NetworkScanner
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_object("config.Config")

scanner = NetworkScanner()

@app.route("/")
def index():
    """Main scanner page."""
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan_target():
    """Perform network scan."""
    data = request.get_json()
    target = data.get("target")
    scan_type = data.get("scan_type", "host")
    
    if not target:
        return jsonify({"error": "Target is required"}), 400
    
    try:
        if scan_type == "network":
            results = scanner.scan_network(target)
        else:
            results = scanner.scan_host(target)
        
        return jsonify(results)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

