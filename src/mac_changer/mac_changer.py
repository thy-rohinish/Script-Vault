#!/usr/bin/env python

import subprocess
import random
import time

# Print the signature in white
print("\033[37m" + """
   _____           _       _    __      __         _ _   
  / ____|         (_)     | |   \ \    / /        | | |  
 | (___   ___ _ __ _ _ __ | |_   \ \  / /_ _ _   _| | |_ 
  \___ \ / __| '__| | '_ \| __|   \ \/ / _` | | | | | __|
  ____) | (__| |  | | |_) | |_     \  / (_| | |_| | | |_ 
 |_____/ \___|_|  |_| .__/ \__|     \/ \__,_|\__,_|_|\__|
                    | |                                  
                    |_|                                  
""" + "\033[0m")

# Define the network interface
interface = input("Enter the network interface (e.g., wlan0, eth0): ").strip()

# Generate a random MAC address
def generate_random_mac():
    mac = [0x00, 0x16, 0x3E, random.randint(0x00, 0x7F), random.randint(0x00, 0xFF), random.randint(0x00, 0xFF)]
    return ':'.join(map(lambda x: f"{x:02x}", mac))

# Retrieve the current MAC address of the interface
def get_current_mac(interface):
    output = subprocess.check_output(["cat", f"/sys/class/net/{interface}/address"])
    return output.decode().strip()

# Verify that the MAC address has been changed successfully
def verify_mac(interface, expected_mac):
    current_mac = get_current_mac(interface)
    if current_mac == expected_mac:
        print(f"MAC address successfully changed to {current_mac}")
    else:
        print(f"MAC address change failed. Current MAC is {current_mac}")

# Save the original MAC address for later reversion
original_mac = get_current_mac(interface)
print(f"Original MAC: {original_mac}")

# Prompt user for custom or random MAC choice
user_choice = input("Do you want to enter a custom MAC address or use a random one? (custom/random): ").strip().lower()

# Handle user choice for custom or random MAC generation
if user_choice == "custom":
    new_mac = input("Enter the MAC address (format XX:XX:XX:XX:XX:XX): ")
elif user_choice == "random":
    new_mac = generate_random_mac()
    print(f"Generated random MAC address: {new_mac}")
else:
    print("Invalid choice. Exiting.")
    exit()

# Apply the new MAC address
subprocess.call(["sudo", "ip", "link", "set", "dev", interface, "down"])
subprocess.call(["sudo", "ip", "link", "set", "dev", interface, "address", new_mac])
subprocess.call(["sudo", "ip", "link", "set", "dev", interface, "up"])

# Verify if MAC change was successful
verify_mac(interface, new_mac)

# Check if user wants to enable auto-randomization
auto_randomize = input("Do you want to automatically change MAC address at intervals? (yes/no): ").strip().lower()
if auto_randomize == "yes":
    interval = int(input("Enter time interval in seconds between MAC changes: "))
    while True:
        # Generate and set a new random MAC address
        new_mac = generate_random_mac()
        print(f"Changing MAC to: {new_mac}")
        subprocess.call(["sudo", "ip", "link", "set", "dev", interface, "down"])
        subprocess.call(["sudo", "ip", "link", "set", "dev", interface, "address", new_mac])
        subprocess.call(["sudo", "ip", "link", "set", "dev", interface, "up"])
        verify_mac(interface, new_mac)
        time.sleep(interval)

# Ask if the user wants to revert to the original MAC address
revert = input("Do you want to revert to the original MAC? (yes/no): ").strip().lower()
if revert == "yes":
    subprocess.call(["sudo", "ip", "link", "set", "dev", interface, "down"])
    subprocess.call(["sudo", "ip", "link", "set", "dev", interface, "address", original_mac])
    subprocess.call(["sudo", "ip", "link", "set", "dev", interface, "up"])
    print(f"MAC address reverted to original: {original_mac}")
else:
    print(f"Current MAC remains as {new_mac}")
