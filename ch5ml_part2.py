# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/home/claude')
from gen_helpers import topic, sub, box

parts = []

parts.append(topic('t-bayesian-stats', '6. Bayesian Statistics', 'H', f'''
{sub('⭐ Importance')}<p>Important conceptual contrast to MLE; commonly tested with MAP estimation and prior/posterior questions.</p>
{sub('📌 Definition')}
{box('def', '<b>Bayesian statistics</b> treats the parameter θ itself as a random variable with a <b>prior distribution</b> p(θ) representing belief before seeing data; after observing data, Bayes\\u2019 Rule is used to compute the <b>posterior</b> p(θ|X) ∝ p(X|θ)p(θ).')}
{sub('🧠 Intuition')}<p>Unlike MLE (which gives a single best-fit point estimate), the Bayesian approach maintains a full DISTRIBUTION over possible parameter values, naturally capturing uncertainty about which θ is correct — especially valuable with limited data.</p>
{sub('📖 Detailed Explanation')}<p><b>Maximum A Posteriori (MAP)</b> estimation is a practical compromise: instead of the full posterior distribution, pick the single θ that maximizes the posterior: θ<sub>MAP</sub> = argmax<sub>θ</sub> p(X|θ)p(θ) = argmax<sub>θ</sub> [log p(X|θ) + log p(θ)]. This shows MAP = MLE + a regularization-like term from the log-prior — e.g., a Gaussian prior on weights yields exactly the L2 regularization penalty (weight decay) seen in Ch.4!</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'Posterior: p(θ|X) ∝ p(X|θ) · p(θ) <br>MAP: θ<sub>MAP</sub> = argmax<sub>θ</sub> [log p(X|θ) + log p(θ)]')}
{sub('💡 Simple Example')}<p>Estimating a coin\\u2019s bias with a Beta prior; after observing tosses, the posterior is updated (also Beta-distributed) — combining prior belief with observed evidence rather than relying purely on the small sample.</p>
{sub('🎯 Real-World/ML Example')}<p>L2 regularization (weight decay) is mathematically equivalent to MAP estimation with a zero-mean Gaussian prior on the weights; Bayesian neural networks maintain uncertainty estimates over predictions, useful in safety-critical applications.</p>
{sub('✅ Advantages')}<p>Naturally incorporates prior knowledge; provides full uncertainty quantification, not just a point estimate; helps prevent overfitting on small datasets via the regularizing effect of the prior.</p>
{sub('❌ Limitations')}<p>Computing the full posterior is often computationally intractable for complex models (requires approximate inference methods like MCMC or variational inference); choice of prior can be subjective and influence results.</p>
{sub('🔄 Comparison with Related Concepts')}
<table><tr><th>Aspect</th><th>MLE</th><th>MAP</th><th>Full Bayesian</th></tr>
<tr><td>Uses prior?</td><td>No</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Output</td><td>Point estimate</td><td>Point estimate</td><td>Full distribution</td></tr>
<tr><td>Objective</td><td>argmax p(X|θ)</td><td>argmax p(X|θ)p(θ)</td><td>Compute p(θ|X)</td></tr></table>
{sub('⚠️ Common Mistakes')}<p>Forgetting the normalizing constant p(X) is not needed for argmax (since it does not depend on θ); confusing MAP (still a point estimate) with full Bayesian inference (a distribution).</p>
{sub('🧠 Important Points to Remember')}<ul><li>MAP = MLE + log-prior term.</li><li>Gaussian prior on weights ⟺ L2 regularization.</li><li>Laplace prior on weights ⟺ L1 regularization.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul><li>(2M) Define Bayesian statistics / MAP estimation.</li><li>(5M) Explain the relationship between MAP estimation and MLE.</li><li>(10M) Show that a Gaussian prior in MAP estimation is equivalent to L2 regularization.</li></ul>
'''))

