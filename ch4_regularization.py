# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '.')
from gen_helpers import topic, sub, box, chapter_header

parts = [chapter_header('ch4', 'Chapter 4: Regularization for Deep Learning')]

parts.append(topic('t-param-norm', '1. Parameter Norm Penalties', 'VH', f'''
{sub('⭐ Importance')}<p>Very important — directly connected to L1/L2 regularization, overfitting, and optimization. Common 5- and 10-mark topic.</p>
{sub('📌 Definition')}
{box('def', '<b>Parameter norm penalties</b> add a penalty term based on the magnitude of model parameters to the training objective. This discourages excessively large weights and helps reduce overfitting.')}
{sub('🧠 Intuition')}<p>A model with very large weights can become overly sensitive to training data. Penalizing large weights encourages a simpler model that generalizes better.</p>
{sub('🔢 Mathematical Formulation')}
{box('formula', 'L<sub>total</sub> = L<sub>data</sub> + αΩ(θ)<br><br>L1: Ω(θ) = ‖θ‖<sub>1</sub> = Σ|θ<sub>i</sub>|<br>L2: Ω(θ) = ‖θ‖<sub>2</sub><sup>2</sup> = Σθ<sub>i</sub><sup>2</sup>')}
{sub('📖 Detailed Explanation')}<p>L1 regularization tends to produce sparse parameters because the absolute-value penalty encourages some weights to become exactly zero. L2 regularization smoothly discourages large weights and is commonly called weight decay.</p>
{sub('💡 Example')}<p>If the original loss is 10 and the L2 penalty contributes 0.8, the regularized objective becomes 10.8.</p>
{sub('🔄 Comparison with Related Concepts')}<p>L1 → sparsity and feature selection. L2 → smaller, distributed weights and smoother solutions.</p>
{sub('⚠️ Common Mistakes')}<p>Confusing ‖θ‖₂ with ‖θ‖₂² and forgetting that the regularization coefficient controls penalty strength.</p>
{sub('🧠 Important Points to Remember')}<ul><li>Regularization reduces overfitting.</li><li>L1 encourages sparsity.</li><li>L2 penalizes large weights.</li></ul>
{sub('🎯 Exam-Oriented Questions')}<ul><li>(2M) Define L1 and L2 regularization.</li><li>(5M) Explain parameter norm penalties.</li><li>(10M) Compare L1 and L2 regularization mathematically.</li></ul>
'''))

parts.append(topic('t-constrained-reg', '2. Norm Penalties as Constrained Optimization', 'H', f'''
{sub('⭐ Importance')}<p>Important mathematical connection between regularization and constrained optimization.</p>
{sub('📌 Definition')}
{box('def', 'A regularized optimization problem can often be expressed as an equivalent constrained optimization problem in which the parameter norm is restricted to a fixed budget.')}
{sub('🔢 Mathematical Formulation')}
{box('formula', 'Penalty form: minimize L(θ) + αΩ(θ)<br><br>Constrained form: minimize L(θ) subject to Ω(θ) ≤ c')}
{sub('🧠 Intuition')}<p>Instead of saying "large weights are expensive", we can say "the model is allowed only a limited weight budget."</p>
{sub('📖 Detailed Explanation')}<p>The parameter α controls the strength of the penalty, while c controls the size of the feasible region. Under appropriate conditions these formulations are closely related through Lagrange multipliers.</p>
{sub('🎯 Exam-Oriented Questions')}<ul><li>(5M) Explain regularization as constrained optimization.</li><li>(10M) Derive the relationship between penalty and constrained forms.</li></ul>
'''))

parts.append(topic('t-underconstrained', '3. Regularization and Under-Constrained Problems', 'H', f'''
{sub('⭐ Importance')}<p>Important for understanding why regularization is necessary when many parameter settings can fit the training data.</p>
{sub('📌 Definition')}
{box('def', 'An under-constrained problem has insufficient information or restrictions to determine a unique desirable solution. Regularization adds useful constraints or preferences to select a better solution.')}
{sub('🧠 Intuition')}<p>If many models produce almost identical training performance, regularization prefers simpler parameter configurations.</p>
{sub('📖 Detailed Explanation')}<p>Deep networks can have huge numbers of parameters and may have many solutions with low training error. Regularization introduces an inductive preference toward solutions that are less likely to overfit.</p>
{sub('🎯 Exam-Oriented Questions')}<ul><li>(5M) Why is regularization useful in under-constrained problems?</li><li>(10M) Discuss regularization as an inductive bias.</li></ul>
'''))

