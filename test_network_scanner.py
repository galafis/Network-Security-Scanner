import unittest
from unittest.mock import patch, MagicMock
import socket
from network_scanner import NetworkScanner

class TestNetworkScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = NetworkScanner()

    @patch("socket.socket")
    def test_scan_port_open(self, mock_socket):
        mock_sock_instance = MagicMock()
        mock_socket.return_value = mock_sock_instance
        mock_sock_instance.connect_ex.return_value = 0  # Port is open

        result = self.scanner._scan_port("127.0.0.1", 80, 1)
        self.assertTrue(result)
        mock_sock_instance.connect_ex.assert_called_with(("127.0.0.1", 80))
        mock_sock_instance.close.assert_called_once()

    @patch("socket.socket")
    def test_scan_port_closed(self, mock_socket):
        mock_sock_instance = MagicMock()
        mock_socket.return_value = mock_sock_instance
        mock_sock_instance.connect_ex.return_value = 1  # Port is closed

        result = self.scanner._scan_port("127.0.0.1", 80, 1)
        self.assertFalse(result)
        mock_sock_instance.connect_ex.assert_called_with(("127.0.0.1", 80))
        mock_sock_instance.close.assert_called_once()

    def test_identify_service(self):
        self.assertEqual(self.scanner._identify_service(80), "HTTP")
        self.assertEqual(self.scanner._identify_service(22), "SSH")
        self.assertEqual(self.scanner._identify_service(9999), "Unknown")

    def test_check_vulnerabilities(self):
        self.assertGreater(len(self.scanner._check_vulnerabilities(21, "FTP")), 0)
        self.assertGreater(len(self.scanner._check_vulnerabilities(23, "Telnet")), 0)
        self.assertEqual(len(self.scanner._check_vulnerabilities(80, "HTTP")), 1)
        self.assertEqual(len(self.scanner._check_vulnerabilities(22, "SSH")), 0)

    @patch("network_scanner.NetworkScanner._scan_port", return_value=True)
    @patch("socket.gethostbyname", return_value="127.0.0.1")
    def test_scan_host_open_ports(self, mock_gethostbyname, mock_scan_port):
        results = self.scanner.scan_host("localhost", ports=[80, 443])
        self.assertIn(80, results["open_ports"])
        self.assertIn(443, results["open_ports"])
        self.assertIn("HTTP", results["services"].values())
        self.assertIn("HTTPS", results["services"].values())

    @patch("network_scanner.NetworkScanner._scan_port", return_value=False)
    @patch("socket.gethostbyname", return_value="127.0.0.1")
    def test_scan_host_closed_ports(self, mock_gethostbyname, mock_scan_port):
        results = self.scanner.scan_host("localhost", ports=[80, 443])
        self.assertIn(80, results["closed_ports"])
        self.assertIn(443, results["closed_ports"])
        self.assertEqual(results["services"], {})

    @patch("network_scanner.NetworkScanner._scan_port", side_effect=[True, False])
    @patch("socket.gethostbyname", return_value="127.0.0.1")
    def test_scan_host_mixed_ports(self, mock_gethostbyname, mock_scan_port):
        results = self.scanner.scan_host("localhost", ports=[80, 22])
        self.assertIn(80, results["open_ports"])
        self.assertIn(22, results["closed_ports"])
        self.assertEqual(results["services"][80], "HTTP")

    @patch("socket.gethostbyname", side_effect=socket.gaierror)
    def test_scan_host_resolution_failure(self, mock_gethostbyname):
        results = self.scanner.scan_host("nonexistent.domain")
        self.assertIn("error", results)
        self.assertEqual(results["error"], "Host resolution failed")

    @patch("network_scanner.NetworkScanner.scan_host")
    @patch("ipaddress.ip_network")
    def test_scan_network(self, mock_ip_network, mock_scan_host):
        mock_ip_network.return_value.hosts.return_value = ["192.168.1.1", "192.168.1.2"]
        mock_scan_host.side_effect = [
            {"host": "192.168.1.1", "open_ports": [80]},
            {"host": "192.168.1.2", "open_ports": [22]}
        ]

        results = self.scanner.scan_network("192.168.1.0/24")
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["host"], "192.168.1.1")
        self.assertEqual(results[1]["host"], "192.168.1.2")
        mock_scan_host.assert_any_call("192.168.1.1", None)
        mock_scan_host.assert_any_call("192.168.1.2", None)

    def test_analyze_security_high_risk(self):
        results = {
            "open_ports": [21, 80],
            "services": {21: "FTP", 80: "HTTP"},
            "vulnerabilities": []
        }
        analysis = self.scanner._analyze_security(results)
        self.assertEqual(analysis["risk_level"], "High")
        self.assertIn("Disable or secure high-risk services", analysis["recommendations"])

    def test_analyze_security_medium_risk(self):
        results = {
            "open_ports": [80, 443],
            "services": {80: "HTTP", 443: "HTTPS"},
            "vulnerabilities": []
        }
        analysis = self.scanner._analyze_security(results)
        self.assertEqual(analysis["risk_level"], "Medium")
        self.assertIn("Use encrypted alternatives (HTTPS, SFTP, SSH)", analysis["recommendations"])

    def test_analyze_security_low_risk(self):
        results = {
            "open_ports": [443],
            "services": {443: "HTTPS"},
            "vulnerabilities": []
        }
        analysis = self.scanner._analyze_security(results)
        self.assertEqual(analysis["risk_level"], "Low")
        self.assertIn("Regular security audits recommended", analysis["recommendations"])

if __name__ == '__main__':
    unittest.main()

