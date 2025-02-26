from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
import csv
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from joblib import dump

# Load text data from CSV file
with open('clean_message.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    text_data = [row[0] for row in reader]

# Load numeric data from CSV file
numeric_data = np.genfromtxt('SGABS_sub_items.csv', delimiter=',')

# Load labels from CSV file
labels = np.genfromtxt('label4FASTTEXT.csv', dtype=np.int32)

# Tokenize the text data
tokenizer = Tokenizer()
tokenizer.fit_on_texts(text_data)
text_data = tokenizer.texts_to_sequences(text_data)
max_text_length = max([len(x) for x in text_data])
text_data = pad_sequences(text_data, maxlen=max_text_length)

# Combine text and numeric data
combined_data = np.concatenate((text_data, numeric_data), axis=1)

# Standardize the data
scaler = StandardScaler()
combined_data = scaler.fit_transform(combined_data)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(combined_data, labels, test_size=0.15, random_state=24)

# Define the SVM model
model = SVC(kernel='linear', C=1)

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
F1_score = f1_score(y_test, y_pred)

print('Accuracy:', accuracy)
print('F1 Score', F1_score)

dump(model, 'svm_model_test.pkl')
