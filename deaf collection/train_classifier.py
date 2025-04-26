import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the data
data_dict = pickle.load(open('./data.pickle', 'rb'))

# Extract data and labels
data = data_dict['data']
labels = data_dict['labels']

# Determine the maximum length of the data entries
max_length = max(len(entry) for entry in data)

# Pad all data entries to the same length
padded_data = np.array([entry + [0] * (max_length - len(entry)) for entry in data])

# Convert labels to numpy array
labels = np.asarray(labels)

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(padded_data, labels, test_size=0.2, shuffle=True, stratify=labels)

# Initialize and train the model
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Predict and calculate accuracy
y_predict = model.predict(x_test)
score = accuracy_score(y_predict, y_test)

print('{}% of samples were classified correctly!'.format(score * 100))

# Save the trained model
with open('model.p', 'wb') as f:
    pickle.dump({'model': model}, f)
