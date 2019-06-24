import json


def set_flags(username):
    """Устанавливает нужные флаги в файле Local State"""
    u_path = "\\" + "\\" + "milandr01.local" + "\\" + "Home" + username + "\\" + "Chrome" + "\\" + "Local State"

    with open(u_path, 'r') as f:
        data = f.read()
        d = json.loads(data)
        d["browser"]["enabled_labs_experiments"] = ["expensive-background-timer-throttling@1",
                                                    "stop-non-timers-in-background@1"]
    with open(u_path, 'r+') as f:
        f.write(json.dumps(d))
    print('Done')
