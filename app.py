import os
import logging
import re
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from network_scanner import NetworkScanner
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.config.from_object("config.Config")

# Configure CORS
CORS(app, resources={r"/*": {"origins": os.getenv("CORS_ORIGINS", "*")}})

# Initialize scanner
scanner = NetworkScanner()

def validate_ip_address(ip):
    """Validate IPv4 address format."""
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.match(pattern, ip):
        return False
    parts = ip.split('.')
    return all(0 <= int(part) <= 255 for part in parts)

def validate_network(network):
    """Validate network CIDR notation."""
    pattern = r'^(\d{1,3}\.){3}\d{1,3}/\d{1,2}$'
    if not re.match(pattern, network):
        return False
    ip, cidr = network.split('/')
    if not validate_ip_address(ip):
        return False
    return 0 <= int(cidr) <= 32

def validate_hostname(hostname):
    """Validate hostname format."""
    pattern = r'^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
    return bool(re.match(pattern, hostname)) or hostname == "localhost"

@app.route("/")
def index():
    """Main scanner page."""
    logger.info("Main page accessed")
    return render_template("index.html")

@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "service": "Network Security Scanner"}), 200

@app.route("/scan", methods=["POST"])
def scan_target():
    """Perform network scan with input validation."""
    try:
        # Get and validate JSON data
        data = request.get_json(silent=True)
        if not data:
            logger.warning("Scan request received with no data")
            return jsonify({"error": "Request body must be JSON"}), 400
        
        target = data.get("target")
        scan_type = data.get("scan_type", "host")
        
        # Validate target
        if not target:
            logger.warning("Scan request received without target")
            return jsonify({"error": "Target is required"}), 400
        
        # Validate target format based on scan type
        if scan_type == "network":
            if not validate_network(target):
                logger.warning(f"Invalid network format: {target}")
                return jsonify({"error": "Invalid network format. Use CIDR notation (e.g., 192.168.1.0/24)"}), 400
        else:
            if not (validate_ip_address(target) or validate_hostname(target)):
                logger.warning(f"Invalid target format: {target}")
                return jsonify({"error": "Invalid target format. Use IP address or hostname"}), 400
        
        # Validate scan type
        if scan_type not in ["host", "network"]:
            logger.warning(f"Invalid scan type: {scan_type}")
            return jsonify({"error": "Invalid scan_type. Use 'host' or 'network'"}), 400
        
        # Log scan request
        logger.info(f"Starting {scan_type} scan for target: {target}")
        
        # Perform scan
        if scan_type == "network":
            results = scanner.scan_network(target)
        else:
            results = scanner.scan_host(target)
        
        logger.info(f"Scan completed for target: {target}")
        return jsonify(results)
        
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        # Don't expose internal error details to users
        return jsonify({"error": "Invalid input parameters"}), 400
    except Exception as e:
        logger.error(f"Scan error: {str(e)}", exc_info=True)
        # Don't expose internal error details to users
        return jsonify({"error": "An error occurred during scanning. Please check your input and try again."}), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "False") == "True"
    logger.info(f"Starting Network Security Scanner on port {port}")
    app.run(debug=debug, host="0.0.0.0", port=port)

