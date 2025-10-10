# Network Security Scanner

[English](#english) | [Português](#português)

## English

### Overview

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

Advanced network security scanner built with Python and Flask. Features comprehensive network discovery, vulnerability scanning, port analysis, and security assessment capabilities for identifying potential security risks in network infrastructure.

### Screenshots

#### Web Interface

![Network Scanner Dashboard](https://via.placeholder.com/1200x600/1f2937/ffffff?text=Network+Security+Scanner+Dashboard)

*Web interface showing network scan results, open ports, and security analysis*

#### Scan Results

![Scan Results View](https://via.placeholder.com/1200x400/1f2937/ffffff?text=Scan+Results+and+Vulnerability+Report)

*Detailed scan results with vulnerability assessment and recommendations*

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

3. Run the application:
```bash
python app.py
```

### Running Tests

To run the backend tests, navigate to the project root and execute:
```bash
python3 -m pytest test_network_scanner.py
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
curl -X POST http://localhost:5000/scan \
  -H "Content-Type: application/json" \
  -d '{"target": "192.168.1.0/24", "scan_type": "network"}'
```

**Get Scan Results (Example for a single host scan)**
```bash
curl -X POST http://localhost:5000/scan \
  -H "Content-Type: application/json" \
  -d '{"target": "192.168.1.1", "scan_type": "host"}'
```

#### Python API
```python
from network_scanner import NetworkScanner

# Initialize scanner
scanner = NetworkScanner()

# Discover network devices
devices = scanner.scan_network("192.168.1.0/24")

# Scan specific host
results = scanner.scan_host(
    host="192.168.1.100",
    ports=[21, 22, 80, 443],
    timeout=2
)

# Print results
print(results)
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
Configure scanner settings in `config.py` and environment variables.

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

### Author

**Gabriel Demetrios Lafis**
- GitHub: [@galafis](https://github.com/galafis)
- LinkedIn: [Gabriel Demetrios Lafis](https://linkedin.com/in/gabriel-lafis)

---

## Português

### Visão Geral

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

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

3. Execute a aplicação:
```bash
python app.py
```

### Running Tests

To run the backend tests, navigate to the project root and execute:
```bash
python3 -m pytest test_network_scanner.py
```

4. Abra seu navegador em `http://localhost:5000`

### Uso

#### Interface Web
1. **Configuração de Alvo**: Defina alvos e parâmetros de varredura
2. **Execução da Varredura**: Inicie varreduras de segurança de rede
3. **Análise de Resultados**: Revise os resultados da varredura e vulnerabilidades
4. **Geração de Relatórios**: Crie relatórios detalhados de segurança
5. **Painel de Monitoramento**: Status de segurança de rede em tempo real

#### Endpoints da API

**Iniciar Varredura de Rede**
```bash
curl -X POST http://localhost:5000/scan \
  -H "Content-Type: application/json" \
  -d '{"target": "192.168.1.0/24", "scan_type": "network"}'
```

**Obter Resultados da Varredura (Exemplo para varredura de host único)**
```bash
curl -X POST http://localhost:5000/scan \
  -H "Content-Type: application/json" \
  -d '{"target": "192.168.1.1", "scan_type": "host"}'
```

#### API Python
```python
from network_scanner import NetworkScanner

# Inicializar scanner
scanner = NetworkScanner()

# Descobrir dispositivos de rede
dispositivos = scanner.scan_network("192.168.1.0/24")

# Varredura de host específico
resultados = scanner.scan_host(
    host="192.168.1.100",
    ports=[21, 22, 80, 443],
    timeout=2
)

# Imprimir resultados
print(resultados)
```

### Recursos de Varredura

#### Descoberta de Rede
- **Ping Sweep**: Detecção de hosts ativos
- **Descoberta ARP**: Descoberta de dispositivos de rede local
- **Resolução DNS**: Resolução de nomes de host
- **Mapeamento de Rede**: Visualização da topologia de rede

#### Varredura de Portas
- **Varredura TCP Connect**: Varredura completa de conexão TCP
- **Varredura SYN**: Varredura SYN furtiva
- **Varredura UDP**: Varredura de portas UDP
- **Detecção de Serviços**: Identificação de serviços e versões

#### Avaliação de Vulnerabilidades
- **Vulnerabilidades Comuns**: Integração com banco de dados CVE
- **Problemas de Configuração**: Configurações de segurança incorretas
- **Credenciais Fracas**: Detecção de senhas padrão
- **Serviços Desatualizados**: Análise de vulnerabilidade de versão

#### Análise de Segurança
- **Portas Abertas**: Identificação de portas abertas desnecessárias
- **Banners de Serviço**: Coleta de informações de serviço
- **Análise SSL/TLS**: Análise de certificados e criptografia
- **Detecção de Firewall**: Análise de regras de firewall

### Tipos de Varredura

#### Varredura Rápida
- **Descoberta Rápida**: Visão geral rápida da rede
- **Portas Comuns**: As 100 portas mais comuns
- **Serviços Básicos**: Detecção de serviços essenciais
- **Avaliação Rápida**: Visão geral de segurança de alto nível

#### Varredura Abrangente
- **Faixa Completa de Portas**: Todas as 65535 portas
- **Análise Detalhada**: Análise aprofundada de serviços
- **Verificações de Vulnerabilidade**: Avaliação completa de vulnerabilidades
- **Impacto no Desempenho**: Varredura completa, mas mais lenta

#### Varredura Furtiva
- **Baixo Perfil**: Mínima pegada de rede
- **Técnicas de Evasão**: Evasão de IDS/IPS
- **Pacotes Fragmentados**: Fragmentação de pacotes
- **Controle de Tempo**: Otimização do tempo de varredura

#### Varredura Personalizada
- **Definida pelo Usuário**: Parâmetros de varredura personalizados
- **Alvos Flexíveis**: Múltiplos formatos de alvo
- **Portas Seletivas**: Intervalos de portas específicas
- **Opções Avançadas**: Configuração especializada

### Relatórios de Segurança

#### Resumo Executivo
- **Visão Geral de Risco**: Avaliação de segurança de alto nível
- **Problemas Críticos**: Preocupações de segurança prioritárias
- **Recomendações**: Itens de ação imediata
- **Status de Conformidade**: Conformidade com padrões de segurança

#### Detalhes Técnicos
- **Lista de Vulnerabilidades**: Informações detalhadas sobre vulnerabilidades
- **Análise de Portas**: Avaliação de segurança de portas abertas
- **Informações de Serviço**: Detalhes de configuração de serviço
- **Etapas de Remediação**: Instruções técnicas de correção

#### Relatórios de Conformidade
- **PCI DSS**: Conformidade com o padrão da indústria de cartões de pagamento
- **HIPAA**: Requisitos de segurança de saúde
- **SOX**: Conformidade com Sarbanes-Oxley
- **Padrões Personalizados**: Requisitos específicos da organização

### Painel de Monitoramento

#### Status em Tempo Real
- **Varreduras Ativas**: Varreduras em execução no momento
- **Saúde da Rede**: Status geral de segurança da rede
- **Resumo de Alertas**: Alertas e avisos de segurança
- **Métricas de Desempenho**: Estatísticas de desempenho da varredura

#### Análise Histórica
- **Análise de Tendências**: Tendências da postura de segurança
- **Rastreamento de Vulnerabilidades**: Ciclo de vida das vulnerabilidades
- **Progresso da Remediação**: Rastreamento da implementação de correções
- **Monitoramento de Conformidade**: Status de conformidade contínuo

### Configuração
Configure as configurações do scanner em `config.py` e variáveis de ambiente.

### Considerações de Segurança
- **Uso Autorizado Apenas**: Varredura apenas em redes de sua propriedade ou com permissão para testar
- **Conformidade Legal**: Siga as leis e regulamentos locais
- **Divulgação Responsável**: Relate vulnerabilidades de forma responsável
- **Impacto na Rede**: Considere o impacto da varredura no desempenho da rede

### Integração
- **Sistemas SIEM**: Gerenciamento de informações e eventos de segurança
- **Gerenciamento de Vulnerabilidades**: Integração com scanners de vulnerabilidades
- **Sistemas de Tickets**: Criação automática de tickets para problemas
- **Ferramentas de Conformidade**: Integração com plataformas de conformidade

### Contribuindo
1. Faça um fork do repositório
2. Crie uma branch de feature (`git checkout -b feature/new-feature`)
3. Commit suas mudanças (`git commit -am 'Add new feature'`)
4. Push para a branch (`git push origin feature/new-feature`)
5. Crie um Pull Request

### Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

### Autor

**Gabriel Demetrios Lafis**
- GitHub: [@galafis](https://github.com/galafis)
- LinkedIn: [Gabriel Demetrios Lafis](https://linkedin.com/in/gabriel-lafis)

