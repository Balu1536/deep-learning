# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/home/claude')
from gen_helpers import topic, sub, box, chapter_header

parts = [chapter_header('ch3', 'Chapter 3: Numerical Computation')]

parts.append(topic('t-overflow-underflow', '1. Overflow and Underflow', 'M', f'''
{sub('⭐ Importance')}<p>Conceptual + practical topic; commonly a 2-5 mark question about why softmax/log-sum-exp tricks are needed.</p>
{sub('📌 Definition')}
{box('def', '<b>Underflow</b> occurs when numbers very close to zero are rounded to zero by finite-precision computer arithmetic. <b>Overflow</b> occurs when numbers with very large magnitude are approximated as +∞ or −∞. Both cause loss of numerical accuracy.')}
{sub('🧠 Intuition')}<p>Computers cannot store real numbers with infinite precision — they use floating-point representations with a limited number of bits. Extremely small or large values "fall off the edge" of what can be represented, causing errors that can silently corrupt computations (e.g., dividing by an underflowed zero).</p>
{sub('📖 Detailed Explanation')}<p>A classic example is the <b>softmax function</b> softmax(x)ᵢ = exp(xᵢ)/Σⱼexp(xⱼ). If any xᵢ is very large, exp(xᵢ) overflows to infinity; if all xᵢ are very negative, exp(xᵢ) underflows to zero for all i, causing a 0/0 division. The standard fix is to subtract the maximum value: softmax(x)ᵢ = exp(xᵢ−max(x)) / Σⱼexp(xⱼ−max(x)) — this keeps the largest exponent at 0 (exp(0)=1) and all others ≤0, avoiding overflow while preserving the mathematically correct result.</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'Stable softmax: softmax(x)ᵢ = exp(xᵢ − max(x)) / Σⱼ exp(xⱼ − max(x)) <br>Log-sum-exp trick: log Σᵢexp(xᵢ) = max(x) + log Σᵢ exp(xᵢ−max(x))')}
{sub('💡 Simple Example')}<p>x = [1000, 1000]. Naive exp(1000) = overflow (inf). Stable version: subtract max=1000 → exp(0)+exp(0)=2, softmax=[0.5,0.5] — correct result recovered.</p>
{sub('🎯 Real-World/ML Example')}<p>Computing log-likelihoods for many small probabilities multiplied together (e.g., in Naive Bayes or HMMs) underflows quickly; practitioners work in log-space and use log-sum-exp for numerical stability.</p>
{sub('✅ Advantages')}<p>Stabilization techniques (max-subtraction, log-space computation) allow deep networks to be trained reliably without numerical corruption.</p>
{sub('❌ Limitations')}<p>Adds slight extra computation; must be applied carefully and consistently throughout a pipeline (loss functions, activation functions) or errors can resurface elsewhere.</p>
{sub('⚠️ Common Mistakes')}<p>Implementing softmax/log-likelihood without numerical stabilization; forgetting that log(0) = −∞ causes NaN propagation.</p>
{sub('🧠 Important Points to Remember')}<ul><li>Stable softmax subtracts max(x) before exponentiating — MEMORIZE.</li><li>Underflow → treated as 0; Overflow → treated as ±∞.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul><li>(2M) Define overflow and underflow.</li><li>(5M) Explain the numerically stable softmax function and why it is needed.</li></ul>
'''))

