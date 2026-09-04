# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/home/claude')
from gen_helpers import topic, sub, box, chapter_header

parts = [chapter_header('ch2', 'Chapter 2: Probability and Information Theory')]

parts.append(topic('t-random-variables', '1. Random Variables', 'M', f'''
{sub('⭐ Importance')}<p>Foundational vocabulary — usually a 2-mark definition question, but essential to understand every other topic in this chapter.</p>
{sub('📌 Definition')}
{box('def', 'A <b>random variable</b> X is a variable that can take on different values randomly/stochastically, each with an associated probability. It can be <b>discrete</b> (finite/countable set of values, e.g., dice roll) or <b>continuous</b> (uncountably infinite values over an interval, e.g., height, temperature).')}
{sub('🧠 Intuition')}<p>A random variable is a rule that maps outcomes of a random process to numbers. It does not have a fixed value — instead it is described by how likely each of its possible values is.</p>
{sub('📖 Detailed Explanation')}<p>Discrete random variables are described by a Probability Mass Function (PMF), P(X=x); continuous random variables are described by a Probability Density Function (PDF), p(x), where probability is obtained by integrating over an interval (P(a≤X≤b) = ∫ₐᵇ p(x)dx). Random variables are usually written with uppercase letters (X), and their possible realizations with lowercase (x).</p>
{sub('💡 Simple Example')}<p>X = outcome of a fair die roll: X ∈ {{1,2,3,4,5,6}}, each with probability 1/6 (discrete). Y = height of a randomly selected student (continuous).</p>
{sub('🎯 Real-World/ML Example')}<p>In classification, the true class label Y and predicted probability output of a softmax layer are treated as random variables; in generative models, pixel values of an image are modeled as random variables.</p>
{sub('✅ Advantages')}<p>Provides rigorous mathematical language for describing uncertainty, which is central to ML (noisy data, uncertain predictions).</p>
{sub('❌ Limitations')}<p>Requires knowing/estimating the underlying distribution, which is often unknown in practice and must be approximated from data.</p>
{sub('⚠️ Common Mistakes')}<p>Confusing a random variable (the function/rule) with its realization (a specific observed value); treating PDF values as probabilities directly (a PDF value can exceed 1; only the integral gives probability).</p>
{sub('🧠 Important Points to Remember')}<ul><li>Discrete → PMF; Continuous → PDF.</li><li>Σ P(x)=1 for discrete; ∫p(x)dx=1 for continuous.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul><li>(2M) Define random variable with example.</li><li>(2M) Differentiate discrete and continuous random variables.</li></ul>
'''))

parts.append(topic('t-prob-dist', '2. Probability Distributions', 'H', f'''
{sub('⭐ Importance')}<p>Commonly tested — need to know PMF/PDF properties and common named distributions (Bernoulli, Gaussian).</p>
{sub('📌 Definition')}
{box('def', 'A <b>probability distribution</b> describes how likely a random variable is to take on each of its possible values. For discrete variables this is the PMF P(X=x); for continuous variables this is the PDF p(x).')}
{sub('🧠 Intuition')}<p>A distribution is the complete "shape" describing uncertainty about a variable — e.g. a bell curve (Gaussian) says values near the mean are most likely, with likelihood falling off symmetrically.</p>
{sub('📖 Detailed Explanation')}<p>Key properties: PMF requires P(x)≥0 for all x, and Σₓ P(x)=1. PDF requires p(x)≥0, and ∫p(x)dx=1 (note p(x) itself is NOT a probability — only areas under the curve are). Common distributions in ML: <b>Bernoulli</b> (single binary trial, P(X=1)=φ), <b>Gaussian/Normal</b> N(μ,σ²) (bell curve, most common assumption for continuous noise), <b>Multinoulli/Categorical</b> (generalizes Bernoulli to K categories, used in softmax outputs), <b>Uniform</b> (equal probability over a range).</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'Bernoulli: P(X=x) = φ<sup>x</sup>(1−φ)<sup>1−x</sup>, x∈{{0,1}} <br>Gaussian PDF: p(x) = (1/√(2πσ²)) · exp(−(x−μ)²/(2σ²))')}
{sub('💡 Simple Example')}<p>Coin toss: Bernoulli with φ=0.5. Exam scores approximated as Gaussian with μ=70, σ=10.</p>
{sub('🎯 Real-World/ML Example')}<p>Binary classification output modeled as Bernoulli; weight initialization sampled from Gaussian/Uniform distribution; softmax output modeled as Multinoulli (categorical) distribution over classes.</p>
{sub('🖼️ Diagram')}
<svg class="diagram" viewBox="0 0 260 110" xmlns="http://www.w3.org/2000/svg">
<path d="M20,90 C60,90 70,10 130,10 C190,10 200,90 240,90" fill="none" stroke="#2f57a3" stroke-width="2"/>
<line x1="10" y1="90" x2="250" y2="90" stroke="#999"/>
<text x="110" y="105" font-size="10">Gaussian (bell curve) PDF</text>
</svg>
{sub('✅ Advantages')}<p>Compactly encodes all uncertainty information about a variable; Gaussian assumption enables closed-form solutions in many ML algorithms.</p>
{sub('❌ Limitations')}<p>Real data may not fit any standard named distribution; wrong distributional assumptions bias model results.</p>
{sub('🔄 Comparison with Related Concepts')}<p>PMF (discrete, sums to 1) vs PDF (continuous, integrates to 1) — a key distinction tested frequently.</p>
{sub('⚠️ Common Mistakes')}<p>Treating PDF value p(x) as a probability (it can be &gt;1); forgetting normalization constraint.</p>
{sub('🧠 Important Points to Remember')}<ul><li>PMF: Σ=1. PDF: ∫=1.</li><li>Bernoulli → binary; Multinoulli → multi-class categorical.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul><li>(2M) Define PMF and PDF.</li><li>(5M) Explain Bernoulli and Gaussian distribution with formula and use in ML.</li></ul>
'''))

