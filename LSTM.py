import tensorflow as tf
from tensorflow.keras.layers import Input, Embedding, LSTM, Dense, Concatenate, Dropout
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
import numpy as np
import csv
import pickle

# Load text data from CSV file
with open('clean_message.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    text_data = [row[0] for row in reader]

# Load numeric data from CSV file
numeric_data = np.genfromtxt('SGABS_sub_items_allZERO.csv', delimiter=',')

# Load labels from CSV file
labels = np.genfromtxt('label4FASTTEXT.csv', dtype=np.int32)

# Tokenize the text data
tokenizer = Tokenizer()
tokenizer.fit_on_texts(text_data)
text_data = tokenizer.texts_to_sequences(text_data)
max_text_length = max([len(x) for x in text_data])
text_data = tf.keras.preprocessing.sequence.pad_sequences(text_data, maxlen=max_text_length)

# Split the data into train and test sets
X_text_train, X_text_test, X_num_train, X_num_test, y_train, y_test = train_test_split(text_data, numeric_data, labels, test_size=0.15, random_state=24)

# Load pre-trained word vectors
word_vectors = 'crawl-300d-2M.vec'

# Create an embedding matrix
num_words = len(tokenizer.word_index) + 1
embedding_dim = 300
embedding_matrix = np.zeros((num_words, embedding_dim))
with open(word_vectors, 'r', encoding='utf-8') as f:
    for line in f:
        values = line.split()
        word = values[0]
        if word in tokenizer.word_index:
            embedding_matrix[tokenizer.word_index[word]] = np.asarray(values[1:], dtype='float32')

# Define the LSTM model
text_input = Input(shape=(max_text_length,))
text_embedded = Embedding(input_dim=num_words, output_dim=embedding_dim, weights=[embedding_matrix], trainable=True)(text_input)
text_encoded = LSTM(units=128)(text_embedded)
text_encoded = Dropout(0.5)(text_encoded)

num_input = Input(shape=(numeric_data.shape[1],))
num_dense1 = Dense(64, activation='relu')(num_input)
num_dense2 = Dense(32, activation='relu')(num_dense1)
num_dense3 = Dense(2, activation='relu')(num_dense2)

combined = Concatenate()([text_encoded, num_dense3])
output = Dense(len(np.unique(labels)), activation='softmax')(combined)

model = tf.keras.models.Model(inputs=[text_input, num_input], outputs=output)

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Convert labels to one-hot encoded format
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Train the model
model.fit([X_text_train, X_num_train], y_train, epochs=150, batch_size=32)

# Evaluate the model
y_pred = model.predict([X_text_test, X_num_test])
y_pred = np.argmax(y_pred, axis=1)
y_test = np.argmax(y_test, axis=1)
accuracy = accuracy_score(y_test, y_pred)
F1_score = f1_score(y_test, y_pred, average='weighted')
print('Accuracy:', accuracy)
print('F1 Score', F1_score)

# Save the model
model.save('LSTMModel.h5')
