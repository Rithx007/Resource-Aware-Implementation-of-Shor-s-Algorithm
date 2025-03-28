#Full view circuit
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.circuit.library import QFT
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
from math import gcd, ceil, log2
from fractions import Fraction
import matplotlib.pyplot as plt
import numpy as np
import time

# Add memory monitoring
try:
    import pynvml
    HAS_NVML = True
except ImportError:
    HAS_NVML = False

try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False

def get_gpu_memory():
    """Get current GPU memory usage in MB"""
    if not HAS_NVML:
        return 0
    pynvml.nvmlInit()
    handle = pynvml.nvmlDeviceGetHandleByIndex(0)
    info = pynvml.nvmlDeviceGetMemoryInfo(handle)
    return info.used / 1024**2

def get_cpu_memory():
    """Get current process memory usage in MB"""
    if not HAS_PSUTIL:
        return 0
    process = psutil.Process()
    return process.memory_info().rss / 1024**2

def validate_input(N):
    """34-qubit optimized validation"""
    n = ceil(log2(N))
    if 3 * n > 34:
        raise ValueError(f"Requires {3*n} qubits (max 34)")
    return n

def Binary(j, size):
    """LSB-first binary conversion"""
    return [int(b) for b in bin(j)[2:].zfill(size)[-size:]][::-1]

def controlled_modular_mult(qc, control, target, a, N):
    """34-qubit optimized multiplication"""
    n = len(target)
    for q in range(n):
        angle = (a**(2**q)) % N
        qc.cp(2 * np.pi * angle / N, control, target[q])

def shors_algorithm(N, a):
    """34-qubit circuit visualization with size handling"""
    n = validate_input(N)
    m = 2 * n
    
    qr_period = QuantumRegister(m, 'period')
    qr_value = QuantumRegister(n, 'value')
    cr = ClassicalRegister(m, 'c')
    
    qc = QuantumCircuit(qr_period, qr_value, cr)
    
    # Initialize
    qc.h(qr_period)
    qc.x(qr_value[0])
    
    # Modular exponentiation
    for ctrl in range(m):
        a_pow = pow(a, 2**ctrl, N)
        controlled_modular_mult(qc, qr_period[ctrl], qr_value, a_pow, N)
    
    qc.append(QFT(m, inverse=True), qr_period)
    qc.measure(qr_period, cr)
    
    print("\n Full Circuit Diagram:")
    
    try:
        plt.figure(figsize=(50, qc.num_qubits*0.5))
        pdf_fig = qc.draw('mpl',
                         fold=-1,
                         scale=0.6,
                         cregbundle=True)
        pdf_fig.savefig('full_circuit.pdf', 
                       format='pdf', 
                       bbox_inches='tight',
                       dpi=300)
        print("- PDF version saved: full_circuit.pdf")
    except Exception as e:
        print(f"PDF generation failed: {str(e)}")
    return qc


def run_shor(N, a, shots=1000):
    """34-qubit execution with memory monitoring"""
    # Memory tracking setup
    max_gpu_mem = 0
    max_cpu_mem = 0
    
    if HAS_NVML:
        pynvml.nvmlInit()
    
    simulator = AerSimulator(
        method='statevector',
        device='GPU',
        blocking_enable=True,
        blocking_qubits=31,
        precision='single'
    )
    
    circuit = shors_algorithm(N, a)
    transpiled = transpile(circuit, simulator)
    
    # Start memory monitoring
    def update_max_memory():
        nonlocal max_gpu_mem, max_cpu_mem
        max_gpu_mem = max(max_gpu_mem, get_gpu_memory())
        max_cpu_mem = max(max_cpu_mem, get_cpu_memory())
    
    print(f"\n Quantum Resources:")
    print(f" - Total qubits: {circuit.num_qubits}/34")
    print(f" - Circuit depth: {transpiled.depth()}")
    print(f" - Operations: {transpiled.count_ops()}")
    
    # Execute with memory tracking
    start_time = time.time()
    job = simulator.run(transpiled, shots=shots)
    result = job.result()
    counts = result.get_counts()
    
    # Get final memory measurements
    update_max_memory()
    
    # Memory report
    print("\n Memory Usage:")
    if HAS_NVML:
        print(f" - Peak GPU Memory: {max_gpu_mem:.2f} MB")
    else:
        print(" - GPU monitoring not available (install pynvml)")
    
    if HAS_PSUTIL:
        print(f" - Peak CPU Memory: {max_cpu_mem:.2f} MB")
    else:
        print(" - CPU monitoring not available (install psutil)")
    
    print(f"\n Execution time: {time.time() - start_time:.2f}s")
    return counts

def process_results(N, a, counts):
    """34-qubit result processing"""
    factors = set()
    for outcome in counts:
        phase = int(outcome, 2)/(2**len(outcome))
        frac = Fraction(phase).limit_denominator(N)
        r = frac.denominator
        
        if pow(a, r, N) == 1 and r%2 == 0:
            x = pow(a, r//2, N)
            factors.update([gcd(x+1, N), gcd(x-1, N)])
    
    return {f for f in factors if 1<f<N}

if __name__ == "__main__":
    N = 2047
    a = 5  # Correct choice with even period
    
    try:
        print(f" 34-Qubit Shor's Algorithm for N={N} (23×89)")
        counts = run_shor(N, a)
        
        factors = process_results(N, a, counts)
        print(f"\n Factors of {N}: {factors or 'None found'}")
        
    except Exception as e:
        print(f" Error: {str(e)}")
