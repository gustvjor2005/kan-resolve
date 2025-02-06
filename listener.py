import time
from parse_trace import parse_log

def tail_log(file_path):
    with open(file_path, 'r') as file:
        file.seek(0, 2)  # Move to the end of the file
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1)  # Wait for new data
                continue
            # print(line.strip())
            parse_log(line.strip())


if __name__ == "__main__":
    log_file = r"C:\Users\gustavo.choque\Documents\repo\ms-poc\auth-server\logs\application.json"
    print(f"Watching {log_file} for new log entries...")
    try:
        tail_log(log_file)
    except KeyboardInterrupt:
        print("Stopped monitoring logs.")
