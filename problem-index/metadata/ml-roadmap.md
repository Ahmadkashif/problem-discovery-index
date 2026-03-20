# ML Learning Dependency Map

15 levels (0–15). Each topic lists its prerequisites with `←`. Levels 0–6 are pure math, Levels 7–15 are ML topics. Multiple items at the same level can be learned in parallel.

---

## Level 0 — No Prerequisites

- Arithmetic and basic algebra
- Sets and logic
- Functions and graphs

## Level 1 — Requires Level 0

- Exponents and logarithms
- Summation and product notation
- Sequences and series
- Combinatorics and counting
- Trigonometry basics

## Level 2 — Core Math Foundations

- **Single-variable calculus** ← algebra, functions, exponents, trigonometry
- **Vector algebra** ← algebra
- **Probability axioms and rules** ← sets, combinatorics, summation notation

## Level 3 — Building Blocks

- **Multivariable calculus** ← single-variable calculus, vector algebra
- **Matrix algebra** ← vector algebra, algebra
- **Random variables and distributions** ← probability axioms, single-variable calculus (for continuous)
- **Descriptive statistics** ← summation notation, probability axioms

## Level 4 — Core Linear Algebra

- **Systems of linear equations** ← matrix algebra
- **Vector spaces and subspaces** ← matrix algebra, vector algebra
- **Norms and inner products** ← vector algebra, single-variable calculus
- **Linear transformations** ← matrix algebra, vector spaces
- **Expectation, variance, covariance** ← random variables, single-variable calculus
- **Joint, marginal, conditional distributions** ← random variables, multivariable calculus, conditional probability
- **Bayes' theorem** ← probability axioms, conditional probability

## Level 5 — Intermediate Math

- **Eigenvalues and eigenvectors** ← linear transformations, systems of linear equations
- **Orthogonality and projections** ← norms, inner products, vector spaces
- **Matrix decompositions (SVD, LU, QR, Cholesky)** ← eigenvalues, orthogonality
- **Taylor series and approximations** ← single-variable calculus, sequences and series
- **Gradient, Jacobian, Hessian** ← multivariable calculus, matrix algebra
- **Chain rule (multivariate)** ← multivariable calculus, matrix algebra
- **Law of large numbers, CLT** ← expectation, variance, sequences
- **Entropy, cross-entropy, KL divergence** ← probability distributions, logarithms, expectation
- **Hypothesis testing, p-values, confidence intervals** ← distributions, CLT, expectation

## Level 6 — Optimization Foundations

- **Optimization fundamentals (convexity, minima, maxima)** ← multivariable calculus, gradient/Hessian
- **Gradient descent (batch, SGD, mini-batch)** ← optimization fundamentals, chain rule
- **Lagrange multipliers, constrained optimization** ← multivariable calculus, optimization fundamentals
- **Maximum likelihood estimation** ← probability distributions, optimization fundamentals, logarithms
- **Maximum a posteriori estimation** ← MLE, Bayes' theorem

---

## Level 7 — Entry ML

- **Linear regression** ← matrix algebra, gradient descent, MLE, expectation/variance
- **Logistic regression** ← linear regression, probability distributions, cross-entropy, gradient descent
- **k-Nearest Neighbors** ← norms, descriptive statistics
- **k-Means clustering** ← norms, expectation, optimization fundamentals
- **Naive Bayes** ← Bayes' theorem, probability distributions, MLE
- **Principal Component Analysis (PCA)** ← eigenvalues, SVD, orthogonality, variance
- **Feature engineering and preprocessing** ← descriptive statistics, distributions, linear algebra basics
- **Bias-variance tradeoff** ← expectation, variance, MLE, linear regression
- **Cross-validation and model selection** ← bias-variance tradeoff, hypothesis testing

## Level 8 — Core ML

- **Decision trees** ← entropy, information gain (from KL divergence), descriptive statistics
- **Random forests** ← decision trees, combinatorics, bias-variance tradeoff
- **Gradient boosting (XGBoost, LightGBM)** ← decision trees, gradient descent, Taylor approximations, bias-variance tradeoff
- **Support Vector Machines** ← Lagrange multipliers, norms, inner products, optimization fundamentals
- **Regularization (L1, L2, elastic net)** ← linear regression, logistic regression, norms, Lagrange multipliers
- **Dimensionality reduction (t-SNE, UMAP)** ← PCA, probability distributions, KL divergence, norms
- **Evaluation metrics (precision, recall, AUC, F1)** ← probability, conditional probability, hypothesis testing
- **DBSCAN** ← norms, density estimation, graph connectivity
- **Gaussian Mixture Models** ← probability distributions, MLE, k-means
- **Expectation-Maximization algorithm** ← GMMs, MLE, Bayes' theorem, KL divergence

## Level 9 — Neural Network Foundations

- **Perceptron and multilayer perceptrons** ← logistic regression, matrix algebra, chain rule
- **Backpropagation** ← chain rule (multivariate), computational graphs, matrix algebra
- **Automatic differentiation** ← backpropagation, chain rule, computational graphs
- **Activation functions** ← single-variable calculus, logistic regression
- **Loss functions (MSE, cross-entropy, hinge)** ← MLE, entropy, cross-entropy, SVMs
- **Optimizers (Adam, RMSProp, momentum)** ← gradient descent, exponential moving averages, adaptive learning rates
- **Batch normalization** ← descriptive statistics, expectation/variance, chain rule
- **Dropout and regularization in NNs** ← regularization, probability, bias-variance tradeoff
- **Weight initialization** ← variance, distributions, activation functions
- **Kernel methods and kernel trick** ← SVMs, inner products, norms, linear transformations

