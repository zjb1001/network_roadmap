import subprocess
import sys

def run_tcpdump(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, timeout=30)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running tcpdump: {e}", file=sys.stderr)
        return None
    except subprocess.TimeoutExpired:
        print("Command timed out after 30 seconds")
        return None

def monitor_http_traffic(interface):
    command = f"sudo tcpdump -i {interface} port 80 -c 10 -n"
    return run_tcpdump(command)

def capture_specific_ip(interface, ip):
    command = f"sudo tcpdump -i {interface} host {ip} -c 10 -n"
    return run_tcpdump(command)

def analyze_dns_queries(interface):
    command = f"sudo tcpdump -i {interface} udp port 53 -c 10 -n"
    return run_tcpdump(command)

if __name__ == "__main__":
    interface = input("Enter the network interface to capture (e.g., eth0): ")
    
    print("\nMonitoring HTTP traffic:")
    http_traffic = monitor_http_traffic(interface)
    if http_traffic:
        print(http_traffic)
    
    ip = input("\nEnter an IP address to capture packets from: ")
    ip_traffic = capture_specific_ip(interface, ip)
    if ip_traffic:
        print(ip_traffic)
    
    print("\nAnalyzing DNS queries:")
    dns_queries = analyze_dns_queries(interface)
    if dns_queries:
        print(dns_queries)