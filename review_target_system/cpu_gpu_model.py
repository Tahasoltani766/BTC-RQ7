# GPU Name: NVIDIA GeForce RTX 3050 Laptop GPU
# {'python_version': '3.11.9.final.0 (64 bit)', 'cpuinfo_version': [9, 0, 0], 'cpuinfo_version_string': '9.0.0', 'arch': 'X86_64', 'bits': 64, 'count': 12, 'arch_string_raw': 'AMD64', 'vendor_id_raw': 'AuthenticAMD', 'brand_raw': 'AMD Ryzen 5 6600H with Radeon Graphics', 'hz_actual_friendly': '3.3010 GHz', 'hz_actual': [3301000000, 0], 'l2_cache_size': 3145728, 'stepping': 1, 'model': 68, 'family': 25, 'l3_cache_size': 16777216, 'hz_advertised_friendly': '3.2940 GHz', 'hz_advertised': [3294000000, 0], 'flags': ['3dnow', '3dnowext', '3dnowprefetch', 'abm', 'adx', 'aes', 'apic', 'avx', 'avx2', 'bmi1', 'bmi2', 'clflush', 'clflushopt', 'clwb', 'cmov', 'cmp_legacy', 'cr8_legacy', 'cx16', 'cx8', 'de', 'dts', 'erms', 'f16c', 'fma', 'fpu', 'fxsr', 'ht', 'hypervisor', 'ia64', 'invpcid', 'lahf_lm', 'mca', 'mce', 'misalignsse', 'mmx', 'monitor', 'movbe', 'msr', 'mtrr', 'osvw', 'osxsave', 'pae', 'pat', 'pclmulqdq', 'perfctr_core', 'pge', 'pni', 'popcnt', 'pqe', 'pqm', 'pse', 'pse36', 'rdpid', 'rdrnd', 'rdseed', 'sep', 'sepamd', 'serial', 'sha', 'smap', 'smep', 'ss', 'sse', 'sse2', 'sse4_1', 'sse4_2', 'sse4a', 'ssse3', 'tm', 'topoext', 'tsc', 'umip', 'vaes', 'vme', 'vpclmulqdq', 'wdt', 'xsave'], 'l2_cache_line_size': 512, 'l2_cache_associativity': 6} None

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