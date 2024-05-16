
def checker_gpu(gpus):
    for i in range(len(gpus)):
        gpu = gpus[i]
        gpu_name = gpu.name
        if 'NVIDIA' in gpu_name:
            print('nvidia')
        elif 'AMD' in gpu_name:
            print('AMD')
