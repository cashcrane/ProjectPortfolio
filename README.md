# Construction Schedule Subcontractor Trade ML Classification System

## Overview
This project automates the manual process of labeling scheduling activities with trade contractors. Using a Random Forest Classifier, the model achieves 98% accuracy, saving over 3,000 hours annually.

---

## Tools & Technologies
- **Python**: Pandas, Scikit-learn, NLTK
- **FastAPI**: For deployment
- **Vue.js**: Front-end integration

---

## Data
The dataset includes 500,000 records of scheduling activities, with features such as:
- **Activity Description**: Text describing the task.
- **Duration**: Time allocated for the task.
- **Trade Label**: The assigned trade contractor (target variable).

---

## Methodology
### Feature Engineering
```python
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample code for text vectorization
vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(df['activity_description'])

print(X.shape)  # Output: (500000, 1000)
