from gen_helpers import topic

parts = []

# ============================================================
# CHAPTER 6 — DEEP FEEDFORWARD NETWORKS
# PART 2
# ============================================================

# 4. Architecture Design
parts.append(topic('t-architecture-design', '4. Architecture Design', 'H', f'''
<div class="definition">
<strong>Definition:</strong> Architecture design is the process of deciding how the layers,
hidden units, connections, activation functions, and overall structure of a deep neural
network should be arranged for a particular learning problem.
</div>

<h3>Why Architecture Matters</h3>
<p>
The architecture determines what kinds of functions the network can represent and how
effectively it can learn them. A suitable architecture provides enough capacity to model
the problem without making training unnecessarily difficult.
</p>

<h3>Main Design Decisions</h3>
<ul>
<li><strong>Number of layers:</strong> Determines the depth of the network.</li>
<li><strong>Number of hidden units:</strong> Determines the capacity of individual layers.</li>
<li><strong>Connectivity:</strong> Determines how units in different layers communicate.</li>
<li><strong>Activation functions:</strong> Introduce non-linearity into the network.</li>
<li><strong>Output layer:</strong> Depends on the type of prediction required.</li>
</ul>

<h3>Depth vs Width</h3>
<p>
A network can become more expressive by increasing either its depth or its width.
Depth allows the network to build hierarchical representations, where early layers
can learn simpler features and later layers can combine them into more complex features.
</p>

<div class="formula">
<strong>General feedforward computation:</strong><br>
h<sup>(l)</sup> = f(W<sup>(l)</sup>h<sup>(l-1)</sup> + b<sup>(l)</sup>)
</div>

<h3>Typical Architecture</h3>
<div class="diagram">
Input Layer → Hidden Layer 1 → Hidden Layer 2 → ... → Output Layer
</div>

<h3>Important Considerations</h3>
<ul>
<li>Choose sufficient capacity for the complexity of the problem.</li>
<li>Avoid unnecessarily large networks.</li>
<li>Consider computational cost and training difficulty.</li>
<li>Choose activation functions appropriate for the network.</li>
<li>The output layer should match the learning objective.</li>
</ul>

<div class="exam">
<strong>Exam Focus:</strong> Explain architecture design in deep feedforward networks.
Discuss depth, width, hidden layers, hidden units, connectivity, and activation functions.
</div>

<h3>Possible Exam Questions</h3>
<ul>
<li>(5M) Explain the important decisions involved in neural network architecture design.</li>
<li>(10M) Discuss depth and width of deep feedforward networks.</li>
<li>(10M) Explain the architecture of a typical deep feedforward neural network with a diagram.</li>
</ul>
'''))

# 5. Back-Propagation
parts.append(topic('t-backprop', '5. Back-Propagation', 'VH', f'''
<div class="definition">
<strong>Definition:</strong> Back-propagation is an algorithm for efficiently computing
the gradients of a neural network's loss function with respect to its parameters by
propagating error information backward through the network using the chain rule.
</div>

<h3>Purpose</h3>
<p>
The main purpose of back-propagation is to calculate the derivatives required by
gradient-based optimization methods such as gradient descent.
</p>

<h3>Basic Idea</h3>
<p>
Training generally consists of two major stages:
</p>

<ol>
<li><strong>Forward propagation:</strong> Input is passed through the network to produce an output.</li>
<li><strong>Backward propagation:</strong> The loss is propagated backward to calculate gradients.</li>
</ol>

<div class="diagram">
Input → Forward Pass → Prediction → Loss
                         ↓
                  Backward Pass
                         ↓
                   Gradients
                         ↓
                  Update Weights
</div>

<h3>Chain Rule</h3>
<p>
Back-propagation relies heavily on the chain rule of differentiation. If a variable
depends on another variable, which in turn depends on another variable, their derivatives
can be multiplied along the computational path.
</p>

<div class="formula">
For y = f(g(x)):<br>
dy/dx = (dy/dg)(dg/dx)
</div>

<h3>Forward Computation</h3>
<div class="formula">
z<sup>(l)</sup> = W<sup>(l)</sup>a<sup>(l-1)</sup> + b<sup>(l)</sup>
<br>
a<sup>(l)</sup> = f(z<sup>(l)</sup>)
</div>

<p>
Here, W is the weight matrix, b is the bias vector, f is the activation function,
and a is the activation of a layer.
</p>

<h3>Backward Computation</h3>
<p>
Starting from the output loss, gradients are calculated layer by layer in the reverse
direction.
</p>

<div class="formula">
δ<sup>(l)</sup> =
(W<sup>(l+1)</sup>)<sup>T</sup>δ<sup>(l+1)</sup>
⊙ f'(z<sup>(l)</sup>)
</div>

<p>
The resulting error signal can then be used to calculate gradients with respect to
weights and biases.
</p>

<div class="formula">
∂L/∂W<sup>(l)</sup> = δ<sup>(l)</sup>(a<sup>(l-1)</sup>)<sup>T</sup>
</div>

<div class="formula">
∂L/∂b<sup>(l)</sup> = δ<sup>(l)</sup>
</div>

<h3>Weight Update</h3>
<div class="formula">
W ← W − η ∂L/∂W
</div>

<p>
where η is the learning rate.
</p>

<h3>Back-Propagation Algorithm</h3>
<ol>
<li>Initialize network parameters.</li>
<li>Perform forward propagation.</li>
<li>Calculate the loss.</li>
<li>Calculate the output-layer error.</li>
<li>Propagate the error backward through hidden layers.</li>
<li>Calculate gradients for weights and biases.</li>
<li>Update parameters using an optimization algorithm.</li>
<li>Repeat until the desired stopping condition is reached.</li>
</ol>

<h3>Advantages</h3>
<ul>
<li>Efficiently computes gradients in multilayer networks.</li>
<li>Uses the chain rule systematically.</li>
<li>Works with gradient-based optimization.</li>
<li>Can be applied to networks containing many parameters.</li>
</ul>

<h3>Limitations / Challenges</h3>
<ul>
<li>Training can become difficult when gradients become extremely small or large.</li>
<li>Performance depends on architecture, initialization, activation functions, and optimization.</li>
<li>Large networks can require substantial computational resources.</li>
</ul>

<div class="exam">
<strong>Very High Exam Priority:</strong>
Be prepared to explain the complete forward pass, backward pass, chain rule,
gradient calculation, and weight update with a neat diagram.
</div>

<h3>Possible Exam Questions</h3>
<ul>
<li>(5M) Define back-propagation and explain its purpose.</li>
<li>(10M) Explain the back-propagation algorithm with a suitable diagram.</li>
<li>(10M) Derive the back-propagation equations using the chain rule.</li>
<li>(15M) Explain forward propagation and backward propagation and derive the gradient update process.</li>
</ul>
'''))

