# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/home/claude')
from gen_helpers import topic, sub, box

parts = []

# ---------------- 7. Eigen Decomposition ----------------
parts.append(topic('t-eigen', '7. Eigen Decomposition', 'VH', f'''
{sub('⭐ Importance')}<p>One of the most heavily tested topics — numerical problems (find eigenvalues/eigenvectors), derivation, and conceptual link to PCA/SVD. Expect a 10-15 mark question.</p>
{sub('📌 Definition')}
{box('def', 'For a square matrix A, a non-zero vector v is an <b>eigenvector</b> with corresponding <b>eigenvalue</b> λ if: <br><b>Av = λv</b>. <b>Eigen decomposition</b> expresses A as A = VΛV⁻¹, where V is the matrix whose columns are eigenvectors and Λ is a diagonal matrix of eigenvalues.')}
{sub('🧠 Intuition')}<p>Multiplying A by an eigenvector only stretches/shrinks it (by factor λ) without changing its direction. Eigen decomposition reveals the "natural axes" along which a linear transformation acts by pure scaling — this is exactly what PCA exploits to find directions of maximum variance.</p>
{sub('📖 Detailed Explanation')}<p>Not every matrix has a real eigen decomposition, but every real <b>symmetric</b> matrix can be decomposed as A = QΛQᵀ, where Q is orthogonal (columns are orthonormal eigenvectors) and Λ is diagonal (eigenvalues on the diagonal). This special case (spectral theorem) is exactly the form used in PCA, since covariance matrices are symmetric.</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'Av = λv &nbsp;&nbsp;(eigenvalue equation) <br>A = VΛV⁻¹ &nbsp;&nbsp;(general square, diagonalizable A) <br>A = QΛQᵀ &nbsp;&nbsp;(symmetric A, Q orthogonal)')}
{sub('📐 Derivation')}
{box('formula', '''Step 1: Start from Av = λv ⟹ Av − λv = 0 ⟹ (A − λI)v = 0.<br>
Step 2: For a non-zero solution v to exist, (A − λI) must be singular, i.e. det(A − λI) = 0. This is the <b>characteristic equation</b>.<br>
Step 3: Solve det(A − λI) = 0 for λ (the "characteristic polynomial") to get eigenvalues λ₁, λ₂, ..., λₙ.<br>
Step 4: For each λᵢ, substitute back into (A − λᵢI)v = 0 and solve the homogeneous system for the corresponding eigenvector vᵢ.<br>
Step 5: Stack all eigenvectors as columns of V = [v₁ v₂ ... vₙ], and put eigenvalues on the diagonal of Λ. Then A = VΛV⁻¹ (verified since AV = VΛ by construction).''')}
{sub('💡 Simple Example')}
{box('example', '''Let A = [[2,0],[0,3]] (already diagonal). <br>
Characteristic equation: det(A−λI) = (2−λ)(3−λ) = 0 ⟹ λ₁=2, λ₂=3.<br>
For λ₁=2: (A−2I)v=0 ⟹ [[0,0],[0,1]]v=0 ⟹ v=[1,0]ᵀ.<br>
For λ₂=3: (A−3I)v=0 ⟹ [[-1,0],[0,0]]v=0 ⟹ v=[0,1]ᵀ.<br>
So A = VΛV⁻¹ with V=[[1,0],[0,1]], Λ=[[2,0],[0,3]].''')}
<p>A slightly less trivial worked example (typical exam problem): A = [[4,1],[2,3]]. det(A−λI) = (4−λ)(3−λ)−2 = λ²−7λ+10 = 0 ⟹ (λ−5)(λ−2)=0 ⟹ λ₁=5, λ₂=2. For λ₁=5: (A−5I)v=0 ⟹ [[-1,1],[2,-2]]v=0 ⟹ v₁=[1,1]ᵀ. For λ₂=2: (A−2I)v=0 ⟹ [[2,1],[2,1]]v=0 ⟹ v₂=[1,-2]ᵀ.</p>
{sub('🎯 Real-World/ML Example')}<p>PCA computes eigenvectors of the data covariance matrix to find principal directions of variance; PageRank algorithm uses the dominant eigenvector of a link matrix; stability analysis of dynamical systems uses eigenvalues.</p>
{sub('🖼️ Diagram')}
<svg class="diagram" viewBox="0 0 260 150" xmlns="http://www.w3.org/2000/svg">
<g transform="translate(130,75)">
<line x1="-100" y1="0" x2="100" y2="0" stroke="#ccc"/><line x1="0" y1="-60" x2="0" y2="60" stroke="#ccc"/>
<line x1="0" y1="0" x2="70" y2="0" stroke="#2f57a3" stroke-width="3" marker-end="url(#a1)"/>
<line x1="0" y1="0" x2="105" y2="0" stroke="#0e8a6d" stroke-width="3" stroke-dasharray="4,2" marker-end="url(#a2)"/>
<defs>
<marker id="a1" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="#2f57a3"/></marker>
<marker id="a2" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="#0e8a6d"/></marker>
</defs>
<text x="10" y="-10" font-size="10">v (eigenvector)</text>
<text x="10" y="20" font-size="10" fill="#0e8a6d">Av = λv (same direction, scaled)</text>
</g>
</svg>
<p style="font-size:.85rem;color:var(--text-soft);">Exam drawing tip: show that Av lies along the same line as v, just longer/shorter — this is the entire geometric meaning of eigenvectors.</p>
{sub('⚙️ Algorithm / Procedure')}<p><b>Input:</b> square matrix A (n×n). <b>Output:</b> eigenvalues λᵢ and eigenvectors vᵢ.<br>
1. Form characteristic equation det(A−λI)=0.<br>2. Solve polynomial for λ values.<br>3. For each λ, solve (A−λI)v=0 for v.<br>4. Normalize eigenvectors (optional, for orthonormal basis).<br>5. Assemble V and Λ; A = VΛV⁻¹.</p>
{sub('📝 Pseudocode')}
<pre>solve det(A - λI) = 0 for eigenvalues λ_1..λ_n
for each λ_i:
    solve (A - λ_i I) v = 0  -> eigenvector v_i
V = [v_1, v_2, ..., v_n]
Λ = diag(λ_1, ..., λ_n)
A = V Λ V⁻¹</pre>
{sub('✅ Advantages')}<p>Reveals intrinsic geometric structure of a transformation; diagonal form makes powers of A trivial (Aᵏ = VΛᵏV⁻¹); foundation for PCA, spectral clustering, stability analysis.</p>
{sub('❌ Limitations')}<p>Only square matrices have eigenvalues; not all square matrices are diagonalizable (defective matrices); complex eigenvalues can occur for non-symmetric matrices; computationally expensive for very large matrices.</p>
{sub('🔄 Comparison with Related Concepts')}<p>Eigen decomposition works only for square matrices; SVD (next topic) generalizes this idea to ANY rectangular matrix using two different orthogonal bases instead of one.</p>
{sub('⚠️ Common Mistakes')}<p>Forgetting to set determinant of (A−λI) to zero (using A−λ instead); arithmetic errors solving the quadratic/characteristic polynomial; not normalizing eigenvectors when required; assuming V is always orthogonal (only true when A is symmetric).</p>
{sub('🧠 Important Points to Remember')}<ul><li>Av = λv is the defining equation — MEMORIZE.</li><li>det(A−λI) = 0 gives eigenvalues.</li><li>Symmetric matrix ⟹ A = QΛQᵀ with orthogonal Q.</li><li>Sum of eigenvalues = trace(A); product of eigenvalues = det(A).</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul>
<li>(2M) Define eigenvalue and eigenvector.</li>
<li>(2M) State the characteristic equation.</li>
<li>(5M) Find eigenvalues and eigenvectors of a given 2×2 matrix.</li>
<li>(10M) Derive the eigen decomposition of a matrix and explain its geometric meaning with a diagram; solve a numerical example.</li>
<li>(10M) Explain how eigen decomposition is used in PCA.</li>
</ul>
'''))