parts.append(topic('t-gradient-opt', '2. Gradient-Based Optimization', 'VH', f'''
{sub('⭐ Importance')}<p>Extremely important — foundation of ALL neural network training; expect derivation + numerical + algorithm questions.</p>
{sub('📌 Definition')}
{box('def', '<b>Gradient-based optimization</b> minimizes (or maximizes) an objective/cost function f(x) by iteratively moving x in the direction that most rapidly decreases f, which is the negative gradient direction −∇ₓf(x).')}
{sub('🧠 Intuition')}<p>Imagine standing on a hilly landscape (the cost surface) in fog, only able to feel the local slope under your feet. The gradient tells you the steepest uphill direction; walking in the OPPOSITE direction (steepest descent) takes you toward a valley (minimum) fastest, step by step.</p>
{sub('📖 Detailed Explanation')}<p>The gradient ∇ₓf(x) is the vector of partial derivatives [∂f/∂x₁, ..., ∂f/∂xₙ]. At any point, it points in the direction of steepest increase of f; hence its negative points toward steepest decrease. The learning rate (step size) ε controls how large each step is: too small → slow convergence; too large → overshooting/divergence. A <b>critical point</b> is where ∇f(x)=0 — could be a minimum, maximum, or saddle point (checked using the second derivative / Hessian).</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'Update rule (Gradient Descent): x ← x − ε∇ₓf(x) <br>ε = learning rate (step size)')}
{sub('📐 Derivation')}
{box('formula', '''Using first-order Taylor expansion: f(x+Δx) ≈ f(x) + Δxᵀ∇f(x).<br>
We want to choose Δx (with fixed small magnitude ‖Δx‖) that MINIMIZES this approximation.<br>
Δxᵀ∇f(x) is minimized (most negative) when Δx points exactly opposite to ∇f(x), i.e. Δx = −ε∇f(x) for some small ε&gt;0 (by Cauchy-Schwarz inequality, the dot product is most negative when vectors are anti-parallel).<br>
Substituting: x_new = x − ε∇f(x) — this is the gradient descent update rule.''')}
{sub('💡 Simple Example')}
{box('example', '''Minimize f(x)=x². ∇f(x)=2x. Start x₀=4, ε=0.1.<br>
x₁ = 4 − 0.1(8) = 3.2. x₂ = 3.2 − 0.1(6.4) = 2.56. x₃=2.56−0.1(5.12)=2.048 ... converging toward the true minimum x=0.''')}
{sub('🎯 Real-World/ML Example')}<p>Training a neural network updates all weights via gradient descent (or its stochastic variant, SGD) on the loss function computed via backpropagation.</p>
{sub('🖼️ Diagram')}
<svg class="diagram" viewBox="0 0 260 130" xmlns="http://www.w3.org/2000/svg">
<path d="M20,110 Q130,10 240,110" fill="none" stroke="#2f57a3" stroke-width="2"/>
<circle cx="200" cy="90" r="4" fill="#c0392b"/><circle cx="160" cy="45" r="4" fill="#c0392b"/><circle cx="130" cy="18" r="4" fill="#c0392b"/>
<text x="140" y="125" font-size="10">Steps descending toward minimum</text>
</svg>
{sub('⚙️ Algorithm / Procedure')}<p>1. Initialize x (parameters). 2. Compute gradient ∇f(x). 3. Update x ← x−ε∇f(x). 4. Repeat until convergence (gradient≈0 or max iterations reached).</p>
{sub('📝 Pseudocode')}
<pre>x = initialize()
while not converged:
    grad = compute_gradient(f, x)
    x = x - epsilon * grad
return x</pre>
{sub('✅ Advantages')}<p>Simple, general-purpose, scales to millions of parameters (with stochastic variants); only needs first-order derivative information.</p>
{sub('❌ Limitations')}<p>Can get stuck in local minima/saddle points for non-convex functions; sensitive to learning rate choice; slow near flat regions (vanishing gradient); does not use curvature information (unlike second-order methods).</p>
{sub('🔄 Comparison with Related Concepts')}<p>First-order (gradient descent, only uses ∇f) vs Second-order methods (e.g., Newton\\u2019s method, uses Hessian ∇²f for faster but costlier convergence) — covered in Ch.5 Optimization for Training Deep Models.</p>
{sub('⚠️ Common Mistakes')}<p>Choosing too large a learning rate (divergence/oscillation); forgetting the negative sign in the update rule; confusing gradient (vector) with derivative (scalar, 1-D case only).</p>
{sub('🧠 Important Points to Remember')}<ul><li>x←x−ε∇f(x) — MEMORIZE.</li><li>∇f(x)=0 at critical points (minima, maxima, saddle points).</li><li>Direction of steepest descent = −∇f(x).</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul>
<li>(2M) Define gradient descent.</li>
<li>(2M) What is the role of the learning rate?</li>
<li>(5M) Derive the gradient descent update rule from the first-order Taylor expansion.</li>
<li>(10M) Explain gradient-based optimization with a numerical example and discuss the effect of learning rate (too small vs too large) with diagrams.</li>
</ul>
'''))

