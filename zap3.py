from zapv2 import ZAPv2
import time
import json

# Define the target URL
target = 'https://sundartechno.com/'

# Initialize ZAP API client
zap = ZAPv2(apikey='s51ncr19l34t9tdd1e2d2ppv8l', proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})

# Dictionary to hold the results
results = {}

# Start spidering the target
print(f'Starting spider on target: {target}')
scan_id = zap.spider.scan(target)
time.sleep(2)

# Monitor the spider status
while int(zap.spider.status(scan_id)) < 100:
    print(f'Spider progress: {zap.spider.status(scan_id)}%')
    time.sleep(2)

print('Spider completed.')
results['spider_status'] = 'completed'

# Start active scanning
print(f'Starting active scan on target: {target}')
scan_id = zap.ascan.scan(target)
while int(zap.ascan.status(scan_id)) < 100:
    print(f'Scan progress: {zap.ascan.status(scan_id)}%')
    time.sleep(5)

print('Scan completed.')
results['scan_status'] = 'completed'

# Print the vulnerabilities found
print('Vulnerabilities found:')
alerts = zap.core.alerts()
for alert in alerts:
    print(alert)

# Store the alerts in the results dictionary
results['alerts'] = alerts

# Write the results to a JSON file
with open('zap_scan_results.json', 'w') as json_file:
    json.dump(results, json_file, indent=4)

print('Results saved to zap_scan_results.json')
