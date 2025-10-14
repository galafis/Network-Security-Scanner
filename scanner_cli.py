#!/usr/bin/env python3
"""
Command-Line Interface for Network Security Scanner

Provides a CLI interface for scanning networks and hosts without the web UI.
"""

import argparse
import json
import sys
from network_scanner import NetworkScanner


def print_banner():
    """Print application banner."""
    banner = """
    ╔═══════════════════════════════════════════════════════════╗
    ║        Network Security Scanner - CLI Interface          ║
    ║              Comprehensive Security Assessment            ║
    ╚═══════════════════════════════════════════════════════════╝
    """
    print(banner)


def print_results(results):
    """Print scan results in a formatted way.
    
    Args:
        results: Scan results (dict for single host, list for network)
    """
    if isinstance(results, dict):
        # Handle error case
        if 'error' in results:
            print(f"\n❌ Error: {results['error']}\n")
            return
        
        # Single host result
        print_host_result(results)
    elif isinstance(results, list):
        # Network scan results
        print(f"\n📊 Network Scan Complete - {len(results)} hosts scanned\n")
        print("=" * 80)
        for result in results:
            print_host_result(result)
            print("-" * 80)


def print_host_result(result):
    """Print a single host scan result.
    
    Args:
        result (dict): Host scan result
    """
    if 'error' in result:
        print(f"\n❌ Host: {result['host']} - Error: {result['error']}")
        return
    
    # Host header
    print(f"\n🎯 Host: {result['host']} ({result.get('ip', 'N/A')})")
    print(f"⏰ Timestamp: {result['timestamp']}")
    
    # Open ports
    print(f"\n🟢 Open Ports ({len(result['open_ports'])}):")
    if result['open_ports']:
        for port in result['open_ports']:
            service = result['services'].get(port, 'Unknown')
            print(f"   • Port {port}: {service}")
    else:
        print("   None detected")
    
    # Vulnerabilities
    print(f"\n⚠️  Vulnerabilities ({len(result['vulnerabilities'])}):")
    if result['vulnerabilities']:
        for vuln in result['vulnerabilities']:
            print(f"   • [{vuln['severity']}] {vuln['type']}")
            print(f"     {vuln['description']}")
            if 'recommendation' in vuln:
                print(f"     💡 {vuln['recommendation']}")
    else:
        print("   ✅ No vulnerabilities detected")
    
    # Security analysis
    analysis = result.get('security_analysis', {})
    risk_level = analysis.get('risk_level', 'Unknown')
    score = analysis.get('score', 0)
    
    # Risk level with color
    risk_emoji = {
        'Low': '✅',
        'Medium': '⚠️',
        'High': '🔴'
    }
    
    print(f"\n📊 Security Analysis:")
    print(f"   {risk_emoji.get(risk_level, '❓')} Risk Level: {risk_level}")
    print(f"   📈 Security Score: {score}/100")
    
    # Recommendations
    if analysis.get('recommendations'):
        print(f"\n💡 Recommendations:")
        for rec in analysis['recommendations']:
            print(f"   • {rec}")
    
    print()


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Network Security Scanner - Command Line Interface',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s -t 192.168.1.1                    # Scan single host
  %(prog)s -t example.com                    # Scan hostname
  %(prog)s -t 192.168.1.0/24 --network       # Scan network range
  %(prog)s -t 192.168.1.1 -p 80,443,8080     # Scan specific ports
  %(prog)s -t 192.168.1.1 -o results.json    # Save to JSON file
  %(prog)s -t 192.168.1.1 --timeout 2        # Set custom timeout
        '''
    )
    
    parser.add_argument(
        '-t', '--target',
        required=True,
        help='Target to scan (IP address, hostname, or network in CIDR notation)'
    )
    
    parser.add_argument(
        '-n', '--network',
        action='store_true',
        help='Perform network scan (target should be in CIDR notation)'
    )
    
    parser.add_argument(
        '-p', '--ports',
        help='Comma-separated list of ports to scan (e.g., 80,443,8080)'
    )
    
    parser.add_argument(
        '--timeout',
        type=int,
        default=1,
        help='Socket timeout in seconds (default: 1)'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Output file for JSON results'
    )
    
    parser.add_argument(
        '-q', '--quiet',
        action='store_true',
        help='Suppress banner and only show results'
    )
    
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output results as raw JSON'
    )
    
    args = parser.parse_args()
    
    # Print banner unless quiet mode
    if not args.quiet:
        print_banner()
    
    # Parse ports if provided
    ports = None
    if args.ports:
        try:
            ports = [int(p.strip()) for p in args.ports.split(',')]
        except ValueError:
            print("❌ Error: Invalid port format. Use comma-separated numbers (e.g., 80,443,8080)")
            sys.exit(1)
    
    # Initialize scanner
    scanner = NetworkScanner()
    
    # Perform scan
    try:
        if not args.quiet:
            scan_type = "network" if args.network else "host"
            print(f"🔍 Starting {scan_type} scan of {args.target}...\n")
        
        if args.network:
            results = scanner.scan_network(args.target, ports)
        else:
            results = scanner.scan_host(args.target, ports, args.timeout)
        
        # Output results
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print_results(results)
        
        # Save to file if requested
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2)
            if not args.quiet:
                print(f"✅ Results saved to {args.output}")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Scan interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"\n❌ Error during scan: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
