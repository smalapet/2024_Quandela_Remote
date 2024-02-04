# Author Sivarat Malapet
# https://www.linkedin.com/in/sivaratmalapet

from perceval.components import catalog
from perceval.converters import QiskitConverter, MyQLMConverter
from perceval.algorithm import Analyzer, Sampler
from qiskit.quantum_info import Statevector
from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram

import numpy as np
import perceval as pcvl

def ccz_gate(circuit, ctrl1, ctrl2, target):

    # 1. Apply Hadamard gate on target qubit
    circuit.h(target)

    # ******************************************************************** #

    # 2. Apply Hadamard gate on target qubit
    circuit.h(target)
    
    # 3. Apply CNOT gate with ctrl1 as control and target as target
    circuit.cx(ctrl1, target)
    
    # 4. Apply TDG gate on target qubit
    circuit.tdg(target)
    
    # 5. Apply CNOT gate with ctrl2 as control and target as target
    circuit.cx(ctrl2, target)
    
    # 6. Apply T gate on target qubit
    circuit.t(target)
    
    # 7. Apply CNOT gate with ctrl1 as control and target as target
    circuit.cx(ctrl1, target)
    
    # 8. Apply T gate on ctrl2
    circuit.t(ctrl2)
    
    # 9. Apply CNOT gate with ctrl2 as control and target as target
    circuit.cx(ctrl2, target)
    
    # 10. Apply T gate on target qubit
    circuit.t(target)
    
    # 11. Apply CNOT gate with ctrl1 as control and target as target
    circuit.cx(ctrl1, target)
    
    # 12. Apply T gate on ctrl1
    circuit.t(ctrl1)
    
    # 13. Apply Hadamard gate on target qubit
    circuit.h(target)

    # ******************************************************************** #
    
    # 14. Apply Hadamard gate on target qubit
    circuit.h(target)

def get_CCZ() -> pcvl.Processor:

    # *********************************** #
    # 1. CCZ circuit
    # *********************************** #
    
    # Create a quantum circuit with three qubits
    qc = QuantumCircuit(3)

    # Apply CCNOT gate
    ccz_gate(qc, 0, 1, 2)

    # Visualize the circuit
    print(qc)

    # Simulate the circuit
    simulator = Aer.get_backend('statevector_simulator')
    compiled_circuit = transpile(qc, simulator)
    result = execute(compiled_circuit, simulator).result()
    statevector = result.get_statevector()

    # Print the final statevector
    print("Final Statevector:", statevector)

    # Plot the probability amplitudes
    plot_histogram(result.get_counts())

    # *********************************** #
    # 2. Circuit converter
    # *********************************** #
    qiskit_converter = QiskitConverter(catalog, backend_name="Naive")
    qiskit_converter = QiskitConverter(catalog, backend_name="SLOS")
    # qiskit_converter = QiskitConverter(catalog, backend_name="CliffordClifford2017")
    quantum_processor = qiskit_converter.convert(qc, use_postselection=True)
    pcvl.pdisplay(quantum_processor, recursive=True)

    return quantum_processor
    # return pcvl.catalog["postprocessed ccz"].build_processor()

if __name__ == "__main__":
    get_CCZ()

