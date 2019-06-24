import json
import os

u_path = os.getenv("HOMEDRIVE") + '\\' + os.getenv("USERNAME") + '\\' + 'Chrome' + '\\' + 'Local State'
host = os.getenv("COMPUTERNAME")
chrome = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'

if host == "RDSPROD-01":
    print("Right host!_____________________________________________________________")
    with open(u_path, 'r') as f:
        data = f.read()
        d = json.loads(data)
        d["browser"]["enabled_labs_experiments"] = ["expensive-background-timer-throttling@1",
                                                    "stop-non-timers-in-background@1"]
    with open(u_path, 'r+') as f:
        f.write(json.dumps(d))
    os.startfile(chrome)
    print('Starting Google Chrome...')
else:
    print("___________________________________________________________________Wrong host!")
    with open(u_path) as f:
        data = f.read()
        d = json.loads(data)
        d["browser"]["enabled_labs_experiments"] = []
    with open(u_path, 'w') as f:
        f.write(json.dumps(d))
    os.startfile(chrome)
    print('Starting Google Chrome...')
print(u_path)
