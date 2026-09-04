# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/home/claude')
from gen_helpers import topic, sub, box, chapter_header

parts = [chapter_header('ch5ml', 'Chapter 5: Machine Learning')]

parts.append(topic('t-basics-underfitting', '1. Basics and Underfitting', 'H', f'''
{sub('⭐ Importance')}<p>Fundamental vocabulary connecting to bias-variance and overfitting; frequently tested with capacity/generalization questions.</p>
{sub('📌 Definition')}
{box('def', '<b>Machine learning</b> is the study of algorithms that improve their performance on a task T, measured by performance measure P, through experience E (data). <b>Underfitting</b> occurs when a model is too simple to capture the underlying pattern in the training data, resulting in high error on BOTH training and test data.')}
{sub('🧠 Intuition')}<p>Underfitting is like trying to fit a straight line through data that clearly curves — the model lacks the flexibility (capacity) to represent the true relationship, so it performs poorly everywhere, not just on new data.</p>
{sub('📖 Detailed Explanation')}<p>Central to ML is <b>generalization</b> — performing well on unseen test data, not just memorizing training data. The <b>training error</b> is measured on data the model has seen; the <b>generalization (test) error</b> is measured on held-out data. A model\\u2019s <b>capacity</b> (roughly, its ability to fit a wide variety of functions) must be matched to the complexity of the true underlying data-generating process — too little capacity causes underfitting (high training error); too much causes overfitting (low training error, high test error, covered under Bias-Variance).</p>
{sub('💡 Simple Example')}<p>Fitting a straight line (degree-1 polynomial) to data generated from a quadratic curve — the line cannot bend to match the curvature, so both training and test error remain high.</p>
{sub('🎯 Real-World/ML Example')}<p>A linear regression model used to predict house prices when the true relationship involves complex non-linear interactions (location, size, amenities) will underfit and give poor predictions everywhere.</p>
{sub('✅ Advantages')}<p>Simple/low-capacity models are less likely to overfit, are computationally cheap, and are easier to interpret.</p>
{sub('❌ Limitations')}<p>Too little capacity cannot represent the true data pattern, hurting performance regardless of how much training data is available.</p>
{sub('🔄 Comparison with Related Concepts')}<p>Underfitting (high bias, low capacity) vs Overfitting (high variance, excessive capacity) — the two failure modes on opposite ends of the capacity spectrum (see Bias-Variance topic).</p>
{sub('⚠️ Common Mistakes')}<p>Assuming more training data always fixes underfitting (it does not — the model needs more capacity, not more data); confusing training error with generalization error.</p>
{sub('🧠 Important Points to Remember')}<ul><li>Underfitting: high training error AND high test error.</li><li>Goal of ML: low training error + small gap between training and test error.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul><li>(2M) Define underfitting.</li><li>(5M) Explain the concept of generalization in machine learning.</li></ul>
'''))

