# McCulloch-Pitts (M-P) Neuron Model

A comprehensive guide and reference implementation for modeling fundamental logic gates using the **McCulloch-Pitts (M-P) Neuron**, the earliest mathematical abstraction of a biological neuron proposed by Warren McCulloch and Walter Pitts in 1943.

## 🧠 Overview of the M-P Neuron

The McCulloch-Pitts neuron receives a set of binary inputs ($X_i \in \{0, 1\}$), multiplies them by specified weights ($w_i$), and sums them together. If the calculated weighted sum meets or exceeds a predefined threshold ($\theta$), the neuron fires (outputs $1$); otherwise, it remains inactive (outputs $0$).

### Mathematical Formulation

1. **Weighted Sum (**$Z$**):**

$$
Z = \sum_{i=1}^{n} w_i X_i
$$

2. **Activation Function (**$Y$**):**

$$
Y = f(Z) = \begin{cases} 1 & \text{if } Z \ge \theta \\ 0 & \text{if } Z < \theta \end{cases}
$$

## ⚡ Excitatory vs. Inhibitory Signals

Biological neurons rely on a balance of stimulation and inhibition to perform selective computation:

* **Excitatory Weights (**$w > 0$**):** Add to the sum $Z$, encouraging the neuron to cross the threshold and fire.

* **Inhibitory Weights (**$w \ll 0$**):** Act as a **biological veto** (or kill-switch). A sufficiently large negative weight forces $Z$ below the threshold regardless of how many excitatory inputs are active.

## ⚙️ Logic Gate Configurations

The table below summarizes the weight ($w$) and threshold ($\theta$) parameters required to represent standard logic gates using a single M-P neuron:

| Logic Gate | Inputs ($X$) | Weights ($w$) | Threshold ($\theta$) | Behavior / Notes | 
| ----- | ----- | ----- | ----- | ----- | 
| **AND** | $[X_1, X_2]$ | $[1, 1]$ | $\theta = 2$ | Fires only when all inputs are $1$. | 
| **OR** | $[X_1, X_2]$ | $[1, 1]$ | $\theta = 1$ | Fires if at least one input is $1$. | 
| **NOT** | $[X_1]$ | $[-1]$ | $\theta = 0$ | Inverts single input ($0 \to 1, 1 \to 0$). | 
| **NAND** | $[X_1, X_2]$ | $[-1, -1]$ | $\theta = -1$ | Negation of AND logic. | 
| **NOR** | $[X_1, X_2]$ | $[-1, -1]$ | $\theta = 0$ | Negation of OR logic. | 
| **AND-NOT (Veto)** | $[X_1, X_2]$ | $[1, -2]$ | $\theta = 1$ | Fires if $X_1 = 1$, unless vetoed by $X_2 = 1$. | 

## ⚠️ Limitations

Single-layer McCulloch-Pitts neurons can only represent **linearly separable** functions. They cannot compute non-linearly separable logic gates such as **XOR** or **XNOR** using a single threshold unit. Solving XOR requires a multi-layer network architecture (combining AND, OR, and NOT gates).

## 📄 License

This repository is licensed under the MIT License.
