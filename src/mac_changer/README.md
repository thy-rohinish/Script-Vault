# MAC Address Changer 

## Overview

The MAC Address Changer is a Python script designed to change the MAC address of your network interface. This tool is useful for maintaining anonymity on local networks, conducting security assessments, and testing network vulnerabilities. 

## Features

- **Simple Interface**: User-friendly command-line interface for ease of use.
- **Cross-Platform Support**: Compatible with major operating systems (Windows, Linux, macOS).
- **Quick Execution**: Fast and efficient MAC address changing process.
- **Network Interface Selection**: Automatically detects available network interfaces for user selection.

## Installation

To run the MAC Address Changer, follow these steps:

**1.Clone the Repository**:

``` bash
git clone https://github.com/thy-rohinish/Script-Vault.git
cd Script-Vault/src/mac_changer
```

**2.Install Requirements: Make sure you have the required libraries. You can install them using pip:**

``` bash
pip install -r ../../requirements.txt
```

## Usage

To change your MAC address, run the following command in your terminal:

``` bash
python mac_changer.py
```

## Example Commands

**1.To display available network interfaces:**
``` bash
python mac_changer.py --list
```

**2.To change the MAC address of a specific interface:**
``` bash
python mac_changer.py --interface <interface_name> --new_mac <new_mac_address>
```

## Parameters

- ```list```: Displays the list of available network interfaces.
- ```interface```: Specifies the network interface for which you want to change the MAC address.
- ```new_mac```: Specifies the new MAC address to assign.

## Important Notes

- Running this script may require administrative privileges. Ensure you run the terminal as an administrator or with sudo on Unix-based systems.
- Changing your MAC address may violate your ISP's terms of service. Use this tool responsibly and at your own risk.

## Contribution

Contributions are welcome! If you have ideas, suggestions, or improvements, feel free to fork this repository and submit a pull request.

## License

This project is licensed under the MIT LICENSE