parts.append(topic('t-hyperparams', '2. Hyperparameters and Validation Sets', 'M', f'''
{sub('⭐ Importance')}<p>Practical/conceptual — commonly a 2-mark or short 5-mark question.</p>
{sub('📌 Definition')}
{box('def', '<b>Hyperparameters</b> are settings of a learning algorithm that are NOT learned from data during training (e.g., learning rate, number of layers, regularization strength) — they are set before training begins. A <b>validation set</b> is a held-out portion of data (separate from training and test sets) used to tune hyperparameters and estimate generalization without touching the true test set.')}
{sub('🧠 Intuition')}<p>Since hyperparameters cannot be learned by the training algorithm itself (they control the learning process), we need a separate dataset — the validation set — to check how different hyperparameter choices perform, without "cheating" by looking at the final test set.</p>
{sub('📖 Detailed Explanation')}<p>Typically the available data is split into three parts: <b>Training set</b> (fit model parameters), <b>Validation set</b> (tune hyperparameters, model selection), <b>Test set</b> (final, unbiased performance estimate — used only once, after all decisions are finalized). A common technique is <b>k-fold cross-validation</b>, which repeatedly splits data into k folds, training on k−1 folds and validating on the remaining fold, to make efficient use of limited data.</p>
{sub('💡 Simple Example')}<p>Choosing the best value of k in a k-NN classifier: try k=1,3,5,7 on the validation set, pick the k with lowest validation error.</p>
{sub('🎯 Real-World/ML Example')}<p>Tuning the learning rate, batch size, or number of hidden layers of a neural network using a validation set before evaluating final performance on the test set.</p>
{sub('✅ Advantages')}<p>Prevents overfitting to the test set through repeated hyperparameter tuning; gives a more honest estimate of real-world performance.</p>
{sub('❌ Limitations')}<p>Reduces the amount of data available for training (mitigated by k-fold cross-validation, at the cost of extra computation).</p>
{sub('⚠️ Common Mistakes')}<p>Tuning hyperparameters directly on the test set (data leakage, gives overly optimistic performance estimates); confusing validation set with test set.</p>
{sub('🧠 Important Points to Remember')}<ul><li>Test set must be touched only ONCE, at the very end.</li><li>k-fold CV trades compute for better data utilization.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul><li>(2M) Define hyperparameter.</li><li>(2M) What is the purpose of a validation set?</li><li>(5M) Explain k-fold cross-validation.</li></ul>
'''))

parts.append(topic('t-estimators', '3. Estimators', 'M', f'''
{sub('⭐ Importance')}<p>Bridges into Bias-Variance and Maximum Likelihood; typically a 2-5 mark question.</p>
{sub('📌 Definition')}
{box('def', 'An <b>estimator</b> is any function of observed data used to estimate/approximate an unknown quantity — a parameter of a distribution (<b>point estimation</b>) or a target function (<b>function estimation</b>).')}
{sub('🧠 Intuition')}<p>Since we never know the true underlying parameters (e.g., the true mean of a population), we use a rule (estimator) applied to a finite sample to produce our best guess (estimate).</p>
{sub('📖 Detailed Explanation')}<p>An estimator θ̂ is itself a random variable (since it depends on the random sample drawn); it has its own sampling distribution. Two key properties: <b>Bias</b> = E[θ̂] − θ (systematic error); <b>Variance</b> = spread of θ̂ across different samples (covered in depth in the next topic). Function estimation generalizes point estimation to estimating an entire function f (e.g., the function mapping input x to output y in supervised learning) rather than a single parameter.</p>
{sub('💡 Simple Example')}<p>The sample mean x̄ = (1/n)Σxᵢ is an estimator of the true population mean μ.</p>
{sub('🎯 Real-World/ML Example')}<p>The weights learned by a neural network are estimators of the (unknown) true function mapping inputs to outputs; the sample variance is an estimator of the true population variance.</p>
{sub('✅ Advantages')}<p>Provides principled framework to reason about how good our learned parameters/functions are, using concepts like bias, variance, and consistency.</p>
{sub('❌ Limitations')}<p>Estimators are only as good as the sample data available; small/biased samples give unreliable estimates.</p>
{sub('⚠️ Common Mistakes')}<p>Confusing an estimator (the rule/function) with an estimate (the specific numeric output for a given sample).</p>
{sub('🧠 Important Points to Remember')}<ul><li>Estimator = function of data; Estimate = its numeric output.</li><li>Point estimation vs Function estimation.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul><li>(2M) Define estimator with example.</li><li>(2M) Differentiate point estimation and function estimation.</li></ul>
'''))

