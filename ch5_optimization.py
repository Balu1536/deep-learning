# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '.')
from gen_helpers import topic, sub, box, chapter_header

parts = [chapter_header('ch5opt', 'Chapter 5: Optimization for Training Deep Models')]

parts.append(topic('t-pure-opt', '1. Pure Optimization', 'H', f'''
{sub('⭐ Importance')}<p>Important foundation for understanding how neural networks are trained and why practical deep-learning optimization methods are needed.</p>

{sub('📌 Definition')}
{box('def', '<b>Optimization</b> is the process of finding parameter values that minimize or maximize an objective function. In deep learning, training usually means minimizing a loss function with respect to model parameters.')}

{sub('🔢 Mathematical Formulation')}
{box('formula', 'θ* = arg min<sub>θ</sub> J(θ)<br><br>where θ represents model parameters and J(θ) is the objective/loss function.')}

{sub('🧠 Intuition')}<p>Imagine a landscape where height represents loss. Optimization attempts to move from the current point toward a low point in the landscape.</p>

{sub('📖 Detailed Explanation')}<p>For a neural network, the objective depends on millions or billions of parameters. Exact global optimization is generally impractical, so iterative numerical methods are used. Gradient-based methods use derivatives to determine useful directions for parameter updates.</p>

{sub('🎯 Exam-Oriented Questions')}
<ul>
<li>(2M) Define optimization in deep learning.</li>
<li>(5M) Explain the objective function used in neural network training.</li>
<li>(10M) Explain the role of optimization in training deep models.</li>
</ul>
'''))

parts.append(topic('t-challenges', '2. Challenges in Neural Network Optimization', 'VH', f'''
{sub('⭐ Importance')}<p>Very High — commonly asked as a conceptual long-answer topic.</p>

{sub('📌 Definition')}
{box('def', 'Neural network optimization is difficult because deep models produce high-dimensional, non-convex objective functions with saddle points, ill-conditioned regions, and complicated parameter interactions.')}

{sub('🧠 Major Challenges')}
<ul>
<li><b>Non-convexity:</b> the loss surface can contain many local structures.</li>
<li><b>Saddle points:</b> gradients can become small even when the point is not a minimum.</li>
<li><b>Ill-conditioning:</b> curvature may differ greatly in different directions.</li>
<li><b>Vanishing gradients:</b> gradients may become extremely small.</li>
<li><b>Exploding gradients:</b> gradients may become extremely large.</li>
<li><b>Plateaus:</b> progress can become very slow in flat regions.</li>
<li><b>Large parameter spaces:</b> modern networks may contain enormous numbers of parameters.</li>
</ul>

{sub('📖 Detailed Explanation')}<p>Unlike simple convex optimization problems, neural-network objectives can have complicated geometry. A method that works well in one region of the loss surface may behave poorly in another. Good initialization, learning-rate selection, normalization, momentum, adaptive methods, and suitable architectures help address these difficulties.</p>

{sub('⚠️ Common Mistakes')}<p>Do not claim that neural-network training always gets trapped in local minima. In high-dimensional deep-learning problems, saddle points and poor conditioning can be important practical difficulties.</p>

{sub('🎯 Exam-Oriented Questions')}
<ul>
<li>(5M) List the challenges in neural network optimization.</li>
<li>(10M) Explain non-convexity, saddle points, vanishing gradients, and ill-conditioning.</li>
<li>(15M) Discuss the major challenges involved in optimizing deep neural networks.</li>
</ul>
'''))

parts.append(topic('t-basic-algorithms', '3. Basic Algorithms', 'VH', f'''
{sub('⭐ Importance')}<p>Very High — formulas and update rules are important for examinations.</p>

{sub('📌 Definition')}
{box('def', 'Basic optimization algorithms iteratively update parameters using gradient information to reduce the objective function.')}

{sub('🔢 Gradient Descent')}
{box('formula', 'θ<sub>t+1</sub> = θ<sub>t</sub> − η ∇<sub>θ</sub>J(θ<sub>t</sub>)')}

{sub('🧠 Intuition')}<p>The gradient points toward increasing loss, so moving in the negative-gradient direction generally decreases the loss.</p>

{sub('🔢 Stochastic / Minibatch Gradient Descent')}
{box('formula', 'θ ← θ − η ĝ<br><br>where ĝ is a gradient estimate calculated using a randomly selected example or minibatch.')}

{sub('🔢 Momentum')}
{box('formula', 'v<sub>t</sub> = βv<sub>t−1</sub> + ∇J(θ<sub>t</sub>)<br>θ<sub>t+1</sub> = θ<sub>t</sub> − ηv<sub>t</sub>')}

{sub('📖 Algorithm / Procedure')}
<ol>
<li>Initialize parameters.</li>
<li>Compute the loss.</li>
<li>Compute the gradient.</li>
<li>Update parameters.</li>
<li>Repeat until a stopping condition is reached.</li>
</ol>

{sub('🎯 Exam-Oriented Questions')}
<ul>
<li>(2M) Write the gradient descent update rule.</li>
<li>(5M) Explain batch, stochastic, and minibatch gradient descent.</li>
<li>(10M) Explain gradient descent with momentum and derive its update equations.</li>
</ul>
'''))