parts.append(topic('t-augmentation', '4. Dataset Augmentation', 'H', f'''
{sub('⭐ Importance')}<p>Common practical regularization technique, especially in image and speech applications.</p>
{sub('📌 Definition')}
{box('def', 'Dataset augmentation creates additional training examples by applying label-preserving transformations to existing examples.')}
{sub('🧠 Intuition')}<p>Instead of collecting entirely new data, create realistic variations of existing data so the model learns more robust patterns.</p>
{sub('💡 Example')}<p>For an image classifier, small rotations, crops, translations, or horizontal flips may create additional valid training examples when the label remains unchanged.</p>
{sub('🎯 Exam-Oriented Questions')}<ul><li>(2M) Define data augmentation.</li><li>(5M) Explain how data augmentation reduces overfitting.</li></ul>
'''))

parts.append(topic('t-noise', '5. Noise Robustness', 'M', f'''
{sub('📌 Definition')}
{box('def', 'Noise robustness is the ability of a model to maintain useful performance when training or input data contains perturbations or noise.')}
{sub('🧠 Intuition')}<p>Training with appropriate noise can prevent the network from depending too strongly on individual training examples or features.</p>
{sub('💡 Example')}<p>Adding small noise to inputs during training can encourage the model to learn stable representations.</p>
{sub('🎯 Exam-Oriented Questions')}<ul><li>(2M) What is noise robustness?</li><li>(5M) Explain noise-based regularization.</li></ul>
'''))

parts.append(topic('t-semi-supervised', '6. Semi-Supervised Learning', 'M', f'''
{sub('📌 Definition')}
{box('def', 'Semi-supervised learning uses a small amount of labeled data together with a larger amount of unlabeled data.')}
{sub('🧠 Intuition')}<p>Unlabeled examples can provide information about the structure of the data distribution, helping improve generalization.</p>
{sub('🎯 Exam-Oriented Questions')}<ul><li>(2M) Define semi-supervised learning.</li><li>(5M) Explain its role in deep learning.</li></ul>
'''))

parts.append(topic('t-multitask', '7. Multi-Task Learning', 'M', f'''
{sub('📌 Definition')}
{box('def', '<b>Multi-task learning</b> trains one model to perform multiple related tasks simultaneously, allowing tasks to share useful representations.')}
{sub('🧠 Intuition')}<p>Learning several related tasks together can act as a regularizer because the shared representation must work across multiple objectives.</p>
{sub('🎯 Exam-Oriented Questions')}<ul><li>(2M) Define multi-task learning.</li><li>(5M) Explain how multi-task learning regularizes a model.</li></ul>
'''))

parts.append(topic('t-early-stop', '8. Early Stopping', 'VH', f'''
{sub('⭐ Importance')}<p>Very important and frequently asked practical regularization method.</p>
{sub('📌 Definition')}
{box('def', '<b>Early stopping</b> stops training when performance on a validation set stops improving, rather than continuing until training error is minimized.')}
{sub('🧠 Intuition')}<p>Training too long may make the model memorize training data. Stop near the point where validation performance is best.</p>
{sub('🔢 Procedure')}<p>Train → monitor validation loss → save best model → stop after validation performance fails to improve for a chosen patience period.</p>
{sub('🎯 Exam-Oriented Questions')}<ul><li>(2M) Define early stopping.</li><li>(5M) Explain early stopping with a validation-loss diagram.</li><li>(10M) Discuss early stopping as regularization.</li></ul>
'''))

parts.append(topic('t-parameter-sharing', '9. Parameter Tying and Parameter Sharing', 'H', f'''
{sub('📌 Definition')}
{box('def', 'Parameter sharing forces different parts of a model to use the same parameter values, reducing the number of independent parameters.')}
{sub('🧠 Intuition')}<p>If the same pattern detector is useful in multiple locations, one shared set of parameters can be reused rather than learning separate copies.</p>
{sub('💡 Example')}<p>Convolutional neural networks use shared convolution filters across spatial locations.</p>
{sub('🎯 Exam-Oriented Questions')}<ul><li>(2M) Define parameter sharing.</li><li>(5M) Explain parameter tying with an ML example.</li></ul>
'''))

parts.append(topic('t-sparse', '10. Sparse Representations', 'M', f'''
{sub('📌 Definition')}
{box('def', 'A sparse representation describes an input using relatively few active features or non-zero components.')}
{sub('🧠 Intuition')}<p>Instead of representing information using every available feature, only a small subset becomes strongly active.</p>
{sub('🎯 Exam-Oriented Questions')}<ul><li>(2M) Define sparse representation.</li><li>(5M) Explain sparsity as a regularization idea.</li></ul>
'''))