parts.append(topic('t-constrained-opt', '3. Constrained Optimization', 'H', f'''
{sub('⭐ Importance')}<p>Important conceptually and mathematically — connects directly to PCA derivation and regularization (Ch.4); Lagrange multipliers and KKT conditions are common exam topics.</p>
{sub('📌 Definition')}
{box('def', '<b>Constrained optimization</b> seeks to minimize (or maximize) an objective function f(x) subject to equality constraints g(x)=0 and/or inequality constraints h(x)≤0, restricting the feasible search space for x.')}
{sub('🧠 Intuition')}<p>Instead of searching the whole space for the best x, constrained optimization only considers points satisfying certain rules — e.g., "find the best solution, but the weight vector must have unit length" (exactly the PCA constraint).</p>
{sub('📖 Detailed Explanation')}<p>The classical technique for EQUALITY constraints is the method of <b>Lagrange multipliers</b>: form the Lagrangian L(x,λ) = f(x) + λg(x), and solve ∇ₓL=0 and ∇_λL=0 simultaneously. For INEQUALITY constraints, the <b>Karush-Kuhn-Tucker (KKT) conditions</b> generalize this — they require stationarity, primal feasibility (h(x)≤0), dual feasibility (μ≥0), and complementary slackness (μh(x)=0).</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'Lagrangian (equality constraint): L(x,λ) = f(x) + λ g(x) <br>Stationarity: ∇ₓL = ∇f(x) + λ∇g(x) = 0 <br>KKT (inequality h(x)≤0): stationarity, h(x)≤0, μ≥0, μh(x)=0')}
{sub('📐 Derivation')}<p>DERIVATION NOT REQUIRED for full KKT theory — but be ready to reproduce the PCA-style derivation (maximize wᵀΣw subject to wᵀw=1 using Lagrange multipliers) shown in Chapter 1\\u2019s PCA topic, which is the most likely numerical/derivation application.</p>
{sub('💡 Simple Example')}
{box('example', '''Maximize f(x,y)=xy subject to x+y=10.<br>
L = xy + λ(x+y−10). ∂L/∂x = y+λ=0, ∂L/∂y = x+λ=0 ⟹ x=y. With x+y=10 ⟹ x=y=5. Max value = 25.''')}
{sub('🎯 Real-World/ML Example')}<p>PCA\\u2019s variance maximization subject to unit-norm constraint; SVM\\u2019s margin maximization subject to correct-classification constraints (uses KKT conditions); L1/L2 regularization can be viewed as constrained optimization (norm penalty ≤ budget) — covered in Ch.4.</p>
{sub('✅ Advantages')}<p>Allows encoding of domain knowledge/restrictions directly into the optimization problem; Lagrangian framework converts constrained problems into unconstrained ones (easier to solve with standard calculus).</p>
{sub('❌ Limitations')}<p>KKT conditions are necessary but not always sufficient for non-convex problems; can be computationally complex for many constraints.</p>
{sub('🔄 Comparison with Related Concepts')}<p>Equality-constrained (Lagrange multipliers only) vs inequality-constrained (needs full KKT conditions with additional non-negativity and complementary slackness conditions).</p>
{sub('⚠️ Common Mistakes')}<p>Forgetting to include the constraint equation itself as one of the equations to solve (∇_λL=0 just restates g(x)=0); sign errors in the Lagrangian.</p>
{sub('🧠 Important Points to Remember')}<ul><li>L(x,λ)=f(x)+λg(x) — MEMORIZE for equality constraints.</li><li>KKT extends this to inequality constraints with complementary slackness.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul><li>(2M) What is constrained optimization?</li><li>(5M) Explain the method of Lagrange multipliers with an example.</li><li>(10M) State and explain the KKT conditions with an example application in ML (e.g., PCA or SVM).</li></ul>
'''))

