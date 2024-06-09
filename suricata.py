import subprocess
import json

def run_suricata():
    output = {}
    try:
        # Run Suricata command
        result = subprocess.run(
            ["sudo", "suricata", "-c", "/etc/suricata/suricata.yaml", "-i", "eth0"],
            capture_output=True,
            text=True,
            timeout=30
        )
        # Check if Suricata command was successful
        if result.returncode == 0:
            # Store Suricata output
            output['status'] = 'success'
            output['suricata_output'] = result.stdout
            print("Suricata output:")
            print(result.stdout)
        else:
            # Store error message
            output['status'] = 'error'
            output['suricata_output'] = result.stderr
            print("Error running Suricata:")
            print(result.stderr)
    except subprocess.TimeoutExpired:
        print("Suricata command timed out.")
        # Store timeout message
        output['status'] = 'timeout'
        output['suricata_output'] = "Suricata command timed out."

    return output

def read_suricata_logs():
    log_output = []
    try:
        # Open the fast.log file in read mode
        with open("/var/log/suricata/fast.log", "r") as logfile:
            # Read all lines from the file
            lines = logfile.readlines()
            # Collect each line
            for line in lines:
                log_output.append(line.strip())  # Remove newline characters for cleaner output
    except FileNotFoundError:
        log_output.append("Error: fast.log file not found.")
    
    return log_output

if __name__ == "__main__":
    # Run Suricata
    suricata_result = run_suricata()
    
    # Read Suricata logs
    suricata_logs = read_suricata_logs()
    
    # Combine results into a single dictionary
    combined_output = {
        "suricata_result": suricata_result,
        "suricata_logs": suricata_logs
    }
    
    # Write combined output to JSON file
    with open('suricata.json', 'w') as json_file:
        json.dump(combined_output, json_file, indent=4)

    print('Results saved to suricata.json')
