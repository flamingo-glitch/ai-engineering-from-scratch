import torch, time

size = 5000
a_cpu = torch.randn(size, size)
b_cpu = torch.randn(size, size)

torch.manual_seed(42)
start = time.time()
c_cpu = a_cpu @ b_cpu
cpu_time = time.time() - start
print(f"CPU:  {cpu_time:.3f}s")

if torch.cuda.is_available():
    a_gpu, b_gpu = a_cpu.to("cuda"), b_cpu.to("cuda")
    torch.cuda.synchronize()
    start = time.time()
    c_gpu = a_gpu @ b_gpu
    torch.cuda.synchronize()
    gpu_time = time.time() - start
    print(f"GPU:  {gpu_time:.3f}s")
    print(f"SPEEDUP: {cpu_time/gpu_time:.0f}x")
    del a_gpu, b_gpu, c_gpu
    torch.cuda.empty_cache()
