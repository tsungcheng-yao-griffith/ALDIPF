import shap
import numpy as np
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
import csv
from sklearn.model_selection import train_test_split


model = load_model('CNNModel_bucket.h5')

with open('clean_message.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    text_data = [row[0] for row in reader]

# Load numeric data from CSV file
numeric_data = np.genfromtxt('SGABS_sub_items_bucketed.csv', delimiter=',')

# Load labels from CSV file
labels = np.genfromtxt('label4FASTTEXT.csv', dtype=np.int32)

# Tokenize the text data
tokenizer = Tokenizer()
tokenizer.fit_on_texts(text_data)
text_data = tokenizer.texts_to_sequences(text_data)
max_text_length = max([len(x) for x in text_data])
text_data = pad_sequences(text_data, maxlen=max_text_length)

# Split the data into train and test sets
X_text_train, X_text_test, X_num_train, X_num_test, y_train, y_test = train_test_split(text_data, numeric_data, labels, test_size=0.15, random_state=24)

print(X_text_train.shape)
print(X_num_train.shape)
print(X_text_test.shape)
print(X_num_test.shape)
print(y_train.shape)

# Step 3: Load the trained model and the SHAP Deep Explainer
explainer = shap.DeepExplainer(model, [X_text_train[:100], X_num_train[:100]])  # Provide suitable data for the explainer



# Step 4: Generate explanations
input_data = [X_text_train[:100], X_num_train[:100]]
explanation = explainer.shap_values([X_text_train[:100], X_num_train[:100]])


# Step 5: Visualize the explanations
shap.summary_plot(explanation, input_data, plot_type="bar")  # Example of a summary plot

