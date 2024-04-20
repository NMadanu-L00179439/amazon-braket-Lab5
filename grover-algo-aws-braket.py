from braket.circuits import Circuit
from braket.aws import AwsDevice
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
    
    circuit = Circuit()
    
    initialize_state(circuit, range(num_qubits))

    num_iterations = int(np.ceil(np.pi/4 * np.sqrt(2**num_qubits)))
    
    for _ in range(num_iterations):
        oracle(circuit, range(num_qubits), target_item)
        
        diffusion_operator(circuit, range(num_qubits))
    
    return circuit

target_item = '100'

num_shots = 4096


device = AwsDevice("arn:aws:braket:::device/quantum-simulator/amazon/sv1")

grover_circuit = grover_algorithm(target_item)

result = device.run(grover_circuit, shots=num_shots).result()

counts = result.measurement_counts
print(counts)

plt.bar(counts.keys(), counts.values(), color=['blue' if key == target_item else 'grey' for key in counts.keys()])
plt.xlabel('State')
plt.ylabel('Counts')
plt.title('Grover Algorithm Result')
plt.show()
