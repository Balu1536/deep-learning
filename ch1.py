# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/home/claude')
from gen_helpers import topic, sub, box, chapter_header

parts = []
parts.append(chapter_header('ch1', 'Chapter 1: Linear Algebra'))

# ---------------- 1. Scalars ----------------
parts.append(topic('t-scalars', '1. Scalars', 'L', f'''
{sub('⭐ Importance')}<p>Foundational vocabulary term; rarely asked alone but used to define vectors/matrices. Quick 2-mark question material.</p>
{sub('📌 Definition')}
{box('def', 'A <b>scalar</b> is a single, standalone numerical quantity — just one number, as opposed to an ordered collection of numbers. Scalars are usually written in italic lowercase letters, e.g. <i>s</i>, <i>n</i>, <i>x</i>. They belong to a set such as ℝ (real numbers) or ℕ (natural numbers).')}
{sub('🧠 Intuition')}<p>Think of a scalar as a "plain number" — temperature (25°C), a learning rate (0.01), or the number of layers in a network (5). It has magnitude only, no direction or structure.</p>
{sub('📖 Detailed Explanation')}<p>In machine learning, scalars appear as hyperparameters (learning rate α, regularization coefficient λ), as individual entries inside vectors/matrices/tensors, and as outputs of loss functions (a single number summarizing model error). Formally we write <i>s</i> ∈ ℝ to state "s is a real-valued scalar".</p>
{sub('💡 Simple Example')}<p>s = 7, π = 3.14159, or a single pixel intensity value 235.</p>
{sub('🎯 Real-World/ML Example')}<p>The loss value returned by a loss function (e.g., Cross-Entropy Loss = 0.023) is a scalar; the learning rate used in gradient descent update is a scalar.</p>
{sub('✅ Advantages')}<p>Simplest possible mathematical object — easy to manipulate with ordinary arithmetic.</p>
{sub('❌ Limitations')}<p>Cannot represent multi-dimensional relationships (direction, spatial structure) — for that we need vectors, matrices, tensors.</p>
{sub('🔄 Comparison with Related Concepts')}
<table><tr><th>Object</th><th>Dimension</th><th>Example</th></tr>
<tr><td>Scalar</td><td>0-D</td><td>5</td></tr>
<tr><td>Vector</td><td>1-D</td><td>[5, 2, 9]</td></tr>
<tr><td>Matrix</td><td>2-D</td><td>3×3 grid of numbers</td></tr>
<tr><td>Tensor</td><td>n-D</td><td>RGB image (H×W×3)</td></tr></table>
{sub('🧠 Important Points to Remember')}<ul><li>Scalars are 0-dimensional (rank-0 tensors).</li><li>Denoted by lowercase italics.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul><li>(2M) Define a scalar with an example.</li><li>(2M) Differentiate scalar and vector.</li></ul>
'''))

