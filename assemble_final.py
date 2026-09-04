import os
import runpy
import builtins
import re

BASE = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE, "_chapter_output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Redirect old /home/claude output paths to our local output folder
_original_open = builtins.open

def redirected_open(file, mode="r", *args, **kwargs):
    if isinstance(file, str) and file.startswith("/home/claude/"):
        filename = os.path.basename(file)
        file = os.path.join(OUTPUT_DIR, filename)

    if "b" not in mode:
        kwargs.setdefault("encoding", "utf-8")

    return _original_open(file, mode, *args, **kwargs)

builtins.open = redirected_open


def run_source(py_file):
    print(f"Processing: {py_file}")

    path = os.path.join(BASE, py_file)

    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing source: {py_file}")

    runpy.run_path(path, run_name="__main__")


def load_html(filename):
    # First check _chapter_output
    path = os.path.join(OUTPUT_DIR, filename)

    # If not there, check the main DL folder
    if not os.path.exists(path):
        path = os.path.join(BASE, filename)

    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Generated file not found in either location: {filename}"
        )

    with _original_open(path, "r", encoding="utf-8") as f:
        return f.read()
# ============================================================
# RUN UNIT 2 SOURCES
# ============================================================

run_source("ch5ml_part1.py")
run_source("ch5ml_part2.py")
run_source("ch6_part1.py")
run_source("ch6_part2.py")

# ============================================================
# RUN UNIT 3 SOURCES
# ============================================================

run_source("ch4_regularization.py")
run_source("ch5_optimization.py")


# ============================================================
# LOAD ORIGINAL COMPLETE HTML
# ============================================================

original_path = os.path.join(BASE, "deep_learning_complete_notes.html")

with _original_open(original_path, "r", encoding="utf-8") as f:
    html = f.read()


# ============================================================
# LOAD GENERATED CHAPTER CONTENT
# ============================================================

ch5ml_1 = load_html("ch5ml_part1.html")
ch5ml_2 = load_html("ch5ml_part2.html")
ch6_1 = load_html("ch6_part1.html")
ch6_2 = load_html("ch6_part2.html")
ch4 = load_html("ch4_regularization.html")
ch5opt = load_html("ch5_optimization.html")


# ============================================================
# BUILD UNIT 2
# ============================================================

unit2 = """
<section class="unit-section" id="unit2">

<h2>UNIT 2</h2>

<section class="chapter-section" id="unit2-ch5">
<h2>Chapter 5: Machine Learning</h2>
""" + ch5ml_1 + ch5ml_2 + """
</section>

<section class="chapter-section" id="unit2-ch6">
<h2>Chapter 6: Deep Feedforward Networks</h2>
""" + ch6_1 + ch6_2 + """
</section>

<div id="unit2-revision" class="revision-section">
<h2>📚 Unit 2 Revision</h2>

<h3>Important Topics</h3>
<ul>
<li>Machine Learning basics and underfitting</li>
<li>Hyperparameters and validation sets</li>
<li>Bias and variance</li>
<li>Maximum likelihood and Bayesian statistics</li>
<li>Supervised and unsupervised learning</li>
<li>Stochastic Gradient Descent</li>
<li>Challenges motivating deep learning</li>
<li>Learning XOR</li>
<li>Gradient-based learning</li>
<li>Hidden units</li>
<li>Architecture design</li>
<li>Back-Propagation</li>
<li>Other Differentiation Algorithms</li>
</ul>

</div>

</section>
"""


# ============================================================
# BUILD UNIT 3
# ============================================================

unit3 = """
<section class="unit-section" id="unit3">

<h2>UNIT 3</h2>

<section class="chapter-section" id="unit3-ch4">
<h2>Chapter 4: Regularization for Deep Learning</h2>
""" + ch4 + """
</section>

<section class="chapter-section" id="unit3-ch5">
<h2>Chapter 5: Optimization for Training Deep Models</h2>
""" + ch5opt + """
</section>

<div id="unit3-revision" class="revision-section">
<h2>📚 Unit 3 Revision</h2>

<h3>Important Topics</h3>
<ul>
<li>Parameter norm penalties</li>
<li>Dataset augmentation</li>
<li>Noise robustness</li>
<li>Early stopping</li>
<li>Parameter tying and parameter sharing</li>
<li>Sparse representations</li>
<li>Bagging and ensemble methods</li>
<li>Dropout</li>
<li>Adversarial training</li>
<li>Tangent distance and Tangent Prop</li>
<li>Manifold Tangent Classifiers</li>
<li>Pure optimization</li>
<li>Neural network optimization challenges</li>
<li>Basic optimization algorithms</li>
<li>Parameter initialization</li>
<li>Adaptive learning rates</li>
<li>Approximate second-order methods</li>
<li>Optimization strategies and meta-algorithms</li>
</ul>

</div>

</section>
"""


# ============================================================
# INSERT AFTER UNIT 1 REVISION
# ============================================================

marker = '<!-- CONTENT_INSERT_POINT -->'

if marker not in html:
    raise RuntimeError("CONTENT_INSERT_POINT not found in original HTML.")

html = html.replace(
    marker,
    unit2 + "\n" + unit3 + "\n" + marker,
    1
)


# ============================================================
# FIX NAVIGATION IDs
# ============================================================

replacements = {
    "#t-ml-basics": "#t-basics-underfitting",
    "#t-hyperparameters": "#t-hyperparams",
    "#t-bayesian": "#t-bayesian-stats",
    "#t-motivating": "#t-challenges-dl",
    "#t-gradient-learning": "#t-gradient-based-learning",
    "#t-hidden": "#t-hidden-units",
    "#t-architecture": "#t-architecture-design",
}

for old, new in replacements.items():
    html = html.replace(f'href="{old}"', f'href="{new}"')


# ============================================================
# WRITE FINAL FILE
# ============================================================

final_path = os.path.join(
    BASE,
    "deep_learning_complete_notes_FINAL_V2.html"
)

with _original_open(final_path, "w", encoding="utf-8") as f:
    f.write(html)


# ============================================================
# VERIFICATION
# ============================================================

print()
print("=" * 60)
print("FINAL HTML ASSEMBLY COMPLETE")
print("=" * 60)
print("Created:", os.path.basename(final_path))
print("Size:", os.path.getsize(final_path), "bytes")

checks = [
    "t-backprop",
    "t-differentiation",
    "t-architecture-design",
    "t-param-norm",
    "t-pure-opt",
    "unit2",
    "unit3",
    "unit2-revision",
    "unit3-revision",
]

print()
print("CONTENT CHECK:")

for item in checks:
    if item in html:
        print("✓", item)
    else:
        print("✗ MISSING:", item)

print()
print("Original HTML was NOT overwritten.")