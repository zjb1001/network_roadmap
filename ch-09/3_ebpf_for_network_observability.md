# 3. eBPF for network observability

## Introduction to eBPF (extended Berkeley Packet Filter)

eBPF (extended Berkeley Packet Filter) is a powerful technology in the Linux kernel that allows you to run custom programs in kernel space. It's particularly useful for network observability, performance analysis, and security monitoring.

## eBPF tools for network monitoring

There are several eBPF-based tools available for network monitoring. One popular suite of tools is BCC (BPF Compiler Collection). Let's use a simple BCC tool to demonstrate network monitoring with eBPF.

First, install BCC:

```bash
sudo apt-get install bcc-tools
```

Now, let's use the `tcpconnect` tool to monitor TCP connections:

```bash
sudo /usr/share/bcc/tools/tcpconnect
```

This command will show you real-time TCP connections being established on your system.

## Writing custom eBPF programs for network analysis

While using pre-built tools is convenient, writing custom eBPF programs gives you more flexibility. Here's a simple example of a custom eBPF program that counts packets:

```c
#include <linux/bpf.h>
#include <linux/if_ether.h>
#include <linux/ip.h>
#include <linux/in.h>

BPF_HASH(packet_count, u32, u64);

int packet_counter(struct xdp_md *ctx) {
    void *data_end = (void *)(long)ctx->data_end;
    void *data = (void *)(long)ctx->data;
    struct ethhdr *eth = data;

    if (data + sizeof(*eth) > data_end)
        return XDP_PASS;

    u32 key = 0;
    u64 *count = packet_count.lookup(&key);
    if (count) {
        *count += 1;
    } else {
        u64 init_val = 1;
        packet_count.insert(&key, &init_val);
    }

    return XDP_PASS;
}
```

To use this program, you'll need to compile it with LLVM and load it into the kernel. Here's a Python script that uses the BCC library to compile and load the eBPF program:

```python
from bcc import BPF

# eBPF program code (the C code above)
ebpf_code = """
#include <linux/bpf.h>
#include <linux/if_ether.h>
#include <linux/ip.h>
#include <linux/in.h>

BPF_HASH(packet_count, u32, u64);

int packet_counter(struct xdp_md *ctx) {
    void *data_end = (void *)(long)ctx->data_end;
    void *data = (void *)(long)ctx->data;
    struct ethhdr *eth = data;

    if (data + sizeof(*eth) > data_end)
        return XDP_PASS;

    u32 key = 0;
    u64 *count = packet_count.lookup(&key);
    if (count) {
        *count += 1;
    } else {
        u64 init_val = 1;
        packet_count.insert(&key, &init_val);
    }

    return XDP_PASS;
}
"""

# Load the eBPF program
b = BPF(text=ebpf_code)

# Attach the eBPF program to the network interface
interface = "eth0"  # Change this to your network interface
b.attach_xdp(interface, fn=b.load_func("packet_counter", BPF.XDP))

try:
    print("Counting packets... Press Ctrl+C to stop.")
    while True:
        packet_count = b["packet_count"][0].value
        print(f"Packets counted: {packet_count}")
        b.kprobe_poll()
except KeyboardInterrupt:
    pass

# Clean up
b.remove_xdp(interface)
```

Save this script as `ebpf_packet_counter.py` and run it with sudo privileges:

```bash
sudo python3 ebpf_packet_counter.py
```

## Performance considerations and use cases

eBPF programs run directly in the kernel, providing high-performance monitoring capabilities. Some use cases include:

1. Real-time network traffic analysis
2. Detecting and preventing DDoS attacks
3. Monitoring application performance at the network level
4. Custom protocol analysis

To observe the effects of the eBPF packet counter:
1. Run the `ebpf_packet_counter.py` script.
2. Generate some network traffic (e.g., browse websites, download files).
3. Watch the packet count increase in real-time.
4. Compare the performance impact with traditional packet capture methods like tcpdump.

You'll notice that the eBPF program can count packets with minimal performance overhead, demonstrating its efficiency for network monitoring tasks.