parts.append(topic('t-marginal', '3. Marginal Probability', 'M', f'''
{sub('⭐ Importance')}<p>Conceptually simple, tested as 2-mark definition + small numerical using a joint probability table.</p>
{sub('📌 Definition')}
{box('def', 'Given a joint distribution over a set of variables, the <b>marginal probability distribution</b> of a subset is obtained by summing (discrete) or integrating (continuous) over all possible values of the remaining variables. This is also called the <b>sum rule</b>.')}
{sub('🧠 Intuition')}<p>If you know the full joint probability table of two variables, "marginalizing out" one variable means adding along its rows/columns to get the distribution of the other variable alone, ignoring the first.</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'Discrete: P(X=x) = Σ_y P(X=x, Y=y) <br>Continuous: p(x) = ∫ p(x,y) dy')}
{sub('💡 Simple Example')}
{box('example', '''Joint table P(X,Y):<br>
P(X=0,Y=0)=0.1, P(X=0,Y=1)=0.2, P(X=1,Y=0)=0.3, P(X=1,Y=1)=0.4.<br>
Marginal P(X=0) = 0.1+0.2 = 0.3. Marginal P(X=1) = 0.3+0.4 = 0.7.''')}
{sub('🎯 Real-World/ML Example')}<p>Given the joint distribution of (weather, whether-a-match-is-played), the marginal probability of "match played" is obtained by summing over all weather conditions.</p>
{sub('✅ Advantages')}<p>Lets us reason about a single variable of interest, ignoring nuisance variables, without losing information encoded by the joint distribution.</p>
{sub('❌ Limitations')}<p>Requires full knowledge of the joint distribution, which may be expensive/impossible to compute for many variables (curse of dimensionality).</p>
{sub('🔄 Comparison with Related Concepts')}<p>Marginal probability (sum rule) vs Conditional probability (which additionally divides by a marginal, see next topic).</p>
{sub('⚠️ Common Mistakes')}<p>Forgetting to sum over ALL values of the marginalized variable; confusing marginal with conditional probability.</p>
{sub('🧠 Important Points to Remember')}<ul><li>Sum rule: P(x) = Σ_y P(x,y).</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul><li>(2M) Define marginal probability.</li><li>(5M) Given a joint probability table, compute marginal probabilities.</li></ul>
'''))

