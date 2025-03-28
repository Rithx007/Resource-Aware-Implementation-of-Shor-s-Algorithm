# Resource-Aware-Implementation-of-Shor-s-Algorithm
Shor’s algorithm faces scalability issues due to memory bottlenecks and inefficient classical post-processing in near-term implementations. This work optimizes Shor’s for 34 qubits (can be scaled to higher number of qubits) via GPU acceleration with validated resource profiling.

1.[code](shor34.py)
2.[view results](results 34 qubit.txt)
3.[circuit visualtization](full_circuit.png)
4.[circuit visualization(pdf)](full_circuit.pdf)

## Overview
->Current shor's algorithm implementation faces several issues such as Factoring numbers like 2047 (n=11) demands >30 qubits, overwhelming most simulators. GPU/CPU memory bottlenecks arise during modular exponentiation and QFT steps. GPU/CPU memory bottlenecks arise during modular exponentiation and QFT steps. Classical simulation of large circuits (e.g. 34 qubits) crashes most GPUs/CPUs during modular exponentiation and Quantum Fourier Transform (QFT) steps.  
->This work demonstrates reduced qubit count via in-place arithmetic and register reuse, enabling N=2047 (23×89) on 34 qubits.Memory monitoring to profile GPU/CPU usage is analysed.This code can be customised for any number of qubits given, availability of required memory.

## Installation

To install the required dependencies, run the following command:

```sh
pip install qiskit qiskit-aer-gpu numpy matplotlib psutil pynvml