# 6. Other Differentiation Algorithms
parts.append(topic('t-differentiation', '6. Other Differentiation Algorithms', 'H', f'''
<div class="definition">
<strong>Definition:</strong> Differentiation algorithms are computational methods used
to calculate derivatives or gradients of functions. Neural-network training requires
efficient calculation of derivatives of the loss with respect to model parameters.
</div>

<h3>Why Differentiation Algorithms Are Needed</h3>
<p>
Deep learning models contain many layers and parameters. Computing derivatives manually
for every parameter would be inefficient. Automatic differentiation techniques provide
systematic ways to calculate these derivatives.
</p>

<h3>Major Approaches</h3>

<h4>1. Symbolic Differentiation</h4>
<p>
Symbolic differentiation manipulates mathematical expressions to produce another
expression representing their derivative.
</p>

<p><strong>Advantage:</strong> Produces an explicit derivative expression.</p>
<p><strong>Limitation:</strong> Expressions can become very large and complicated.</p>

<h4>2. Numerical Differentiation</h4>
<p>
Numerical differentiation approximates derivatives using function evaluations.
A common approximation is the finite-difference method.
</p>

<div class="formula">
f'(x) ≈ [f(x + ε) − f(x)] / ε
</div>

<p>
Numerical differentiation is useful for checking gradients, but it is generally
not the preferred method for training large neural networks.
</p>

<h4>3. Automatic Differentiation</h4>
<p>
Automatic differentiation decomposes a computation into elementary operations and
applies the chain rule systematically to calculate derivatives.
</p>

<h3>Forward-Mode Differentiation</h3>
<p>
Forward-mode differentiation propagates derivative information in the same direction
as the computational graph: from inputs toward outputs.
</p>

<div class="diagram">
Input → Operation 1 → Operation 2 → Operation 3 → Output
  ↓          ↓             ↓             ↓
Derivative information propagated forward
</div>

<h3>Reverse-Mode Differentiation</h3>
<p>
Reverse-mode differentiation propagates derivative information from outputs back toward
inputs. Back-propagation is an important application of reverse-mode automatic
differentiation.
</p>

<div class="diagram">
Input ← Operation 1 ← Operation 2 ← Operation 3 ← Output
  ↑          ↑             ↑             ↑
Gradient information propagated backward
</div>

<h3>Comparison</h3>

<table>
<tr>
<th>Method</th>
<th>Main Idea</th>
<th>Typical Use</th>
</tr>
<tr>
<td>Symbolic</td>
<td>Manipulates mathematical expressions</td>
<td>Deriving formulas</td>
</tr>
<tr>
<td>Numerical</td>
<td>Approximates derivatives</td>
<td>Gradient checking</td>
</tr>
<tr>
<td>Forward-mode</td>
<td>Propagates derivatives forward</td>
<td>Functions with relatively few inputs</td>
</tr>
<tr>
<td>Reverse-mode</td>
<td>Propagates gradients backward</td>
<td>Functions with many parameters and scalar outputs</td>
</tr>
</table>

<h3>Relation to Back-Propagation</h3>
<p>
Back-propagation can be understood as an efficient reverse-mode differentiation
procedure applied to a neural network computational graph. It allows gradients of
the loss with respect to a large number of parameters to be computed efficiently.
</p>

<div class="exam">
<strong>Exam Focus:</strong> Know symbolic, numerical, forward-mode, and reverse-mode
differentiation and understand the relationship between reverse-mode differentiation
and back-propagation.
</div>

<h3>Possible Exam Questions</h3>
<ul>
<li>(5M) Explain numerical and symbolic differentiation.</li>
<li>(5M) What is automatic differentiation?</li>
<li>(10M) Compare forward-mode and reverse-mode differentiation.</li>
<li>(10M) Explain the relationship between back-propagation and reverse-mode differentiation.</li>
</ul>
'''))

# ============================================================
# WRITE CHAPTER FILE
# ============================================================

html = "\n".join(parts)

with open("ch6_part2.html", "w", encoding="utf-8") as f:
    f.write(html)

print("ch6_part2 generated:", len(html), "characters")