# -*- coding: utf-8 -*-

from pathlib import Path
import re

INPUT = Path("deep_learning_complete_notes_FINAL.html")
OUTPUT = Path("deep_learning_complete_notes_COMPLETE.html")

if not INPUT.exists():
    raise FileNotFoundError(
        "deep_learning_complete_notes_FINAL.html not found."
    )

html = INPUT.read_text(encoding="utf-8")


# ============================================================
# COMPLETE SIDEBAR
# ============================================================

sidebar = r'''
<div class="sidebar-content">

    <div class="sidebar-title">
        📚 Complete Syllabus
    </div>

    <a href="#unit1" class="unit-link">
        UNIT–1
    </a>

    <div class="chapter-group">
        <div class="chapter-title">
            Chapter 1 — Linear Algebra
        </div>

        <a href="#t-scalars" class="topic-link">Scalars</a>
        <a href="#t-vectors" class="topic-link">Vectors</a>
        <a href="#t-matrices" class="topic-link">Matrices and Tensors</a>
        <a href="#t-matrix-ops" class="topic-link">Matrix Operations</a>
        <a href="#t-matrix-types" class="topic-link">Types of Matrices</a>
        <a href="#t-norms" class="topic-link">Norms</a>
        <a href="#t-eigen" class="topic-link">Eigen Decomposition</a>
        <a href="#t-svd" class="topic-link">Singular Value Decomposition</a>
        <a href="#t-pca" class="topic-link">Principal Component Analysis</a>
    </div>

    <div class="chapter-group">
        <div class="chapter-title">
            Chapter 2 — Probability and Information Theory
        </div>

        <a href="#t-random" class="topic-link">Random Variables</a>
        <a href="#t-distributions" class="topic-link">Probability Distributions</a>
        <a href="#t-marginal" class="topic-link">Marginal Probability</a>
        <a href="#t-conditional" class="topic-link">Conditional Probability</a>
        <a href="#t-expectation" class="topic-link">Expectation</a>
        <a href="#t-variance" class="topic-link">Variance and Covariance</a>
        <a href="#t-bayes" class="topic-link">Bayes' Rule</a>
        <a href="#t-information" class="topic-link">Information Theory</a>
    </div>

    <div class="chapter-group">
        <div class="chapter-title">
            Chapter 3 — Numerical Computation
        </div>

        <a href="#t-overflow" class="topic-link">Overflow and Underflow</a>
        <a href="#t-gradient" class="topic-link">Gradient-Based Optimization</a>
        <a href="#t-constrained" class="topic-link">Constrained Optimization</a>
        <a href="#t-least" class="topic-link">Linear Least Squares</a>
    </div>


    <a href="#unit2" class="unit-link">
        UNIT–2
    </a>

    <div class="chapter-group">
        <div class="chapter-title">
            Chapter 5 — Machine Learning
        </div>

        <a href="#t-ml-basics" class="topic-link">Basics and Underfitting</a>
        <a href="#t-hyperparameters" class="topic-link">Hyperparameters and Validation Sets</a>
        <a href="#t-estimators" class="topic-link">Estimators</a>
        <a href="#t-bias-variance" class="topic-link">Bias and Variance</a>
        <a href="#t-mle" class="topic-link">Maximum Likelihood</a>
        <a href="#t-bayesian" class="topic-link">Bayesian Statistics</a>
        <a href="#t-supervised" class="topic-link">Supervised Learning</a>
        <a href="#t-unsupervised" class="topic-link">Unsupervised Learning</a>
        <a href="#t-sgd" class="topic-link">Stochastic Gradient Descent</a>
        <a href="#t-motivating" class="topic-link">Challenges Motivating Deep Learning</a>
    </div>

    <div class="chapter-group">
        <div class="chapter-title">
            Chapter 6 — Deep Feedforward Networks
        </div>

        <a href="#t-xor" class="topic-link">Learning XOR</a>
        <a href="#t-gradient-learning" class="topic-link">Gradient-Based Learning</a>
        <a href="#t-hidden" class="topic-link">Hidden Units</a>
        <a href="#t-architecture" class="topic-link">Architecture Design</a>
        <a href="#t-backprop" class="topic-link">Back-Propagation</a>
        <a href="#t-differentiation" class="topic-link">
            Other Differentiation Algorithms
        </a>
    </div>


    <a href="#unit3" class="unit-link">
        UNIT–3
    </a>

    <div class="chapter-group">
        <div class="chapter-title">
            Chapter 4 — Regularization for Deep Learning
        </div>

        <a href="#t-param-norm" class="topic-link">Parameter Norm Penalties</a>
        <a href="#t-constrained-reg" class="topic-link">Norm Penalties as Constrained Optimization</a>
        <a href="#t-underconstrained" class="topic-link">Regularization and Under-Constrained Problems</a>
        <a href="#t-augmentation" class="topic-link">Dataset Augmentation</a>
        <a href="#t-noise" class="topic-link">Noise Robustness</a>
        <a href="#t-semi" class="topic-link">Semi-Supervised Learning</a>
        <a href="#t-multitask" class="topic-link">Multi-Task Learning</a>
        <a href="#t-early" class="topic-link">Early Stopping</a>
        <a href="#t-parameter-sharing" class="topic-link">Parameter Tying and Parameter Sharing</a>
        <a href="#t-sparse" class="topic-link">Sparse Representations</a>
        <a href="#t-bagging" class="topic-link">Bagging and Other Ensemble Methods</a>
        <a href="#t-dropout" class="topic-link">Dropout</a>
        <a href="#t-adversarial" class="topic-link">Adversarial Training</a>
        <a href="#t-tangent-distance" class="topic-link">Tangent Distance</a>
        <a href="#t-tangent-prop" class="topic-link">Tangent Prop</a>
        <a href="#t-manifold" class="topic-link">Manifold Tangent Classifiers</a>
    </div>

    <div class="chapter-group">
        <div class="chapter-title">
            Chapter 5 — Optimization for Training Deep Models
        </div>

        <a href="#t-pure-opt" class="topic-link">Pure Optimization</a>
        <a href="#t-challenges" class="topic-link">Challenges in Neural Network Optimization</a>
        <a href="#t-basic-algorithms" class="topic-link">Basic Algorithms</a>
        <a href="#t-initialization" class="topic-link">Parameter Initialization Strategies</a>
        <a href="#t-adaptive" class="topic-link">Algorithms with Adaptive Learning Rates</a>
        <a href="#t-second-order" class="topic-link">Approximate Second-Order Methods</a>
        <a href="#t-meta" class="topic-link">Optimization Strategies and Meta-Algorithms</a>
    </div>

</div>
'''