# ---------------- 2. Vectors ----------------
parts.append(topic('t-vectors', '2. Vectors', 'M', f'''
{sub('⭐ Importance')}<p>Building block for representing data points/features; needed to understand norms, dot products, gradients.</p>
{sub('📌 Definition')}
{box('def', 'A <b>vector</b> is an ordered array of numbers (scalars), arranged in a single row or column. A vector of size n is written as <b>x</b> ∈ ℝⁿ, x = [x₁, x₂, ..., xₙ]ᵀ. Each xᵢ is called a component/element, and i is its index.')}
{sub('🧠 Intuition')}<p>A vector can be thought of as a point in n-dimensional space, or as an arrow from the origin to that point — carrying both magnitude and direction. In ML, a vector typically represents one data sample described by n features.</p>
{sub('📖 Detailed Explanation')}<p>Vectors support element-wise operations (addition, subtraction, scalar multiplication) and the dot product. Column vectors are the default convention in deep learning (x is n×1). Indexing: x₁ is the first element; x<sub>-1</sub> sometimes denotes "all elements except the first" in set notation used by Goodfellow et al.</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'x = [x₁, x₂, …, xₙ]ᵀ &nbsp;&nbsp; x ∈ ℝⁿ <br>Addition: (x + y)ᵢ = xᵢ + yᵢ <br>Scalar multiply: (αx)ᵢ = α·xᵢ <br>Dot product: x·y = Σᵢ xᵢyᵢ (a scalar)')}
{sub('💡 Simple Example')}<p>x = [2, 4, 6], y = [1, 0, 3]. x + y = [3, 4, 9]. x·y = 2·1 + 4·0 + 6·3 = 20.</p>
{sub('🎯 Real-World/ML Example')}<p>A house described by [area, #bedrooms, age] = [1500, 3, 10] is a feature vector; a word embedding (e.g., 300-dim vector for "king") is a vector.</p>
{sub('🖼️ Diagram')}
<svg class="diagram" viewBox="0 0 300 220" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="190" x2="280" y2="190" stroke="#888" stroke-width="1"/>
<line x1="30" y1="190" x2="30" y2="20" stroke="#888" stroke-width="1"/>
<line x1="30" y1="190" x2="220" y2="60" stroke="#2f57a3" stroke-width="3" marker-end="url(#arrowhead1)"/>
<defs><marker id="arrowhead1" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="#2f57a3"/></marker></defs>
<text x="225" y="55" font-size="12" fill="#2f57a3">x = [190,130]</text>
<text x="140" y="210" font-size="11" fill="#666">Vector as arrow from origin in 2D space</text>
</svg>
<p style="font-size:.85rem;color:var(--text-soft);">Exam drawing tip: draw two axes, then one arrow from origin to point (a,b), label with the vector.</p>
{sub('✅ Advantages')}<p>Compact representation of multi-feature data; enables linear algebra operations used throughout ML (dot products for similarity, projections).</p>
{sub('❌ Limitations')}<p>Only 1-D structure — cannot capture relationships between two independent dimensions (needs matrix/tensor).</p>
{sub('🔄 Comparison with Related Concepts')}<p>Vector (1-D) vs Matrix (2-D) vs Tensor (n-D): a vector is a special case of a matrix with one column (or row).</p>
{sub('⚠️ Common Mistakes')}<p>Confusing row vector and column vector orientation when multiplying with matrices; forgetting the transpose symbol ᵀ.</p>
{sub('🧠 Important Points to Remember')}<ul><li>Vectors are rank-1 tensors.</li><li>Dot product of orthogonal vectors = 0.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul><li>(2M) What is a vector? Give an example.</li><li>(5M) Explain vector operations with examples (addition, scalar multiplication, dot product).</li></ul>
'''))

