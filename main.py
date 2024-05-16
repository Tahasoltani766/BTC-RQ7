from review_target_system.gpu_model import main_gpu_model
from miner_runer.run_miner import checker_gpu

if __name__ == '__main__':
    gpu_check, name_gpu = main_gpu_model()
    if gpu_check:
        checker_gpu(name_gpu)


