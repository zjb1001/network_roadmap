import subprocess
from scapy.all import *
from enum import Enum
import inspect

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

def print_with_line_number(*args, **kwargs):
    frame = inspect.currentframe().f_back
    line_number = frame.f_lineno
    print(f"Line {line_number}:", *args, **kwargs)

# 获取网络接口、IP和MAC地址
interface = get_interface()
my_ip = get_my_ip(interface)
my_mac = get_my_mac(interface)

print_with_line_number(f"Using interface: {interface}")
print_with_line_number(f"My IP: {my_ip}")
print_with_line_number(f"My MAC: {my_mac}")

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
    print_with_line_number(f"Target IP: {received.psrc}")
    print_with_line_number(f"Target MAC: {received.hwsrc}")

# 添加非路由节点的ARP请求
non_router_ip = ".".join(my_ip.split(".")[:3] + ["100"])  # 假设 .100 不是路由器
arp_request_non_router = ARP(pdst=non_router_ip)
packet_non_router = ether_frame/arp_request_non_router
result_non_router = srp(packet_non_router, timeout=3, verbose=0, iface=interface)[0]

if result_non_router:
    print_with_line_number("\nNon-router ARP request result:")
    for sent, received in result_non_router:
        print_with_line_number(f"Non-router IP: {received.psrc}")
        print_with_line_number(f"Non-router MAC: {received.hwsrc}")
else:
    print_with_line_number(f"\nNo response from non-router IP: {non_router_ip}")

# 监听ARP流量
def arp_monitor_callback(pkt):
    if ARP in pkt:
        if pkt[ARP].op == 1:  # ARP request
            return f"ARP Request: Who has {pkt[ARP].pdst}? Tell {pkt[ARP].psrc}"
        elif pkt[ARP].op == 2:  # ARP reply
            return f"ARP Reply: {pkt[ARP].psrc} is at {pkt[ARP].hwsrc}"

print_with_line_number("\nMonitoring ARP traffic (CTRL+C to stop):")
sniff(prn=lambda x: print_with_line_number(arp_monitor_callback(x)), filter="arp", store=0, count=10, iface=interface)