parts.append(topic('t-conditional', '4. Conditional Probability', 'H', f'''
{sub('⭐ Importance')}<p>Core prerequisite for Bayes’ Rule; frequently tested with numericals.</p>
{sub('📌 Definition')}
{box('def', 'The <b>conditional probability</b> of Y given X, written P(Y=y | X=x), is the probability that Y=y, given that we know X=x has occurred. Defined as: P(Y=y|X=x) = P(Y=y, X=x) / P(X=x), provided P(X=x) &gt; 0.')}
{sub('🧠 Intuition')}<p>Conditional probability "zooms in" on the world where X=x has already happened, and asks how likely Y=y is within that restricted world.</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'P(y|x) = P(x,y) / P(x) &nbsp;&nbsp; (Product/Chain rule rearranged: P(x,y) = P(y|x)P(x))')}
{sub('💡 Simple Example')}
{box('example', 'P(X=1,Y=1)=0.4, P(X=1)=0.7 (from marginal example above). Then P(Y=1|X=1) = 0.4/0.7 ≈ 0.571.')}
{sub('🎯 Real-World/ML Example')}<p>P(disease | positive test result) — the probability a patient has a disease given they tested positive — is a conditional probability, central to medical ML classifiers and directly used via Bayes’ Rule.</p>
{sub('✅ Advantages')}<p>Lets models incorporate evidence/observations to update beliefs — the basis of all supervised learning (P(label | features)).</p>
{sub('❌ Limitations')}<p>Undefined when the conditioning event has probability zero; can be counter-intuitive (base rate fallacy) if marginal (prior) probabilities are ignored.</p>
{sub('🔄 Comparison with Related Concepts')}<p>Chain rule of probability generalizes conditional probability to many variables: P(x₁,...,xₙ) = P(x₁)·P(x₂|x₁)·P(x₃|x₁,x₂)·...</p>
{sub('⚠️ Common Mistakes')}<p>Confusing P(A|B) with P(B|A) — these are generally NOT equal (this exact confusion motivates Bayes’ Rule).</p>
{sub('🧠 Important Points to Remember')}<ul><li>P(y|x) = P(x,y)/P(x) — MEMORIZE.</li><li>Chain rule: P(x₁,...,xₙ) = ∏ᵢ P(xᵢ | x₁,...,xᵢ₋₁).</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul><li>(2M) Define conditional probability.</li><li>(5M) State and prove the chain rule of probability.</li></ul>
'''))

parts.append(topic('t-expectation', '5. Expectation', 'H', f'''
{sub('⭐ Importance')}<p>Building block for variance, bias-variance analysis, loss function definitions (expected loss/risk). Frequently examined.</p>
{sub('📌 Definition')}
{box('def', 'The <b>expectation</b> (expected value / mean) of a function f(x) with respect to a probability distribution P(x) is the average value f(x) takes, weighted by how likely each x is: <br>Discrete: E<sub>x~P</sub>[f(x)] = Σₓ P(x) f(x) &nbsp;&nbsp; Continuous: E<sub>x~p</sub>[f(x)] = ∫ p(x) f(x) dx')}
{sub('🧠 Intuition')}<p>Expectation is the "weighted average" or "center of mass" of a random quantity — if you repeated the random experiment infinitely and averaged the outcomes, you would get the expectation.</p>
{sub('📖 Detailed Explanation')}<p>Expectation is linear: E[αf(x)+βg(x)] = αE[f(x)]+βE[g(x)], regardless of whether f and g are independent — this property is used constantly to simplify derivations (e.g., bias-variance decomposition).</p>
{sub('💡 Simple Example')}
{box('example', 'Fair die: E[X] = Σ (1/6)·i for i=1..6 = (1+2+3+4+5+6)/6 = 3.5.')}
{sub('🎯 Real-World/ML Example')}<p>The expected loss (risk) R(θ) = E<sub>(x,y)~data</sub>[L(f(x;θ), y)] is what ML training tries to minimize (approximated using the empirical average over training data).</p>
{sub('✅ Advantages')}<p>Single summary number capturing central tendency; linearity of expectation makes complex derivations tractable.</p>
{sub('❌ Limitations')}<p>Does not capture spread/uncertainty (need variance too); can be misleading for skewed/multi-modal distributions.</p>
{sub('⚠️ Common Mistakes')}<p>Assuming E[f(X)] = f(E[X]) — false in general (true only for linear f); forgetting expectation is linear even for dependent variables.</p>
{sub('🧠 Important Points to Remember')}<ul><li>E[αX+β] = αE[X]+β.</li><li>E[X+Y] = E[X]+E[Y] always (even if dependent).</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul><li>(2M) Define expectation.</li><li>(5M) State and prove linearity of expectation with example.</li></ul>
'''))

