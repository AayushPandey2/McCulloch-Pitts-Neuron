import numpy as np

class MPNeuron:
    """
    McCulloch-Pitts (M-P) Neuron Model for Binary Classification / Logic Gates.
    Inputs and outputs are binary (0 or 1).
    """

    def __init__(self, weights: list[int], threshold: float):
        """
        Initialize the M-P Neuron with weights and threshold.
        
        :param weights: List of integer weights (positive for excitatory, negative for inhibitory).
        :param threshold: The activation threshold (theta).
        """
        self.weights = np.array(weights)
        self.threshold = threshold

    def predict(self, inputs: list[int]) -> int:
        """
        Calculates the weighted sum Z = sum(w_i * x_i).
        Fires 1 if Z >= threshold, else 0.
        """
        x = np.array(inputs)
        z = np.dot(x, self.weights)
        return 1 if z >= self.threshold else 0


def run_truth_table(gate_name: str, neuron: MPNeuron, num_inputs: int = 2):
    """Utility function to print the truth table for a given logic gate."""
    print(f"=== {gate_name} Gate ===")
    print(f"Weights: {neuron.weights.tolist()} | Threshold (θ): {neuron.threshold}")
    
    # Generate all binary input combinations
    if num_inputs == 1:
        input_combos = [[0], [1]]
        headers = "X1 | Output"
    elif num_inputs == 2:
        input_combos = [[0, 0], [0, 1], [1, 0], [1, 1]]
        headers = "X1 X2 | Output"
    elif num_inputs == 3:
        input_combos = [
            [0,0,0], [0,0,1], [0,1,0], [0,1,1],
            [1,0,0], [1,0,1], [1,1,0], [1,1,1]
        ]
        headers = "X1 X2 X3(Inhibit) | Output"

    print(headers)
    print("-" * len(headers))
    for inp in input_combos:
        out = neuron.predict(inp)
        inp_str = "  ".join(str(val) for val in inp)
        print(f" {inp_str}  |   {out}")
    print("\n")


# ---------------------------------------------------------
# Gate Implementations using M-P Neurons
# ---------------------------------------------------------

if __name__ == "__main__":
    # 1. AND Gate: Requires both inputs to be 1 (w1=1, w2=1, θ=2)
    and_neuron = MPNeuron(weights=[1, 1], threshold=2)
    run_truth_table("AND", and_neuron)

    # 2. OR Gate: Requires at least one input to be 1 (w1=1, w2=1, θ=1)
    or_neuron = MPNeuron(weights=[1, 1], threshold=1)
    run_truth_table("OR", or_neuron)

    # 3. NOT Gate: Single input inverter (w1=-1, θ=0)
    not_neuron = MPNeuron(weights=[-1], threshold=0)
    run_truth_table("NOT", not_neuron, num_inputs=1)

    # 4. NAND Gate: Inverse of AND (w1=-1, w2=-1, θ=-1)
    nand_neuron = MPNeuron(weights=[-1, -1], threshold=-1)
    run_truth_table("NAND", nand_neuron)

    # 5. NOR Gate: Inverse of OR (w1=-1, w2=-1, θ=0)
    nor_neuron = MPNeuron(weights=[-1, -1], threshold=0)
    run_truth_table("NOR", nor_neuron)

    # 6. Inhibitory Gate ( Biological Veto ):
    # X1, X2 excitatory (w=1), X3 strong inhibitor (w=-10), θ=2
    inhibitory_neuron = MPNeuron(weights=[1, 1, -10], threshold=2)
    run_truth_table("Inhibitory AND (Biological Veto)", inhibitory_neuron, num_inputs=3)
