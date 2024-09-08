import subprocess
import time

def run_command(cmd):
    try:
        result = subprocess.run(cmd, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return None

def create_bridge(name):
    print(f"Creating bridge {name}")
    run_command(f"sudo ip link add name {name} type bridge")
    run_command(f"sudo ip link set {name} up")

def create_veth_pair(veth1, veth2):
    print(f"Creating veth pair: {veth1} <-> {veth2}")
    run_command(f"sudo ip link add {veth1} type veth peer name {veth2}")
    run_command(f"sudo ip link set {veth1} up")
    run_command(f"sudo ip link set {veth2} up")

def add_to_bridge(interface, bridge):
    print(f"Adding {interface} to bridge {bridge}")
    run_command(f"sudo ip link set {interface} master {bridge}")

def create_tuntap(name):
    print(f"Creating TUN/TAP device: {name}")
    run_command(f"sudo ip tuntap add dev {name} mode tap")
    run_command(f"sudo ip link set {name} up")

def setup_virtual_network():
    # Create a bridge
    create_bridge("br0")

    # Create veth pair
    create_veth_pair("veth0", "veth1")

    # Add one end of veth pair to bridge
    add_to_bridge("veth0", "br0")

    # Create a TUN/TAP device
    create_tuntap("tap0")

    # Add TUN/TAP device to bridge
    add_to_bridge("tap0", "br0")

def display_network_info():
    print("\nNetwork Interface Information:")
    print(run_command("ip link show"))

def main():
    print("Setting up virtual network...")
    setup_virtual_network()
    time.sleep(2)  # Give some time for network setup
    display_network_info()
    print("\nVirtual network setup complete. Network topology:")
    print("veth1 <-> veth0 <-> br0 <-> tap0")
    print("\nYou can now use these interfaces for further networking experiments.")

if __name__ == "__main__":
    if subprocess.geteuid() != 0:
        print("This script must be run as root. Please use sudo.")
    else:
        main()