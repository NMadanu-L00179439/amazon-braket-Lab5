from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt

def initialize_state(circuit, qubits):
    for qubit in qubits:
        circuit.h(qubit)

def oracle(circuit, qubits, target_item):
    for index, item in enumerate(target_item):
        if item == '1':
            circuit.x(qubits[index])
    
    circuit.cz(qubits[0], qubits[2])
    
    for index, item in enumerate(target_item):
        if item == '1':
            circuit.x(qubits[index])

def diffusion_operator(circuit, qubits):
    for qubit in qubits:
        circuit.h(qubit)
    for qubit in qubits:
        circuit.x(qubit)
    
    circuit.h(qubits[2])
    circuit.cz(qubits[0], qubits[2])
    circuit.h(qubits[2])
    
    for qubit in qubits:
        circuit.x(qubit)
    
    for qubit in qubits:
        circuit.h(qubit)

def grover_algorithm(target_item):
    num_qubits = len(target_item)
    
    num_classical_bits = len(target_item)
    
    circuit = QuantumCircuit(num_qubits, num_classical_bits)
    
    initialize_state(circuit, range(num_qubits))
    
    num_iterations = int(np.ceil(np.pi/4 * np.sqrt(2**num_qubits)))
    
    for _ in range(num_iterations):
        oracle(circuit, range(num_qubits), target_item)
        
        diffusion_operator(circuit, range(num_qubits))
    circuit.measure(range(num_qubits), range(num_classical_bits))
    
    return circuit

target_item = '100'
grover_circuit = grover_algorithm(target_item)


simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(grover_circuit, simulator)
qobj = assemble(compiled_circuit)
result = simulator.run(qobj).result()

counts = result.get_counts()
print(counts)

plt.bar(counts.keys(), counts.values())
plt.xlabel('State')
plt.ylabel('Counts')
plt.title('Grover Algorithm Result')
plt.show()
