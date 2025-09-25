Violet DDOS Tool

A powerful and versatile DDoS testing tool written in Python, designed for educational purposes and authorized penetration testing.

⚠️ DISCLAIMER

This tool is for educational and authorized testing purposes only. Unauthorized use against any network or system without explicit permission is illegal. The developers are not responsible for any misuse of this software.

Features

> Multiple Attack Protocols: UDP, TCP, HTTP, Slowloris
> 
> Advanced TCP Methods: SYN Flood, Data Flood (Single/Multi-threaded)
> 
> UDP Variants: Plain payload and Random payload attacks
>
> HTTP Attacks: GET and POST flood capabilities
> 
> Proxy Support: Built-in proxy integration
>
> User-Friendly Interface: Color-coded console interface
> 
> Input Validation: Comprehensive validation for all parameters

Installation

Prerequisites

> Python 3.7 or higher
> 
> pip package manager

Setup

1. Clone the repository:

```bash
git clone https://github.com/exsarorrayzer/violet-ddos.git
cd violet-ddos
```

1. Install required dependencies:

```bash
pip install -r requirements.txt
```

Usage

Run the tool with:

```bash
python main.py
```

Protocol Options

1. UDP Attacks
> UDP Plain: Fixed payload flood
>
> UDP Random: Random payload flood

2. TCP Attacks
> SYN Flood: Single socket or multi-threaded
> 
> Data Flood: Single socket or multi-threaded

3. HTTP Attacks
> GET Flood: HTTP GET requests
> 
> POST Flood: HTTP POST requests

4. Slowloris Attack
> Low-and-slow attack keeping connections open

Example Usage

```
VIOLET DDOS

Methods:
1. UDP
2. TCP
3. HTTP
4. Slowloris

Select protocol: 2
```

Project Structure

```
violet-ddos/
├── main.py                 # Main application entry point
├── proxy.txt              # Proxy File
├── user_agents.txt        # User Agent File
├── utils/
│   ├── colors.py          # Terminal color utilities
│   ├── validate.py        # Input validation functions
│   ├── proxy.py           # Proxy management
│   ├── banner.py          # Application banner
│   ├── clear.py           # Screen clearing utilities
│   └── creds.py           # Credit display
├── methods/
│   ├── udp.py            # UDP attack implementations
│   ├── tcp.py            # TCP attack implementations
│   ├── http.py           # HTTP attack implementations
│   └── slowloris.py      # Slowloris attack implementation
└── requirements.txt       # Python dependencies
```

Configuration

Proxy Setup

Edit the proxy configuration in proxy.txt to add your proxy servers

UserAgent Setup

Edit the useragent configuration in useragent.txt to add your useragents


> Optional


Legal and Ethical Use

This tool must only be used in the following scenarios:

> With explicit written permission from the target owner
> 
> In educational environments for learning purposes
> 
> For security research with proper authorization

Acknowledgments

> Developed by Rayzer
>
> For educational purposes only
>
> Use responsibly and ethically

Support

For questions or support, please open an issue on the GitHub repository.

---