parts.append(topic('t-var-cov', '6. Variance and Covariance', 'VH', f'''
{sub('⭐ Importance')}<p>Extremely high-yield — direct numerical problems, derivations, and conceptual link to PCA (covariance matrix) and bias-variance tradeoff. Expect long-answer questions.</p>
{sub('📌 Definition')}
{box('def', '<b>Variance</b> measures how much values of a random variable X spread out from its mean: Var(X) = E[(X−E[X])²]. <b>Covariance</b> measures how two variables change together: Cov(X,Y) = E[(X−E[X])(Y−E[Y])].')}
{sub('🧠 Intuition')}<p>Variance answers "how spread out is X?" — small variance means values cluster near the mean; large variance means values are widely dispersed. Covariance answers "do X and Y tend to move together?" — positive covariance means they increase together, negative means one increases as the other decreases, zero means no linear relationship.</p>
{sub('📖 Detailed Explanation')}<p>Standard deviation SD(X) = √Var(X) puts the spread measure back into the original units (variance is in squared units). The <b>correlation coefficient</b> ρ = Cov(X,Y)/(SD(X)SD(Y)) normalizes covariance to lie in [−1,1], making it scale-independent. For a vector of random variables, the <b>covariance matrix</b> Σ collects all pairwise covariances: Σ<sub>i,j</sub> = Cov(Xᵢ,Xⱼ); the diagonal holds variances.</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'Var(X) = E[(X−E[X])²] = E[X²] − (E[X])² <br>Cov(X,Y) = E[(X−E[X])(Y−E[Y])] = E[XY] − E[X]E[Y] <br>Cov(X,X) = Var(X) <br>Var(X+Y) = Var(X)+Var(Y)+2Cov(X,Y)')}
{sub('📐 Derivation')}
{box('formula', '''Derive Var(X) = E[X²]−(E[X])²:<br>
Var(X) = E[(X−μ)²], where μ=E[X]<br>
= E[X² − 2μX + μ²]<br>
= E[X²] − 2μE[X] + μ² &nbsp;(by linearity of expectation)<br>
= E[X²] − 2μ·μ + μ²  &nbsp;(since E[X]=μ)<br>
= E[X²] − μ² = E[X²] − (E[X])² ∎ <br><br>
Derive Var(X+Y) = Var(X)+Var(Y)+2Cov(X,Y):<br>
Var(X+Y) = E[((X+Y)−E[X+Y])²] = E[((X−μₓ)+(Y−μᵧ))²]<br>
= E[(X−μₓ)²] + E[(Y−μᵧ)²] + 2E[(X−μₓ)(Y−μᵧ)]<br>
= Var(X) + Var(Y) + 2Cov(X,Y) ∎''')}
{sub('💡 Simple Example')}
{box('example', '''X takes values 2,4,6 each with prob 1/3. E[X]=4. E[X²]=(4+16+36)/3=56/3≈18.67.<br>
Var(X) = 18.67 − 16 = 2.67.<br>
If Y = 2X (perfectly correlated), Cov(X,Y) = E[XY]−E[X]E[Y]. Since Y=2X, Cov(X,Y)=2Var(X)=5.33 (maximal positive covariance).''')}
{sub('🎯 Real-World/ML Example')}<p>The covariance matrix of features is exactly what PCA eigen-decomposes to find principal components; in the bias-variance tradeoff, the variance term measures how much model predictions fluctuate across different training sets.</p>
{sub('🖼️ Diagram')}
<svg class="diagram" viewBox="0 0 260 110" xmlns="http://www.w3.org/2000/svg">
<g transform="translate(40,55)"><circle cx="0" cy="0" r="4" fill="#2f57a3"/><circle cx="8" cy="4" r="4" fill="#2f57a3"/><circle cx="-6" cy="-3" r="4" fill="#2f57a3"/><circle cx="10" cy="9" r="4" fill="#2f57a3"/><circle cx="-10" cy="-8" r="4" fill="#2f57a3"/>
<text x="-30" y="35" font-size="9">Positive covariance</text></g>
<g transform="translate(180,55)"><circle cx="0" cy="0" r="4" fill="#c0392b"/><circle cx="8" cy="-4" r="4" fill="#c0392b"/><circle cx="-6" cy="3" r="4" fill="#c0392b"/><circle cx="10" cy="-9" r="4" fill="#c0392b"/><circle cx="-10" cy="8" r="4" fill="#c0392b"/>
<text x="150" y="35" font-size="9">Negative covariance</text></g>
</svg>
{sub('✅ Advantages')}<p>Variance quantifies uncertainty/reliability of predictions; covariance matrix captures full linear relationship structure among many variables at once.</p>
{sub('❌ Limitations')}<p>Only captures LINEAR relationships (Cov=0 does not imply independence, only no linear relationship); sensitive to outliers; variance/covariance scale with units (correlation is preferred for comparability).</p>
{sub('🔄 Comparison with Related Concepts')}
<table><tr><th>Measure</th><th>Range</th><th>Meaning</th></tr>
<tr><td>Variance</td><td>[0,∞)</td><td>Spread of single variable</td></tr>
<tr><td>Covariance</td><td>(−∞,∞)</td><td>Joint linear variability of two variables</td></tr>
<tr><td>Correlation</td><td>[−1,1]</td><td>Normalized, scale-free covariance</td></tr></table>
{sub('⚠️ Common Mistakes')}<p>Assuming Cov(X,Y)=0 implies X,Y independent (false — only true for jointly Gaussian variables in general); forgetting the factor of 2 in Var(X+Y) expansion; sign errors when expanding squares.</p>
{sub('🧠 Important Points to Remember')}<ul><li>Var(X)=E[X²]−(E[X])² — MEMORIZE.</li><li>Cov(X,Y)=E[XY]−E[X]E[Y] — MEMORIZE.</li><li>Covariance matrix is symmetric, diagonal = variances.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul>
<li>(2M) Define variance and covariance.</li>
<li>(2M) What does zero covariance imply (and not imply)?</li>
<li>(5M) Derive Var(X)=E[X²]−(E[X])².</li>
<li>(10M) Derive Var(X+Y) in terms of Var(X), Var(Y), Cov(X,Y) and solve a numerical example.</li>
<li>(10M) Explain the covariance matrix and its role in PCA.</li>
</ul>
'''))

