import psutil
import socket
import struct

def get_interface_info(interface):
    addrs = psutil.net_if_addrs()
    stats = psutil.net_if_stats()
    
    print(f"Interface: {interface}")
    print("  Addresses:")
    for addr in addrs.get(interface, []):
        print(f"    {addr.family.name}: {addr.address}")
    
    if interface in stats:
        print("  Stats:")
        print(f"    isup: {stats[interface].isup}")
        print(f"    duplex: {stats[interface].duplex}")
        print(f"    speed: {stats[interface].speed}")
        print(f"    mtu: {stats[interface].mtu}")

def get_ethtool_info(interface):
    import fcntl

    # Define constants
    SIOCETHTOOL = 0x8946
    ETHTOOL_GSET = 0x00000001
    ETHTOOL_GDRVINFO = 0x00000003

    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Prepare the struct for the ioctl call
    ifr = struct.pack('16sP', interface.encode(), 0)
    
    try:
        # Get driver information
        ecmd = struct.pack('I39s', ETHTOOL_GDRVINFO, b'\x00'*39)
        ifreq = struct.pack('16sP', interface.encode(), ecmd)
        res = fcntl.ioctl(sock.fileno(), SIOCETHTOOL, ifreq)
        driver = struct.unpack('16sI39s', res[16:])[2].split(b'\x00')[0].decode()
        print(f"  Driver: {driver}")

        # Get link settings
        ecmd = struct.pack('I' + 'c'*127, ETHTOOL_GSET, *([b'\x00']*127))
        ifreq = struct.pack('16sP', interface.encode(), ecmd)
        res = fcntl.ioctl(sock.fileno(), SIOCETHTOOL, ifreq)
        (cmd, speed, duplex, auto_neg) = struct.unpack('12xIH3x5xB51x', res[16:16+128])
        print(f"  Speed: {speed}")
        print(f"  Duplex: {'full' if duplex == 1 else 'half'}")
        print(f"  Auto-negotiation: {'on' if auto_neg == 1 else 'off'}")
    except IOError:
        print("  Unable to get ethtool information")

def main():
    interfaces = psutil.net_if_addrs().keys()
    for interface in interfaces:
        get_interface_info(interface)
        get_ethtool_info(interface)
        print()

if __name__ == "__main__":
    main()