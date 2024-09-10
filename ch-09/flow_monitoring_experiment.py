import subprocess
import time
import matplotlib.pyplot as plt

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode('utf-8')

def plot_results(netflow_packets, netflow_bytes, sflow_packets, sflow_bytes):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    ax1.bar(['Netflow', 'sFlow'], [netflow_packets, sflow_packets])
    ax1.set_title('Total Packets Reported')
    ax1.set_ylabel('Number of Packets')
    
    ax2.bar(['Netflow', 'sFlow'], [netflow_bytes, sflow_bytes])
    ax2.set_title('Total Bytes Reported')
    ax2.set_ylabel('Number of Bytes')
    
    plt.tight_layout()
    plt.savefig('flow_monitoring_comparison.png')
    plt.close()

# Start Netflow collector
print("Starting Netflow collector...")
netflow_collector = subprocess.Popen(["nfcapd", "-p", "9995", "-b", "127.0.0.1", "-T", "all", "-t", "60"])

# Start sFlow collector
print("Starting sFlow collector...")
sflow_collector = subprocess.Popen(["sflowtool", "-p", "6343"], stdout=subprocess.PIPE)

# Generate traffic
print("Generating network traffic...")
run_command("python3 traffic_generator.py")

# Run Netflow simulator
print("Running Netflow simulator...")
netflow_output = run_command("python3 netflow_simulator.py")
netflow_packets = int(netflow_output.split()[-4])
netflow_bytes = int(netflow_output.split()[-2])

# Run sFlow simulator
print("Running sFlow simulator...")
sflow_output = run_command("python3 sflow_simulator.py")
sflow_packets = int(sflow_output.split()[-4])
sflow_bytes = int(sflow_output.split()[-2])

# Stop collectors
netflow_collector.terminate()
sflow_collector.terminate()

# Analyze Netflow data
print("Analyzing Netflow data...")
netflow_analysis = run_command("nfdump -R /var/cache/nfdump -s ip/bytes")
print(netflow_analysis)

# Analyze sFlow data
print("Analyzing sFlow data...")
sflow_analysis = run_command("sflowtool -r /tmp/sflow.pcap")
print(sflow_analysis)

# Plot results
plot_results(netflow_packets, netflow_bytes, sflow_packets, sflow_bytes)
print("Results plotted and saved as 'flow_monitoring_comparison.png'")

print("\nExperiment Summary:")
print(f"Netflow reported {netflow_packets} packets and {netflow_bytes} bytes")
print(f"sFlow reported {sflow_packets} packets and {sflow_bytes} bytes")
print("For detailed analysis, check the Netflow and sFlow analysis outputs above.")