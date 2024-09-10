from systemd import journal

def log_to_journal(message):
    journal.send(message)

if __name__ == "__main__":
    log_to_journal("Network interface eth0 is down")
    log_to_journal("Attempting to reconnect to WiFi")
    log_to_journal("Firewall rules updated")
    print("Journal messages have been sent. Use 'journalctl' to view them.")