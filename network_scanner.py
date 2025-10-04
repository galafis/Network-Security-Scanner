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
import ipaddress
import re

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