# ============================================================
# FIND SIDEBAR
# ============================================================

sidebar_patterns = [
    r'<aside[^>]*id=["\']sidebar["\'][^>]*>.*?</aside>',
    r'<div[^>]*id=["\']sidebar["\'][^>]*>.*?</div>',
]


new_html = None

for pattern in sidebar_patterns:
    match = re.search(
        pattern,
        html,
        flags=re.IGNORECASE | re.DOTALL
    )

    if match:
        opening = re.search(
            r'<(?:aside|div)[^>]*id=["\']sidebar["\'][^>]*>',
            match.group(0),
            flags=re.IGNORECASE
        )

        if opening:
            replacement = (
                opening.group(0)
                + sidebar
                + "</"
                + ("aside" if opening.group(0).lower().startswith("<aside")
                   else "div")
                + ">"
            )

            new_html = (
                html[:match.start()]
                + replacement
                + html[match.end():]
            )

            break


# ============================================================
# FALLBACK
# ============================================================

if new_html is None:

    print("Existing sidebar structure not detected.")
    print("Adding navigation block before the main content.")

    marker = '<div id="content">'

    if marker in html:
        new_html = html.replace(
            marker,
            sidebar + "\n" + marker,
            1
        )
    else:
        raise RuntimeError(
            "Could not find sidebar or content container."
        )


# ============================================================
# ADD UNIT IDS IF POSSIBLE
# ============================================================

new_html = new_html.replace(
    '<section class="unit-section">',
    '<section class="unit-section" id="unit2">',
    1
)

new_html = new_html.replace(
    '<section class="unit-section">',
    '<section class="unit-section" id="unit3">',
    1
)


# ============================================================
# WRITE OUTPUT
# ============================================================

OUTPUT.write_text(
    new_html,
    encoding="utf-8"
)


print()
print("=" * 60)
print("        NAVIGATION UPDATE COMPLETE")
print("=" * 60)
print()
print("Created:")
print(OUTPUT)
print()
print("Size:", OUTPUT.stat().st_size, "bytes")
print()
print("✓ Complete syllabus navigation")
print("✓ Unit 1")
print("✓ Unit 2")
print("✓ Unit 3")
print("✓ Chapter/topic links")
print("✓ Original FINAL HTML preserved")
print("=" * 60)