parts.append(topic('t-supervised', '7. Supervised Learning', 'H', f'''
{sub('⭐ Importance')}<p>Basic but essential vocabulary; usually a 2-mark question, sometimes combined with examples/algorithms.</p>
{sub('📌 Definition')}
{box('def', '<b>Supervised learning</b> algorithms learn a mapping from inputs x to outputs y using a training set of LABELED examples {{(x⁽¹⁾,y⁽¹⁾),...,(x⁽ⁿ⁾,y⁽ⁿ⁾)}}, where each input is paired with its correct/desired output.')}
{sub('🧠 Intuition')}<p>Like learning with a teacher who provides the correct answer for every practice question — the algorithm adjusts itself to reduce the difference between its predictions and the known correct labels.</p>
{sub('📖 Detailed Explanation')}<p>Two main sub-types: <b>Classification</b> (y is discrete/categorical, e.g., spam vs not-spam) and <b>Regression</b> (y is continuous, e.g., predicting house price). The learning objective is typically to minimize a loss function measuring the discrepancy between predicted ŷ and true y (e.g., cross-entropy for classification, MSE for regression) — connects directly to MLE.</p>
{sub('💡 Simple Example')}<p>Predicting whether an email is spam (classification) given a labeled dataset of emails marked spam/not-spam.</p>
{sub('🎯 Real-World/ML Example')}<p>Image classification (CNNs trained on labeled images), speech recognition, and most deep feedforward networks (Ch.6) are trained using supervised learning.</p>
{sub('✅ Advantages')}<p>Directly optimizes for the task of interest with clear feedback signal (labels); well-understood theory and evaluation metrics.</p>
{sub('❌ Limitations')}<p>Requires large amounts of labeled data, which can be expensive/time-consuming to obtain; does not scale well to domains where labels are scarce.</p>
{sub('🔄 Comparison with Related Concepts')}<p>Supervised (uses labels y) vs Unsupervised (no labels, next topic) vs Semi-Supervised (mix of labeled and unlabeled, Ch.4).</p>
{sub('⚠️ Common Mistakes')}<p>Confusing classification (discrete output) with regression (continuous output) when choosing loss functions.</p>
{sub('🧠 Important Points to Remember')}<ul><li>Supervised = requires labeled data.</li><li>Classification (discrete y) vs Regression (continuous y).</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul><li>(2M) Define supervised learning with example.</li><li>(2M) Differentiate classification and regression.</li></ul>
'''))

parts.append(topic('t-unsupervised', '8. Unsupervised Learning', 'H', f'''
{sub('⭐ Importance')}<p>Essential vocabulary, frequently paired with PCA/clustering examples; usually a 2-5 mark question.</p>
{sub('📌 Definition')}
{box('def', '<b>Unsupervised learning</b> algorithms learn useful structure/patterns from UNLABELED data — only input x is given, with no corresponding target y. The algorithm must discover structure on its own.')}
{sub('🧠 Intuition')}<p>Like exploring data without a teacher — the algorithm groups similar items together, finds compact representations, or estimates the underlying probability distribution, purely from the data\\u2019s own structure.</p>
{sub('📖 Detailed Explanation')}<p>Common tasks: <b>Clustering</b> (grouping similar data points, e.g., k-means), <b>Dimensionality reduction</b> (PCA, autoencoders — finding compact representations that preserve important structure), and <b>Density estimation</b> (modeling the underlying probability distribution p(x) that generated the data).</p>
{sub('💡 Simple Example')}<p>Grouping customers into segments based on purchasing behavior, without any predefined labels for "segment type".</p>
{sub('🎯 Real-World/ML Example')}<p>PCA (Ch.1) is unsupervised dimensionality reduction; k-means clustering for customer segmentation; autoencoders learning compressed representations of images without labels.</p>
{sub('✅ Advantages')}<p>Does not require expensive labeled data; can reveal hidden structure/patterns not apparent from a supervised task alone; useful for pretraining/feature learning.</p>
{sub('❌ Limitations')}<p>Harder to evaluate objectively (no ground-truth labels to compare against); results can be ambiguous or hard to interpret; quality of discovered structure not guaranteed to align with human-meaningful categories.</p>
{sub('🔄 Comparison with Related Concepts')}<p>Unsupervised (no labels, discovers structure) vs Supervised (labels, predicts known targets).</p>
{sub('⚠️ Common Mistakes')}<p>Assuming unsupervised methods always produce human-interpretable clusters/components; forgetting these methods have no access to ground truth for validation.</p>
{sub('🧠 Important Points to Remember')}<ul><li>Unsupervised = no labels.</li><li>Clustering, dimensionality reduction, density estimation are the three main tasks.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul><li>(2M) Define unsupervised learning with example.</li><li>(5M) Explain clustering and dimensionality reduction as unsupervised learning tasks.</li></ul>
'''))

