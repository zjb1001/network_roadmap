import subprocess
import datetime

def search_syslog(keyword, time_range=None):
    command = f"grep '{keyword}' /var/log/syslog"
    if time_range:
        command = f"grep '{keyword}' /var/log/syslog | grep '{time_range}'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def search_journal(keyword, time_range=None):
    command = f"journalctl -g '{keyword}'"
    if time_range:
        command = f"journalctl -g '{keyword}' --since '{time_range}'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

if __name__ == "__main__":
    # Get current timestamp
    now = datetime.datetime.now()
    time_range = now.strftime("%Y-%m-%d %H:%M:%S")

    # Run syslog and journald example scripts
    subprocess.run(["python3", "syslog_example.py"])
    subprocess.run(["python3", "journald_example.py"])

    print("\nSearching for syslog entries:")
    print(search_syslog("Network", time_range))

    print("\nSearching for journal entries:")
    print(search_journal("Network", time_range))