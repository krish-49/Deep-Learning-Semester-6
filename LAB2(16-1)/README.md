# DEEP LEARNING LAB – 2  
## Handwritten Digit Recognition Using MNIST

Course Name: Deep Learning  
Semester: VI  
Experiment No.: 2  
Title of Experiment:  
Study and Analysis of Activation Functions, Optimizers, Batch Normalization, and Dropout for Handwritten Digit Recognition  

---

## 1. Aim

To study the effect of different activation functions, optimizers, batch normalization, and dropout techniques on the performance of a Multi-Layer Perceptron (MLP) model for handwritten digit recognition using the MNIST dataset.

---

## 2. Results and Comparison

### 2.1 Activation Function Comparison  
(Optimizer = SGD, Batch Normalization = Enabled, Dropout = 0.0)

| Activation Function | Final Accuracy |
|-------------------|----------------|
| Sigmoid | 91.29% |
| Tanh | 94.47% |
| ReLU | 96.54% |

---

### 2.2 Optimizer Comparison  
(Activation = ReLU, Batch Normalization = Enabled, Dropout = 0.0)

| Optimizer | Final Accuracy |
|----------|----------------|
| SGD | 96.54% |
| SGD with Momentum | 98.18% |
| Adam | 98.14% |

---

### 2.3 Effect of Batch Normalization and Dropout  
(Activation = ReLU, Optimizer = Adam)

| Batch Normalization | Dropout Rate | Final Accuracy |
|--------------------|--------------|----------------|
| No | 0.0 | 98.21% |
| No | 0.1 | 98.17% |
| Yes | 0.25 | 97.92% |

---

## 3. Observations

- ReLU activation outperformed Sigmoid and Tanh.  
- Momentum and Adam optimizers improved convergence speed compared to basic SGD.  
- Batch Normalization did not significantly improve performance for shallow MLP models.  
- Dropout reduced overfitting, but higher dropout slightly reduced accuracy.  
- Minor accuracy variations occurred due to random initialization and batch shuffling.  

---

## 4. Conclusion

The experiment demonstrates that activation functions, optimizers, and regularization techniques significantly affect model performance. ReLU activation combined with Adam or Momentum optimizer achieved the best accuracy for handwritten digit recognition using the MNIST dataset.

---

End of Experiment – LAB 2