parts.append(topic('t-bagging', '11. Bagging and Other Ensemble Methods', 'M', f'''
{sub('📌 Definition')}
{box('def', '<b>Bagging</b> trains multiple models on different bootstrap samples and combines their predictions, often reducing variance.')}
{sub('🧠 Intuition')}<p>Several imperfect models can collectively make a more stable prediction than one model.</p>
{sub('🎯 Exam-Oriented Questions')}<ul><li>(2M) Define bagging.</li><li>(5M) Explain how ensemble methods reduce variance.</li></ul>
'''))

parts.append(topic('t-dropout', '12. Dropout', 'VH', f'''
{sub('⭐ Importance')}<p>Very High — one of the most important deep-learning regularization topics and a common exam question.</p>
{sub('📌 Definition')}
{box('def', '<b>Dropout</b> randomly sets a subset of activations to zero during training, preventing units from relying too strongly on specific other units.')}
{sub('🧠 Intuition')}<p>Each training step uses a slightly different sub-network. This reduces co-adaptation and behaves like training an ensemble of many related networks.</p>
{sub('🔢 Mathematical Formulation')}<p>With keep probability p, a unit is retained with probability p. In inverted dropout, retained activations are scaled by 1/p during training.</p>
{sub('🎯 Exam-Oriented Questions')}<ul><li>(2M) Define dropout.</li><li>(5M) Explain the working of dropout.</li><li>(10M) Discuss dropout as a regularization technique.</li></ul>
'''))

parts.append(topic('t-adversarial', '13. Adversarial Training', 'M', f'''
{sub('📌 Definition')}
{box('def', 'Adversarial training exposes a model to deliberately constructed small input perturbations during training so that it becomes more robust to such perturbations.')}
{sub('🧠 Intuition')}<p>The model learns not only from normal examples but also from challenging nearby examples.</p>
{sub('🎯 Exam-Oriented Questions')}<ul><li>(2M) Define adversarial training.</li><li>(5M) Explain how adversarial training improves robustness.</li></ul>
'''))

parts.append(topic('t-tangent-distance', '14. Tangent Distance', 'L', f'''
{sub('📌 Definition')}
{box('def', 'Tangent distance measures similarity by considering small transformations of examples along directions that preserve their essential identity.')}
{sub('💡 Example')}<p>For handwritten digits, small translations or rotations may change the pixels but not the identity of the digit.</p>
{sub('🎯 Exam-Oriented Questions')}<ul><li>(2M) What is tangent distance?</li><li>(5M) Explain its motivation.</li></ul>
'''))

parts.append(topic('t-tangent-prop', '15. Tangent Prop', 'L', f'''
{sub('📌 Definition')}
{box('def', 'Tangent Prop encourages a neural network to produce stable outputs under specified small transformations of its inputs.')}
{sub('🧠 Intuition')}<p>If a small transformation should not change the label, the network should ideally change its output very little.</p>
{sub('🎯 Exam-Oriented Questions')}<ul><li>(2M) Define Tangent Prop.</li><li>(5M) Explain transformation invariance using Tangent Prop.</li></ul>
'''))

parts.append(topic('t-manifold', '16. Manifold Tangent Classifiers', 'L', f'''
{sub('📌 Definition')}
{box('def', 'Manifold Tangent Classifiers use tangent directions of the data manifold to encourage representations that are invariant to small transformations along that manifold.')}
{sub('🧠 Intuition')}<p>Real-world data often lies near a lower-dimensional manifold. Small movements along that manifold can preserve semantic identity.</p>
{sub('🎯 Exam-Oriented Questions')}<ul><li>(2M) What is a manifold tangent classifier?</li><li>(5M) Explain the connection between manifolds and invariance.</li></ul>
'''))

parts.append('''
<div class="revision-box">
<h3>📚 Unit 3 — Chapter 4 Quick Revision</h3>
<ul class="priority-list">
<li>🔥 Parameter Norm Penalties — L1 vs L2</li>
<li>🔥 Early Stopping</li>
<li>🔥 Dropout</li>
<li>🟠 Norm Penalties as Constrained Optimization</li>
<li>🟠 Dataset Augmentation</li>
<li>🟠 Parameter Tying and Parameter Sharing</li>
<li>🟡 Noise Robustness</li>
<li>🟡 Semi-Supervised Learning</li>
<li>🟡 Multi-Task Learning</li>
<li>🟡 Sparse Representations</li>
<li>🟡 Bagging and Ensemble Methods</li>
<li>🟡 Adversarial Training</li>
<li>🟢 Tangent Distance</li>
<li>🟢 Tangent Prop</li>
<li>🟢 Manifold Tangent Classifiers</li>
</ul>
</div>
''')

if __name__ == '__main__':
    with open('ch4_regularization.html', 'w', encoding='utf-8') as f:
        f.write(''.join(parts))
    print("Chapter 4 generated:", len(''.join(parts)), "characters")