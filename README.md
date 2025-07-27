# 📰 Fake News Detector

A simple Flask web application that detects whether a news article is **Fake** or **Real** using machine learning.

---

## 🔍 Features

- Paste a news article and check if it's FAKE or REAL
- Built with Flask (Python) for the backend
- Trained using TF-IDF + PassiveAggressiveClassifier
- Clean and minimal frontend using HTML & CSS
- No JavaScript required — fast and lightweight!

---

## 💻 Technologies Used

| Layer       | Tools Used                                     |
|-------------|------------------------------------------------|
| **Frontend**| HTML, CSS                                       |
| **Backend** | Python, Flask                                   |
| **ML Model**| Scikit-learn, TF-IDF, PassiveAggressiveClassifier |
| **Data**    | News dataset (CSV format)                       |


---

## 🚀 How to Run the Project

✅ Step 1: Navigate to your project folder using:

cd path/to/your/FakeNews
Example (if it's on Desktop):

cd Desktop/FakeNews

✅ Step 2: Install Required Python Libraries
Run this command:
pip install flask scikit-learn pandas
It installs the necessary packages.

✅ Step 3: (Optional) Train the Model
If you don’t have model.pkl, train the model using:
python model/train_model.py
Make sure news.csv is in the same folder.

✅ Step 4: Run the Flask App
Now start the web app by running:
python app.py
Then open your browser
You’ll see a simple webpage where you can paste a news article and click Predict.

✅ Done!
You’ll get a result like:
✅ REAL News
⚠ FAKE News

🙋‍♂️ Author
Muzammil Khan
Feel free to connect on LinkedIn or drop a ⭐ on the repo if you like it.
