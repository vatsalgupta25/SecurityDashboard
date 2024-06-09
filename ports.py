import nmap
import json
begin = 4990
end = 5010
target = '127.0.0.1'
scanner = nmap.PortScanner()
scan_results = {}
for i in range(begin, end + 1):
    try:
        res = scanner.scan(target, str(i))
        state = res['scan'][target]['tcp'][i]['state']
        scan_results[i] = state
    except KeyError as e:
        scan_results[i] = str(e)
with open('scan_results.json', 'w') as file:
    json.dump(scan_results, file, indent=4)
print("Nmap scan results saved to scan_results.json")