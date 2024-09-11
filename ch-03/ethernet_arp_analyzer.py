import subprocess
from scapy.all import *
from enum import Enum

class ARPOperation(Enum):
    who_has = 1
    is_at = 2

def get_interface():
    # 获取默认网络接口
    result = subprocess.run(['route', '-n', 'get', '0.0.0.0'], capture_output=True, text=True)
    for line in result.stdout.split('\n'):
        if 'interface:' in line:
            return line.split()[-1]
    return "eth0"  # 默认返回eth0

def get_my_ip(interface):
    # 获取指定接口的IP地址
    result = subprocess.run(['ifconfig', interface], capture_output=True, text=True)
    for line in result.stdout.split('\n'):
        if 'inet ' in line:
            return line.split()[1]
    return "127.0.0.1"  # 如果无法获取，返回localhost

def get_my_mac(interface):
    # 获取指定接口的MAC地址
    result = subprocess.run(['ifconfig', interface], capture_output=True, text=True)
    for line in result.stdout.split('\n'):
        if 'ether' in line:
            return line.split()[1]
    return "00:00:00:00:00:00"  # 如果无法获取，返回默认MAC

# 获取网络接口、IP和MAC地址
interface = get_interface()
my_ip = get_my_ip(interface)
my_mac = get_my_mac(interface)

print(f"Using interface: {interface}")
print(f"My IP: {my_ip}")
print(f"My MAC: {my_mac}")

# 设置目标IP(这里我们用网关IP作为示例)
target_ip = conf.route.route("0.0.0.0")[2]

# 创建ARP请求包
arp_request = ARP(pdst=target_ip)
ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether_frame/arp_request

# 发送ARP请求并接收响应
result = srp(packet, timeout=3, verbose=0, iface=interface)[0]

# 解析响应
for sent, received in result:
    print(f"Target IP: {received.psrc}")
    print(f"Target MAC: {received.hwsrc}")

# 监听ARP流量
def arp_monitor_callback(pkt):
    if ARP in pkt and pkt[ARP].op in (1,2): #who-has or is-at
        return f"ARP {ARPOperation(pkt[ARP].op).name} {pkt[ARP].hwsrc} {pkt[ARP].psrc}"

print("\nMonitoring ARP traffic (CTRL+C to stop):")
sniff(prn=arp_monitor_callback, filter="arp", store=0, count=10, iface=interface)