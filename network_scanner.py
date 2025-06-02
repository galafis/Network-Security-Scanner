#!/usr/bin/env python3
"""
Network Security Scanner
Comprehensive network security scanning and vulnerability assessment tool.
"""

import socket
import threading
import subprocess
import json
from datetime import datetime
from flask import Flask, render_template_string, jsonify, request
import ipaddress
import re

app = Flask(__name__)

class NetworkScanner:
    """Network security scanning functionality."""
    
    def __init__(self):
        self.common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995, 3389, 5432, 3306]
        self.scan_results = []
    
    def scan_host(self, host, ports=None, timeout=1):
        """Scan a single host for open ports."""
        if ports is None:
            ports = self.common_ports
        
        results = {
            'host': host,
            'timestamp': datetime.now().isoformat(),
            'open_ports': [],
            'closed_ports': [],
            'services': {},
            'vulnerabilities': []
        }
        
        # Resolve hostname
        try:
            ip = socket.gethostbyname(host)
            results['ip'] = ip
        except socket.gaierror:
            results['error'] = 'Host resolution failed'
            return results
        
        # Port scanning
        for port in ports:
            if self._scan_port(ip, port, timeout):
                results['open_ports'].append(port)
                service = self._identify_service(port)
                if service:
                    results['services'][port] = service
                    # Check for common vulnerabilities
                    vulns = self._check_vulnerabilities(port, service)
                    results['vulnerabilities'].extend(vulns)
            else:
                results['closed_ports'].append(port)
        
        # Additional security checks
        results['security_analysis'] = self._analyze_security(results)
        
        return results
    
    def scan_network(self, network, ports=None):
        """Scan an entire network range."""
        try:
            net = ipaddress.ip_network(network, strict=False)
            hosts = list(net.hosts())
            
            # Limit to first 10 hosts for demo
            hosts = hosts[:10]
            
            results = []
            threads = []
            
            def scan_worker(host):
                result = self.scan_host(str(host), ports)
                results.append(result)
            
            # Create threads for parallel scanning
            for host in hosts:
                thread = threading.Thread(target=scan_worker, args=(host,))
                threads.append(thread)
                thread.start()
            
            # Wait for all threads to complete
            for thread in threads:
                thread.join()
            
            return results
            
        except ValueError as e:
            return {'error': f'Invalid network format: {e}'}
    
    def _scan_port(self, host, port, timeout):
        """Scan a single port on a host."""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            sock.close()
            return result == 0
        except:
            return False
    
    def _identify_service(self, port):
        """Identify service running on port."""
        services = {
            21: 'FTP',
            22: 'SSH',
            23: 'Telnet',
            25: 'SMTP',
            53: 'DNS',
            80: 'HTTP',
            110: 'POP3',
            143: 'IMAP',
            443: 'HTTPS',
            993: 'IMAPS',
            995: 'POP3S',
            3389: 'RDP',
            5432: 'PostgreSQL',
            3306: 'MySQL'
        }
        return services.get(port, 'Unknown')
    
    def _check_vulnerabilities(self, port, service):
        """Check for common vulnerabilities based on service."""
        vulnerabilities = []
        
        if port == 21:  # FTP
            vulnerabilities.append({
                'type': 'Insecure Protocol',
                'severity': 'Medium',
                'description': 'FTP transmits data in plaintext'
            })
        
        elif port == 23:  # Telnet
            vulnerabilities.append({
                'type': 'Insecure Protocol',
                'severity': 'High',
                'description': 'Telnet transmits credentials in plaintext'
            })
        
        elif port == 80:  # HTTP
            vulnerabilities.append({
                'type': 'Unencrypted Web Traffic',
                'severity': 'Medium',
                'description': 'HTTP traffic is not encrypted'
            })
        
        elif port == 3389:  # RDP
            vulnerabilities.append({
                'type': 'Remote Access',
                'severity': 'High',
                'description': 'RDP exposed to network - potential brute force target'
            })
        
        return vulnerabilities
    
    def _analyze_security(self, results):
        """Analyze overall security posture."""
        analysis = {
            'risk_level': 'Low',
            'recommendations': [],
            'score': 100
        }
        
        # Check for high-risk services
        high_risk_ports = [21, 23, 3389]
        exposed_high_risk = [p for p in results['open_ports'] if p in high_risk_ports]
        
        if exposed_high_risk:
            analysis['risk_level'] = 'High'
            analysis['score'] -= 30
            analysis['recommendations'].append('Disable or secure high-risk services')
        
        # Check for unencrypted services
        unencrypted_ports = [21, 23, 80]
        exposed_unencrypted = [p for p in results['open_ports'] if p in unencrypted_ports]
        
        if exposed_unencrypted:
            if analysis['risk_level'] != 'High':
                analysis['risk_level'] = 'Medium'
            analysis['score'] -= 20
            analysis['recommendations'].append('Use encrypted alternatives (HTTPS, SFTP, SSH)')
        
        # Check for too many open ports
        if len(results['open_ports']) > 5:
            analysis['score'] -= 10
            analysis['recommendations'].append('Close unnecessary ports')
        
        # Add general recommendations
        if not analysis['recommendations']:
            analysis['recommendations'].append('Regular security audits recommended')
        
        return analysis

