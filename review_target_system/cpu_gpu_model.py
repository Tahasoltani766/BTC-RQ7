import GPUtil
import cpuinfo
import multiprocessing

def gpu_detection():
    gpus = GPUtil.getGPUs()
    if gpus:
        for i in range(len(gpus)):
            gpu = gpus[i]
            print("GPU Name:", gpu.name)
    else:
        print("No GPU found.")


def get_cpu_info():
    return cpuinfo.get_cpu_info()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    cpu_model = get_cpu_info()
    gpu_model = gpu_detection()
    print(cpu_model, gpu_model)