import syslog

def log_message(message):
    syslog.syslog(syslog.LOG_INFO, message)

if __name__ == "__main__":
    log_message("Network connection established")
    log_message("DHCP request sent")
    log_message("IP address assigned: 192.168.1.100")
    print("Syslog messages have been sent. Check /var/log/syslog or /var/log/messages.")