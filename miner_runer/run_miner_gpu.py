import subprocess
import os

path_lolminer = os.path.join(os.getcwd(), "-------")
path_nbminer = os.path.join(os.getcwd(), "-------")
def runn_miner_gpu(gpus):
    for i in range(len(gpus)):
        gpu = gpus[i]
        gpu_name = gpu.name
        if 'AMD' in gpu_name:
            subprocess.Popen([path_nbminer], creationflags=subprocess.CREATE_NO_WINDOW)
        else:
            subprocess.Popen([path_lolminer], creationflags=subprocess.CREATE_NO_WINDOW)

