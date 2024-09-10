import subprocess
import time
import matplotlib.pyplot as plt

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode('utf-8')

def plot_results(traditional_count, ebpf_count):
    labels = ['Traditional', 'eBPF']
    counts = [traditional_count, ebpf_count]
    
    plt.bar(labels, counts)
    plt.title('Packet Count Comparison')
    plt.ylabel('Number of Packets')
    plt.savefig('packet_count_comparison.png')
    plt.close()

# Run traditional packet capture
print("Running traditional packet capture...")
run_command("sudo tcpdump -i eth0 -c 100 -w captured_packets.pcap")
traditional_count = int(run_command("tcpdump -r captured_packets.pcap | wc -l"))

# Run eBPF packet capture
print("Running eBPF packet capture...")
ebpf_process = subprocess.Popen(["sudo", "python3", "ebpf_network_observer.py"])
time.sleep(2)  # Give eBPF program time to start

# Generate traffic
print("Generating traffic...")
run_command("python3 traffic_generator.py")

time.sleep(5)  # Wait for eBPF program to process all packets
ebpf_process.terminate()

# Get eBPF packet count
ebpf_output = run_command("sudo cat /sys/kernel/debug/tracing/trace_pipe | grep 'Packets counted' | tail -n 1")
ebpf_count = int(ebpf_output.split(":")[1].strip())

print(f"Traditional packet count: {traditional_count}")
print(f"eBPF packet count: {ebpf_count}")

# Plot results
plot_results(traditional_count, ebpf_count)
print("Results plotted and saved as 'packet_count_comparison.png'")