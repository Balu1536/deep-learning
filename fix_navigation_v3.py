# -*- coding: utf-8 -*-
from pathlib import Path
import re

INPUT = Path("deep_learning_complete_notes_FINAL_V2.html")
OUTPUT = Path("deep_learning_complete_notes_FINAL_V3.html")

if not INPUT.exists():
    raise FileNotFoundError("deep_learning_complete_notes_FINAL.html not found.")

html = INPUT.read_text(encoding="utf-8")

sidebar = r"""
<nav id="sidebar">
  <h1>📘 DL/ML Study Portal</h1>
  <input type="text" id="searchBox" placeholder="🔍 Search all topics...">
  <div id="searchResults"></div>
  <div id="navTree">

  <div class="unit-title">Unit 1</div>
  <a href="#unit1" class="chapter-link">UNIT 1 Overview</a>
  <a href="#ch1" class="chapter-link">Chapter 1: Linear Algebra</a>
  <a href="#t-scalars" class="topic-link">1. Scalars</a>
  <a href="#t-vectors" class="topic-link">2. Vectors</a>
  <a href="#t-matrices-tensors" class="topic-link">3. Matrices and Tensors</a>
  <a href="#t-matrix-ops" class="topic-link">4. Matrix Operations</a>
  <a href="#t-types-matrices" class="topic-link">5. Types of Matrices</a>
  <a href="#t-norms" class="topic-link">6. Norms</a>
  <a href="#t-eigen" class="topic-link">7. Eigen Decomposition</a>
  <a href="#t-svd" class="topic-link">8. SVD</a>
  <a href="#t-pca" class="topic-link">9. PCA</a>

  <a href="#ch2" class="chapter-link">Chapter 2: Probability &amp; Info Theory</a>
  <a href="#t-random-variables" class="topic-link">1. Random Variables</a>
  <a href="#t-prob-dist" class="topic-link">2. Probability Distributions</a>
  <a href="#t-marginal" class="topic-link">3. Marginal Probability</a>
  <a href="#t-conditional" class="topic-link">4. Conditional Probability</a>
  <a href="#t-expectation" class="topic-link">5. Expectation</a>
  <a href="#t-var-cov" class="topic-link">6. Variance and Covariance</a>
  <a href="#t-bayes" class="topic-link">7. Bayes' Rule</a>
  <a href="#t-info-theory" class="topic-link">8. Information Theory</a>

  <a href="#ch3" class="chapter-link">Chapter 3: Numerical Computation</a>
  <a href="#t-overflow-underflow" class="topic-link">1. Overflow and Underflow</a>
  <a href="#t-gradient-opt" class="topic-link">2. Gradient-Based Optimization</a>
  <a href="#t-constrained-opt" class="topic-link">3. Constrained Optimization</a>
  <a href="#t-least-squares" class="topic-link">4. Linear Least Squares</a>
  <a href="#unit1-revision" class="chapter-link">📚 Unit 1 Revision</a>

  <div class="unit-title">Unit 2</div>
  <a href="#unit2" class="chapter-link">UNIT 2 Overview</a>
  <a href="#unit2-ch5" class="chapter-link">Chapter 5: Machine Learning</a>
  <a href="#t-basics-underfitting" class="topic-link">1. Basics and Underfitting</a>
  <a href="#t-hyperparams" class="topic-link">2. Hyperparameters and Validation Sets</a>
  <a href="#t-estimators" class="topic-link">3. Estimators</a>
  <a href="#t-bias-variance" class="topic-link">4. Bias and Variance</a>
  <a href="#t-mle" class="topic-link">5. Maximum Likelihood</a>
  <a href="#t-bayesian-stats" class="topic-link">6. Bayesian Statistics</a>
  <a href="#t-supervised" class="topic-link">7. Supervised Learning</a>
  <a href="#t-unsupervised" class="topic-link">8. Unsupervised Learning</a>
  <a href="#t-sgd" class="topic-link">9. Stochastic Gradient Descent</a>
  <a href="#t-challenges-dl" class="topic-link">10. Challenges Motivating Deep Learning</a>

  <a href="#unit2-ch6" class="chapter-link">Chapter 6: Deep Feedforward Networks</a>
  <a href="#t-xor" class="topic-link">1. Learning XOR</a>
  <a href="#t-gradient-based-learning" class="topic-link">2. Gradient-Based Learning</a>
  <a href="#t-hidden-units" class="topic-link">3. Hidden Units</a>
  <a href="#t-architecture-design" class="topic-link">4. Architecture Design</a>
  <a href="#t-backprop" class="topic-link">5. Back-Propagation</a>
  <a href="#t-differentiation" class="topic-link">6. Other Differentiation Algorithms</a>
  <a href="#unit2-revision" class="chapter-link">📚 Unit 2 Revision</a>

  <div class="unit-title">Unit 3</div>
  <a href="#unit3" class="chapter-link">UNIT 3 Overview</a>
  <a href="#unit3-ch4" class="chapter-link">Chapter 4: Regularization for Deep Learning</a>
  <a href="#t-param-norm" class="topic-link">1. Parameter Norm Penalties</a>
  <a href="#t-constrained-reg" class="topic-link">2. Norm Penalties as Constrained Optimization</a>
  <a href="#t-underconstrained" class="topic-link">3. Regularization and Under-Constrained Problems</a>
  <a href="#t-augmentation" class="topic-link">4. Dataset Augmentation</a>
  <a href="#t-noise" class="topic-link">5. Noise Robustness</a>
  <a href="#t-semi-supervised" class="topic-link">6. Semi-Supervised Learning</a>
  <a href="#t-multitask" class="topic-link">7. Multi-Task Learning</a>
  <a href="#t-early-stop" class="topic-link">8. Early Stopping</a>
  <a href="#t-parameter-sharing" class="topic-link">9. Parameter Tying and Parameter Sharing</a>
  <a href="#t-sparse" class="topic-link">10. Sparse Representations</a>
  <a href="#t-bagging" class="topic-link">11. Bagging and Other Ensemble Methods</a>
  <a href="#t-dropout" class="topic-link">12. Dropout</a>
  <a href="#t-adversarial" class="topic-link">13. Adversarial Training</a>
  <a href="#t-tangent-distance" class="topic-link">14. Tangent Distance</a>
  <a href="#t-tangent-prop" class="topic-link">15. Tangent Prop</a>
  <a href="#t-manifold" class="topic-link">16. Manifold Tangent Classifiers</a>

  <a href="#unit3-ch5" class="chapter-link">Chapter 5: Optimization for Training Deep Models</a>
  <a href="#t-pure-opt" class="topic-link">1. Pure Optimization</a>
  <a href="#t-challenges" class="topic-link">2. Challenges in Neural Network Optimization</a>
  <a href="#t-basic-algorithms" class="topic-link">3. Basic Algorithms</a>
  <a href="#t-initialization" class="topic-link">4. Parameter Initialization Strategies</a>
  <a href="#t-adaptive" class="topic-link">5. Algorithms with Adaptive Learning Rates</a>
  <a href="#t-second-order" class="topic-link">6. Approximate Second-Order Methods</a>
  <a href="#t-meta" class="topic-link">7. Optimization Strategies and Meta-Algorithms</a>
  <a href="#unit3-revision" class="chapter-link">📚 Unit 3 Revision</a>

  </div>
</nav>
"""

pattern = re.compile(r"""<nav\s+id=["']sidebar["'][^>]*>.*?</nav>""", re.I | re.S)
match = pattern.search(html)
if not match:
    raise RuntimeError('Could not find <nav id="sidebar"> in FINAL HTML.')

html = html[:match.start()] + sidebar + html[match.end():]

# Verify every navigation target exists somewhere in the body.
targets = re.findall(r'href="#([^"]+)"', sidebar)
missing = [
    x for x in targets
    if not re.search(r"id=[\"']" + re.escape(x) + r"[\"']", html)
]
if missing:
    raise RuntimeError("Broken navigation targets: " + ", ".join(missing))

OUTPUT.write_text(html, encoding="utf-8")

print("=" * 65)
print("NAVIGATION V3 CREATED SUCCESSFULLY")
print("=" * 65)
print(f"Created: {OUTPUT}")
print(f"Navigation links checked: {len(targets)}")
print("✓ Unit 1: all topics")
print("✓ Unit 2: all topics")
print("✓ Unit 3: all topics")
print("✓ Every navigation target verified against body IDs")
print("✓ Body/content preserved")
print("✓ Original FINAL HTML preserved")
print("=" * 65)
