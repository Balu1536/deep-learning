# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/home/claude')
from gen_helpers import topic, sub, box, chapter_header

parts = [chapter_header('ch6', 'Chapter 6: Deep Feedforward Networks')]

parts.append(topic('t-xor', '1. Learning XOR', 'VH', f'''
{sub('⭐ Importance')}<p>Classic, extremely popular exam example — demonstrates WHY hidden layers/non-linearity are necessary; expect a full worked derivation question.</p>
{sub('📌 Definition')}
{box('def', 'The <b>XOR problem</b> is the classic example showing that a single-layer linear model (no hidden units) CANNOT represent the XOR (exclusive-OR) function, motivating the need for hidden layers with non-linear activation functions in feedforward networks.')}
{sub('🧠 Intuition')}<p>XOR outputs 1 only when its two inputs DIFFER. Plotting the 4 input points (0,0)→0, (0,1)→1, (1,0)→1, (1,1)→0 on a 2D plane shows the two classes CANNOT be separated by any single straight line — but a hidden layer can bend/combine the space so that a linear separator becomes possible afterward.</p>
{sub('📖 Detailed Explanation')}<p>A purely linear model f(x)=Wx+b (no hidden layer) can only represent linear functions. XOR is NOT linearly separable, so no choice of W, b can make a linear model solve it exactly. Adding a hidden layer with a non-linear activation function (e.g., ReLU) lets the network first transform the input into a new representation h=g(W⁽¹⁾x+b⁽¹⁾) where the problem BECOMES linearly separable, then apply a final linear layer y=W⁽²⁾h+b⁽²⁾ to solve it.</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'Hidden layer: h = max(0, W⁽¹⁾x + b⁽¹⁾) &nbsp;(ReLU activation) <br>Output: y = W⁽²⁾h + b⁽²⁾')}
{sub('📐 Derivation')}
{box('formula', '''A known solution (Goodfellow et al.) using ReLU: <br>
W⁽¹⁾ = [[1,1],[1,1]], b⁽¹⁾ = [0,−1]ᵀ, w⁽²⁾ = [1,−2]ᵀ, b⁽²⁾=0.<br>
For input x=(0,0): h = ReLU([0,0]+[0,−1]) = ReLU([0,−1]) = [0,0]. y = 1(0)+(−2)(0) = 0. ✓<br>
For input x=(1,0): h = ReLU([1,1]+[0,−1]) = ReLU([1,0]) = [1,0]. y = 1(1)+(−2)(0) = 1. ✓<br>
For input x=(0,1): h = ReLU([1,1]+[0,−1]) = ReLU([1,0]) = [1,0]. y = 1. ✓<br>
For input x=(1,1): h = ReLU([2,2]+[0,−1]) = ReLU([2,1]) = [2,1]. y = 1(2)+(−2)(1) = 0. ✓<br>
All 4 XOR outputs correctly reproduced — the hidden layer transforms the space so a simple linear output layer suffices.''')}
{sub('💡 Simple Example')}<p>Truth table: (0,0)→0, (0,1)→1, (1,0)→1, (1,1)→0 — verified exactly by the derivation above.</p>
{sub('🎯 Real-World/ML Example')}<p>XOR is a toy problem, but the same principle (hidden layers make non-linearly-separable problems solvable) is why deep networks can model highly complex real-world functions like image recognition and language understanding.</p>
{sub('🖼️ Diagram')}
<svg class="diagram" viewBox="0 0 260 130" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="110" x2="230" y2="110" stroke="#999"/><line x1="30" y1="110" x2="30" y2="15" stroke="#999"/>
<circle cx="40" cy="105" r="5" fill="#c0392b"/><text x="20" y="122" font-size="8">(0,0)→0</text>
<circle cx="200" cy="20" r="5" fill="#c0392b"/><text x="180" y="15" font-size="8">(1,1)→0</text>
<circle cx="200" cy="105" r="5" fill="#2f57a3"/><text x="185" y="122" font-size="8">(1,0)→1</text>
<circle cx="40" cy="20" r="5" fill="#2f57a3"/><text x="20" y="15" font-size="8">(0,1)→1</text>
<text x="60" y="65" font-size="9">No single line separates red from blue!</text>
</svg>
{sub('✅ Advantages')}<p>Simple, easy-to-verify by hand demonstration of the power of hidden layers/non-linearity — the canonical teaching example for feedforward networks.</p>
{sub('❌ Limitations')}<p>Toy problem — does not directly reflect complexity of real datasets, but the underlying principle (linear separability requires non-linear transformation) generalizes.</p>
{sub('🔄 Comparison with Related Concepts')}<p>Linear model (fails on XOR) vs single-hidden-layer network (solves XOR exactly) — direct illustration of the Universal Approximation power gained from hidden units.</p>
{sub('⚠️ Common Mistakes')}<p>Forgetting to include a non-linear activation function in the hidden layer (without non-linearity, stacking linear layers is still just one big linear function, mathematically no different from no hidden layer at all).</p>
{sub('🧠 Important Points to Remember')}<ul><li>XOR is NOT linearly separable — classic proof by counterexample.</li><li>Hidden layer + non-linear activation (e.g., ReLU) makes XOR solvable.</li><li>Purely linear networks (no activation) collapse to a single linear transform, regardless of depth.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul>
<li>(2M) Why can\\u2019t a single-layer linear model solve XOR?</li>
<li>(10M) Show, with a worked example, how a feedforward network with one hidden layer (ReLU) solves the XOR problem.</li>
<li>(10M) Explain the significance of the XOR example in motivating deep feedforward network architecture.</li>
</ul>
'''))

