import GPUtil
import platform


def gpu_detection():
    gpus = GPUtil.getGPUs()
    if gpus:
        for i in range(len(gpus)):
            gpu = gpus[i]
            print("GPU Name:", gpu.name)
    else:
        print("No GPU found.")

def get_cpu_info():
    try:
        # Fetching CPU information using the platform module
        system_info = platform.uname()
        cpu_model = system_info.processor
        return cpu_model
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    cpu_model = get_cpu_info()
    gpu_model = gpu_detection()
    print(cpu_model, gpu_model)
