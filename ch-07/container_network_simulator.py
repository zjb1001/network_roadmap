import subprocess
import os

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode('utf-8'), error.decode('utf-8')

def create_network_namespace(name):
    return run_command(f"ip netns add {name}")

def create_veth_pair(veth1, veth2):
    return run_command(f"ip link add {veth1} type veth peer name {veth2}")

def move_to_namespace(interface, namespace):
    return run_command(f"ip link set {interface} netns {namespace}")

def setup_interface(namespace, interface, ip):
    commands = [
        f"ip netns exec {namespace} ip addr add {ip}/24 dev {interface}",
        f"ip netns exec {namespace} ip link set {interface} up"
    ]
    return [run_command(cmd) for cmd in commands]

def create_bridge(name):
    return run_command(f"ip link add name {name} type bridge")

def add_to_bridge(interface, bridge):
    return run_command(f"ip link set {interface} master {bridge}")

def setup_container_network():
    print("Setting up container network simulation...")

    # Create network namespaces (simulating containers)
    create_network_namespace("container1")
    create_network_namespace("container2")

    # Create veth pairs
    create_veth_pair("veth1", "veth1_c")
    create_veth_pair("veth2", "veth2_c")

    # Move veth endpoints to namespaces
    move_to_namespace("veth1_c", "container1")
    move_to_namespace("veth2_c", "container2")

    # Setup interfaces in namespaces
    setup_interface("container1", "veth1_c", "172.18.0.2")
    setup_interface("container2", "veth2_c", "172.18.0.3")

    # Create and setup bridge
    create_bridge("br0")
    run_command("ip link set br0 up")
    add_to_bridge("veth1", "br0")
    add_to_bridge("veth2", "br0")

    print("Container network simulation setup complete.")

def test_connectivity():
    print("\nTesting connectivity between containers:")
    output, _ = run_command("ip netns exec container1 ping -c 3 172.18.0.3")
    print(output)

if __name__ == "__main__":
    if os.geteuid() != 0:
        exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
    
    setup_container_network()
    test_connectivity()