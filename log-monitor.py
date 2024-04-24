import logging
import time

# Initialize logging
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Function to monitor log file
def monitor_log_file():
    with open('app.log', 'r') as file:
        file.seek(0, 2)  # Go to the end of the file
        while True:
            line = file.readline()
            if line:
                print(line.strip())  # Display new log entry
                analyze_log_entry(line.strip())  # Analyze log entry
            else:
                time.sleep(0.1)  # Wait for new log entry

# Function to analyze log entry
def analyze_log_entry(entry):
    if 'INFO' in entry:
        logging.info('Log entry analyzed: {}'.format(entry))
    elif 'DEBUG' in entry:
        logging.debug('Log entry analyzed: {}'.format(entry))
    elif 'ERROR' in entry:
        logging.error('Log entry analyzed: {}'.format(entry))

# Main function
def main():
    try:
        print('Monitoring log file...')
        monitor_log_file()
    except KeyboardInterrupt:
        print('Monitoring stopped by user.')

if __name__ == '__main__':
    main()
