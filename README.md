Log Analysis and Monitoring Script

Overview

This script provides basic log file monitoring and analysis functionalities. It continuously monitors a specified log file for new entries, displays new log entries in real-time, and performs basic log analysis by counting occurrences of specific keywords (INFO, DEBUG, ERROR) and generating summary reports.

Features

Log File Monitoring: Continuously monitors a specified log file for new entries using tail-like functionality.

Log Analysis: Performs basic analysis on log entries to count occurrences of specific keywords (INFO, DEBUG, ERROR) and generates summary reports.

Requirements

Python 3.x

An empty app.log file in the same directory as the script

Usage

Clone the repository:

git clone https://github.com/your-username/log-monitor.git

Navigate to the project directory:

cd log-monitor

Run the script:

python log-monitor.py

To stop the monitoring loop, press Ctrl+C.

Example

After running the script, you can manually add new log entries to the app.log file to test the monitoring and analysis functionalities.

echo "INFO - Sample INFO message" >> app.log

echo "DEBUG - Sample DEBUG message" >> app.log

echo "ERROR - Sample ERROR message" >> app.log
