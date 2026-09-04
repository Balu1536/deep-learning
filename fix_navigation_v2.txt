# -*- coding: utf-8 -*-

from pathlib import Path
import re

INPUT = Path("deep_learning_complete_notes_FINAL.html")
OUTPUT = Path("deep_learning_complete_notes_FINAL_V2.html")

html = INPUT.read_text(encoding="utf-8")


# ============================================================
# UNIT 2 + UNIT 3 NAVIGATION
# ============================================================

new_navigation = r'''
<br>

<div class="nav-unit-title">
    <a href="#unit2">UNIT 2</a>
</div>

<div class="nav-chapter">
    <a href="#unit2-ch5">
        <b>Chapter 5: Machine Learning</b>
    </a>

    <a href="#t-ml-basics">1. Basics and Underfitting</a>
    <a href="#t-hyperparameters">2. Hyperparameters and Validation Sets</a>
    <a href="#t-estimators">3. Estimators</a>
    <a href="#t-bias-variance">4. Bias and Variance</a>
    <a href="#t-mle">5. Maximum Likelihood</a>
    <a href="#t-bayesian">6. Bayesian Statistics</a>
    <a href="#t-supervised">7. Supervised Learning</a>
    <a href="#t-unsupervised">8. Unsupervised Learning</a>
    <a href="#t-sgd">9. Stochastic Gradient Descent</a>
    <a href="#t-motivating">10. Challenges Motivating Deep Learning</a>
</div>

<div class="nav-chapter">
    <a href="#unit2-ch6">
        <b>Chapter 6: Deep Feedforward Networks</b>
    </a>

    <a href="#t-xor">1. Learning XOR</a>
    <a href="#t-gradient-learning">2. Gradient-Based Learning</a>
    <a href="#t-hidden">3. Hidden Units</a>
    <a href="#t-architecture">4. Architecture Design</a>
    <a href="#t-backprop">5. Back-Propagation</a>
    <a href="#t-differentiation">6. Other Differentiation Algorithms</a>
</div>

<a href="#unit2-revision">
    <b>📚 Unit 2 Revision</b>
</a>


<br>

<div class="nav-unit-title">
    <a href="#unit3">UNIT 3</a>
</div>

<div class="nav-chapter">
    <a href="#unit3-ch4">
        <b>Chapter 4: Regularization for Deep Learning</b>
    </a>

    <a href="#t-param-norm">1. Parameter Norm Penalties</a>
    <a href="#t-constrained-reg">2. Norm Penalties as Constrained Optimization</a>
    <a href="#t-underconstrained">3. Regularization and Under-Constrained Problems</a>
    <a href="#t-augmentation">4. Dataset Augmentation</a>
    <a href="#t-noise">5. Noise Robustness</a>
    <a href="#t-semi">6. Semi-Supervised Learning</a>
    <a href="#t-multitask">7. Multi-Task Learning</a>
    <a href="#t-early">8. Early Stopping</a>
    <a href="#t-parameter-sharing">9. Parameter Tying and Parameter Sharing</a>
    <a href="#t-sparse">10. Sparse Representations</a>
    <a href="#t-bagging">11. Bagging and Other Ensemble Methods</a>
    <a href="#t-dropout">12. Dropout</a>
    <a href="#t-adversarial">13. Adversarial Training</a>
    <a href="#t-tangent-distance">14. Tangent Distance</a>
    <a href="#t-tangent-prop">15. Tangent Prop</a>
    <a href="#t-manifold">16. Manifold Tangent Classifiers</a>
</div>

<div class="nav-chapter">
    <a href="#unit3-ch5">
        <b>Chapter 5: Optimization for Training Deep Models</b>
    </a>

    <a href="#t-pure-opt">1. Pure Optimization</a>
    <a href="#t-challenges">2. Challenges in Neural Network Optimization</a>
    <a href="#t-basic-algorithms">3. Basic Algorithms</a>
    <a href="#t-initialization">4. Parameter Initialization Strategies</a>
    <a href="#t-adaptive">5. Algorithms with Adaptive Learning Rates</a>
    <a href="#t-second-order">6. Approximate Second-Order Methods</a>
    <a href="#t-meta">7. Optimization Strategies and Meta-Algorithms</a>
</div>

<a href="#unit3-revision">
    <b>📚 Unit 3 Revision</b>
</a>
'''


# ============================================================
# INSERT AFTER UNIT 1 REVISION LINK
# ============================================================

pattern = re.compile(
    r'(<a\s+href="#unit1-revision"[^>]*>.*?</a>)',
    re.IGNORECASE | re.DOTALL
)

match = pattern.search(html)

if not match:
    raise RuntimeError(
        "Could not find the existing Unit 1 Revision navigation link."
    )

html = (
    html[:match.end()]
    + "\n"
    + new_navigation
    + html[match.end():]
)


# ============================================================
# ADD ANCHORS TO UNIT 2/3 SECTIONS
# ============================================================

# Add useful navigation anchors immediately before our
# generated unit sections.

html = html.replace(
    '<section class="unit-section">',
    '<div id="unit2"></div><section class="unit-section">',
    1
)

html = html.replace(
    '<section class="unit-section">',
    '<div id="unit3"></div><section class="unit-section">',
    1
)


# ============================================================
# WRITE
# ============================================================

OUTPUT.write_text(
    html,
    encoding="utf-8"
)

print()
print("=" * 60)
print("       NAVIGATION V2 CREATED")
print("=" * 60)
print()
print("Created:")
print(OUTPUT)
print()
print("✓ Existing Unit 1 navigation preserved")
print("✓ Unit 2 navigation added")
print("✓ Unit 3 navigation added")
print("✓ Chapter/topic links added")
print("✓ Original file preserved")
print("=" * 60)