parts.append(topic('t-bayes', "7. Bayes’ Rule", 'VH', f'''
{sub('⭐ Importance')}<p>One of the single most-examined formulas in the entire syllabus — expect a derivation + numerical almost every exam (medical test/spam-filter style problems).</p>
{sub('📌 Definition')}
{box('def', '<b>Bayes’ Rule (Bayes’ Theorem)</b> lets us reverse the direction of conditioning — computing P(Y|X) from P(X|Y): <br><b>P(y|x) = [P(x|y) · P(y)] / P(x)</b>')}
{sub('🧠 Intuition')}<p>Bayes’ Rule updates our belief about a hypothesis Y after observing evidence X. P(y) is the <b>prior</b> belief before seeing data; P(x|y) is the <b>likelihood</b> of the evidence under that hypothesis; P(y|x) is the <b>posterior</b> — updated belief after seeing evidence.</p>
{sub('📖 Detailed Explanation')}<p>The denominator P(x) acts as a normalizing constant and can be expanded via marginalization: P(x) = Σ_y P(x|y)P(y) (sum over all possible hypotheses). This ensures the posterior sums to 1 over all y.</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'P(y|x) = P(x|y)P(y) / P(x), where P(x) = Σ_y′ P(x|y′)P(y′)<br>Posterior ∝ Likelihood × Prior')}
{sub('📐 Derivation')}
{box('formula', '''From the definition of conditional probability (both directions):<br>
P(x,y) = P(x|y)·P(y) &nbsp;&nbsp;(1)<br>
P(x,y) = P(y|x)·P(x) &nbsp;&nbsp;(2)<br>
Since both equal P(x,y), set (1) = (2): P(y|x)·P(x) = P(x|y)·P(y)<br>
Divide both sides by P(x): <b>P(y|x) = P(x|y)P(y) / P(x)</b> ∎''')}
{sub('💡 Simple Example')}
{box('example', '''Medical test problem: Disease prevalence P(D)=0.01. Test sensitivity P(+|D)=0.99. False positive rate P(+|¬D)=0.05.<br>
P(+) = P(+|D)P(D)+P(+|¬D)P(¬D) = 0.99×0.01 + 0.05×0.99 = 0.0099+0.0495 = 0.0594.<br>
P(D|+) = P(+|D)P(D)/P(+) = 0.0099/0.0594 ≈ 0.1667 (only ~16.7%! — classic counter-intuitive base-rate result).''')}
{sub('🎯 Real-World/ML Example')}<p>Naive Bayes classifier computes P(class|features) using Bayes’ Rule with a "naive" conditional-independence assumption on features; spam filters classify P(spam|words); Bayesian statistics (next chapter) makes Bayes’ Rule the central engine for parameter estimation.</p>
{sub('🖼️ Diagram')}
<svg class="diagram" viewBox="0 0 260 110" xmlns="http://www.w3.org/2000/svg">
<g font-size="10" fill="#333">
<rect x="10" y="10" width="90" height="30" fill="#eef3ff" stroke="#2f57a3"/><text x="18" y="30">Prior P(y)</text>
<text x="105" y="30">+</text>
<rect x="115" y="10" width="110" height="30" fill="#fff8e6" stroke="#e8c766"/><text x="122" y="30">Likelihood P(x|y)</text>
<text x="115" y="55">↓ (normalize by P(x))</text>
<rect x="60" y="70" width="140" height="30" fill="#eefaf5" stroke="#0e8a6d"/><text x="90" y="90">Posterior P(y|x)</text>
</g>
</svg>
{sub('⚙️ Algorithm / Procedure')}<p>1. Identify prior P(y) for each hypothesis. 2. Identify likelihood P(x|y) for the observed evidence under each hypothesis. 3. Compute marginal P(x)=Σ_y P(x|y)P(y). 4. Compute posterior P(y|x) for the hypothesis of interest.</p>
{sub('✅ Advantages')}<p>Provides principled way to update beliefs with new evidence; foundation of Bayesian statistics and Naive Bayes classifiers; handles uncertainty rigorously.</p>
{sub('❌ Limitations')}<p>Requires knowing/estimating the prior, which can be subjective or unavailable; computing the marginal P(x) can be intractable for complex/high-dimensional problems (motivates approximate inference methods).</p>
{sub('🔄 Comparison with Related Concepts')}<p>Bayes’ Rule (reverses conditioning) vs Chain Rule (decomposes joint into a product of conditionals) — Bayes’ Rule is actually derived from two applications of the chain rule/conditional-probability definition.</p>
{sub('⚠️ Common Mistakes')}<p>Forgetting to compute/expand the denominator P(x) via marginalization; confusing P(x|y) with P(y|x) (this exact confusion is called the "prosecutor\\'s fallacy"); ignoring the prior (base rate) in intuitive reasoning.</p>
{sub('🧠 Important Points to Remember')}<ul><li>P(y|x)=P(x|y)P(y)/P(x) — MEMORIZE with full derivation.</li><li>Posterior ∝ Likelihood × Prior.</li><li>Always double-check by expanding P(x) via total probability/marginalization.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul>
<li>(2M) State Bayes’ theorem.</li>
<li>(5M) Derive Bayes’ Rule from the definition of conditional probability.</li>
<li>(10M) Solve a numerical Bayes’ theorem problem (e.g., medical diagnosis/spam filter) showing full working.</li>
<li>(10M) Explain the role of Bayes’ Rule in Naive Bayes classification / Bayesian statistics.</li>
</ul>
'''))