## Level 10 — Deep Learning Architectures

- **Convolutional Neural Networks (CNNs)** ← MLPs, backpropagation, linear transformations, matrix algebra
- **Recurrent Neural Networks (RNNs)** ← MLPs, backpropagation, sequences, chain rule
- **LSTMs and GRUs** ← RNNs, vanishing gradients, activation functions
- **Autoencoders** ← MLPs, PCA, loss functions, dimensionality reduction
- **Word embeddings (Word2Vec, GloVe)** ← matrix decompositions (SVD), probability distributions, cross-entropy
- **Sequence-to-sequence models** ← RNNs/LSTMs, conditional probability
- **Object detection (YOLO, Faster R-CNN)** ← CNNs, regression, classification, IoU metrics
- **Semantic segmentation** ← CNNs, object detection, upsampling/transposed convolutions

## Level 11 — Advanced Deep Learning

- **Attention mechanisms** ← seq2seq, softmax (from logistic regression), matrix algebra
- **Transformers** ← attention mechanisms, layer normalization, positional encoding
- **BERT and masked language models** ← transformers, cross-entropy, probability distributions
- **Large Language Models (GPT family)** ← transformers, autoregressive modeling, cross-entropy
- **Generative Adversarial Networks (GANs)** ← MLPs/CNNs, game theory basics, KL divergence, optimization
- **Variational Autoencoders (VAEs)** ← autoencoders, Bayesian inference, KL divergence, variational inference
- **Diffusion models** ← VAEs, Markov chains, score matching, stochastic differential equations
- **Transfer learning and fine-tuning** ← any deep architecture, bias-variance tradeoff
- **Graph Neural Networks** ← MLPs, graph theory, adjacency/Laplacian matrices, spectral graph theory
- **Contrastive learning (SimCLR, CLIP)** ← cross-entropy, norms, data augmentation, CNNs/transformers

## Level 12 — Probabilistic and Bayesian ML

- **Bayesian linear regression** ← linear regression, Bayes' theorem, Gaussian distributions, prior/posterior
- **Gaussian processes** ← Bayesian inference, kernel methods, matrix algebra, multivariate Gaussians
- **Bayesian neural networks** ← neural networks, Bayesian inference, variational inference
- **Markov chains** ← conditional probability, matrix algebra, eigenvalues
- **Hidden Markov Models** ← Markov chains, EM algorithm, dynamic programming
- **MCMC sampling (Metropolis-Hastings, Gibbs)** ← Markov chains, Bayesian inference, probability distributions
- **Variational inference** ← KL divergence, Bayesian inference, optimization
- **Bayesian optimization** ← Gaussian processes, acquisition functions, optimization

## Level 13 — Reinforcement Learning

- **Markov Decision Processes** ← Markov chains, conditional probability, expectation
- **Dynamic programming (value/policy iteration)** ← MDPs, matrix algebra, convergence (sequences)
- **Monte Carlo methods for RL** ← MDPs, law of large numbers, sampling
- **Temporal difference learning (Q-learning, SARSA)** ← Monte Carlo RL, dynamic programming, gradient descent
- **Policy gradient methods (REINFORCE)** ← TD learning, gradient descent, probability distributions, log-derivative trick
- **Actor-Critic methods (A2C, A3C, PPO)** ← policy gradients, value functions, optimization
- **Deep Q-Networks (DQN)** ← Q-learning, CNNs/MLPs, experience replay
- **Model-based RL** ← MDPs, Gaussian processes or neural networks, planning

## Level 14 — Time Series and Structured Prediction

- **Autoregressive models (AR, ARIMA)** ← linear regression, time series stationarity, autocorrelation
- **Exponential smoothing** ← weighted averages, optimization
- **Time series forecasting with ML** ← gradient boosting or neural networks, feature engineering, cross-validation for time series
- **Recurrent forecasting (DeepAR, N-BEATS)** ← LSTMs, probability distributions, autoregressive models
- **Temporal Fusion Transformers** ← transformers, time series forecasting, attention
- **Survival analysis** ← probability distributions, MLE, hazard functions, censored data
- **Change-point detection** ← hypothesis testing, Bayesian inference, time series
- **Causal inference** ← probability, conditional independence, graph theory, regression, counterfactuals

## Level 15 — Advanced Theory

- **Convex optimization and duality** ← Lagrange multipliers, convexity, linear algebra
- **PAC learning and VC dimension** ← probability, combinatorics, hypothesis testing
- **Rademacher complexity** ← PAC learning, expectation, probability
- **Concentration inequalities (Hoeffding, Chernoff)** ← probability, expectation, CLT
- **Reproducing kernel Hilbert spaces (RKHS)** ← kernel methods, functional analysis, inner products
- **Optimal transport** ← probability distributions, linear programming, measure theory
- **Information geometry** ← KL divergence, differential geometry, manifolds, Fisher information
- **Tensor algebra** ← linear algebra, multilinear maps
- **Manifold learning** ← differential geometry basics, dimensionality reduction, eigenvalues
- **Neural tangent kernels** ← kernel methods, neural networks, functional analysis
