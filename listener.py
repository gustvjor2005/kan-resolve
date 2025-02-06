import time
from parse_trace import parse_log
from argparse import ArgumentParser

def main(arg):
    path = arg.p
    print(f"path is {path}")

    try:
        tail_log(path)
    except KeyboardInterrupt:
        print("Stopped monitoring logs.")

    

def tail_log(file_path):
    with open(file_path, 'r') as file:
        file.seek(0, 2)  # Move to the end of the file
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1)  # Wait for new data
                continue
            parse_log(line.strip())


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-p", dest="p", type=str)
    options = parser.parse_args()
    print("OPTIONS", options)
    main(options)
    #log_file = r"C:\Users\s381201\Documents\repo\aepe-data-model-synchronizer\logs\application.json"    
    #print(f"Watching {log_file} for new log entries...")