# ---------------- 8. SVD ----------------
parts.append(topic('t-svd', '8. Singular Value Decomposition (SVD)', 'VH', f'''
{sub('⭐ Importance')}<p>Extremely important — generalizes eigen decomposition to non-square matrices; used in PCA, dimensionality reduction, recommender systems, pseudo-inverse. Very common 10-15 mark question.</p>
{sub('📌 Definition')}
{box('def', 'For ANY real matrix A ∈ ℝ<sup>m×n</sup> (not necessarily square), the <b>Singular Value Decomposition</b> factorizes it as: <br><b>A = UΣVᵀ</b> <br>where U ∈ ℝ<sup>m×m</sup> is orthogonal (left singular vectors), Σ ∈ ℝ<sup>m×n</sup> is a rectangular diagonal matrix of non-negative <b>singular values</b> σ₁≥σ₂≥...≥0, and V ∈ ℝ<sup>n×n</sup> is orthogonal (right singular vectors).')}
{sub('🧠 Intuition')}<p>SVD says: ANY linear transformation can be broken into (1) a rotation Vᵀ, (2) a pure axis-aligned scaling Σ, (3) another rotation U. Geometrically, SVD shows that any matrix maps the unit sphere to an ellipsoid — the singular values are the lengths of the ellipsoid's semi-axes.</p>
{sub('📖 Detailed Explanation')}<p>Columns of U are eigenvectors of AAᵀ; columns of V are eigenvectors of AᵀA; singular values σᵢ are the square roots of the (shared, non-zero) eigenvalues of both AAᵀ and AᵀA. Unlike eigen decomposition, SVD exists for EVERY matrix, including rectangular and singular ones.</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'A = UΣVᵀ <br>AAᵀ = UΣ²Uᵀ  (eigen decomposition of AAᵀ gives U and σᵢ²) <br>AᵀA = VΣ²Vᵀ  (eigen decomposition of AᵀA gives V and σᵢ²) <br>σᵢ = √(λᵢ of AᵀA or AAᵀ)')}
{sub('📐 Derivation')}
{box('formula', '''Step 1: Consider AᵀA (an n×n symmetric, positive semi-definite matrix). By the spectral theorem it can be eigen-decomposed as AᵀA = VΛVᵀ, with V orthogonal and Λ diagonal (eigenvalues ≥ 0).<br>
Step 2: Define singular values σᵢ = √λᵢ (square roots of eigenvalues of AᵀA), placed in decreasing order in the diagonal matrix Σ.<br>
Step 3: Define uᵢ = (1/σᵢ) A vᵢ for each σᵢ ≠ 0 — these form the columns of U, and can be shown to be orthonormal and to be eigenvectors of AAᵀ.<br>
Step 4: Combine: A vᵢ = σᵢ uᵢ for all i ⟹ in matrix form AV = UΣ ⟹ A = UΣVᵀ (since V is orthogonal, V⁻¹=Vᵀ).''')}
{sub('💡 Simple Example')}
{box('example', '''Let A = [[1,0],[0,-2]] (already diagonal, easy case). AᵀA = [[1,0],[0,4]] ⟹ eigenvalues 1, 4 ⟹ singular values σ₁=2, σ₂=1 (sorted). V = I (eigenvectors of AᵀA). U columns computed as A vᵢ/σᵢ: u₁ = A[0,1]ᵀ/2 = [0,-2]ᵀ/2=[0,-1]ᵀ, u₂ = A[1,0]ᵀ/1=[1,0]ᵀ. So A = UΣVᵀ with Σ=diag(2,1).''')}
{sub('🎯 Real-World/ML Example')}<p>SVD powers PCA (principal components = right singular vectors scaled by singular values), image compression (keep only top-k singular values to reconstruct a close approximation), recommender systems (matrix factorization of user-item ratings), and computing the Moore-Penrose pseudo-inverse A⁺ = VΣ⁺Uᵀ for solving least-squares problems.</p>
{sub('🖼️ Diagram')}
<svg class="diagram" viewBox="0 0 340 120" xmlns="http://www.w3.org/2000/svg">
<g font-size="11" fill="#333">
<text x="10" y="20">A</text><text x="30" y="20">=</text>
<rect x="45" y="5" width="40" height="40" fill="#eef3ff" stroke="#2f57a3"/><text x="52" y="60" fill="#666">U (rotate)</text>
<text x="95" y="30">×</text>
<rect x="110" y="5" width="40" height="40" fill="#fff8e6" stroke="#e8c766"/><text x="105" y="60" fill="#666">Σ (scale)</text>
<text x="160" y="30">×</text>
<rect x="175" y="5" width="40" height="40" fill="#eefaf5" stroke="#0e8a6d"/><text x="165" y="60" fill="#666">Vᵀ (rotate)</text>
<text x="240" y="30" font-size="10">unit circle → ellipse under A</text>
</g>
</svg>
<p style="font-size:.85rem;color:var(--text-soft);">Exam drawing tip: draw a unit circle transforming into an ellipse, with axes labeled σ₁, σ₂ — the classic SVD picture.</p>
{sub('⚙️ Algorithm / Procedure')}<p><b>Input:</b> matrix A (m×n). <b>Output:</b> U, Σ, V such that A=UΣVᵀ.<br>1. Compute AᵀA.<br>2. Eigen-decompose AᵀA to get eigenvalues λᵢ and eigenvectors (columns of V).<br>3. Set σᵢ=√λᵢ, sort descending, form Σ.<br>4. Compute uᵢ = Avᵢ/σᵢ for non-zero σᵢ to form U.<br>5. Assemble A = UΣVᵀ.</p>
{sub('📝 Pseudocode')}
<pre>compute M = A^T A
[V, Λ] = eig(M)          # eigenvectors, eigenvalues
Σ = sqrt(Λ), sorted descending
for i in singular values with σ_i != 0:
    u_i = (A @ v_i) / σ_i
U = [u_1, ..., u_m]
return U, Σ, V</pre>
{sub('✅ Advantages')}<p>Works for ANY matrix (square, rectangular, singular); numerically stable; enables low-rank approximation (truncated SVD) for compression/denoising; basis for PCA and pseudo-inverse.</p>
{sub('❌ Limitations')}<p>Computationally expensive for very large matrices (O(min(m²n, mn²))); result not always intuitive to interpret directly without further processing.</p>
{sub('🔄 Comparison with Related Concepts')}
<table><tr><th>Aspect</th><th>Eigen Decomposition</th><th>SVD</th></tr>
<tr><td>Applies to</td><td>Square matrices only</td><td>Any matrix (m×n)</td></tr>
<tr><td>Form</td><td>A=VΛV⁻¹ (or QΛQᵀ if symmetric)</td><td>A=UΣVᵀ</td></tr>
<tr><td>Basis vectors</td><td>Same space (V)</td><td>Two different orthogonal bases (U, V)</td></tr>
<tr><td>Always exists?</td><td>No (only diagonalizable matrices)</td><td>Yes, always</td></tr></table>
{sub('⚠️ Common Mistakes')}<p>Confusing dimensions of U, Σ, V for non-square A; forgetting singular values must be non-negative and sorted in decreasing order; mixing up SVD of A with eigen decomposition of A directly (SVD uses AᵀA/AAᵀ, not A itself).</p>
{sub('🧠 Important Points to Remember')}<ul><li>A = UΣVᵀ — MEMORIZE.</li><li>Singular values = √(eigenvalues of AᵀA).</li><li>SVD exists for every matrix; eigen decomposition does not.</li><li>Truncated SVD (top-k singular values) gives best rank-k approximation (Eckart–Young theorem).</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul>
<li>(2M) Define SVD.</li>
<li>(2M) What are singular values?</li>
<li>(5M) State the relationship between SVD and eigen decomposition of AᵀA and AAᵀ.</li>
<li>(10M) Derive SVD of a matrix and explain geometric interpretation with diagram.</li>
<li>(15M) Compare eigen decomposition and SVD; explain applications of SVD in Machine Learning (PCA, compression, pseudo-inverse).</li>
</ul>
'''))

