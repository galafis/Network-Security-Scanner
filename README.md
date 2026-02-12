# Network Security Scanner

[English](#english) | [Português](#português)

## English

### Overview

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Security](https://img.shields.io/badge/Security-Scanner-red?style=for-the-badge&logo=security)](https://github.com/galafis/Network-Security-Scanner)
[![Network](https://img.shields.io/badge/Network-Analysis-green?style=for-the-badge&logo=cisco)](https://github.com/galafis/Network-Security-Scanner)

Network security scanner built with Python and Flask. Provides host discovery across network ranges, TCP port scanning, service identification, and basic vulnerability flagging to help spot potential risks in your network infrastructure.

### Screenshots

#### Web Interface - Main Dashboard

![Network Scanner Dashboard](https://github.com/user-attachments/assets/b1d8e387-a633-4ea0-ba88-0d9d57e9390d)

*Modern web interface for configuring and executing network security scans*

#### Scan Results View

![Scan Results](https://github.com/user-attachments/assets/98b7b020-0910-4f02-8991-e0c5a57ed630)

*Comprehensive scan results showing open ports, services, and vulnerability assessments*

### Features
- **Network Discovery**: Host detection across network ranges (CIDR notation)
- **Port Scanning**: Multi-threaded TCP port scanning
- **Service Identification**: Port-to-service name mapping for common services
- **Vulnerability Flagging**: Warnings for insecure protocols and exposed services
- **Security Scoring**: Risk-level assessment with recommendations
- **CLI Interface**: Command-line interface for scripted and terminal-based scanning
- **REST API**: JSON API for programmatic access
- **Web Dashboard**: Browser-based interface for running scans and viewing results
- **JSON Export**: Save scan results to file via the CLI
- **Input Validation**: Request validation and error handling on all endpoints
- **Logging**: Detailed logging for audit trails

### Technologies Used
- **Python 3.8+**: Core programming language
- **Flask**: Web framework and REST API
- **Flask-CORS**: Cross-Origin Resource Sharing support
- **Socket**: Low-level network communication
- **Threading**: Concurrent port scanning
- **ipaddress**: Network address manipulation
- **JSON**: Configuration and reporting format
- **HTML/CSS/JavaScript**: Modern web interface
- **pytest**: Testing framework

### Architecture

```mermaid
graph TB
    subgraph "Client Layer"
        A[Web Interface<br/>HTML/CSS/JavaScript]
        B[CLI Interface<br/>scanner_cli.py]
        C[Python API<br/>Direct Integration]
    end
    
    subgraph "API Layer"
        D[Flask REST API<br/>app.py]
        E[Input Validation &<br/>Error Handling]
        F[Logging & Security<br/>Headers]
    end
    
    subgraph "Core Engine"
        G[Network Scanner Module<br/>network_scanner.py]
        H[Port Scanning Engine<br/>Multi-threaded]
        I[Service Identification]
        J[Vulnerability Assessment]
        K[Security Analysis &<br/>Reporting]
    end
    
    A -->|HTTP/JSON| D
    B -->|Direct Call| G
    C -->|Import| G
    D --> E
    E --> F
    F --> G
    G --> H
    G --> I
    G --> J
    G --> K
    
    style A fill:#e3f2fd
    style B fill:#e3f2fd
    style C fill:#e3f2fd
    style D fill:#fff3e0
    style E fill:#fff3e0
    style F fill:#fff3e0
    style G fill:#f3e5f5
    style H fill:#f3e5f5
    style I fill:#f3e5f5
    style J fill:#f3e5f5
    style K fill:#f3e5f5
```

### Scan Workflow

The following diagram illustrates the complete scanning process from input to report generation:

```mermaid
flowchart LR
    A[User Input<br/>Target IP/Network] --> B{Validate<br/>Input}
    B -->|Valid| C[Network Discovery<br/>Ping Sweep]
    B -->|Invalid| Z[Error Response]
    C --> D[Active Hosts<br/>Identified]
    D --> E[Port Scanning<br/>Multi-threaded]
    E --> F[Open Ports<br/>Detected]
    F --> G[Service<br/>Identification]
    G --> H[Vulnerability<br/>Assessment]
    H --> I[Security<br/>Analysis]
    I --> J[Risk Scoring]
    J --> K[Generate<br/>Report]
    K --> L[Return Results<br/>JSON/HTML]
    
    style A fill:#e1f5ff
    style C fill:#fff4e6
    style E fill:#fff4e6
    style G fill:#fff4e6
    style H fill:#ffe6e6
    style I fill:#ffe6e6
    style J fill:#ffe6e6
    style K fill:#e6ffe6
    style L fill:#e6ffe6
    style Z fill:#ffcccc
```

### Installation

#### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

#### Step-by-Step Installation

1. **Clone the repository:**
```bash
git clone https://github.com/galafis/Network-Security-Scanner.git
cd Network-Security-Scanner
```

2. **Create and activate a virtual environment (recommended):**
```bash
# On Linux/Mac
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables (optional):**
```bash
cp .env.example .env
# Edit .env file with your preferred settings
```

5. **Run the application:**
```bash
python app.py
```

6. **Access the web interface:**
Open your browser to `http://localhost:5000`

### Running Tests

The project includes comprehensive unit and integration tests.

**Run all tests:**
```bash
python3 -m pytest test_network_scanner.py test_app.py -v
```

**Run specific test file:**
```bash
# Backend scanner tests
python3 -m pytest test_network_scanner.py -v

# Flask app tests
python3 -m pytest test_app.py -v
```

**Run with coverage:**
```bash
python3 -m pytest --cov=network_scanner --cov=app --cov-report=html
```

**Using unittest (alternative):**
```bash
python3 -m unittest discover -v
```

### Usage

#### Command Line Interface (CLI)

The scanner provides a powerful CLI for terminal-based scanning.

**Basic host scan:**
```bash
python3 scanner_cli.py -t 192.168.1.1
```

**Scan hostname:**
```bash
python3 scanner_cli.py -t example.com
```

**Network range scan:**
```bash
python3 scanner_cli.py -t 192.168.1.0/24 --network
```

**Scan specific ports:**
```bash
python3 scanner_cli.py -t 192.168.1.1 -p 80,443,8080,3306
```

**Save results to JSON file:**
```bash
python3 scanner_cli.py -t 192.168.1.1 -o results.json
```

**JSON output mode:**
```bash
python3 scanner_cli.py -t 192.168.1.1 --json
```

**Quiet mode (no banner):**
```bash
python3 scanner_cli.py -t 192.168.1.1 -q
```

**Custom timeout:**
```bash
python3 scanner_cli.py -t 192.168.1.1 --timeout 2
```

#### Web Interface
1. **Target Configuration**: Set scan targets and parameters
2. **Scan Execution**: Run network security scans
3. **Results Analysis**: Review scan results and vulnerabilities
4. **Report Generation**: Create detailed security reports
5. **Monitoring Dashboard**: Real-time network security status

#### API Endpoints

The scanner provides a REST API for programmatic access.

**Health Check**
```bash
curl -X GET http://localhost:5000/health
```

Response:
```json
{
  "status": "healthy",
  "service": "Network Security Scanner"
}
```

**Start Network Scan**
```bash
curl -X POST http://localhost:5000/scan \
  -H "Content-Type: application/json" \
  -d '{"target": "192.168.1.0/24", "scan_type": "network"}'
```

**Scan Single Host**
```bash
curl -X POST http://localhost:5000/scan \
  -H "Content-Type: application/json" \
  -d '{"target": "192.168.1.1", "scan_type": "host"}'
```

**Scan with Hostname**
```bash
curl -X POST http://localhost:5000/scan \
  -H "Content-Type: application/json" \
  -d '{"target": "example.com", "scan_type": "host"}'
```

Response Example:
```json
{
  "host": "example.com",
  "ip": "93.184.216.34",
  "timestamp": "2024-01-15T10:30:00.123456",
  "open_ports": [80, 443],
  "closed_ports": [21, 22, 23],
  "services": {
    "80": "HTTP",
    "443": "HTTPS"
  },
  "vulnerabilities": [
    {
      "type": "Unencrypted Web Traffic",
      "severity": "Medium",
      "description": "HTTP traffic is not encrypted",
      "recommendation": "Use HTTPS with valid SSL/TLS certificate"
    }
  ],
  "security_analysis": {
    "risk_level": "Medium",
    "score": 80,
    "recommendations": [
      "Use encrypted alternatives (HTTPS, SFTP, SSH)",
      "Regular security audits recommended"
    ]
  }
}
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

### Configuration
Configure scanner settings in `config.py` and environment variables.

### Security Considerations

#### Legal and Ethical Use
- **Authorized Use Only**: Only scan networks you own or have explicit written permission to test
- **Legal Compliance**: Follow all local, state, and federal laws regarding network scanning
- **Responsible Disclosure**: Report discovered vulnerabilities responsibly to affected parties
- **Professional Ethics**: Use this tool only for legitimate security assessment purposes

#### Best Practices
- **Network Impact**: Schedule scans during low-usage periods to minimize network disruption
- **Rate Limiting**: Use appropriate timeouts and delays to avoid overwhelming target systems
- **Documentation**: Keep detailed records of all scans performed, including authorization
- **Data Protection**: Secure scan results containing sensitive information
- **Regular Updates**: Keep the scanner and all dependencies updated for security patches

#### Security Recommendations
- **Use HTTPS**: Always use HTTPS in production environments
- **Authentication**: Implement authentication for the web interface in production
- **Access Control**: Restrict access to the scanner to authorized personnel only
- **Logging**: Monitor and review scan logs regularly for unusual activity
- **Encryption**: Use encrypted channels when transmitting scan results

#### Disclaimer
This tool is provided for educational and authorized security assessment purposes only. Users are solely responsible for ensuring their use of this tool complies with all applicable laws and regulations. The authors assume no liability for misuse or damage caused by this tool.

### Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

Quick start:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Make your changes with tests
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/new-feature`)
6. Create a Pull Request

For bug reports, feature requests, or questions, please open an issue on GitHub.

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
[![Security](https://img.shields.io/badge/Segurança-Scanner-red?style=for-the-badge&logo=security)](https://github.com/galafis/Network-Security-Scanner)
[![Network](https://img.shields.io/badge/Rede-Análise-green?style=for-the-badge&logo=cisco)](https://github.com/galafis/Network-Security-Scanner)

Scanner de segurança de rede construído com Python e Flask. Oferece descoberta de hosts em faixas de rede, varredura de portas TCP, identificação de serviços e sinalização básica de vulnerabilidades para ajudar a identificar riscos potenciais na infraestrutura de rede.

### Capturas de Tela

#### Interface Web - Painel Principal

![Painel do Scanner de Rede](https://github.com/user-attachments/assets/b1d8e387-a633-4ea0-ba88-0d9d57e9390d)

*Interface web moderna para configurar e executar varreduras de segurança de rede*

#### Visualização de Resultados da Varredura

![Resultados da Varredura](https://github.com/user-attachments/assets/98b7b020-0910-4f02-8991-e0c5a57ed630)

*Resultados abrangentes mostrando portas abertas, serviços e avaliações de vulnerabilidades*

### Funcionalidades
- **Descoberta de Rede**: Detecção de hosts em faixas de rede (notação CIDR)
- **Varredura de Portas**: Varredura TCP multi-threaded
- **Identificação de Serviços**: Mapeamento de porta para nome de serviço
- **Sinalização de Vulnerabilidades**: Alertas para protocolos inseguros e serviços expostos
- **Pontuação de Segurança**: Avaliação de nível de risco com recomendações
- **Interface CLI**: Interface de linha de comando para varreduras via terminal
- **API REST**: API JSON para acesso programático
- **Painel Web**: Interface no navegador para executar varreduras e ver resultados
- **Exportação JSON**: Salvar resultados de varredura em arquivo via CLI
- **Validação de Entrada**: Validação de requisições e tratamento de erros em todos os endpoints
- **Logging**: Logging detalhado para trilhas de auditoria

### Tecnologias Utilizadas
- **Python 3.8+**: Linguagem de programação principal
- **Flask**: Framework web e API REST
- **Flask-CORS**: Suporte para Cross-Origin Resource Sharing
- **Socket**: Comunicação de rede de baixo nível
- **Threading**: Varredura concorrente de portas
- **ipaddress**: Manipulação de endereços de rede
- **JSON**: Formato de configuração e relatórios
- **HTML/CSS/JavaScript**: Interface web moderna
- **pytest**: Framework de testes

### Arquitetura

```mermaid
graph TB
    subgraph "Camada de Cliente"
        A[Interface Web<br/>HTML/CSS/JavaScript]
        B[Interface CLI<br/>scanner_cli.py]
        C[API Python<br/>Integração Direta]
    end
    
    subgraph "Camada de API"
        D[API REST Flask<br/>app.py]
        E[Validação de Entrada e<br/>Tratamento de Erros]
        F[Logging e Cabeçalhos<br/>de Segurança]
    end
    
    subgraph "Motor Principal"
        G[Módulo Network Scanner<br/>network_scanner.py]
        H[Motor de Varredura<br/>Multi-threaded]
        I[Identificação de Serviços]
        J[Avaliação de<br/>Vulnerabilidades]
        K[Análise de Segurança<br/>e Relatórios]
    end
    
    A -->|HTTP/JSON| D
    B -->|Chamada Direta| G
    C -->|Import| G
    D --> E
    E --> F
    F --> G
    G --> H
    G --> I
    G --> J
    G --> K
    
    style A fill:#e3f2fd
    style B fill:#e3f2fd
    style C fill:#e3f2fd
    style D fill:#fff3e0
    style E fill:#fff3e0
    style F fill:#fff3e0
    style G fill:#f3e5f5
    style H fill:#f3e5f5
    style I fill:#f3e5f5
    style J fill:#f3e5f5
    style K fill:#f3e5f5
```

### Fluxo de Varredura

O diagrama a seguir ilustra o processo completo de varredura desde a entrada até a geração de relatórios:

```mermaid
flowchart LR
    A[Entrada do Usuário<br/>IP/Rede Alvo] --> B{Validar<br/>Entrada}
    B -->|Válido| C[Descoberta de Rede<br/>Ping Sweep]
    B -->|Inválido| Z[Resposta de Erro]
    C --> D[Hosts Ativos<br/>Identificados]
    D --> E[Varredura de Portas<br/>Multi-threaded]
    E --> F[Portas Abertas<br/>Detectadas]
    F --> G[Identificação<br/>de Serviços]
    G --> H[Avaliação de<br/>Vulnerabilidades]
    H --> I[Análise de<br/>Segurança]
    I --> J[Pontuação<br/>de Risco]
    J --> K[Gerar<br/>Relatório]
    K --> L[Retornar Resultados<br/>JSON/HTML]
    
    style A fill:#e1f5ff
    style C fill:#fff4e6
    style E fill:#fff4e6
    style G fill:#fff4e6
    style H fill:#ffe6e6
    style I fill:#ffe6e6
    style J fill:#ffe6e6
    style K fill:#e6ffe6
    style L fill:#e6ffe6
    style Z fill:#ffcccc
```

### Instalação

#### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Ambiente virtual (recomendado)

#### Instalação Passo a Passo

1. **Clone o repositório:**
```bash
git clone https://github.com/galafis/Network-Security-Scanner.git
cd Network-Security-Scanner
```

2. **Crie e ative um ambiente virtual (recomendado):**
```bash
# No Linux/Mac
python3 -m venv venv
source venv/bin/activate

# No Windows
python -m venv venv
venv\Scripts\activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente (opcional):**
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações preferidas
```

5. **Execute a aplicação:**
```bash
python app.py
```

6. **Acesse a interface web:**
Abra seu navegador em `http://localhost:5000`

### Executando Testes

O projeto inclui testes unitários e de integração abrangentes.

**Executar todos os testes:**
```bash
python3 -m pytest test_network_scanner.py test_app.py -v
```

**Executar arquivo de teste específico:**
```bash
# Testes do scanner backend
python3 -m pytest test_network_scanner.py -v

# Testes da aplicação Flask
python3 -m pytest test_app.py -v
```

**Executar com cobertura:**
```bash
python3 -m pytest --cov=network_scanner --cov=app --cov-report=html
```

**Usando unittest (alternativa):**
```bash
python3 -m unittest discover -v
```

### Uso

#### Interface de Linha de Comando (CLI)

O scanner fornece uma CLI poderosa para varreduras baseadas em terminal.

**Varredura básica de host:**
```bash
python3 scanner_cli.py -t 192.168.1.1
```

**Varredura de nome de host:**
```bash
python3 scanner_cli.py -t example.com
```

**Varredura de faixa de rede:**
```bash
python3 scanner_cli.py -t 192.168.1.0/24 --network
```

**Varredura de portas específicas:**
```bash
python3 scanner_cli.py -t 192.168.1.1 -p 80,443,8080,3306
```

**Salvar resultados em arquivo JSON:**
```bash
python3 scanner_cli.py -t 192.168.1.1 -o resultados.json
```

**Modo de saída JSON:**
```bash
python3 scanner_cli.py -t 192.168.1.1 --json
```

**Modo silencioso (sem banner):**
```bash
python3 scanner_cli.py -t 192.168.1.1 -q
```

**Timeout personalizado:**
```bash
python3 scanner_cli.py -t 192.168.1.1 --timeout 2
```

#### Interface Web
1. **Configuração de Alvo**: Defina alvos e parâmetros de varredura
2. **Execução da Varredura**: Inicie varreduras de segurança de rede
3. **Análise de Resultados**: Revise os resultados da varredura e vulnerabilidades
4. **Geração de Relatórios**: Crie relatórios detalhados de segurança
5. **Painel de Monitoramento**: Status de segurança de rede em tempo real

#### Endpoints da API

O scanner fornece uma API REST para acesso programático.

**Verificação de Saúde**
```bash
curl -X GET http://localhost:5000/health
```

Resposta:
```json
{
  "status": "healthy",
  "service": "Network Security Scanner"
}
```

**Iniciar Varredura de Rede**
```bash
curl -X POST http://localhost:5000/scan \
  -H "Content-Type: application/json" \
  -d '{"target": "192.168.1.0/24", "scan_type": "network"}'
```

**Varredura de Host Único**
```bash
curl -X POST http://localhost:5000/scan \
  -H "Content-Type: application/json" \
  -d '{"target": "192.168.1.1", "scan_type": "host"}'
```

**Varredura com Nome de Host**
```bash
curl -X POST http://localhost:5000/scan \
  -H "Content-Type: application/json" \
  -d '{"target": "example.com", "scan_type": "host"}'
```

Exemplo de Resposta:
```json
{
  "host": "example.com",
  "ip": "93.184.216.34",
  "timestamp": "2024-01-15T10:30:00.123456",
  "open_ports": [80, 443],
  "closed_ports": [21, 22, 23],
  "services": {
    "80": "HTTP",
    "443": "HTTPS"
  },
  "vulnerabilities": [
    {
      "type": "Unencrypted Web Traffic",
      "severity": "Medium",
      "description": "HTTP traffic is not encrypted",
      "recommendation": "Use HTTPS with valid SSL/TLS certificate"
    }
  ],
  "security_analysis": {
    "risk_level": "Medium",
    "score": 80,
    "recommendations": [
      "Use encrypted alternatives (HTTPS, SFTP, SSH)",
      "Regular security audits recommended"
    ]
  }
}
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

### Configuração
Configure as configurações do scanner em `config.py` e variáveis de ambiente.

### Considerações de Segurança

#### Uso Legal e Ético
- **Uso Autorizado Apenas**: Varredura apenas em redes de sua propriedade ou com permissão explícita por escrito
- **Conformidade Legal**: Siga todas as leis locais, estaduais e federais referentes à varredura de rede
- **Divulgação Responsável**: Relate vulnerabilidades descobertas de forma responsável às partes afetadas
- **Ética Profissional**: Use esta ferramenta apenas para fins legítimos de avaliação de segurança

#### Melhores Práticas
- **Impacto na Rede**: Agende varreduras durante períodos de baixo uso para minimizar a interrupção da rede
- **Limitação de Taxa**: Use timeouts e atrasos apropriados para evitar sobrecarregar sistemas de destino
- **Documentação**: Mantenha registros detalhados de todas as varreduras realizadas, incluindo autorização
- **Proteção de Dados**: Proteja os resultados de varredura contendo informações sensíveis
- **Atualizações Regulares**: Mantenha o scanner e todas as dependências atualizadas para patches de segurança

#### Recomendações de Segurança
- **Use HTTPS**: Sempre use HTTPS em ambientes de produção
- **Autenticação**: Implemente autenticação para a interface web em produção
- **Controle de Acesso**: Restrinja o acesso ao scanner apenas ao pessoal autorizado
- **Logging**: Monitore e revise os logs de varredura regularmente para atividades incomuns
- **Criptografia**: Use canais criptografados ao transmitir resultados de varredura

#### Aviso Legal
Esta ferramenta é fornecida apenas para fins educacionais e de avaliação de segurança autorizados. Os usuários são os únicos responsáveis por garantir que o uso desta ferramenta esteja em conformidade com todas as leis e regulamentos aplicáveis. Os autores não assumem qualquer responsabilidade por uso indevido ou danos causados por esta ferramenta.

### Contribuindo

Recebemos contribuições com prazer! Consulte [CONTRIBUTING.md](CONTRIBUTING.md) para diretrizes detalhadas.

Início rápido:
1. Faça um fork do repositório
2. Crie uma branch de feature (`git checkout -b feature/new-feature`)
3. Faça suas alterações com testes
4. Commit suas mudanças (`git commit -am 'Add new feature'`)
5. Push para a branch (`git push origin feature/new-feature`)
6. Crie um Pull Request

Para relatórios de bugs, solicitações de recursos ou perguntas, abra uma issue no GitHub.

### Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

### Autor

**Gabriel Demetrios Lafis**
- GitHub: [@galafis](https://github.com/galafis)
- LinkedIn: [Gabriel Demetrios Lafis](https://linkedin.com/in/gabriel-lafis)

