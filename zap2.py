from zapv2 import ZAPv2
import time

# Define the target URL
target = 'https://sundartechno.com/'

# Initialize ZAP API client
zap = ZAPv2(apikey='s51ncr19l34t9tdd1e2d2ppv8l', proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})

# Start spidering the target
print(f'Starting spider on target: {target}')
scan_id = zap.spider.scan(target)
time.sleep(2)

# Monitor the spider status
while int(zap.spider.status(scan_id)) < 100:
    print(f'Spider progress: {zap.spider.status(scan_id)}%')
    time.sleep(2)

print('Spider completed.')

# Start active scanning
print(f'Starting active scan on target: {target}')
scan_id = zap.ascan.scan(target)
while int(zap.ascan.status(scan_id)) < 100:
    print(f'Scan progress: {zap.ascan.status(scan_id)}%')
    time.sleep(5)

print('Scan completed.')

# Print the vulnerabilities found
print('Vulnerabilities found:')
for alert in zap.core.alerts():
    print(alert)