parts.append(topic('t-initialization', '4. Parameter Initialization Strategies', 'VH', f'''
{sub('⭐ Importance')}<p>Very High — initialization strongly affects convergence and gradient propagation in deep networks.</p>

{sub('📌 Definition')}
{box('def', 'Parameter initialization is the process of choosing initial values for neural-network weights and biases before training begins.')}

{sub('🧠 Why Initialization Matters')}<p>If all weights are initialized to the same value, neurons can receive identical gradients and learn identical features. Poorly scaled weights can also cause activations or gradients to vanish or explode.</p>

{sub('🔢 Common Strategies')}
<ul>
<li><b>Zero initialization:</b> generally unsuitable for hidden-layer weights because of symmetry.</li>
<li><b>Small random initialization:</b> breaks symmetry.</li>
<li><b>Glorot/Xavier initialization:</b> designed to maintain useful activation/gradient variance.</li>
<li><b>He initialization:</b> particularly suitable for ReLU-type activations.</li>
</ul>

{sub('🔢 Xavier/Glorot Idea')}
{box('formula', 'Var(W) ≈ 2 / (n<sub>in</sub> + n<sub>out</sub>)')}

{sub('🔢 He Initialization Idea')}
{box('formula', 'Var(W) ≈ 2 / n<sub>in</sub>')}

{sub('⚠️ Common Mistakes')}<p>Do not say zero initialization is always impossible. Biases can often be initialized to zero; the symmetry problem mainly concerns identical hidden-layer weights.</p>

{sub('🎯 Exam-Oriented Questions')}
<ul>
<li>(2M) What is parameter initialization?</li>
<li>(5M) Explain Xavier and He initialization.</li>
<li>(10M) Why is proper initialization important in deep networks?</li>
</ul>
'''))

parts.append(topic('t-adaptive', '5. Algorithms with Adaptive Learning Rates', 'VH', f'''
{sub('⭐ Importance')}<p>Very High — Adam and adaptive learning-rate methods are highly important practical optimization concepts.</p>

{sub('📌 Definition')}
{box('def', 'Adaptive optimization algorithms automatically adjust the effective learning rate for different parameters using information from previous gradients.')}

{sub('🧠 Intuition')}<p>Instead of forcing every parameter to use exactly the same step size, adaptive methods give different parameters different effective update scales based on their gradient history.</p>

{sub('🔢 AdaGrad')}
{box('formula', 'G<sub>t</sub> = G<sub>t−1</sub> + g<sub>t</sub>²<br>θ<sub>t+1</sub> = θ<sub>t</sub> − η g<sub>t</sub> / (√G<sub>t</sub> + ε)')}

{sub('🔢 RMSProp')}
{box('formula', 's<sub>t</sub> = βs<sub>t−1</sub> + (1−β)g<sub>t</sub>²<br>θ<sub>t+1</sub> = θ<sub>t</sub> − η g<sub>t</sub> / (√s<sub>t</sub> + ε)')}

{sub('🔢 Adam')}
{box('formula', 'm<sub>t</sub> = β₁m<sub>t−1</sub> + (1−β₁)g<sub>t</sub><br>s<sub>t</sub> = β₂s<sub>t−1</sub> + (1−β₂)g<sub>t</sub>²<br><br>Bias-corrected estimates are used before updating θ.')}

{sub('📖 Detailed Explanation')}<p>Adam combines ideas related to momentum and adaptive scaling. It is widely used because it often provides fast and convenient convergence, although it is not automatically the best choice for every problem.</p>

{sub('🔄 Comparison with Related Concepts')}<p>AdaGrad continually accumulates squared gradients and can reduce learning rates substantially. RMSProp uses an exponentially weighted average. Adam combines first-moment and second-moment estimates.</p>

{sub('🎯 Exam-Oriented Questions')}
<ul>
<li>(5M) Explain AdaGrad and RMSProp.</li>
<li>(10M) Explain the Adam optimization algorithm with equations.</li>
<li>(10M) Compare SGD, RMSProp, and Adam.</li>
</ul>
'''))

