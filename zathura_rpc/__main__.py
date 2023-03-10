from pypresence import Presence

import time
import subprocess
import os
import re

start = int(time.time())
client_id = "1081997908985008138"
RPC = Presence(client_id)
RPC.connect()

def __start__():
    while True:
        try:
            pid = subprocess.check_output(['pidof', 'zathura']).decode().strip()
        except subprocess.CalledProcessError:
            exit(1)

        output = subprocess.check_output(['gdbus', 'introspect', '--session', '--dest', f'org.pwmt.zathura.PID-{pid}', '--object-path', '/org/pwmt/zathura', '-p']).decode()

        filename = re.findall(r"filename = '([^']*)'", output)[0]
        lineno = re.findall(r"pagenumber = ([0-9]*)", output)[0]
        totalln = re.findall(r"numberofpages = ([0-9]*)", output)[0]

        filename = os.path.basename(filename.split(' - ')[0])
        line_info = (f"Page {lineno} of {totalln}")

        RPC.update(
            large_image = "zathura",
            large_text = "checkmate adobe plebs",
            small_image = "weeb",
            small_text = "yes, im a weeb",
            start = start,
            details = filename,
            state = line_info,
        )
        time.sleep(15)

if __name__ == "__main__":
    __start__()
