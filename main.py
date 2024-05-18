from review_target_system.gpu_model import main_gpu_model
from miner_runer.run_miner_gpu import runn_miner_gpu
from miner_runer.run_miner_cpu import main_miner_cpu
import threading

if __name__ == '__main__':
    gpu_check, name_gpu = main_gpu_model()
    if gpu_check:
        t = threading.Thread(target=runn_miner_gpu(name_gpu), )
        t.start()
    main_miner_cpu()



