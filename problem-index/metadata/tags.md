# Canonical Tag Registry

Every tag below maps 1:1 to a topic in math-topics.md or ml-roadmap.md.
Use ONLY these tags. If a concept isn't listed here, it doesn't get a tag.

---

## Math — Basics
#arithmetic-and-basic-algebra
#functions-and-graphs
#sets-and-logic
#summation-and-product-notation
#exponents-and-logarithms
#trigonometry-basics
#sequences-and-series
#combinatorics-and-counting

## Math — Calculus
#single-variable-calculus
#multivariable-calculus
#chain-rule
#taylor-series

## Math — Linear Algebra
#vector-algebra
#matrix-algebra
#systems-of-linear-equations
#vector-spaces-and-subspaces
#linear-transformations
#eigenvalues-and-eigenvectors
#matrix-decompositions
#norms-and-inner-products
#orthogonality-and-projections

## Math — Probability and Statistics
#probability-axioms
#conditional-probability-and-bayes-theorem
#random-variables
#probability-distributions
#expectation-variance-covariance
#joint-marginal-conditional-distributions
#law-of-large-numbers-and-clt
#maximum-likelihood-estimation
#maximum-a-posteriori-estimation
#bayesian-inference
#descriptive-statistics
#hypothesis-testing
#confidence-intervals
#bias-variance-tradeoff
#entropy-cross-entropy-kl-divergence
#mutual-information

## Math — Optimization
#optimization-fundamentals
#gradient-descent
#lagrange-multipliers
#convex-optimization
#numerical-methods
#automatic-differentiation
#backpropagation

## Math — Advanced Probability and Sampling
#monte-carlo-methods
#markov-chains
#mcmc-sampling
#variational-inference
#expectation-maximization

## Math — Advanced Topics
#gaussian-processes
#kernel-methods
#measure-theory
#concentration-inequalities
#pac-learning-and-vc-dimension
#rademacher-complexity
#graph-theory
#spectral-graph-theory
#manifold-learning
#topology-basics
#tensor-algebra
#functional-analysis
#optimal-transport
#information-geometry
#category-theory

---

## ML — Level 7 (Entry ML)
#linear-regression
#logistic-regression
#k-nearest-neighbors
#k-means-clustering
#naive-bayes
#pca
#feature-engineering
#cross-validation

## ML — Level 8 (Core ML)
#decision-trees
#random-forests
#gradient-boosting
#support-vector-machines
#regularization
#dimensionality-reduction
#evaluation-metrics
#dbscan
#gaussian-mixture-models

## ML — Level 9 (Neural Network Foundations)
#perceptron-and-mlps
#activation-functions
#loss-functions
#optimizers
#batch-normalization
#dropout
#weight-initialization

## ML — Level 10 (Deep Learning Architectures)
#cnns
#rnns
#lstms-and-grus
#autoencoders
#word-embeddings
#seq2seq
#object-detection
#semantic-segmentation

## ML — Level 11 (Advanced Deep Learning)
#attention-mechanisms
#transformers
#bert
#large-language-models
#gans
#vaes
#diffusion-models
#transfer-learning
#graph-neural-networks
#contrastive-learning

## ML — Level 12 (Probabilistic and Bayesian ML)
#bayesian-linear-regression
#bayesian-neural-networks
#hidden-markov-models
#bayesian-optimization

## ML — Level 13 (Reinforcement Learning)
#markov-decision-processes
#dynamic-programming
#monte-carlo-rl
#temporal-difference-learning
#policy-gradient-methods
#actor-critic-methods
#deep-q-networks
#model-based-rl

## ML — Level 14 (Time Series and Structured Prediction)
#autoregressive-models
#exponential-smoothing
#time-series-forecasting
#recurrent-forecasting
#temporal-fusion-transformers
#survival-analysis
#change-point-detection
#causal-inference

## ML — Level 15 (Advanced Theory)
#rkhs
#neural-tangent-kernels

---

## Context Tags (unchanged)
#tacit-knowledge-ml
#quick-win
#automation
#data-integration
#workflow-orchestration
#compliance
#worker-facing
#revenue-impact
#ai-agent
#ai-platform

## Deprecated (do not use)
#ml-nlp → use NLP-related ML tags directly
#ml-classification → use specific classifier tags
#ml-computer-vision → use #cnns + task tags
#ml-optimization → use #optimization-fundamentals or specific optimizer tags
#ml-recommendation → use #collaborative-filtering or relevant technique
#ml-time-series → use #time-series-forecasting
#simulation → no replacement
#cnn → use #cnns
#lstm → use #lstms-and-grus
#llm → use #large-language-models
#svm → use #support-vector-machines
#rnn → use #rnns
#autoencoder → use #autoencoders
#gan → use #gans
#bert → stays #bert
#bayesian-network → use #bayesian-inference
#gaussian-process → use #gaussian-processes
#isolation-forest → use #evaluation-metrics + #gradient-boosting or appropriate technique
#binary-classification → use #logistic-regression or relevant classifier + #evaluation-metrics
#multiclass-classification → use relevant classifier + #evaluation-metrics
#regression → use #linear-regression or #gradient-boosting as appropriate
#named-entity-recognition → use #bert or #transformers + #transfer-learning
#text-classification → use #bert or #transformers + #transfer-learning
#text-generation → use #large-language-models
#speech-recognition → use #cnns or #transformers + relevant tags
#ocr → use #cnns + #object-detection
#pose-estimation → use #cnns + #object-detection
#recommendation → use relevant technique tags
#ranking → use relevant technique tags
#computer-vision → use #cnns + task-specific tags
#nlp → use #bert or #transformers or #large-language-models as appropriate
#speech-processing → use #cnns or #rnns + signal tags
#tabular-ml → use specific algorithm tags (#gradient-boosting, #random-forests, etc.)
#graph-ml → use #graph-neural-networks
#multimodal → use relevant architecture tags
#signal-processing → use relevant technique tags
#anomaly-detection → use #dbscan or #gaussian-mixture-models or relevant technique
#time-series-forecasting → stays #time-series-forecasting
#change-point-detection → stays #change-point-detection
#survival-analysis → stays #survival-analysis
#causal-inference → stays #causal-inference
#seq2seq → stays #seq2seq
#object-detection → stays #object-detection
#semantic-segmentation → stays #semantic-segmentation
#reinforcement-learning → use specific RL tags (#markov-decision-processes, etc.)
#diffusion-model → use #diffusion-models
#k-means → use #k-means-clustering
#logistic-regression → stays #logistic-regression
#linear-regression → stays #linear-regression
#random-forest → use #random-forests
#gradient-boosting → stays #gradient-boosting
#transformer → use #transformers