parts.append(topic('t-second-order', '6. Approximate Second-Order Methods', 'H', f'''
{sub('⭐ Importance')}<p>Important theoretical topic; understand the role of curvature and the Hessian.</p>

{sub('📌 Definition')}
{box('def', 'Second-order optimization methods use curvature information represented by the Hessian matrix, while approximate methods estimate or simplify this curvature information to reduce computational cost.')}

{sub('🔢 Hessian')}
{box('formula', 'H = ∇²J(θ)')}

{sub('🧠 Intuition')}<p>Gradient tells us which direction the objective changes, while the Hessian describes how the gradient itself changes — effectively providing information about curvature.</p>

{sub('🔢 Newton-Style Update')}
{box('formula', 'θ<sub>t+1</sub> = θ<sub>t</sub> − H⁻¹ ∇J(θ<sub>t</sub>)')}

{sub('📖 Why Approximate?')}<p>For a network with millions of parameters, explicitly storing and inverting a full Hessian is prohibitively expensive. Approximate methods attempt to obtain useful curvature information without constructing the full Hessian.</p>

{sub('🎯 Exam-Oriented Questions')}
<ul>
<li>(2M) Define the Hessian.</li>
<li>(5M) Compare first-order and second-order optimization.</li>
<li>(10M) Explain why approximate second-order methods are needed for deep networks.</li>
</ul>
'''))

parts.append(topic('t-meta', '7. Optimization Strategies and Meta-Algorithms', 'H', f'''
{sub('⭐ Importance')}<p>Important — combines optimization methods with practical strategies used during neural-network training.</p>

{sub('📌 Definition')}
{box('def', 'Optimization strategies and meta-algorithms are higher-level techniques that control or improve the optimization process, such as learning-rate schedules, early stopping, batch-size choices, and optimizer selection.')}

{sub('🔢 Learning-Rate Scheduling')}
<ul>
<li>Step decay</li>
<li>Exponential decay</li>
<li>Cosine-style schedules</li>
<li>Warm-up strategies</li>
</ul>

{sub('🧠 Important Strategies')}
<ul>
<li><b>Learning-rate tuning:</b> choose a suitable step size.</li>
<li><b>Batch-size selection:</b> balance computational efficiency and gradient noise.</li>
<li><b>Gradient clipping:</b> limit excessively large gradients.</li>
<li><b>Early stopping:</b> stop when validation performance stops improving.</li>
<li><b>Optimizer selection:</b> choose SGD, momentum, Adam, or another suitable method.</li>
<li><b>Hyperparameter search:</b> systematically explore important training settings.</li>
</ul>

{sub('📖 Detailed Explanation')}<p>No single optimization algorithm is universally best. Practical training usually combines an optimizer with an appropriate learning rate, schedule, initialization strategy, batch size, regularization method, and stopping criterion.</p>

{sub('🎯 Exam-Oriented Questions')}
<ul>
<li>(2M) What is a learning-rate schedule?</li>
<li>(5M) Explain optimization strategies used in deep learning.</li>
<li>(10M) Discuss how learning rate, initialization, batch size, and regularization affect training.</li>
</ul>
'''))

parts.append('''
<div class="revision-box">
<h3>📚 Unit 3 — Chapter 5 Quick Revision</h3>
<ul class="priority-list">
<li>🔥 Challenges in Neural Network Optimization</li>
<li>🔥 Basic Algorithms — Gradient Descent, SGD, Momentum</li>
<li>🔥 Parameter Initialization — Xavier and He</li>
<li>🔥 Adaptive Learning Rates — AdaGrad, RMSProp, Adam</li>
<li>🟠 Pure Optimization</li>
<li>🟠 Approximate Second-Order Methods</li>
<li>🟠 Optimization Strategies and Meta-Algorithms</li>
</ul>

<h3>⭐ Must-Memorize Formulas</h3>
<ul>
<li>Gradient descent: θ ← θ − η∇J(θ)</li>
<li>Momentum update</li>
<li>AdaGrad update</li>
<li>RMSProp update</li>
<li>Adam first- and second-moment equations</li>
<li>Newton update: θ ← θ − H⁻¹∇J(θ)</li>
<li>Xavier variance ≈ 2/(n<sub>in</sub>+n<sub>out</sub>)</li>
<li>He variance ≈ 2/n<sub>in</sub></li>
</ul>
</div>
''')

if __name__ == '__main__':
    with open('ch5_optimization.html', 'w', encoding='utf-8') as f:
        f.write(''.join(parts))
    print("Chapter 5 Optimization generated:", len(''.join(parts)), "characters")