parts.append(topic('t-least-squares', '4. Linear Least Squares', 'H', f'''
{sub('⭐ Importance')}<p>Important — directly testable derivation connecting linear algebra + calculus + optimization; classic 10-mark question.</p>
{sub('📌 Definition')}
{box('def', '<b>Linear least squares</b> finds the parameter vector x that minimizes the squared error between a linear model Ax and target vector b: minimize f(x) = ‖Ax−b‖₂².')}
{sub('🧠 Intuition')}<p>When an exact solution to Ax=b does not exist (an over-determined system with more equations than unknowns), least squares finds the "closest possible" x — the one minimizing the total squared distance between predictions Ax and actual targets b. This is exactly linear regression\\u2019s fitting criterion.</p>
{sub('📖 Detailed Explanation')}<p>The objective f(x)=‖Ax−b‖₂² = (Ax−b)ᵀ(Ax−b) is a smooth, convex quadratic function of x, guaranteeing a unique global minimum (when AᵀA is invertible), found simply by setting its gradient to zero.</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'Objective: f(x) = ‖Ax − b‖₂² <br>Normal Equation: AᵀAx = Aᵀb <br>Closed-form solution: x* = (AᵀA)⁻¹ Aᵀb')}
{sub('📐 Derivation')}
{box('formula', '''f(x) = (Ax−b)ᵀ(Ax−b) = xᵀAᵀAx − 2xᵀAᵀb + bᵀb<br>
∇ₓf(x) = 2AᵀAx − 2Aᵀb &nbsp;(using matrix calculus identities: ∇ₓ(xᵀMx)=2Mx for symmetric M; ∇ₓ(xᵀc)=c)<br>
Set gradient to zero: 2AᵀAx − 2Aᵀb = 0 ⟹ AᵀAx = Aᵀb &nbsp;(the Normal Equation)<br>
If AᵀA is invertible: <b>x* = (AᵀA)⁻¹Aᵀb</b> ∎''')}
{sub('💡 Simple Example')}
{box('example', '''Fit y=mx (no intercept) to points (1,2),(2,3),(3,5). A=[[1],[2],[3]], b=[2,3,5]ᵀ.<br>
AᵀA = 1+4+9=14. Aᵀb = 1(2)+2(3)+3(5)=2+6+15=23.<br>
x* = 23/14 ≈ 1.643 (best-fit slope m).''')}
{sub('🎯 Real-World/ML Example')}<p>Linear Regression is exactly linear least squares: fitting a line/hyperplane to data by minimizing sum of squared residuals; used as a baseline model and building block for more complex regression techniques.</p>
{sub('🖼️ Diagram')}
<svg class="diagram" viewBox="0 0 260 130" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="110" x2="240" y2="110" stroke="#999"/><line x1="20" y1="110" x2="20" y2="10" stroke="#999"/>
<line x1="30" y1="100" x2="220" y2="30" stroke="#2f57a3" stroke-width="2"/>
<circle cx="50" cy="85" r="4" fill="#c0392b"/><line x1="50" y1="85" x2="50" y2="93" stroke="#c0392b" stroke-dasharray="2,2"/>
<circle cx="110" cy="55" r="4" fill="#c0392b"/><line x1="110" y1="55" x2="110" y2="66" stroke="#c0392b" stroke-dasharray="2,2"/>
<circle cx="180" cy="45" r="4" fill="#c0392b"/><line x1="180" y1="45" x2="180" y2="45" stroke="#c0392b" stroke-dasharray="2,2"/>
<text x="60" y="125" font-size="9">Fitted line minimizes sum of squared vertical residuals</text>
</svg>
{sub('⚙️ Algorithm / Procedure')}<p>1. Form design matrix A and target vector b. 2. Compute AᵀA and Aᵀb. 3. Solve the normal equation AᵀAx=Aᵀb (via matrix inverse or numerically stable methods like QR/SVD decomposition). 4. Output x* as the least-squares solution.</p>
{sub('📝 Pseudocode')}
<pre>ATA = A.T @ A
ATb = A.T @ b
x_star = solve(ATA, ATb)   # or inv(ATA) @ ATb
return x_star</pre>
{sub('✅ Advantages')}<p>Closed-form solution (no iterative optimization needed for small/medium problems); convex objective guarantees global optimum; simple to implement and interpret.</p>
{sub('❌ Limitations')}<p>Requires AᵀA to be invertible (fails if features are linearly dependent/collinear — needs regularization, i.e., Ridge Regression); computing matrix inverse is expensive (O(n³)) for large feature dimension; sensitive to outliers (squared error penalizes large errors heavily).</p>
{sub('🔄 Comparison with Related Concepts')}<p>Ordinary Least Squares (closed-form, exact) vs Gradient-Based Optimization (iterative, scales better to huge datasets/parameters, used when closed-form is infeasible).</p>
{sub('⚠️ Common Mistakes')}<p>Forgetting the factor of 2 when differentiating the squared norm; attempting to invert a singular/non-invertible AᵀA without regularization; sign errors in the normal equation.</p>
{sub('🧠 Important Points to Remember')}<ul><li>Normal equation: AᵀAx=Aᵀb — MEMORIZE.</li><li>x*=(AᵀA)⁻¹Aᵀb — closed-form solution.</li><li>This is the mathematical foundation of Linear Regression.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul>
<li>(2M) Define linear least squares.</li>
<li>(5M) Derive the normal equation for linear least squares.</li>
<li>(10M) Derive the closed-form solution x*=(AᵀA)⁻¹Aᵀb step-by-step and solve a numerical example.</li>
</ul>
'''))

with open('/home/claude/ch3_full.html','w') as f:
    f.write(''.join(parts))
print("ch3 written, length:", len(''.join(parts)))