parts.append(topic('t-sgd', '9. Stochastic Gradient Descent', 'VH', f'''
{sub('⭐ Importance')}<p>Extremely important — the actual algorithm used to train virtually all deep networks; near-guaranteed exam question, often compared with batch gradient descent.</p>
{sub('📌 Definition')}
{box('def', '<b>Stochastic Gradient Descent (SGD)</b> approximates the true gradient (computed over the ENTIRE training set) using the gradient computed on a small, randomly-sampled <b>minibatch</b> of examples, dramatically reducing per-step computational cost.')}
{sub('🧠 Intuition')}<p>Computing the exact gradient over millions of training examples every single update step is far too slow. SGD instead takes a "noisy but unbiased" estimate of the gradient from a small random subset — noisy individual steps still average out to move in roughly the correct overall direction, much faster.</p>
{sub('📖 Detailed Explanation')}<p>Standard (batch) gradient descent computes ∇θJ(θ) using ALL n training examples per update — cost scales with n, becoming prohibitive for large datasets. SGD instead samples a minibatch of size m (e.g., 32, 64, 256) and computes the gradient estimate on just that subset; because minibatches are drawn uniformly at random, the expected value of the minibatch gradient equals the true gradient, so SGD converges (in expectation) despite the added noise. The noise itself can even help escape shallow local minima/saddle points.</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'Minibatch gradient estimate: ĝ = (1/m) Σᵢ₌₁<sup>m</sup> ∇θ L(f(x⁽ⁱ⁾;θ), y⁽ⁱ⁾) <br>Update: θ ← θ − ε ĝ')}
{sub('💡 Simple Example')}<p>Dataset of 1,000,000 images; instead of computing gradient over all 1,000,000 per step (batch GD), SGD samples a minibatch of 64 images, computes the gradient on just those, and updates weights — repeating with new random minibatches until the full dataset has been seen (one "epoch").</p>
{sub('🎯 Real-World/ML Example')}<p>Virtually every deep learning framework (PyTorch, TensorFlow) trains networks using minibatch SGD (or its adaptive variants like Adam, covered in Ch.5 Unit 3) rather than full-batch gradient descent.</p>
{sub('🖼️ Diagram')}
<svg class="diagram" viewBox="0 0 260 130" xmlns="http://www.w3.org/2000/svg">
<path d="M20,110 Q130,10 240,110" fill="none" stroke="#ccc" stroke-width="2"/>
<polyline points="210,95 195,80 185,60 155,45 165,30 130,20 120,15" fill="none" stroke="#c0392b" stroke-width="2"/>
<text x="20" y="125" font-size="9">Noisy zig-zag SGD path vs smooth batch GD path (gray)</text>
</svg>
{sub('⚙️ Algorithm / Procedure')}<p>1. Initialize θ. 2. Repeat: shuffle data, split into minibatches. 3. For each minibatch, compute gradient estimate ĝ. 4. Update θ ← θ−εĝ. 5. Repeat over multiple epochs until convergence.</p>
{sub('📝 Pseudocode')}
<pre>theta = initialize()
for epoch in range(num_epochs):
    shuffle(training_data)
    for minibatch in split_into_batches(training_data, batch_size=m):
        g_hat = (1/m) * sum(grad(loss(f(x,theta), y)) for (x,y) in minibatch)
        theta = theta - epsilon * g_hat
return theta</pre>
{sub('✅ Advantages')}<p>Much faster per-update than full-batch GD; scales to massive datasets (does not need all data in memory); inherent noise can help escape poor local minima/saddle points; enables online/streaming learning.</p>
{sub('❌ Limitations')}<p>Noisy updates cause the loss to fluctuate rather than decrease smoothly; requires careful learning-rate tuning/decay schedules; convergence can be slower in terms of number of updates needed near the minimum.</p>
{sub('🔄 Comparison with Related Concepts')}
<table><tr><th>Method</th><th>Batch size</th><th>Speed/Update</th><th>Gradient noise</th></tr>
<tr><td>Batch GD</td><td>All n examples</td><td>Slow</td><td>None (exact)</td></tr>
<tr><td>SGD (true)</td><td>1 example</td><td>Fastest</td><td>High</td></tr>
<tr><td>Minibatch SGD</td><td>m (e.g., 32-256)</td><td>Fast</td><td>Moderate (most common in practice)</td></tr></table>
{sub('⚠️ Common Mistakes')}<p>Calling minibatch SGD simply "SGD" without clarifying batch size (technically true SGD uses batch size 1; in practice "SGD" commonly refers to minibatch SGD); forgetting to shuffle data between epochs (causes correlated/biased minibatches).</p>
{sub('🧠 Important Points to Remember')}<ul><li>θ←θ−εĝ where ĝ is a minibatch gradient estimate — MEMORIZE.</li><li>SGD trades exactness for massive speed/scalability gains.</li><li>Expected minibatch gradient = true gradient (unbiased estimator).</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul>
<li>(2M) Define stochastic gradient descent.</li>
<li>(5M) Compare batch gradient descent and stochastic gradient descent.</li>
<li>(10M) Explain the SGD algorithm with pseudocode, and discuss why it is preferred over batch gradient descent for deep learning.</li>
</ul>
'''))