# ---------------- 3. Matrices and Tensors ----------------
parts.append(topic('t-matrices-tensors', '3. Matrices and Tensors', 'H', f'''
{sub('⭐ Importance')}<p>Core data structure of deep learning — weight matrices, batch tensors. Frequently tested with dimension/notation questions.</p>
{sub('📌 Definition')}
{box('def', 'A <b>matrix</b> A ∈ ℝ<sup>m×n</sup> is a 2-D array of numbers with m rows and n columns; element in row i, column j is A<sub>i,j</sub>. A <b>tensor</b> generalizes this to any number of dimensions (an n-dimensional array), written A<sub>i,j,k,...</sub>.')}
{sub('🧠 Intuition')}<p>A matrix is a "table" of numbers — think of a grayscale image as a matrix of pixel intensities. A tensor is a matrix extended to more axes — a color image (height × width × channels) is a rank-3 tensor; a batch of color images (batch × height × width × channels) is a rank-4 tensor.</p>
{sub('📖 Detailed Explanation')}<p>Matrices are indexed with two subscripts (row, column). Rows are extracted as A<sub>i,:</sub>, columns as A<sub>:,j</sub>. Tensors extend indexing to k subscripts. In deep learning frameworks (PyTorch/TensorFlow), all data — inputs, weights, activations, gradients — are stored as tensors; a scalar is a rank-0 tensor, vector rank-1, matrix rank-2.</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'A ∈ ℝ<sup>m×n</sup>, A = [A<sub>i,j</sub>], i=1..m, j=1..n <br>Tensor: T ∈ ℝ<sup>d₁×d₂×...×d_k</sup>, rank = k')}
{sub('💡 Simple Example')}<p>A = [[1,2,3],[4,5,6]] is a 2×3 matrix. A<sub>1,2</sub> = 2 (using 1-indexing), A<sub>2,3</sub> = 6.</p>
{sub('🎯 Real-World/ML Example')}<p>A CNN input image batch of 32 RGB images sized 64×64 is a tensor of shape (32, 64, 64, 3) — rank 4.</p>
{sub('🖼️ Diagram')}
<svg class="diagram" viewBox="0 0 420 150" xmlns="http://www.w3.org/2000/svg">
<g font-size="11" fill="#333">
<rect x="10" y="55" width="30" height="30" fill="#eef3ff" stroke="#2f57a3"/><text x="18" y="105" fill="#666">Scalar</text>
<rect x="80" y="40" width="18" height="60" fill="#eef3ff" stroke="#2f57a3"/>
<rect x="100" y="40" width="18" height="60" fill="#eef3ff" stroke="#2f57a3"/>
<rect x="120" y="40" width="18" height="60" fill="#eef3ff" stroke="#2f57a3"/>
<text x="80" y="115" fill="#666">Vector</text>
<rect x="180" y="30" width="20" height="20" fill="#eef3ff" stroke="#2f57a3"/><rect x="200" y="30" width="20" height="20" fill="#eef3ff" stroke="#2f57a3"/><rect x="220" y="30" width="20" height="20" fill="#eef3ff" stroke="#2f57a3"/>
<rect x="180" y="50" width="20" height="20" fill="#eef3ff" stroke="#2f57a3"/><rect x="200" y="50" width="20" height="20" fill="#eef3ff" stroke="#2f57a3"/><rect x="220" y="50" width="20" height="20" fill="#eef3ff" stroke="#2f57a3"/>
<rect x="180" y="70" width="20" height="20" fill="#eef3ff" stroke="#2f57a3"/><rect x="200" y="70" width="20" height="20" fill="#eef3ff" stroke="#2f57a3"/><rect x="220" y="70" width="20" height="20" fill="#eef3ff" stroke="#2f57a3"/>
<text x="185" y="105" fill="#666">Matrix</text>
<g transform="translate(290,20)">
<rect x="0" y="0" width="18" height="18" fill="#eefaf5" stroke="#0e8a6d"/><rect x="18" y="0" width="18" height="18" fill="#eefaf5" stroke="#0e8a6d"/>
<rect x="8" y="8" width="18" height="18" fill="#eefaf5" stroke="#0e8a6d" opacity="0.7"/><rect x="26" y="8" width="18" height="18" fill="#eefaf5" stroke="#0e8a6d" opacity="0.7"/>
<rect x="16" y="16" width="18" height="18" fill="#eefaf5" stroke="#0e8a6d" opacity="0.5"/><rect x="34" y="16" width="18" height="18" fill="#eefaf5" stroke="#0e8a6d" opacity="0.5"/>
</g>
<text x="290" y="115" fill="#666">Tensor (3D+)</text>
</g>
</svg>
{sub('✅ Advantages')}<p>Unified representation for all data shapes; efficient GPU parallel computation via tensor operations.</p>
{sub('❌ Limitations')}<p>Higher-rank tensors are harder to visualize and reason about; computationally expensive for very large ranks/sizes.</p>
{sub('🔄 Comparison with Related Concepts')}
<table><tr><th>Rank</th><th>Name</th><th>Example</th></tr><tr><td>0</td><td>Scalar</td><td>5</td></tr><tr><td>1</td><td>Vector</td><td>[1,2,3]</td></tr><tr><td>2</td><td>Matrix</td><td>image (grayscale)</td></tr><tr><td>≥3</td><td>Tensor</td><td>RGB image, video, batch</td></tr></table>
{sub('⚠️ Common Mistakes')}<p>Mixing up row-major vs column-major indexing; confusing matrix shape (rows×cols) order.</p>
{sub('🧠 Important Points to Remember')}<ul><li>Matrix transpose: (Aᵀ)<sub>i,j</sub> = A<sub>j,i</sub>.</li><li>Tensor rank = number of axes/indices needed.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul><li>(2M) Define matrix and tensor.</li><li>(5M) Differentiate scalar, vector, matrix, and tensor with examples and diagram.</li></ul>
'''))

