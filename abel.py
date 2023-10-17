import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Generate sample data
X = np.random.rand(200, 2) * 10
y = np.zeros(200)
y[100:] = 1

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create SVM classifier
clf = SVC(kernel='linear')

# Train classifier on training set
clf.fit(X_train, y_train)

# Predict labels for testing set
y_pred = clf.predict(X_test)

# Calculate accuracy of classifier
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)