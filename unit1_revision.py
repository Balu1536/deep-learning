# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/home/claude')
from gen_helpers import revision_box, sub, box

html = revision_box('unit1-revision', '📚 UNIT 1 — Revision Summary', f'''
{sub('🔥 MUST STUDY')}
<ul class="priority-list"><li>🔥 Eigen Decomposition</li><li>🔥 Singular Value Decomposition (SVD)</li><li>🔥 Principal Component Analysis (PCA)</li><li>🔥 Variance and Covariance</li><li>🔥 Bayes' Rule</li><li>🔥 Gradient-Based Optimization</li></ul>
{sub('🟠 HIGH PRIORITY')}
<ul class="priority-list"><li>🟠 Matrices and Tensors</li><li>🟠 Matrix Operations</li><li>🟠 Norms</li><li>🟠 Probability Distributions</li><li>🟠 Conditional Probability</li><li>🟠 Expectation</li><li>🟠 Information Theory</li><li>🟠 Constrained Optimization</li><li>🟠 Linear Least Squares</li></ul>
{sub('🟡 MODERATE PRIORITY')}
<ul class="priority-list"><li>🟡 Vectors</li><li>🟡 Types of Matrices</li><li>🟡 Random Variables</li><li>🟡 Marginal Probability</li><li>🟡 Overflow and Underflow</li></ul>
{sub('🟢 LOW PRIORITY')}
<ul class="priority-list"><li>🟢 Scalars</li></ul>

{sub('🔢 Important Formulas')}
{box('formula', '''‖x‖₂² = xᵀx &nbsp;|&nbsp; Av=λv &nbsp;|&nbsp; A=VΛV⁻¹ (or QΛQᵀ if symmetric) &nbsp;|&nbsp; A=UΣVᵀ (SVD) <br>
Var(X)=E[X²]−(E[X])² &nbsp;|&nbsp; Cov(X,Y)=E[XY]−E[X]E[Y] &nbsp;|&nbsp; P(y|x)=P(x|y)P(y)/P(x) <br>
H(X)=−ΣP(x)log P(x) &nbsp;|&nbsp; x←x−ε∇f(x) &nbsp;|&nbsp; x*=(AᵀA)⁻¹Aᵀb''')}

{sub('📐 Important Derivations')}
<ul><li>Eigen decomposition from Av=λv → det(A−λI)=0</li><li>SVD from eigen decomposition of AᵀA</li><li>PCA variance maximization via Lagrange multipliers → Σw=λw</li><li>Var(X+Y)=Var(X)+Var(Y)+2Cov(X,Y)</li><li>Bayes' Rule from conditional probability definition</li><li>Gradient descent update from Taylor expansion</li><li>Normal equation for Linear Least Squares</li></ul>

{sub('🖼️ Important Diagrams')}
<ul><li>Vector as arrow in 2D space</li><li>Scalar→Vector→Matrix→Tensor progression</li><li>L1 (diamond) vs L2 (circle) norm balls</li><li>Eigenvector direction preservation (Av ∥ v)</li><li>SVD: rotate-scale-rotate (unit circle → ellipse)</li><li>PCA: PC1/PC2 axes on scattered data</li><li>Gaussian bell curve</li><li>Gradient descent steps on a bowl-shaped curve</li><li>Least squares fitted line with residuals</li></ul>

{sub('🔄 Important Comparisons')}
<table><tr><th>Comparison</th><th>Key Difference</th></tr>
<tr><td>Eigen Decomposition vs SVD</td><td>Eigen: square matrices only, one basis. SVD: any matrix, two bases (U,V)</td></tr>
<tr><td>L1 vs L2 norm</td><td>L1→sparsity; L2→shrinkage, smooth, unique minimum</td></tr>
<tr><td>PMF vs PDF</td><td>PMF sums to 1 (discrete); PDF integrates to 1 (continuous)</td></tr>
<tr><td>Marginal vs Conditional Probability</td><td>Marginal sums out a variable; Conditional restricts to a sub-world and normalizes</td></tr>
<tr><td>Entropy vs Cross-Entropy vs KL Divergence</td><td>H(P) uncertainty of P alone; H(P,Q) cost of using Q for P; KL = difference between them</td></tr>
</table>

{sub('🧮 Numerical Topics to Practice')}
<ul><li>Eigenvalues/eigenvectors of 2×2 matrices</li><li>Computing L1, L2, L∞ norms of a vector</li><li>Bayes' theorem numericals (medical test style)</li><li>Variance/covariance calculation from data</li><li>Gradient descent iterations by hand</li><li>Linear least squares normal equation solving</li></ul>

{sub('❓ Expected 2-Mark Questions')}
<ul><li>Define scalar, vector, matrix, tensor.</li><li>Define eigenvalue and eigenvector.</li><li>Define SVD.</li><li>Define PCA.</li><li>Define variance and covariance.</li><li>State Bayes' theorem.</li><li>Define entropy.</li><li>Define gradient descent.</li><li>Define overflow and underflow.</li><li>Define linear least squares.</li></ul>

{sub('📝 Expected 5-Mark Questions')}
<ul><li>Explain types of matrices with examples.</li><li>Compute L1/L2/L∞ norms for a given vector.</li><li>Find eigenvalues/eigenvectors of a 2×2 matrix.</li><li>Derive Bayes' Rule from conditional probability.</li><li>Explain PCA algorithm steps.</li><li>Derive Var(X)=E[X²]−(E[X])².</li><li>Explain cross-entropy as a loss function.</li><li>Explain Lagrange multipliers with example.</li></ul>

{sub('📚 Expected 10/15-Mark Questions')}
<ul><li>Derive eigen decomposition and explain geometric meaning; solve numerical.</li><li>Derive SVD and compare with eigen decomposition.</li><li>Derive PCA using Lagrange multipliers; explain algorithm and applications.</li><li>Derive Var(X+Y) and solve numerical covariance problem.</li><li>Solve a full Bayes' theorem numerical problem (medical/spam).</li><li>Explain gradient descent with derivation, numerical, and learning-rate discussion.</li><li>Derive linear least squares normal equation and closed-form solution.</li><li>Explain KKT conditions with an ML application.</li></ul>

{sub('⚡ One-Page Rapid Revision')}
<p>Linear Algebra gives us the language (scalars→vectors→matrices→tensors) and tools (norms, eigen decomposition, SVD) to represent and manipulate data; PCA applies eigen decomposition to reduce dimensionality by keeping high-variance directions. Probability gives us a language for uncertainty (random variables, distributions), tools to combine/reason about it (marginal, conditional, Bayes' Rule), and information theory to measure it (entropy, cross-entropy, KL divergence — directly used as deep learning loss functions). Numerical Computation addresses practical computer-arithmetic issues (overflow/underflow) and the optimization machinery (gradient descent, constrained optimization, least squares) used to actually train models.</p>
''')

with open('/home/claude/unit1_revision.html','w') as f:
    f.write(html)
print("unit1 revision written, length:", len(html))