parts.append(topic('t-gradient-based-learning', '2. Gradient-Based Learning', 'H', f'''
{sub('⭐ Importance')}<p>Connects Ch.3 optimization theory specifically to neural network training; important conceptual + formula-based topic.</p>
{sub('📌 Definition')}
{box('def', '<b>Gradient-based learning</b> in the context of neural networks means training the network\\u2019s weights by defining a differentiable COST FUNCTION J(θ) (comparing predictions to targets) and using gradient descent (or SGD) to iteratively minimize it.')}
{sub('🧠 Intuition')}<p>Unlike linear models with convex cost functions (guaranteed global minimum), neural networks have NON-CONVEX cost functions due to the composition of non-linear layers — gradient-based learning provides no convergence guarantee to a global minimum, only to SOME local minimum/critical point, yet works remarkably well in practice.</p>
{sub('📖 Detailed Explanation')}<p>Two crucial design choices for gradient-based learning of neural nets: (1) <b>Choosing the cost function</b> — typically negative log-likelihood / cross-entropy (from MLE, Ch.5), which provides large, useful gradients even when predictions are very wrong (unlike, e.g., using 0/1 loss which gives zero gradient almost everywhere). (2) <b>Choosing the output unit</b> — e.g., sigmoid output for binary classification (paired with cross-entropy), softmax for multi-class, linear output for regression (paired with MSE) — each output unit type must be paired with a compatible, well-behaved cost function to ensure the gradient does not saturate/vanish inappropriately.</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'Cost function (cross-entropy, classification): J(θ) = −E<sub>x,y~data</sub>[log p<sub>model</sub>(y|x;θ)] <br>Update rule: θ ← θ − ε∇θJ(θ)')}
{sub('💡 Simple Example')}<p>For binary classification with sigmoid output ŷ=σ(z), cross-entropy loss L=−[y log ŷ + (1−y)log(1−ŷ)] gives a clean, well-behaved gradient ∂L/∂z = ŷ−y (simple and never vanishes when predictions are very wrong) — much better behaved than pairing sigmoid with squared error, which CAN saturate.</p>
{sub('🎯 Real-World/ML Example')}<p>Every deep learning classifier (CNNs, transformers) uses gradient-based learning with cross-entropy loss; regression networks use MSE with linear output units.</p>
{sub('✅ Advantages')}<p>Scales to networks with millions/billions of parameters; works despite non-convexity in practice, especially combined with good initialization (covered in Ch.5 Unit 3) and adaptive optimizers.</p>
{sub('❌ Limitations')}<p>No global optimality guarantee (non-convex); sensitive to cost function/output unit pairing — poor choices can cause vanishing gradients and stalled learning.</p>
{sub('🔄 Comparison with Related Concepts')}<p>Gradient-based learning in linear models (convex, guaranteed global min) vs deep networks (non-convex, only local guarantees) — this distinction is a common exam contrast.</p>
{sub('⚠️ Common Mistakes')}<p>Pairing sigmoid/softmax output with mean-squared-error loss (causes vanishing gradients when predictions saturate near 0/1) instead of the recommended cross-entropy pairing.</p>
{sub('🧠 Important Points to Remember')}<ul><li>Neural network cost functions are non-convex — no global minimum guarantee.</li><li>Cross-entropy + sigmoid/softmax is the standard, well-behaved pairing.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul><li>(2M) Why is the cost function of a neural network non-convex?</li><li>(5M) Explain why cross-entropy is preferred over MSE for classification output layers.</li></ul>
'''))

