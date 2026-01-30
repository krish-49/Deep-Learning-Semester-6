# Deep Learning Practical-3  
## Comparative Analysis of CNN Architectures

---

## Part A: CNN Architecture Comparison

<!-- ### Output Table

| Model     | Dataset  | Epochs | Training Accuracy (%) | Testing Accuracy (%) |
|-----------|----------|--------|------------------------|-----------------------|
| LeNet-5   | MNIST    | 5      | XX.XX                  | XX.XX                 |
| AlexNet   | CIFAR-10 | 10     | XX.XX                  | XX.XX                 |
| VGGNet    | CIFAR-10 | 10     | XX.XX                  | XX.XX                 |
| ResNet    | CIFAR-10 | 15     | XX.XX                  | XX.XX                 |
| MobileNet | CIFAR-10 | 10     | XX.XX                  | XX.XX                 |

### Observation

- LeNet performed well on MNIST due to simple patterns.
- Deep CNNs achieved higher accuracy on CIFAR-10.
- ResNet showed stable training due to residual connections.
- MobileNet reduced parameters with acceptable accuracy.

### Reason

- MNIST contains simple grayscale images, so shallow networks are sufficient.
- CIFAR-10 is complex and requires deeper feature extraction.
- Residual connections help prevent vanishing gradients.
- Depthwise convolution reduces computation cost. -->

---

## Part B: Loss Function and Optimizer Analysis

### Output Table

| Model   | Optimizer | Epochs | Loss Function | Train Accuracy (%) | Test Accuracy (%) |
|---------|-----------|--------|---------------|--------------------|-------------------|
| VGGNet  | Adam      | 10     | CrossEntropy  | 90.30              | XX.XX             |
| AlexNet | SGD       | 20     | Focal Loss    | 97.78              | XX.XX             |
| ResNet  | Adam      | 15     | ArcFace       | 75.95              | XX.XX             |

### Observation

- Adam optimizer converged faster than SGD.
- Focal loss improved learning on difficult samples.
- ArcFace loss produced better feature discrimination.
- SGD showed slower convergence.

### Reason

- Adam adapts learning rate automatically for each parameter.
- Focal loss focuses on misclassified samples.
- ArcFace enforces angular margin between classes.
- SGD uses fixed learning rate and converges slowly.

---

## Part C: Feature Visualization Using t-SNE

### Output Table

| Model  | Loss Function | Cluster Separation | Overlap Level | Observation |
|--------|---------------|--------------------|---------------|-------------|
| VGGNet | CrossEntropy  | Medium             | Moderate      | Partial separation |
| AlexNet| Focal Loss    | Good               | Low           | Better grouping |
| ResNet | ArcFace       | Excellent          | Very Low      | Best clustering |

### Observation

- ArcFace loss produced compact and well-separated clusters.
- CrossEntropy showed overlapping clusters.
- Focal loss showed moderate separation.
- Better clustering indicates better feature learning.

### Reason

- ArcFace increases inter-class distance.
- CrossEntropy focuses only on classification accuracy.
- Focal loss emphasizes difficult samples.
- t-SNE preserves neighborhood relationships.

---

## Overall Conclusion

- CNN performance increases with network depth.
- Adam optimizer provides faster convergence.
- ArcFace improves feature separability.
- Feature visualization validates classification performance.
<!-- - Model selection depends on dataset complexity. -->
