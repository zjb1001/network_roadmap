# 2. syslog and journald

## Overview of system logging in Linux

System logging is crucial for monitoring and troubleshooting network issues in Linux systems. Two primary logging systems are syslog and journald.

## Configuring and using syslog

syslog is the traditional logging system in Linux. Here's a basic example of how to log a custom message using syslog:

```python
import syslog

def log_message(message):
    syslog.syslog(syslog.LOG_INFO, message)

log_message("Network connection established")
```

Save this script as `syslog_example.py` and run it. The message will be logged to the system log, typically found in `/var/log/syslog` or `/var/log/messages`.

## Introduction to systemd's journald

journald is a more modern logging system that comes with systemd. It provides structured logging and improved querying capabilities.

Here's a Python script that demonstrates how to log messages using journald:

```python
from systemd import journal

def log_to_journal(message):
    journal.send(message)

log_to_journal("Network interface eth0 is down")
```

Save this script as `journald_example.py` and run it. The message will be logged to the systemd journal.

## Analyzing logs for network-related issues

To analyze logs for network-related issues, we can use tools like `grep` for syslog and `journalctl` for journald.

Here's a Python script that demonstrates how to search for network-related log entries:

```python
import subprocess

def search_syslog(keyword):
    command = f"grep '{keyword}' /var/log/syslog"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def search_journal(keyword):
    command = f"journalctl -g '{keyword}'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

# Search for network-related entries in syslog
print("Syslog entries:")
print(search_syslog("network"))

# Search for network-related entries in journald
print("\nJournald entries:")
print(search_journal("network"))
```

Save this script as `log_analysis.py` and run it with sudo privileges:

```bash
sudo python3 log_analysis.py
```

This script will search for the keyword "network" in both syslog and journald, displaying relevant log entries.

To observe the effects:
1. Run the `syslog_example.py` and `journald_example.py` scripts to generate log entries.
2. Then run the `log_analysis.py` script to search for these entries.
3. You should see the custom log messages you created, along with other network-related log entries from your system.

This demonstration shows how you can programmatically interact with system logs to monitor and analyze network-related events on your Linux system.
