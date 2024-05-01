import GPUtil
import cpuinfo
import multiprocessing
# OUT PUT :
# NVIDIA GeForce RTX 3050 Laptop GPU

def gpu_detection():
    gpus = GPUtil.getGPUs()
    if gpus:
        for i in range(len(gpus)):
            gpu = gpus[i]
            print(gpu.name)
    else:
        print("No GPU found.")


if __name__ == "__main__":
    multiprocessing.freeze_support()
    gpu_model = gpu_detection()
    print(gpu_model)