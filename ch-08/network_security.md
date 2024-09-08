# Chapter 8: Network Security

## 8.1 Netfilter and iptables/nftables

Netfilter is a framework within the Linux kernel that allows various networking-related operations to be implemented in the form of customized handlers. iptables and nftables are user-space applications that allow system administrators to configure the kernel's netfilter packet filtering rules.

### 8.1.1 iptables

iptables is the traditional packet filtering system for Linux. It operates based on tables (filter, nat, mangle, raw) and chains (INPUT, OUTPUT, FORWARD).

Example of setting up a basic firewall with iptables:

```bash
# Allow established connections
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Allow SSH
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow HTTP and HTTPS
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Drop all other incoming traffic
iptables -A INPUT -j DROP
```

### 8.1.2 nftables

nftables is the successor to iptables, providing a more efficient and flexible packet classification system.

Example of setting up a basic firewall with nftables:

```bash
# Create a table and chain
nft add table inet filter
nft add chain inet filter input { type filter hook input priority 0 \; }

# Allow established connections
nft add rule inet filter input ct state established,related accept

# Allow SSH
nft add rule inet filter input tcp dport 22 accept

# Allow HTTP and HTTPS
nft add rule inet filter input tcp dport { 80, 443 } accept

# Drop all other incoming traffic
nft add rule inet filter input drop
```

## 8.2 SELinux network controls

Security-Enhanced Linux (SELinux) is a Linux kernel security module that provides a mechanism for supporting access control security policies. SELinux can be used to enforce fine-grained network access controls.

Example of configuring SELinux to allow a custom web server to listen on port 8080:

```bash
# Allow the web server to listen on port 8080
semanage port -a -t http_port_t -p tcp 8080

# Restart the web server
systemctl restart my_custom_webserver
```

## 8.3 VPNs and IPsec

Virtual Private Networks (VPNs) and Internet Protocol Security (IPsec) are critical technologies for securing network communications.

### 8.3.1 Setting up a VPN with OpenVPN

Example of setting up a basic OpenVPN server:

```bash
# Install OpenVPN
apt-get install openvpn

# Generate server certificates and keys
./easyrsa init-pki
./easyrsa build-ca
./easyrsa build-server-full server nopass
./easyrsa gen-dh

# Configure OpenVPN server
cp /usr/share/doc/openvpn/examples/sample-config-files/server.conf /etc/openvpn/

# Start OpenVPN server
systemctl start openvpn@server
```

### 8.3.2 Configuring IPsec

Example of setting up a basic IPsec connection using strongSwan:

```bash
# Install strongSwan
apt-get install strongswan

# Configure IPsec
cat << EOF > /etc/ipsec.conf
conn myconnection
    authby=secret
    left=%defaultroute
    leftid=@host1
    leftsubnet=10.1.0.0/24
    right=203.0.113.1
    rightid=@host2
    rightsubnet=10.2.0.0/24
    auto=start
EOF

# Start IPsec
ipsec start
```

## 8.4 Intrusion Detection/Prevention Systems (IDS/IPS)

Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS) are essential for monitoring network traffic for malicious activities and taking action to prevent attacks.

### 8.4.1 Setting up Snort as an IDS

Example of installing and configuring Snort:

```bash
# Install Snort
apt-get install snort

# Configure Snort
vim /etc/snort/snort.conf

# Start Snort in IDS mode
snort -A console -q -u snort -g snort -c /etc/snort/snort.conf -i eth0
```

### 8.4.2 Using Suricata as an IPS

Example of installing and configuring Suricata:

```bash
# Install Suricata
apt-get install suricata

# Configure Suricata
vim /etc/suricata/suricata.yaml

# Start Suricata in IPS mode
suricata -c /etc/suricata/suricata.yaml -i eth0
```

## Testing and Observing Network Security Implementations

To test and observe the network security implementations described above, you can use various tools and techniques:

1. For iptables/nftables:
   - Use `iptables -L` or `nft list ruleset` to view current firewall rules.
   - Use tools like nmap to scan ports and verify firewall effectiveness.

2. For SELinux:
   - Use `sestatus` to check SELinux status.
   - Use `ausearch -m AVC` to view SELinux access violations.

3. For VPNs and IPsec:
   - Use `ipsec status` or `openvpn --status` to check connection status.
   - Use tools like Wireshark to capture and analyze encrypted traffic.

4. For IDS/IPS:
   - Check log files (e.g., /var/log/snort, /var/log/suricata) for detected threats.
   - Use tools like tcpreplay to replay captured traffic and test detection capabilities.

By implementing and testing these network security measures, you can significantly enhance the security posture of your Linux-based networks.