# ---------------- 4. Matrix Operations ----------------
parts.append(topic('t-matrix-ops', '4. Matrix Operations', 'H', f'''
{sub('⭐ Importance')}<p>Directly tested via numerical problems (multiplication, transpose); essential for understanding neural network forward pass (Wx+b).</p>
{sub('📌 Definition')}
{box('def', 'Matrix operations include <b>addition</b>, <b>scalar multiplication</b>, <b>transpose</b>, <b>matrix multiplication</b>, and <b>matrix inverse</b> — the algebraic rules that let matrices be combined and manipulated.')}
{sub('🧠 Intuition')}<p>Matrix multiplication composes linear transformations — e.g., multiplying an input vector by a weight matrix "transforms" it into a new space (this is exactly what a neural network layer does).</p>
{sub('📖 Detailed Explanation')}<p><b>Addition:</b> element-wise, requires same shape. <b>Transpose:</b> flips rows/columns. <b>Multiplication:</b> C = AB is valid only if #columns(A) = #rows(B); C<sub>i,j</sub> = Σ<sub>k</sub> A<sub>i,k</sub>B<sub>k,j</sub>. Matrix multiplication is associative and distributive but NOT commutative (AB ≠ BA in general). <b>Inverse:</b> A⁻¹ exists only for square, non-singular (det ≠ 0) matrices, and satisfies AA⁻¹ = I.</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'C = AB ⟹ C<sub>i,j</sub> = Σ<sub>k=1</sub><sup>n</sup> A<sub>i,k</sub> B<sub>k,j</sub> <br>(AB)ᵀ = Bᵀ Aᵀ &nbsp;&nbsp; (A+B)ᵀ = Aᵀ + Bᵀ <br>AA⁻¹ = A⁻¹A = I')}
{sub('📐 Derivation')}<p>DERIVATION NOT REQUIRED — understand the rule and dimension compatibility; be ready to compute numerically.</p>
{sub('💡 Simple Example')}<p>A = [[1,2],[3,4]], B = [[5,6],[7,8]]. AB = [[1·5+2·7, 1·6+2·8],[3·5+4·7, 3·6+4·8]] = [[19,22],[43,50]].</p>
{sub('🎯 Real-World/ML Example')}<p>Forward pass of a dense layer: z = Wx + b, where W is the weight matrix, x the input vector, b the bias vector — this is matrix-vector multiplication plus addition.</p>
{sub('⚙️ Algorithm / Procedure')}<p>To multiply A(m×n) and B(n×p): for each i in 1..m, for each j in 1..p, compute C<sub>i,j</sub> as the dot product of row i of A and column j of B.</p>
{sub('📝 Pseudocode')}
<pre>for i in range(m):
  for j in range(p):
    C[i][j] = sum(A[i][k]*B[k][j] for k in range(n))</pre>
{sub('✅ Advantages')}<p>Enables compact representation of linear systems and transformations; vectorized computation is GPU-friendly.</p>
{sub('❌ Limitations')}<p>Matrix multiplication is O(n³) for naive algorithm — costly for very large matrices; not commutative, easy to misapply.</p>
{sub('🔄 Comparison with Related Concepts')}<p>Element-wise (Hadamard) product A⊙B differs from matrix multiplication AB — Hadamard requires identical shapes and multiplies corresponding entries only.</p>
{sub('⚠️ Common Mistakes')}<p>Assuming AB = BA (false in general); trying to multiply matrices with incompatible shapes; forgetting (AB)ᵀ = BᵀAᵀ (order reverses).</p>
{sub('🧠 Important Points to Remember')}<ul><li>Multiplication rule: (m×n)·(n×p) = (m×p).</li><li>Not commutative; associative and distributive.</li><li>(AB)⁻¹ = B⁻¹A⁻¹ (order reverses, when both invertible).</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul><li>(5M) Explain matrix multiplication with a numerical example.</li><li>(10M) Discuss properties of matrix operations (associativity, distributivity, commutativity, transpose rules) with proofs/examples.</li></ul>
'''))

