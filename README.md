# Network Security Scanner

[English](#english) | [Português](#português)

## English

### Overview
Advanced network security scanner built with Python and Flask. Features comprehensive network discovery, vulnerability scanning, port analysis, and security assessment capabilities for identifying potential security risks in network infrastructure.

### Features
- **Network Discovery**: Automatic network device discovery
- **Port Scanning**: Comprehensive port analysis and service detection
- **Vulnerability Assessment**: Security vulnerability identification
- **Service Fingerprinting**: Detailed service and version detection
- **Security Reporting**: Comprehensive security assessment reports
- **Real-time Monitoring**: Live network security monitoring
- **Custom Scan Profiles**: Configurable scanning parameters
- **Export Capabilities**: Multiple report export formats

### Technologies Used
- **Python 3.8+**
- **Flask**: Web framework and dashboard
- **Socket**: Network communication
- **Threading**: Concurrent scanning
- **JSON**: Configuration and reporting
- **HTML/CSS**: Web interface

### Installation

1. Clone the repository:
```bash
git clone https://github.com/galafis/Network-Security-Scanner.git
cd Network-Security-Scanner
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the scanner:
```bash
python network_scanner.py
```

4. Open your browser to `http://localhost:5000`

### Usage

#### Web Interface
1. **Target Configuration**: Set scan targets and parameters
2. **Scan Execution**: Run network security scans
3. **Results Analysis**: Review scan results and vulnerabilities
4. **Report Generation**: Create detailed security reports
5. **Monitoring Dashboard**: Real-time network security status

#### API Endpoints

**Start Network Scan**
```bash
curl -X POST http://localhost:5000/api/scan \
  -H "Content-Type: application/json" \
  -d '{"target": "192.168.1.0/24", "scan_type": "comprehensive"}'
```

**Get Scan Results**
```bash
curl -X GET http://localhost:5000/api/results/scan_id_123
```

**Port Scan**
```bash
curl -X POST http://localhost:5000/api/port-scan \
  -H "Content-Type: application/json" \
  -d '{"host": "192.168.1.1", "ports": "1-1000"}'
```

#### Python API
```python
from network_scanner import NetworkScanner

# Initialize scanner
scanner = NetworkScanner()

# Discover network devices
devices = scanner.discover_network("192.168.1.0/24")

# Scan specific host
results = scanner.scan_host(
    host="192.168.1.100",
    ports="1-1000",
    scan_type="comprehensive"
)

# Generate security report
report = scanner.generate_report(results)
print(f"Vulnerabilities found: {len(report['vulnerabilities'])}")
```

### Scanning Features

#### Network Discovery
- **Ping Sweep**: Live host detection
- **ARP Discovery**: Local network device discovery
- **DNS Resolution**: Hostname resolution
- **Network Mapping**: Network topology visualization

#### Port Scanning
- **TCP Connect Scan**: Full TCP connection scanning
- **SYN Scan**: Stealth SYN scanning
- **UDP Scan**: UDP port scanning
- **Service Detection**: Service and version identification

#### Vulnerability Assessment
- **Common Vulnerabilities**: CVE database integration
- **Configuration Issues**: Security misconfigurations
- **Weak Credentials**: Default password detection
- **Outdated Services**: Version vulnerability analysis

#### Security Analysis
- **Open Ports**: Unnecessary open port identification
- **Service Banners**: Service information gathering
- **SSL/TLS Analysis**: Certificate and encryption analysis
- **Firewall Detection**: Firewall rule analysis

### Scan Types

#### Quick Scan
- **Fast Discovery**: Rapid network overview
- **Common Ports**: Top 100 most common ports
- **Basic Services**: Essential service detection
- **Quick Assessment**: High-level security overview

#### Comprehensive Scan
- **Full Port Range**: All 65535 ports
- **Detailed Analysis**: In-depth service analysis
- **Vulnerability Checks**: Complete vulnerability assessment
- **Performance Impact**: Thorough but slower scanning

#### Stealth Scan
- **Low Profile**: Minimal network footprint
- **Evasion Techniques**: IDS/IPS evasion
- **Fragmented Packets**: Packet fragmentation
- **Timing Control**: Scan timing optimization

#### Custom Scan
- **User-Defined**: Custom scan parameters
- **Flexible Targets**: Multiple target formats
- **Selective Ports**: Specific port ranges
- **Advanced Options**: Expert configuration

### Security Reports

#### Executive Summary
- **Risk Overview**: High-level security assessment
- **Critical Issues**: Priority security concerns
- **Recommendations**: Immediate action items
- **Compliance Status**: Security standard compliance

#### Technical Details
- **Vulnerability List**: Detailed vulnerability information
- **Port Analysis**: Open port security assessment
- **Service Information**: Service configuration details
- **Remediation Steps**: Technical fix instructions

#### Compliance Reports
- **PCI DSS**: Payment card industry compliance
- **HIPAA**: Healthcare security requirements
- **SOX**: Sarbanes-Oxley compliance
- **Custom Standards**: Organization-specific requirements

### Monitoring Dashboard

#### Real-time Status
- **Active Scans**: Currently running scans
- **Network Health**: Overall network security status
- **Alert Summary**: Security alerts and warnings
- **Performance Metrics**: Scan performance statistics

#### Historical Analysis
- **Trend Analysis**: Security posture trends
- **Vulnerability Tracking**: Vulnerability lifecycle
- **Remediation Progress**: Fix implementation tracking
- **Compliance Monitoring**: Ongoing compliance status

### Configuration
Configure scanner settings in `config.json`:
```json
{
  "scan_settings": {
    "default_timeout": 5,
    "max_threads": 100,
    "scan_delay": 0.1,
    "retry_attempts": 3
  },
  "vulnerability_db": {
    "update_frequency": "daily",
    "sources": ["nvd", "cve", "custom"],
    "severity_threshold": "medium"
  },
  "reporting": {
    "include_screenshots": true,
    "export_formats": ["pdf", "html", "json"],
    "auto_email": false
  }
}
```

### Security Considerations
- **Authorized Use Only**: Only scan networks you own or have permission to test
- **Legal Compliance**: Follow local laws and regulations
- **Responsible Disclosure**: Report vulnerabilities responsibly
- **Network Impact**: Consider scan impact on network performance

### Integration
- **SIEM Systems**: Security information and event management
- **Vulnerability Management**: Integration with vulnerability scanners
- **Ticketing Systems**: Automatic ticket creation for issues
- **Compliance Tools**: Integration with compliance platforms

### Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Português

### Visão Geral
Scanner avançado de segurança de rede construído com Python e Flask. Apresenta descoberta abrangente de rede, varredura de vulnerabilidades, análise de portas e capacidades de avaliação de segurança para identificar potenciais riscos de segurança na infraestrutura de rede.

### Funcionalidades
- **Descoberta de Rede**: Descoberta automática de dispositivos de rede
- **Varredura de Portas**: Análise abrangente de portas e detecção de serviços
- **Avaliação de Vulnerabilidades**: Identificação de vulnerabilidades de segurança
- **Fingerprinting de Serviços**: Detecção detalhada de serviços e versões
- **Relatórios de Segurança**: Relatórios abrangentes de avaliação de segurança
- **Monitoramento em Tempo Real**: Monitoramento de segurança de rede ao vivo
- **Perfis de Varredura Personalizados**: Parâmetros de varredura configuráveis
- **Capacidades de Exportação**: Múltiplos formatos de exportação de relatórios

### Tecnologias Utilizadas
- **Python 3.8+**
- **Flask**: Framework web e dashboard
- **Socket**: Comunicação de rede
- **Threading**: Varredura concorrente
- **JSON**: Configuração e relatórios
- **HTML/CSS**: Interface web

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/galafis/Network-Security-Scanner.git
cd Network-Security-Scanner
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o scanner:
```bash
python network_scanner.py
```

4. Abra seu navegador em `http://localhost:5000`

### Contribuindo
1. Faça um fork do repositório
2. Crie uma branch de feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adicionar nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Crie um Pull Request

### Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

