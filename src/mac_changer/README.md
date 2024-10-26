# MAC Address Changer Script

This Python script allows users to change the MAC address of a specified network interface on Linux systems. You can choose to enter a custom MAC address or generate a random one. The script also includes an option to automatically change the MAC address at specified intervals.

## Features

- Change MAC address to a custom or random value.
- Verify the change of MAC address.
- Automatically change the MAC address at defined intervals.
- User-friendly command-line interface.

## Requirements

- Python 3.x
- `sudo` privileges to change the MAC address
- `ip` command available on your system (part of the `iproute2` package)

## Installation

**1. Clone the repository or download the script:**
``` bash
git clone https://github.com/thy-rohinish/Script-Vault.git
cd Script-Vault/src/mac_changer
```

**2. Make sure you have Python installed on your system. You can check this by running:**
```bash
python3 --version
```

**3. Ensure you have the necessary privileges to run the script with --sudo.**

## Usage

**1. Make the script executable:**
``` bash
chmod +x mac_changer.py
```

**2. Run the script:**
```bash
sudo ./mac_changer.py
```

**3. Follow the prompts in the terminal to:**

- Enter the network interface (e.g., wlan0, eth0).
- Choose whether to enter a custom MAC address or generate a random one.
- Optionally set up automatic MAC address changes.

## Example

- Enter the network interface (e.g., wlan0, eth0): **wlan0**
- Do you want to enter a custom MAC address or use a random one? (custom/random): **random**
- Generated random MAC address: **00:16:3e:12:34:56**
- Do you want to automatically change MAC address at intervals? (yes/no): **yes**
- Enter time unit for interval (seconds/minutes): **seconds**
- Enter time interval between MAC changes: **30**
- Changing MAC address every **30 seconds...**

## Reverting to Original MAC Address

After running the script, you can choose to revert to the original MAC address when prompted.

## Important Notes

- Changing your MAC address may disrupt your network connection. Ensure you know how to revert to your original MAC address if needed.
- Use this script responsibly and ensure you comply with your local laws and network policies.

## License

This project is licensed under the [MIT License](./LICENSE.md)