# ---------------- 5. Types of Matrices ----------------
parts.append(topic('t-types-matrices', '5. Types of Matrices', 'M', f'''
{sub('⭐ Importance')}<p>Frequently asked as 2-mark definition/identify questions; special matrices (diagonal, symmetric, orthogonal) reappear in eigen-decomposition and SVD.</p>
{sub('📌 Definition & Types')}
<table><tr><th>Type</th><th>Definition</th></tr>
<tr><td>Square matrix</td><td>#rows = #columns (n×n)</td></tr>
<tr><td>Diagonal matrix</td><td>All off-diagonal entries are 0 (D<sub>i,j</sub>=0 for i≠j)</td></tr>
<tr><td>Identity matrix (I)</td><td>Diagonal matrix with all diagonal entries = 1; AI = A</td></tr>
<tr><td>Symmetric matrix</td><td>A = Aᵀ, i.e. A<sub>i,j</sub> = A<sub>j,i</sub></td></tr>
<tr><td>Orthogonal matrix</td><td>AᵀA = AAᵀ = I, i.e. Aᵀ = A⁻¹; rows/columns are orthonormal</td></tr>
<tr><td>Singular matrix</td><td>det(A) = 0, so A⁻¹ does not exist</td></tr>
<tr><td>Positive Definite matrix</td><td>xᵀAx &gt; 0 for all non-zero x; all eigenvalues &gt; 0</td></tr>
</table>
{sub('🧠 Intuition')}<p>Special matrices have geometric meaning: orthogonal matrices represent pure rotations/reflections (they preserve vector length); diagonal matrices scale each axis independently, making them computationally cheap.</p>
{sub('💡 Simple Example')}<p>Identity: I = [[1,0],[0,1]]. Symmetric: [[2,5],[5,3]]. Diagonal: [[4,0],[0,9]].</p>
{sub('🎯 Real-World/ML Example')}<p>Covariance matrices in PCA are always symmetric positive semi-definite; rotation matrices used in data augmentation are orthogonal.</p>
{sub('✅ Advantages')}<p>Special structure allows faster computation (e.g., inverse of diagonal matrix = reciprocal of each entry) and guarantees useful properties (orthogonal matrices preserve norms).</p>
{sub('❌ Limitations')}<p>Not all real matrices fall into these convenient categories — general (dense, asymmetric) matrices need full computation.</p>
{sub('⚠️ Common Mistakes')}<p>Confusing "symmetric" with "square" (all symmetric matrices are square, but not vice versa); assuming every square matrix is invertible.</p>
{sub('🧠 Important Points to Remember')}<ul><li>Orthogonal ⟹ Aᵀ = A⁻¹ (very testable).</li><li>Covariance matrices used in PCA are symmetric.</li><li>det(A)=0 ⟺ singular ⟺ no inverse.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul><li>(2M) Define orthogonal matrix.</li><li>(2M) What is a singular matrix?</li><li>(5M) List and explain 5 special types of matrices with examples.</li></ul>
'''))