parts.append(topic('t-bias-variance', '4. Bias and Variance', 'VH', f'''
{sub('⭐ Importance')}<p>One of the most important conceptual + derivation topics in the whole syllabus — the bias-variance decomposition is a near-guaranteed long-answer question.</p>
{sub('📌 Definition')}
{box('def', '<b>Bias</b> of an estimator = E[θ̂] − θ (systematic deviation of the estimator\\u2019s expected value from the true parameter). <b>Variance</b> of an estimator = Var(θ̂) (how much the estimate fluctuates across different training samples). Expected generalization error decomposes as: Error = Bias² + Variance + Irreducible Noise.')}
{sub('🧠 Intuition')}<p>Bias measures how wrong the model is ON AVERAGE (systematic error from oversimplified assumptions — underfitting); variance measures how INCONSISTENT the model is across different training sets (sensitivity to noise in the specific training data — overfitting). A good model must balance both — this is the famous <b>bias-variance tradeoff</b>: reducing one often increases the other.</p>
{sub('📖 Detailed Explanation')}<p>Low-capacity models (e.g., linear regression) tend to have HIGH BIAS (they cannot capture complex patterns) but LOW VARIANCE (consistent across different training sets, since they are too rigid to be swayed by noise). High-capacity models (e.g., deep decision trees) tend to have LOW BIAS but HIGH VARIANCE (they fit training noise, giving wildly different models for different training samples). The goal is to find the capacity that minimizes TOTAL error (bias²+variance), not to eliminate either individually.</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'Bias(θ̂) = E[θ̂] − θ <br>Var(θ̂) = E[(θ̂−E[θ̂])²] <br>MSE(θ̂) = E[(θ̂−θ)²] = Bias(θ̂)² + Var(θ̂)')}
{sub('📐 Derivation')}
{box('formula', '''MSE(θ̂) = E[(θ̂−θ)²]. Add and subtract E[θ̂]:<br>
= E[((θ̂−E[θ̂]) + (E[θ̂]−θ))²]<br>
= E[(θ̂−E[θ̂])²] + 2(E[θ̂]−θ)E[θ̂−E[θ̂]] + (E[θ̂]−θ)²<br>
The middle (cross) term vanishes since E[θ̂−E[θ̂]] = E[θ̂]−E[θ̂] = 0.<br>
= E[(θ̂−E[θ̂])²] + (E[θ̂]−θ)²<br>
= <b>Var(θ̂) + Bias(θ̂)²</b> ∎''')}
{sub('💡 Simple Example')}
{box('example', '''Suppose true parameter θ=10. Estimator A always gives θ̂=10 but fluctuates ±0.1 across samples (low bias, low variance — ideal). Estimator B always gives θ̂=7 consistently (high bias=−3, but zero variance). Estimator C wildly fluctuates between 5 and 15 depending on the sample but averages to 10 (zero bias, but high variance). MSE reveals which is best overall.''')}
{sub('🎯 Real-World/ML Example')}<p>A degree-1 polynomial fit to non-linear data has high bias (underfits); a degree-20 polynomial fit to the same small dataset has high variance (overfits, wiggles wildly with tiny changes in data). Regularization (Ch.4) explicitly trades a small increase in bias for a larger reduction in variance.</p>
{sub('🖼️ Diagram')}
<svg class="diagram" viewBox="0 0 260 140" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="120" x2="240" y2="120" stroke="#999"/><line x1="20" y1="120" x2="20" y2="15" stroke="#999"/>
<path d="M25,30 Q130,110 235,20" fill="none" stroke="#c0392b" stroke-width="2"/>
<path d="M25,110 Q130,20 235,115" fill="none" stroke="#2f57a3" stroke-width="2"/>
<text x="150" y="30" font-size="9" fill="#c0392b">Variance (increases with capacity)</text>
<text x="30" y="35" font-size="9" fill="#2f57a3">Bias² (decreases with capacity)</text>
<text x="80" y="135" font-size="9">Model Capacity →</text>
</svg>
<p style="font-size:.85rem;color:var(--text-soft);">Exam drawing tip: draw bias² decreasing and variance increasing as capacity grows, with total error as a U-shaped curve — the minimum is the sweet spot.</p>
{sub('✅ Advantages')}<p>Provides a principled framework for diagnosing whether a model is underfitting (reduce bias — increase capacity) or overfitting (reduce variance — regularize, get more data).</p>
{sub('❌ Limitations')}<p>In practice, true bias/variance cannot be computed exactly (would require access to the true data-generating distribution and many resampled training sets) — only estimated empirically via techniques like cross-validation.</p>
{sub('🔄 Comparison with Related Concepts')}
<table><tr><th>Aspect</th><th>High Bias (Underfitting)</th><th>High Variance (Overfitting)</th></tr>
<tr><td>Training error</td><td>High</td><td>Low</td></tr>
<tr><td>Test error</td><td>High</td><td>High</td></tr>
<tr><td>Fix</td><td>Increase capacity/features</td><td>Regularize, more data, reduce capacity</td></tr></table>
{sub('⚠️ Common Mistakes')}<p>Forgetting the cross-term vanishes in the MSE derivation; confusing "bias" here (statistical, estimator property) with "bias" the term in a neural network (a learnable additive parameter) — these are unrelated.</p>
{sub('🧠 Important Points to Remember')}<ul><li>MSE = Bias² + Variance — MEMORIZE with derivation.</li><li>Underfitting↔high bias; Overfitting↔high variance.</li><li>Regularization intentionally increases bias slightly to reduce variance more, lowering total error.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul>
<li>(2M) Define bias and variance of an estimator.</li>
<li>(5M) Explain the bias-variance tradeoff with a diagram.</li>
<li>(10M) Derive the bias-variance decomposition of MSE step by step.</li>
<li>(10M) Discuss how model capacity affects bias and variance, and how regularization addresses this tradeoff.</li>
</ul>
'''))