parts.append(topic('t-hidden-units', '3. Hidden Units', 'H', f'''
{sub('⭐ Importance')}<p>Very practical/important — activation functions (ReLU, sigmoid, tanh) are frequently tested with formula + pros/cons comparisons.</p>
{sub('📌 Definition')}
{box('def', '<b>Hidden units</b> are the neurons in the hidden layers of a feedforward network; each computes an affine transformation of its input followed by a non-linear <b>activation function</b> g: h = g(Wx+b). The choice of activation function significantly affects training dynamics.')}
{sub('🧠 Intuition')}<p>Without a non-linear activation, stacking layers would collapse into a single linear transformation (no matter how many layers). Activation functions introduce the non-linearity necessary to model complex functions, and different choices trade off gradient behavior, computational cost, and output range.</p>
{sub('📖 Detailed Explanation')}<p><b>ReLU</b> g(z)=max(0,z): default choice in modern deep learning — computationally cheap, does not saturate for z&gt;0 (avoiding vanishing gradients there), but has zero gradient for z&lt;0 ("dying ReLU" problem). <b>Sigmoid</b> g(z)=1/(1+e⁻ᶻ): squashes output to (0,1), historically popular but SATURATES for large |z| (gradient→0), causing vanishing gradients in deep networks — now mainly used only for output layers (binary probabilities), not hidden layers. <b>Tanh</b> g(z)=(eᶻ−e⁻ᶻ)/(eᶻ+e⁻ᶻ): squashes to (−1,1), zero-centered (often better than sigmoid for hidden layers) but still saturates. Variants like <b>Leaky ReLU</b> (small non-zero slope for z&lt;0) address the dying ReLU problem.</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'ReLU: g(z) = max(0,z) <br>Sigmoid: g(z) = 1/(1+e⁻ᶻ) <br>Tanh: g(z) = (eᶻ−e⁻ᶻ)/(eᶻ+e⁻ᶻ) <br>Leaky ReLU: g(z) = max(αz, z), small α (e.g., 0.01)')}
{sub('💡 Simple Example')}<p>z=−2: ReLU(−2)=0, Sigmoid(−2)≈0.119, Tanh(−2)≈−0.964, Leaky ReLU(−2)=−0.02 (with α=0.01).</p>
{sub('🎯 Real-World/ML Example')}<p>Nearly all modern CNNs/deep feedforward networks use ReLU (or variants like Leaky ReLU, GELU) in hidden layers due to superior gradient flow; sigmoid remains standard for binary-classification output layers.</p>
{sub('🖼️ Diagram')}
<svg class="diagram" viewBox="0 0 260 100" xmlns="http://www.w3.org/2000/svg">
<g transform="translate(30,50)"><line x1="-25" y1="0" x2="25" y2="0" stroke="#ccc"/><line x1="0" y1="-30" x2="0" y2="30" stroke="#ccc"/><path d="M-25,0 L0,0 L25,-25" stroke="#2f57a3" stroke-width="2" fill="none"/><text x="-15" y="45" font-size="8">ReLU</text></g>
<g transform="translate(120,50)"><line x1="-25" y1="0" x2="25" y2="0" stroke="#ccc"/><line x1="0" y1="-30" x2="0" y2="30" stroke="#ccc"/><path d="M-25,25 Q0,-25 25,-25" stroke="#0e8a6d" stroke-width="2" fill="none"/><text x="-20" y="45" font-size="8">Sigmoid</text></g>
<g transform="translate(210,50)"><line x1="-25" y1="0" x2="25" y2="0" stroke="#ccc"/><line x1="0" y1="-30" x2="0" y2="30" stroke="#ccc"/><path d="M-25,25 Q0,-25 25,-28" stroke="#e8a24d" stroke-width="2" fill="none"/><text x="-15" y="45" font-size="8">Tanh</text></g>
</svg>
{sub('✅ Advantages')}<p>ReLU: fast, avoids vanishing gradient for positive inputs, sparse activations. Sigmoid/Tanh: smooth, bounded outputs useful for probabilities/gates.</p>
{sub('❌ Limitations')}<p>ReLU: "dying ReLU" (neurons stuck outputting 0 permanently). Sigmoid/Tanh: vanishing gradients for large |z|, computationally more expensive (exponentials).</p>
{sub('🔄 Comparison with Related Concepts')}
<table><tr><th>Activation</th><th>Range</th><th>Saturates?</th><th>Common Use</th></tr>
<tr><td>ReLU</td><td>[0,∞)</td><td>Only for z&lt;0</td><td>Hidden layers (default)</td></tr>
<tr><td>Sigmoid</td><td>(0,1)</td><td>Both ends</td><td>Binary output layer</td></tr>
<tr><td>Tanh</td><td>(−1,1)</td><td>Both ends</td><td>RNN hidden states (legacy)</td></tr></table>
{sub('⚠️ Common Mistakes')}<p>Using sigmoid/tanh in many stacked hidden layers (causes severe vanishing gradients); forgetting ReLU is not differentiable exactly at z=0 (handled by convention, e.g., defining subgradient as 0 or 1).</p>
{sub('🧠 Important Points to Remember')}<ul><li>ReLU is the default modern choice for hidden units.</li><li>Sigmoid/Tanh saturate — avoid in deep hidden stacks.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul><li>(2M) Define activation function.</li><li>(5M) Compare ReLU, Sigmoid, and Tanh activation functions.</li><li>(5M) What is the dying ReLU problem and how is it addressed?</li></ul>
'''))

with open('/home/claude/ch6_part1.html','w') as f:
    f.write(''.join(parts))
print("ch6 part1 written, length:", len(''.join(parts)))
