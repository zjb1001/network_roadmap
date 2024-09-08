import os
from pyroute2 import IPRoute, IPDB, NetNS
from pyroute2.netlink.exceptions import NetlinkError

def create_bridge(ip, name):
    try:
        ip.link('add', ifname=name, kind='bridge')
        with IPDB() as ipdb:
            with ipdb.interfaces[name] as bridge:
                bridge.up()
        print(f"Created bridge: {name}")
    except NetlinkError as e:
        print(f"Error creating bridge {name}: {e}")

def create_veth_pair(ip, veth1, veth2):
    try:
        ip.link('add', ifname=veth1, peer=veth2, kind='veth')
        with IPDB() as ipdb:
            with ipdb.interfaces[veth1] as v1, ipdb.interfaces[veth2] as v2:
                v1.up()
                v2.up()
        print(f"Created veth pair: {veth1} <-> {veth2}")
    except NetlinkError as e:
        print(f"Error creating veth pair {veth1} <-> {veth2}: {e}")

def add_to_bridge(ip, interface, bridge):
    try:
        bridge_idx = ip.link_lookup(ifname=bridge)[0]
        intf_idx = ip.link_lookup(ifname=interface)[0]
        ip.link('set', index=intf_idx, master=bridge_idx)
        print(f"Added {interface} to bridge {bridge}")
    except NetlinkError as e:
        print(f"Error adding {interface} to bridge {bridge}: {e}")

def create_tuntap(ip, name):
    try:
        ip.link('add', ifname=name, kind='tuntap', mode='tap')
        with IPDB() as ipdb:
            with ipdb.interfaces[name] as tap:
                tap.up()
        print(f"Created TUN/TAP device: {name}")
    except NetlinkError as e:
        print(f"Error creating TUN/TAP device {name}: {e}")

def setup_virtual_network():
    with IPRoute() as ip:
        # Create a bridge
        create_bridge(ip, "br0")

        # Create veth pair
        create_veth_pair(ip, "veth0", "veth1")

        # Add one end of veth pair to bridge
        add_to_bridge(ip, "veth0", "br0")

        # Create a TUN/TAP device
        create_tuntap(ip, "tap0")

        # Add TUN/TAP device to bridge
        add_to_bridge(ip, "tap0", "br0")

def display_network_info():
    print("\nNetwork Interface Information:")
    with IPRoute() as ip:
        links = ip.get_links()
        for link in links:
            print(f"Interface: {link.get_attr('IFLA_IFNAME')}, State: {'UP' if link['state'] == 1 else 'DOWN'}")

def main():
    if os.geteuid() != 0:
        print("This script must be run as root. Please use sudo.")
        return

    print("Setting up virtual network...")
    setup_virtual_network()
    display_network_info()
    print("\nVirtual network setup complete. Network topology:")
    print("veth1 <-> veth0 <-> br0 <-> tap0")
    print("\nYou can now use these interfaces for further networking experiments.")

if __name__ == "__main__":
    main()