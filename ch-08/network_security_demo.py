import subprocess
import re

def check_iptables_rules():
    """Check and display iptables rules"""
    try:
        output = subprocess.check_output(["sudo", "iptables", "-L"], universal_newlines=True)
        print("Current iptables rules:")
        print(output)
    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve iptables rules. Make sure you have the necessary permissions.")

def add_iptables_rule(rule):
    """Add an iptables rule"""
    try:
        subprocess.run(["sudo", "iptables"] + rule.split(), check=True)
        print(f"Rule added successfully: {rule}")
    except subprocess.CalledProcessError:
        print(f"Error: Unable to add rule: {rule}")

def check_selinux_status():
    """Check SELinux status"""
    try:
        output = subprocess.check_output(["sestatus"], universal_newlines=True)
        status = re.search(r"SELinux status:\s+(\w+)", output)
        if status:
            print(f"SELinux status: {status.group(1)}")
        else:
            print("Unable to determine SELinux status")
    except subprocess.CalledProcessError:
        print("Error: Unable to check SELinux status")

def check_vpn_status():
    """Check OpenVPN status"""
    try:
        output = subprocess.check_output(["sudo", "systemctl", "is-active", "openvpn"], universal_newlines=True)
        print(f"OpenVPN status: {output.strip()}")
    except subprocess.CalledProcessError:
        print("OpenVPN is not running or not installed")

def main():
    print("Network Security Demo")
    print("=====================")

    # Check iptables rules
    check_iptables_rules()

    # Add a sample iptables rule
    add_iptables_rule("-A INPUT -p tcp --dport 8080 -j ACCEPT")

    # Check SELinux status
    check_selinux_status()

    # Check VPN status
    check_vpn_status()

if __name__ == "__main__":
    main()