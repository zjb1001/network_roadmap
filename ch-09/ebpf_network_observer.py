from bcc import BPF
import time

# eBPF program code
bpf_code = """
#include <uapi/linux/ptrace.h>
#include <net/sock.h>
#include <bcc/proto.h>

BPF_HASH(packet_count, u32, u64);

int count_packets(struct __sk_buff *skb) {
    u32 key = 0;
    u64 *count, init_val = 1;

    count = packet_count.lookup_or_init(&key, &init_val);
    (*count)++;

    return 0;
}
"""

# Load the eBPF program
b = BPF(text=bpf_code)

# Attach the eBPF program to the network interface
interface = "eth0"  # Change this to your network interface
b.attach_xdp(interface, fn=b.load_func("count_packets", BPF.XDP))

print(f"eBPF program attached to {interface}. Counting packets...")

# Print packet count every second
try:
    while True:
        packet_count = b["packet_count"][0].value
        print(f"Packets counted: {packet_count}")
        time.sleep(1)
except KeyboardInterrupt:
    pass

# Clean up
b.remove_xdp(interface)
print("eBPF program detached. Exiting.")