scanner = NetworkScanner()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Network Security Scanner</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            min-height: 100vh;
            color: #333;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            text-align: center;
        }
        
        .scanner-form {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #2c3e50;
        }
        
        input, select {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 16px;
        }
        
        .btn {
            background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            margin-right: 10px;
        }
        
        .results {
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            display: none;
        }
        
        .host-result {
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
        }
        
        .host-header {
            display: flex;
            justify-content: between;
            align-items: center;
            margin-bottom: 15px;
        }
        
        .risk-badge {
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.9rem;
        }
        
        .risk-low { background: #d4edda; color: #155724; }
        .risk-medium { background: #fff3cd; color: #856404; }
        .risk-high { background: #f8d7da; color: #721c24; }
        
        .ports-section {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin: 20px 0;
        }
        
        .port-list {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
        }
        
        .port-item {
            display: flex;
            justify-content: between;
            padding: 5px 0;
            border-bottom: 1px solid #e0e0e0;
        }
        
        .vulnerabilities {
            margin-top: 20px;
        }
        
        .vuln-item {
            background: #fff3cd;
            border: 1px solid #ffeaa7;
            border-radius: 8px;
            padding: 15px;
            margin: 10px 0;
        }
        
        .vuln-severity {
            font-weight: 600;
            margin-bottom: 5px;
        }
        
        .recommendations {
            background: #d1ecf1;
            border: 1px solid #bee5eb;
            border-radius: 8px;
            padding: 15px;
            margin-top: 20px;
        }
        
        .loading {
            text-align: center;
            padding: 40px;
            display: none;
        }
        
        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #e74c3c;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 20px;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🛡️ Network Security Scanner</h1>
            <p>Comprehensive network security scanning and vulnerability assessment</p>
        </div>
        
        <div class="scanner-form">
            <form id="scanForm">
                <div class="form-group">
                    <label for="target">Target (IP or hostname):</label>
                    <input type="text" id="target" name="target" placeholder="192.168.1.1 or example.com" required>
                </div>
                
                <div class="form-group">
                    <label for="scanType">Scan Type:</label>
                    <select id="scanType" name="scanType">
                        <option value="host">Single Host</option>
                        <option value="network">Network Range</option>
                    </select>
                </div>
                
                <button type="submit" class="btn">🔍 Start Scan</button>
                <button type="button" class="btn" onclick="loadSampleData()">📊 Load Sample Data</button>
            </form>
        </div>
        
        <div class="loading" id="loading">
            <div class="spinner"></div>
            <p>Scanning network... This may take a few moments.</p>
        </div>
        
        <div class="results" id="results">
            <!-- Results will be populated here -->
        </div>
    </div>

    <script>
        document.getElementById('scanForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const target = document.getElementById('target').value;
            const scanType = document.getElementById('scanType').value;
            
            const loading = document.getElementById('loading');
            const results = document.getElementById('results');
            
            loading.style.display = 'block';
            results.style.display = 'none';
            
            try {
                const response = await fetch('/scan', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ target: target, scan_type: scanType })
                });
                
                const data = await response.json();
                displayResults(data);
                
            } catch (error) {
                alert('Error: ' + error.message);
            } finally {
                loading.style.display = 'none';
            }
        });
        
        function displayResults(data) {
            const results = document.getElementById('results');
            
            if (data.error) {
                results.innerHTML = `<div class="vuln-item"><strong>Error:</strong> ${data.error}</div>`;
                results.style.display = 'block';
                return;
            }
            
            // Handle both single host and network results
            const hosts = Array.isArray(data) ? data : [data];
            
            let html = '<h3>🔍 Scan Results</h3>';
            
            hosts.forEach(host => {
                if (host.error) {
                    html += `<div class="host-result">
                        <div class="host-header">
                            <h4>${host.host}</h4>
                            <span class="risk-badge risk-high">Error</span>
                        </div>
                        <p>Error: ${host.error}</p>
                    </div>`;
                    return;
                }
                
                const riskClass = `risk-${host.security_analysis.risk_level.toLowerCase()}`;
                
                html += `
                    <div class="host-result">
                        <div class="host-header">
                            <h4>${host.host} (${host.ip || 'N/A'})</h4>
                            <span class="risk-badge ${riskClass}">${host.security_analysis.risk_level} Risk</span>
                        </div>
                        
                        <div class="ports-section">
                            <div class="port-list">
                                <h5>🟢 Open Ports (${host.open_ports.length})</h5>
                                ${host.open_ports.map(port => `
                                    <div class="port-item">
                                        <span>Port ${port}</span>
                                        <span>${host.services[port] || 'Unknown'}</span>
                                    </div>
                                `).join('')}
                            </div>
                            
                            <div class="port-list">
                                <h5>🔴 Closed Ports (${host.closed_ports.length})</h5>
                                ${host.closed_ports.slice(0, 5).map(port => `
                                    <div class="port-item">
                                        <span>Port ${port}</span>
                                        <span>Closed</span>
                                    </div>
                                `).join('')}
                                ${host.closed_ports.length > 5 ? `<p>... and ${host.closed_ports.length - 5} more</p>` : ''}
                            </div>
                        </div>
                        
                        ${host.vulnerabilities.length > 0 ? `
                            <div class="vulnerabilities">
                                <h5>⚠️ Vulnerabilities Found</h5>
                                ${host.vulnerabilities.map(vuln => `
                                    <div class="vuln-item">
                                        <div class="vuln-severity">${vuln.severity} - ${vuln.type}</div>
                                        <div>${vuln.description}</div>
                                    </div>
                                `).join('')}
                            </div>
                        ` : '<div style="color: #27ae60; font-weight: 600;">✅ No vulnerabilities detected</div>'}
                        
                        <div class="recommendations">
                            <h5>💡 Security Recommendations</h5>
                            <ul>
                                ${host.security_analysis.recommendations.map(rec => `<li>${rec}</li>`).join('')}
                            </ul>
                            <p><strong>Security Score:</strong> ${host.security_analysis.score}/100</p>
                        </div>
                    </div>
                `;
            });
            
            results.innerHTML = html;
            results.style.display = 'block';
        }
        
        function loadSampleData() {
            const sampleData = {
                host: 'example.com',
                ip: '93.184.216.34',
                timestamp: new Date().toISOString(),
                open_ports: [80, 443],
                closed_ports: [21, 22, 23, 25, 53],
                services: {80: 'HTTP', 443: 'HTTPS'},
                vulnerabilities: [{
                    type: 'Unencrypted Web Traffic',
                    severity: 'Medium',
                    description: 'HTTP traffic is not encrypted'
                }],
                security_analysis: {
                    risk_level: 'Medium',
                    recommendations: ['Use HTTPS for all web traffic', 'Regular security audits recommended'],
                    score: 80
                }
            };
            
            displayResults(sampleData);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """Main scanner page."""
    return render_template_string(HTML_TEMPLATE)

@app.route('/scan', methods=['POST'])
def scan_target():
    """Perform network scan."""
    data = request.get_json()
    target = data.get('target')
    scan_type = data.get('scan_type', 'host')
    
    if not target:
        return jsonify({'error': 'Target is required'}), 400
    
    try:
        if scan_type == 'network':
            results = scanner.scan_network(target)
        else:
            results = scanner.scan_host(target)
        
        return jsonify(results)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def main():
    """Main execution function."""
    print("Network Security Scanner")
    print("=" * 30)
    
    print("Starting web server...")
    print("Open http://localhost:5000 in your browser")
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()