# ---------------- 6. Norms ----------------
parts.append(topic('t-norms', '6. Norms', 'H', f'''
{sub('⭐ Importance')}<p>Direct numerical-problem topic (compute L1, L2, L∞, Frobenius norm); underlies regularization (Ch.4) and distance metrics.</p>
{sub('📌 Definition')}
{box('def', 'A <b>norm</b> is a function that measures the "size" or length of a vector. Formally, ‖x‖<sub>p</sub> is a function satisfying: (1) ‖x‖=0 ⟺ x=0, (2) ‖αx‖ = |α|‖x‖, (3) triangle inequality ‖x+y‖ ≤ ‖x‖+‖y‖.')}
{sub('🧠 Intuition')}<p>Norms generalize the everyday notion of "distance from origin". Different norms weight large vs. small components differently — L1 treats all deviations linearly (promotes sparsity), L2 penalizes large components quadratically (smooth, unique solutions).</p>
{sub('📖 Detailed Explanation')}<p>The general Lᵖ norm: ‖x‖<sub>p</sub> = (Σᵢ|xᵢ|<sup>p</sup>)<sup>1/p</sup>. Special cases: L1 (Manhattan/taxicab norm) sums absolute values; L2 (Euclidean norm) is the familiar straight-line distance; L∞ (max norm) returns the largest absolute component. The Frobenius norm extends L2 to matrices.</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'L1 norm: ‖x‖₁ = Σᵢ|xᵢ| <br>L2 norm: ‖x‖₂ = √(Σᵢ xᵢ²) <br>L∞ norm: ‖x‖<sub>∞</sub> = maxᵢ|xᵢ| <br>Frobenius norm (matrix): ‖A‖<sub>F</sub> = √(Σᵢ,ⱼ A<sub>i,j</sub>²)')}
{sub('📐 Derivation')}<p>DERIVATION NOT REQUIRED for the general norm axioms — but be ready to derive that L2² = xᵀx: ‖x‖₂² = Σᵢxᵢ² = x·x = xᵀx (used constantly in regularization derivations).</p>
{sub('💡 Simple Example')}<p>x = [3, -4]. ‖x‖₁ = 3+4 = 7. ‖x‖₂ = √(9+16) = √25 = 5. ‖x‖<sub>∞</sub> = max(3,4) = 4.</p>
{sub('🎯 Real-World/ML Example')}<p>L2 norm of weight vector is added as penalty in Ridge Regression / L2 regularization (weight decay); L1 norm penalty in Lasso induces sparse (many-zero) weights.</p>
{sub('🖼️ Diagram')}
<svg class="diagram" viewBox="0 0 260 130" xmlns="http://www.w3.org/2000/svg">
<g transform="translate(40,65)">
<line x1="-30" y1="0" x2="30" y2="0" stroke="#999"/><line x1="0" y1="-30" x2="0" y2="30" stroke="#999"/>
<polygon points="20,0 0,20 -20,0 0,-20" fill="none" stroke="#2f57a3" stroke-width="2"/>
<text x="-15" y="45" font-size="10">L1 ball (diamond)</text>
</g>
<g transform="translate(180,65)">
<line x1="-30" y1="0" x2="30" y2="0" stroke="#999"/><line x1="0" y1="-30" x2="0" y2="30" stroke="#999"/>
<circle cx="0" cy="0" r="20" fill="none" stroke="#0e8a6d" stroke-width="2"/>
<text x="-12" y="45" font-size="10">L2 ball (circle)</text>
</g>
</svg>
<p style="font-size:.85rem;color:var(--text-soft);">Exam tip: draw the diamond (L1) vs circle (L2) constraint regions — this is used to explain why L1 induces sparsity (corners touch axes).</p>
{sub('✅ Advantages')}<p>Provide a principled way to measure error/magnitude; L1 encourages sparse solutions (feature selection); L2 gives smooth, differentiable penalty with unique minimum.</p>
{sub('❌ Limitations')}<p>L1 is non-differentiable at 0 (needs sub-gradient methods); L2 does not zero-out weights, so no automatic feature selection.</p>
{sub('🔄 Comparison with Related Concepts')}
<table><tr><th>Norm</th><th>Formula</th><th>Property</th></tr>
<tr><td>L1</td><td>Σ|xᵢ|</td><td>Sparse solutions, robust to outliers</td></tr>
<tr><td>L2</td><td>√Σxᵢ²</td><td>Smooth, unique min, sensitive to outliers</td></tr>
<tr><td>L∞</td><td>max|xᵢ|</td><td>Focuses on worst-case component</td></tr></table>
{sub('⚠️ Common Mistakes')}<p>Forgetting to take square root in L2 (confusing ‖x‖₂ with ‖x‖₂²); using L1/L2 interchangeably in regularization discussion without noting sparsity difference.</p>
{sub('🧠 Important Points to Remember')}<ul><li>‖x‖₂² = xᵀx — MEMORIZE, used everywhere.</li><li>L1 → sparsity; L2 → shrinkage without sparsity.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul><li>(2M) Define L1 and L2 norm.</li><li>(5M) Compute L1, L2, L∞ norms for a given vector.</li><li>(10M) Explain norms and their role in regularization, with diagram of L1 vs L2 constraint regions.</li></ul>
'''))

with open('/home/claude/ch1_part1.html','w') as f:
    f.write(''.join(parts))
print("ch1 part1 written, length:", len(''.join(parts)))
