from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

app = Flask(__name__)

df = pd.read_csv('news.csv')
x = df['text']
y = df['label']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

tfvect = TfidfVectorizer(stop_words='english', max_df=0.7)
tfvect.fit(x_train)

loaded_model = pickle.load(open('model/model.pkl', 'rb'))

def fake_news_det(news):
    input_data = [news]
    vectorized_input_data = tfvect.transform(input_data)
    prediction = loaded_model.predict(vectorized_input_data)
    return prediction

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    pred = fake_news_det(message)
    return render_template('index.html', prediction=pred)

if __name__ == '__main__':
    app.run(debug=True)