parts.append(topic('t-challenges-dl', '10. Challenges Motivating Deep Learning', 'M', f'''
{sub('⭐ Importance')}<p>Conceptual/motivational topic — usually a 5-mark "why deep learning" question, sets up transition to Chapter 6.</p>
{sub('📌 Definition')}
{box('def', 'Classical (shallow) machine learning algorithms face fundamental challenges in high-dimensional spaces and with complex data (images, audio, text) — these challenges motivate deep learning\\u2019s use of multiple layers to learn hierarchical representations automatically.')}
{sub('🧠 Intuition')}<p>Traditional ML relies heavily on hand-engineered features (a human decides what patterns to look for). This does not scale to complex, high-dimensional data like raw pixels — deep learning instead learns the useful features/representations automatically from data through multiple layers of abstraction.</p>
{sub('📖 Detailed Explanation')}<p>Key challenges include: <b>Curse of dimensionality</b> — the number of possible configurations grows exponentially with the number of input dimensions, so data becomes extremely sparse in high-dimensional space, making it hard for local, similarity-based methods (like k-NN) to generalize. <b>Local constancy / smoothness assumptions</b> fail for complex functions — many classical algorithms assume the target function is smooth/simple and changes only slightly between neighboring points, which breaks down for the highly-varying functions needed for real-world tasks (e.g., image recognition, where a single pixel change is irrelevant but object identity involves complex nonlinear combinations of many pixels). <b>Manifold Learning</b> — deep learning instead assumes real-world high-dimensional data actually lies on a much lower-dimensional manifold (curved surface) embedded in the high-dimensional space; learning to represent this manifold structure (rather than assuming local smoothness everywhere) is more efficient and is what deep architectures naturally do through hierarchical feature learning.</p>
{sub('💡 Simple Example')}<p>A grid-based method to cover just 10 dimensions with 10 divisions each needs 10¹⁰ cells — infeasible; yet many real datasets have thousands of pixel dimensions, illustrating the curse of dimensionality.</p>
{sub('🎯 Real-World/ML Example')}<p>Raw image classification (millions of pixel values) is intractable for classical local-similarity methods but tractable for deep CNNs, which learn hierarchical features (edges → shapes → objects) exploiting the low-dimensional manifold structure of natural images.</p>
{sub('✅ Advantages')}<p>Understanding these challenges justifies WHY deep, hierarchical representation learning is needed rather than shallow models with hand-crafted features.</p>
{sub('❌ Limitations')}<p>Deep learning\\u2019s solutions (many layers, distributed representations) introduce their own new challenges — vanishing/exploding gradients, need for huge data and compute (addressed in Ch.5/6).</p>
{sub('🔄 Comparison with Related Concepts')}<p>Curse of dimensionality (classical ML struggle) vs Manifold hypothesis (deep learning\\u2019s answer — assume/learn lower-dimensional structure).</p>
{sub('⚠️ Common Mistakes')}<p>Assuming deep learning entirely avoids the curse of dimensionality (it mitigates it via representation learning and the manifold hypothesis, but does not eliminate the need for sufficient data).</p>
{sub('🧠 Important Points to Remember')}<ul><li>Curse of dimensionality: data sparsity grows exponentially with dimension.</li><li>Manifold hypothesis: real data lies on a lower-dimensional manifold within high-dimensional space.</li></ul>
{sub('🎓 Exam-Oriented Questions')}<ul><li>(2M) What is the curse of dimensionality?</li><li>(5M) Explain the challenges of classical ML that motivate deep learning.</li><li>(5M) Explain the manifold hypothesis.</li></ul>
'''))

with open('/home/claude/ch5ml_part2.html','w') as f:
    f.write(''.join(parts))
print("ch5ml part2 written, length:", len(''.join(parts)))
