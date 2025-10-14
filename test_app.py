"""
Integration tests for Network Security Scanner Flask application.

Tests API endpoints, validation, error handling, and integration with the scanner.
"""

import unittest
import json
from unittest.mock import patch, MagicMock
from app import app

class TestFlaskApp(unittest.TestCase):
    """Test cases for Flask application endpoints."""
    
    def setUp(self):
        """Set up test client."""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
    
    def test_index_route(self):
        """Test the main index route."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Network Security Scanner', response.data)
    
    def test_health_endpoint(self):
        """Test health check endpoint."""
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')
        self.assertIn('service', data)
    
    def test_scan_endpoint_no_data(self):
        """Test scan endpoint with no data."""
        response = self.client.post('/scan')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)
    
    def test_scan_endpoint_no_target(self):
        """Test scan endpoint without target."""
        response = self.client.post(
            '/scan',
            data=json.dumps({'scan_type': 'host'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)
        self.assertIn('required', data['error'].lower())
    
    def test_scan_endpoint_invalid_ip(self):
        """Test scan endpoint with invalid IP address."""
        response = self.client.post(
            '/scan',
            data=json.dumps({'target': '999.999.999.999', 'scan_type': 'host'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)
    
    def test_scan_endpoint_invalid_network(self):
        """Test scan endpoint with invalid network CIDR."""
        response = self.client.post(
            '/scan',
            data=json.dumps({'target': '192.168.1.0/99', 'scan_type': 'network'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)
    
    def test_scan_endpoint_invalid_scan_type(self):
        """Test scan endpoint with invalid scan type."""
        response = self.client.post(
            '/scan',
            data=json.dumps({'target': '127.0.0.1', 'scan_type': 'invalid'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)
    
    @patch('app.scanner.scan_host')
    def test_scan_endpoint_host_success(self, mock_scan):
        """Test successful host scan."""
        mock_scan.return_value = {
            'host': '127.0.0.1',
            'open_ports': [80, 443],
            'closed_ports': [],
            'services': {80: 'HTTP', 443: 'HTTPS'},
            'vulnerabilities': [],
            'security_analysis': {
                'risk_level': 'Low',
                'score': 100,
                'recommendations': []
            }
        }
        
        response = self.client.post(
            '/scan',
            data=json.dumps({'target': '127.0.0.1', 'scan_type': 'host'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('open_ports', data)
        self.assertEqual(len(data['open_ports']), 2)
    
    @patch('app.scanner.scan_network')
    def test_scan_endpoint_network_success(self, mock_scan):
        """Test successful network scan."""
        mock_scan.return_value = [
            {
                'host': '192.168.1.1',
                'open_ports': [80],
                'closed_ports': [],
                'services': {80: 'HTTP'},
                'vulnerabilities': [],
                'security_analysis': {'risk_level': 'Low', 'score': 90}
            }
        ]
        
        response = self.client.post(
            '/scan',
            data=json.dumps({'target': '192.168.1.0/30', 'scan_type': 'network'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
    
    def test_404_error_handler(self):
        """Test 404 error handler."""
        response = self.client.get('/nonexistent')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertIn('error', data)
    
    def test_validate_hostname_localhost(self):
        """Test localhost validation."""
        from app import validate_hostname
        self.assertTrue(validate_hostname('localhost'))
    
    def test_validate_hostname_valid(self):
        """Test valid hostname."""
        from app import validate_hostname
        self.assertTrue(validate_hostname('example.com'))
        self.assertTrue(validate_hostname('sub.example.com'))
    
    def test_validate_ip_valid(self):
        """Test valid IP address."""
        from app import validate_ip_address
        self.assertTrue(validate_ip_address('192.168.1.1'))
        self.assertTrue(validate_ip_address('127.0.0.1'))
        self.assertTrue(validate_ip_address('10.0.0.1'))
    
    def test_validate_ip_invalid(self):
        """Test invalid IP address."""
        from app import validate_ip_address
        self.assertFalse(validate_ip_address('256.1.1.1'))
        self.assertFalse(validate_ip_address('192.168.1'))
        self.assertFalse(validate_ip_address('invalid'))
    
    def test_validate_network_valid(self):
        """Test valid network CIDR."""
        from app import validate_network
        self.assertTrue(validate_network('192.168.1.0/24'))
        self.assertTrue(validate_network('10.0.0.0/8'))
    
    def test_validate_network_invalid(self):
        """Test invalid network CIDR."""
        from app import validate_network
        self.assertFalse(validate_network('192.168.1.0/33'))
        self.assertFalse(validate_network('256.1.1.0/24'))
        self.assertFalse(validate_network('192.168.1.0'))

if __name__ == '__main__':
    unittest.main()
