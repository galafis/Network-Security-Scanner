#!/usr/bin/env python3
"""
Network Security Scanner
Comprehensive network security scanning and vulnerability assessment tool.

This module provides comprehensive network security scanning capabilities including:
- Port scanning (TCP)
- Service identification
- Vulnerability assessment
- Security posture analysis
- Network range scanning

Author: Gabriel Demetrios Lafis
License: MIT
"""

import socket
import threading
import json
import logging
from datetime import datetime
import ipaddress

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NetworkScanner:
    """Network security scanning functionality.
    
    This class provides methods to scan individual hosts or entire network ranges
    for open ports, identify services, detect vulnerabilities, and analyze
    security posture.
    
    Attributes:
        common_ports (list): List of commonly scanned ports
        scan_results (list): Historical scan results
    """
    
    def __init__(self):
        """Initialize the network scanner with default settings."""
        self.common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995, 3389, 5432, 3306]
        self.scan_results = []
        logger.info("NetworkScanner initialized")
    
    def scan_host(self, host, ports=None, timeout=1):
        """Scan a single host for open ports.
        
        Args:
            host (str): Hostname or IP address to scan
            ports (list, optional): List of ports to scan. Defaults to common_ports.
            timeout (int, optional): Socket timeout in seconds. Defaults to 1.
        
        Returns:
            dict: Scan results containing:
                - host: Target hostname
                - ip: Resolved IP address
                - timestamp: Scan timestamp
                - open_ports: List of open ports
                - closed_ports: List of closed ports
                - services: Dictionary mapping ports to services
                - vulnerabilities: List of detected vulnerabilities
                - security_analysis: Security posture analysis
        
        Example:
            >>> scanner = NetworkScanner()
            >>> results = scanner.scan_host("example.com", ports=[80, 443])
            >>> print(results['open_ports'])
            [80, 443]
        """
        if ports is None:
            ports = self.common_ports
        
        logger.info(f"Starting host scan for {host}")
        
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
            logger.debug(f"Resolved {host} to {ip}")
        except socket.gaierror as e:
            logger.error(f"Failed to resolve host {host}: {e}")
            results['error'] = 'Host resolution failed'
            return results
        
        # Port scanning
        for port in ports:
            try:
                if self._scan_port(ip, port, timeout):
                    results['open_ports'].append(port)
                    service = self._identify_service(port)
                    if service:
                        results['services'][port] = service
                        # Check for common vulnerabilities
                        vulns = self._check_vulnerabilities(port, service)
                        results['vulnerabilities'].extend(vulns)
                    logger.debug(f"Port {port} is open on {host}")
                else:
                    results['closed_ports'].append(port)
            except Exception as e:
                logger.error(f"Error scanning port {port} on {host}: {e}")
                results['closed_ports'].append(port)
        
        # Additional security checks
        results['security_analysis'] = self._analyze_security(results)
        
        logger.info(f"Completed host scan for {host}: {len(results['open_ports'])} open ports found")
        return results
    
    def scan_network(self, network, ports=None):
        """Scan an entire network range.
        
        Args:
            network (str): Network in CIDR notation (e.g., '192.168.1.0/24')
            ports (list, optional): List of ports to scan. Defaults to common_ports.
        
        Returns:
            list or dict: List of scan results for each host, or error dict
        
        Example:
            >>> scanner = NetworkScanner()
            >>> results = scanner.scan_network("192.168.1.0/24")
            >>> print(f"Scanned {len(results)} hosts")
        """
        try:
            logger.info(f"Starting network scan for {network}")
            net = ipaddress.ip_network(network, strict=False)
            hosts = list(net.hosts())
            
            if len(hosts) > 254:
                logger.warning(f"Large network scan requested: {len(hosts)} hosts")
            
            results = []
            threads = []
            
            def scan_worker(host):
                """Worker function for threaded scanning."""
                try:
                    result = self.scan_host(str(host), ports)
                    results.append(result)
                except Exception as e:
                    logger.error(f"Error scanning host {host}: {e}")
            
            # Create threads for parallel scanning
            for host in hosts:
                thread = threading.Thread(target=scan_worker, args=(host,))
                threads.append(thread)
                thread.start()
            
            # Wait for all threads to complete
            for thread in threads:
                thread.join()
            
            logger.info(f"Completed network scan for {network}: {len(results)} hosts scanned")
            return results
            
        except ValueError as e:
            logger.error(f"Invalid network format {network}: {e}")
            return {'error': 'Invalid network format'}
        except Exception as e:
            logger.error(f"Network scan error: {e}")
            return {'error': 'Network scan failed'}
    
    def _scan_port(self, host, port, timeout):
        """Scan a single port on a host.
        
        Args:
            host (str): IP address to scan
            port (int): Port number to scan
            timeout (int): Socket timeout in seconds
        
        Returns:
            bool: True if port is open, False otherwise
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            sock.close()
            return result == 0
        except Exception as e:
            logger.debug(f"Port scan exception for {host}:{port}: {e}")
            return False
    
    def _identify_service(self, port):
        """Identify service running on port.
        
        Args:
            port (int): Port number
        
        Returns:
            str: Service name or 'Unknown'
        """
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
            3306: 'MySQL',
            8080: 'HTTP-Proxy',
            8443: 'HTTPS-Alt'
        }
        return services.get(port, 'Unknown')
    
    def _check_vulnerabilities(self, port, service):
        """Check for common vulnerabilities based on service.
        
        Args:
            port (int): Port number
            service (str): Service name
        
        Returns:
            list: List of vulnerability dictionaries
        """
        vulnerabilities = []
        
        if port == 21:  # FTP
            vulnerabilities.append({
                'type': 'Insecure Protocol',
                'severity': 'Medium',
                'description': 'FTP transmits data in plaintext',
                'recommendation': 'Use SFTP or FTPS instead'
            })
        
        elif port == 23:  # Telnet
            vulnerabilities.append({
                'type': 'Insecure Protocol',
                'severity': 'High',
                'description': 'Telnet transmits credentials in plaintext',
                'recommendation': 'Use SSH instead of Telnet'
            })
        
        elif port == 80:  # HTTP
            vulnerabilities.append({
                'type': 'Unencrypted Web Traffic',
                'severity': 'Medium',
                'description': 'HTTP traffic is not encrypted',
                'recommendation': 'Use HTTPS with valid SSL/TLS certificate'
            })
        
        elif port == 3389:  # RDP
            vulnerabilities.append({
                'type': 'Remote Access',
                'severity': 'High',
                'description': 'RDP exposed to network - potential brute force target',
                'recommendation': 'Use VPN or restrict RDP access to specific IPs'
            })
        
        return vulnerabilities
    
    def _analyze_security(self, results):
        """Analyze overall security posture.
        
        Args:
            results (dict): Scan results dictionary
        
        Returns:
            dict: Security analysis containing risk level, score, and recommendations
        """
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