parts.append(topic('t-info-theory', '8. Information Theory', 'H', f'''
{sub('⭐ Importance')}<p>Very important for understanding loss functions (cross-entropy) used throughout deep learning; frequently tested with entropy/cross-entropy/KL divergence formula-based questions.</p>
{sub('📌 Definition')}
{box('def', '<b>Information theory</b> quantifies how much "information"/"surprise" is associated with observing an event. <b>Self-information</b> of an event x: I(x) = −log P(x). <b>Entropy</b> H(X) is the expected self-information of a distribution: H(X) = −Σₓ P(x) log P(x).')}
{sub('🧠 Intuition')}<p>Rare/unlikely events carry more information when they occur (learning that a rare event happened tells you a lot); certain events (P=1) carry zero information. Entropy measures the average uncertainty/"surprise" inherent in a whole distribution — a fair coin (maximum uncertainty) has higher entropy than a biased coin.</p>
{sub('📖 Detailed Explanation')}<p><b>Cross-Entropy</b> H(P,Q) = −Σₓ P(x) log Q(x) measures the average number of bits needed to encode data from true distribution P using a code optimized for an estimated/model distribution Q — this is exactly the standard loss function for classification in deep learning (comparing true labels P to predicted probabilities Q). <b>KL Divergence</b> D<sub>KL</sub>(P‖Q) = Σₓ P(x) log[P(x)/Q(x)] = H(P,Q) − H(P) measures how different Q is from P (always ≥0, equals 0 only when P=Q; NOT symmetric, so it is a "divergence" not a true distance).</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'Self-information: I(x) = −log P(x) <br>Entropy: H(X) = −Σₓ P(x) log P(x) = E<sub>x~P</sub>[−log P(x)] <br>Cross-Entropy: H(P,Q) = −Σₓ P(x) log Q(x) <br>KL Divergence: D<sub>KL</sub>(P‖Q) = Σₓ P(x) log(P(x)/Q(x)) = H(P,Q) − H(P)')}
{sub('💡 Simple Example')}
{box('example', '''Fair coin: P(H)=P(T)=0.5. H(X) = −(0.5log₂0.5 + 0.5log₂0.5) = −(0.5×−1 + 0.5×−1) = 1 bit (maximum entropy for binary variable).<br>
Biased coin: P(H)=0.9,P(T)=0.1. H(X)= −(0.9log₂0.9+0.1log₂0.1) ≈ −(0.9×−0.152+0.1×−3.32) ≈ 0.469 bits (less uncertain).''')}
{sub('🎯 Real-World/ML Example')}<p>Cross-entropy loss is the standard loss function for classification neural networks (comparing one-hot true label distribution to predicted softmax distribution); KL divergence is used in variational autoencoders (VAEs) and in comparing/regularizing probability distributions; decision tree splitting criteria (information gain) are based on entropy reduction.</p>
{sub('🖼️ Diagram')}
<svg class="diagram" viewBox="0 0 260 110" xmlns="http://www.w3.org/2000/svg">
<path d="M20,95 Q130,5 240,95" fill="none" stroke="#2f57a3" stroke-width="2"/>
<line x1="10" y1="95" x2="250" y2="95" stroke="#999"/>
<text x="115" y="20" font-size="10">H(X) max at p=0.5</text>
<text x="100" y="108" font-size="9">Entropy vs P(Heads) for a coin</text>
</svg>
{sub('✅ Advantages')}<p>Provides a rigorous, unit-consistent way (bits/nats) to measure uncertainty and compare distributions; cross-entropy loss gives well-behaved gradients for classification training.</p>
{sub('❌ Limitations')}<p>Entropy/KL divergence require known probability distributions, which must be estimated from finite data; KL divergence is asymmetric so cannot be used as a true "distance metric".</p>
{sub('🔄 Comparison with Related Concepts')}
<table><tr><th>Quantity</th><th>Formula</th><th>Meaning</th></tr>
<tr><td>Entropy H(P)</td><td>−ΣP log P</td><td>Uncertainty in true distribution alone</td></tr>
<tr><td>Cross-Entropy H(P,Q)</td><td>−ΣP log Q</td><td>Cost of using Q to encode data from P</td></tr>
<tr><td>KL Divergence</td><td>H(P,Q)−H(P)</td><td>Extra cost/difference of using Q instead of P</td></tr></table>
{sub('⚠️ Common Mistakes')}<p>Forgetting the negative sign in entropy/cross-entropy formulas; confusing KL(P‖Q) with KL(Q‖P) — order matters since KL divergence is not symmetric; using natural log vs log base 2 inconsistently (changes units from nats to bits).</p>
{sub('🧠 Important Points to Remember')}<ul><li>H(X) = −Σ P(x)log P(x) — MEMORIZE.</li><li>Cross-entropy = entropy + KL divergence: H(P,Q) = H(P) + D<sub>KL</sub>(P‖Q).</li><li>KL divergence ≥ 0 always; = 0 iff P=Q.</li><li>Uniform distribution has MAXIMUM entropy among all distributions on a fixed support.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul>
<li>(2M) Define entropy.</li>
<li>(2M) Define KL divergence.</li>
<li>(5M) Explain cross-entropy and its use as a loss function in deep learning.</li>
<li>(10M) Derive the relationship between entropy, cross-entropy, and KL divergence; compute entropy for a numerical example.</li>
</ul>
'''))

with open('/home/claude/ch2_full.html','w') as f:
    f.write(''.join(parts))
print("ch2 written, length:", len(''.join(parts)))