parts.append(topic('t-mle', '5. Maximum Likelihood', 'VH', f'''
{sub('⭐ Importance')}<p>Extremely important — foundation for why cross-entropy loss is used in deep learning; expect a full derivation question.</p>
{sub('📌 Definition')}
{box('def', '<b>Maximum Likelihood Estimation (MLE)</b> chooses the parameter θ that maximizes the likelihood of observing the given training data, assuming the data was drawn i.i.d. (independently and identically distributed) from a model distribution p<sub>model</sub>(x;θ): <br>θ<sub>ML</sub> = argmax<sub>θ</sub> p<sub>model</sub>(X;θ) = argmax<sub>θ</sub> ∏ᵢ p<sub>model</sub>(xᵢ;θ)')}
{sub('🧠 Intuition')}<p>MLE asks: "For which parameter value θ would the data I actually observed have been most probable?" — it picks the θ that makes the observed data look "least surprising".</p>
{sub('📖 Detailed Explanation')}<p>Since the product of many probabilities (each ≤1) shrinks toward zero and underflows numerically (recall Ch.3), we instead maximize the <b>log-likelihood</b> (log is monotonically increasing, so it does not change the location of the maximum): θ<sub>ML</sub> = argmax<sub>θ</sub> Σᵢ log p<sub>model</sub>(xᵢ;θ). Dividing by n turns this into an expectation over the empirical data distribution p̂<sub>data</sub>, connecting MLE directly to minimizing the KL divergence / cross-entropy between the true data distribution and the model distribution — this is EXACTLY why cross-entropy loss is the standard loss function in deep learning classifiers.</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'θ<sub>ML</sub> = argmax<sub>θ</sub> Σᵢ₌₁<sup>n</sup> log p<sub>model</sub>(xᵢ;θ) <br>Equivalently: θ<sub>ML</sub> = argmin<sub>θ</sub> D<sub>KL</sub>(p̂<sub>data</sub> ‖ p<sub>model</sub>) = argmin<sub>θ</sub> [−E<sub>x~p̂data</sub> log p<sub>model</sub>(x;θ)] (cross-entropy)')}
{sub('📐 Derivation')}
{box('formula', '''Step 1: Assume i.i.d. samples x₁,...,xₙ. Joint likelihood: L(θ) = ∏ᵢ p(xᵢ;θ).<br>
Step 2: Take log (monotonic transform, preserves argmax): log L(θ) = Σᵢ log p(xᵢ;θ).<br>
Step 3: Divide by n (does not change argmax): (1/n)Σᵢ log p(xᵢ;θ) = E<sub>x~p̂data</sub>[log p(x;θ)].<br>
Step 4: Maximizing this expectation is equivalent to minimizing −E<sub>x~p̂data</sub>[log p(x;θ)], which is the cross-entropy H(p̂<sub>data</sub>, p<sub>model</sub>).<br>
Step 5: Since H(p̂,p<sub>model</sub>) = H(p̂) + D<sub>KL</sub>(p̂‖p<sub>model</sub>), and H(p̂) does not depend on θ, minimizing cross-entropy is equivalent to minimizing KL divergence between the empirical data distribution and the model. ∎''')}
{sub('💡 Simple Example')}
{box('example', '''Coin tosses: 7 Heads, 3 Tails out of 10 (i.i.d. Bernoulli(φ)). <br>
Log-likelihood: ℓ(φ)=7log(φ)+3log(1−φ). dℓ/dφ = 7/φ − 3/(1−φ) = 0 ⟹ 7(1−φ)=3φ ⟹ 7=10φ ⟹ φ<sub>ML</sub>=0.7 (matches intuition: MLE estimate = observed proportion of heads).''')}
{sub('🎯 Real-World/ML Example')}<p>Training a classification neural network with cross-entropy loss IS maximum likelihood estimation under a categorical/Bernoulli model assumption; training a regression network with MSE loss corresponds to MLE under a Gaussian noise assumption.</p>
{sub('⚙️ Algorithm / Procedure')}<p>1. Assume a parametric model p(x;θ). 2. Write the likelihood (or log-likelihood) of the observed data. 3. Differentiate log-likelihood w.r.t. θ and set to zero (or use gradient-based optimization for complex models). 4. Solve for θ<sub>ML</sub>.</p>
{sub('✅ Advantages')}<p>Under certain conditions (correct model, enough data), MLE is consistent (converges to true parameter) and asymptotically efficient (lowest possible variance among consistent estimators); directly connects to standard deep learning loss functions.</p>
{sub('❌ Limitations')}<p>Can overfit with small datasets (no regularization built in — pure MLE has no prior); assumes the model family is correctly specified; can be undefined/unstable for certain distributions (e.g., unbounded likelihood in some mixture models).</p>
{sub('🔄 Comparison with Related Concepts')}<p>MLE (uses only the likelihood, no prior) vs Bayesian estimation / MAP (incorporates a prior distribution over θ, covered in next topic) — MLE can be seen as MAP with a uniform (flat) prior.</p>
{sub('⚠️ Common Mistakes')}<p>Forgetting to take the log before differentiating (leads to messy product-rule derivatives); sign errors when converting "maximize likelihood" to "minimize negative log-likelihood".</p>
{sub('🧠 Important Points to Remember')}<ul><li>θ<sub>ML</sub>=argmax Σlog p(xᵢ;θ) — MEMORIZE.</li><li>MLE ⟺ minimizing cross-entropy ⟺ minimizing KL divergence to empirical data distribution.</li><li>Cross-entropy loss in deep learning = MLE in disguise.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul>
<li>(2M) Define maximum likelihood estimation.</li>
<li>(5M) Derive the MLE estimate for a Bernoulli distribution.</li>
<li>(10M) Show that maximizing likelihood is equivalent to minimizing KL divergence/cross-entropy between data and model distributions.</li>
<li>(10M) Explain the connection between MLE and cross-entropy loss used in deep learning.</li>
</ul>
'''))

with open('/home/claude/ch5ml_part1.html','w') as f:
    f.write(''.join(parts))
print("ch5ml part1 written, length:", len(''.join(parts)))