# ---------------- 9. PCA ----------------
parts.append(topic('t-pca', '9. Principal Component Analysis (PCA)', 'VH', f'''
{sub('⭐ Importance')}<p>One of the highest-yield topics in the whole syllabus — combines eigen decomposition + SVD + variance/covariance; near-guaranteed 10-15 mark question plus numericals.</p>
{sub('📌 Definition')}
{box('def', '<b>PCA</b> is an unsupervised dimensionality-reduction technique that transforms possibly-correlated features into a smaller set of linearly uncorrelated variables called <b>principal components</b>, ordered so the first component captures the maximum possible variance in the data, the second captures the maximum remaining variance orthogonal to the first, and so on.')}
{sub('🧠 Intuition')}<p>Imagine data scattered in a cloud in high dimensions — most of the "spread"/information often lies along just a few directions. PCA finds these directions (axes of maximum spread) and re-expresses the data using them, discarding low-variance directions that contribute little information — this compresses the data while retaining most of its structure.</p>
{sub('📖 Detailed Explanation')}<p>PCA proceeds by centering the data (subtracting the mean), computing the covariance matrix of the centered data, and then finding its eigenvectors/eigenvalues (equivalently, via SVD of the centered data matrix). The eigenvectors (principal directions) with the largest eigenvalues (variances) are kept as the new axes; projecting data onto the top-k eigenvectors gives a k-dimensional reduced representation.</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'Let X be the (mean-centered) data matrix (n samples × d features). <br>Covariance matrix: Σ = (1/n) XᵀX &nbsp;(d×d, symmetric) <br>Eigen decomposition: Σ = WΛWᵀ (W = eigenvectors = principal components, Λ = eigenvalues = variances) <br>Projected data: Z = XW<sub>k</sub> &nbsp;(keep top-k eigenvectors W<sub>k</sub>)')}
{sub('📐 Derivation')}
{box('formula', '''Goal: find unit vector w that maximizes the variance of the projection Xw.<br>
Step 1: Variance of projected data = Var(Xw) = (1/n)(Xw)ᵀ(Xw) = wᵀ[(1/n)XᵀX]w = wᵀΣw, where Σ=(1/n)XᵀX is the covariance matrix.<br>
Step 2: Maximize wᵀΣw subject to constraint ‖w‖²=wᵀw=1 (unit vector, else variance grows unboundedly).<br>
Step 3: Use Lagrange multipliers: L(w,λ) = wᵀΣw − λ(wᵀw − 1).<br>
Step 4: Take derivative w.r.t. w and set to zero: ∂L/∂w = 2Σw − 2λw = 0 ⟹ Σw = λw.<br>
Step 5: This is exactly the eigenvalue equation! So the optimal w is an eigenvector of Σ, and the maximum variance achieved equals its eigenvalue λ. Choosing the eigenvector with the LARGEST eigenvalue gives the first principal component; the next-largest (orthogonal) gives the second, and so on.''')}
{sub('💡 Simple Example')}
{box('example', '''Data points (already mean-centered): (2,1), (0,-1), (-2,0). <br>
Covariance matrix Σ = (1/3)XᵀX where X=[[2,1],[0,-1],[-2,0]]. <br>
XᵀX = [[8,2],[2,2]] ⟹ Σ = [[2.67,0.67],[0.67,0.67]] (approx). <br>
Solving det(Σ−λI)=0 gives eigenvalues λ₁≈2.9 (large, principal direction along mostly-x-axis), λ₂≈0.44 (small). The eigenvector for λ₁ becomes PC1 — data is projected onto this direction for 1-D reduction, retaining ~87% of total variance (λ₁/(λ₁+λ₂)).''')}
{sub('🎯 Real-World/ML Example')}<p>Compressing a dataset of 1000 correlated gene-expression features down to 20 principal components before feeding into a classifier; face recognition ("Eigenfaces") represents face images using top principal components; visualizing high-dimensional data in 2D/3D for exploration.</p>
{sub('🖼️ Diagram')}
<svg class="diagram" viewBox="0 0 260 160" xmlns="http://www.w3.org/2000/svg">
<g transform="translate(130,80)">
<line x1="-100" y1="60" x2="100" y2="-60" stroke="#2f57a3" stroke-width="2"/>
<text x="60" y="-65" font-size="10" fill="#2f57a3">PC1 (max variance)</text>
<line x1="-30" y1="-40" x2="30" y2="40" stroke="#0e8a6d" stroke-width="2" stroke-dasharray="3,2"/>
<text x="20" y="55" font-size="10" fill="#0e8a6d">PC2 (orthogonal)</text>
<circle cx="-40" cy="20" r="3" fill="#333"/><circle cx="-20" cy="10" r="3" fill="#333"/><circle cx="10" cy="-8" r="3" fill="#333"/>
<circle cx="35" cy="-25" r="3" fill="#333"/><circle cx="-55" cy="30" r="3" fill="#333"/><circle cx="50" cy="-32" r="3" fill="#333"/>
</g>
</svg>
<p style="font-size:.85rem;color:var(--text-soft);">Exam drawing tip: scatter points forming an elongated cloud, draw PC1 along the long axis and PC2 perpendicular — always label axes and points.</p>
{sub('⚙️ Algorithm / Procedure')}<p><b>Input:</b> data matrix X (n×d). <b>Output:</b> reduced data Z (n×k).<br>
1. Mean-center: X ← X − mean(X).<br>2. Compute covariance matrix Σ = (1/n)XᵀX.<br>3. Compute eigenvalues/eigenvectors of Σ (or use SVD of X directly for numerical stability).<br>4. Sort eigenvectors by descending eigenvalue.<br>5. Select top-k eigenvectors as W<sub>k</sub>.<br>6. Project: Z = X W<sub>k</sub>.</p>
{sub('📝 Pseudocode')}
<pre>X = X - mean(X, axis=0)          # center data
Sigma = (1/n) * X.T @ X           # covariance matrix
eigvals, eigvecs = eig(Sigma)
sort eigvecs by eigvals descending
W_k = top k eigvecs
Z = X @ W_k                       # reduced representation</pre>
{sub('✅ Advantages')}<p>Reduces dimensionality and noise; removes redundant/correlated features; speeds up downstream learning; enables visualization; components are uncorrelated by construction.</p>
{sub('❌ Limitations')}<p>Only captures LINEAR relationships (fails on non-linear manifolds — needs Kernel PCA/t-SNE); components can be hard to interpret; sensitive to feature scaling (must standardize features first); assumes high variance = high importance, which is not always true (e.g., for classification, discriminative directions may have low variance).</p>
{sub('🔄 Comparison with Related Concepts')}
<table><tr><th>Aspect</th><th>PCA</th><th>Eigen Decomp</th><th>SVD</th></tr>
<tr><td>Goal</td><td>Dimensionality reduction</td><td>General matrix factorization</td><td>General matrix factorization</td></tr>
<tr><td>Uses</td><td>Eigen decomp of covariance (or SVD of X)</td><td>Building block for PCA</td><td>Numerically stable way to do PCA</td></tr>
<tr><td>Input needed</td><td>Data matrix</td><td>Square matrix</td><td>Any matrix</td></tr></table>
{sub('⚠️ Common Mistakes')}<p>Forgetting to mean-center (and often standardize) the data before PCA; confusing eigenvalues (variance explained) with eigenvectors (directions); selecting components arbitrarily instead of by descending eigenvalue / explained variance ratio.</p>
{sub('🧠 Important Points to Remember')}<ul><li>Principal components = eigenvectors of covariance matrix, ranked by eigenvalue.</li><li>Explained variance ratio = λᵢ / Σλⱼ.</li><li>PCA can be computed via SVD of the centered data matrix directly (more numerically stable than forming XᵀX).</li><li>PCA is linear and unsupervised — does not use labels.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul>
<li>(2M) Define PCA.</li>
<li>(2M) What is "explained variance"?</li>
<li>(5M) List the steps of the PCA algorithm.</li>
<li>(10M) Derive PCA as a variance-maximization problem using Lagrange multipliers, showing it reduces to an eigenvalue problem.</li>
<li>(15M) Explain PCA fully: motivation, derivation, algorithm, numerical example, advantages/limitations, and its relation to SVD.</li>
</ul>
'''))

with open('/home/claude/ch1_part2.html','w') as f:
    f.write(''.join(parts))
print("ch1 part2 written, length:", len(''.join(parts)))
