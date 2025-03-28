# Fake_News_Detector
# 📰 Fake News Detector using Deep Learning

## 🚀 Overview
This project is a **Fake News Detection System** built using **Deep Learning (LSTM/BERT)** and NLP techniques. It classifies news articles as **Real** or **Fake** based on textual content. The model is trained on the **ISOT Fake News Dataset** and deployed using **Streamlit & Hugging Face Spaces**.

🔗 **Live Demo**: [Click here to try it out!](https://huggingface.co/spaces/SatyamInCode/FakeNewsDetector)

## ✨ Features
✅ Detects Fake News with high accuracy using Deep Learning  
✅ Uses **LSTM/BERT** for powerful text classification  
✅ Preprocessing with **Tokenization & Embeddings**  
✅ Deployed using **Streamlit & Hugging Face**  
✅ Open-source and customizable  

## 📂 Dataset
- **Source**: ISOT Fake News Dataset
- **Classes**: `Real`, `Fake`
- **Columns**: `title`, `text`, `label`

## 🏗️ Tech Stack
- **Python** 🐍
- **TensorFlow/Keras** for Deep Learning 🔥
- **NLTK & Tokenizer** for Text Processing ✂️
- **Streamlit** for Web Deployment 🌐
- **Hugging Face Spaces** for Hosting ☁️

---

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SatyamInCode/Fake_News_Detector.git
cd Fake-News-Detector
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App Locally
```bash
streamlit run app.py
```

---

## 📜 Training the Model
The model was trained using **LSTM** on tokenized sequences from news articles.

### **Training Code (Jupyter Notebook)**
Check the `Fake_News_Detector.ipynb` file for detailed training steps.

**Steps Involved:**
1. **Data Cleaning**: Removing stopwords, punctuation, and special characters
2. **Tokenization & Embeddings**: Using `Tokenizer` and `pad_sequences`
3. **Model Training**: LSTM model training with `Adam` optimizer
4. **Evaluation**: Precision, Recall, and F1-score calculation

---

## 🚀 Deployment on Hugging Face
### 1️⃣ Push Code to GitHub
```bash
git add .
git commit -m "Initial Commit"
git push origin main
```
### 2️⃣ Create a Space on Hugging Face
1. Go to [Hugging Face Spaces](https://huggingface.co/spaces)
2. Create a **new Space** → Select **Streamlit**
3. Connect to your GitHub repository
4. Deploy and enjoy! 🎉

---

## 📊 Model Performance
| Metric      | Score  |
|------------|--------|
| **Accuracy** | 99.94%  |
| **Precision** | 1.00   |
| **Recall**   | 1.00   |
| **F1-score** | 1.00   |

🔍 **Training Graphs & Logs**: Available in `training_results.png`

---

## 📌 Future Improvements
- ✅ Integrate **BERT** for better accuracy
- ✅ Enable **API Support** for wider usability
- ✅ Enhance **UI/UX** for a smoother experience

---

## 🤝 Contribution
1. Fork the repo
2. Create a new branch (`feature-branch`)
3. Commit your changes & push
4. Submit a **Pull Request**

🙌 **Star this repo** ⭐ if you found it useful!

---

## 📧 Contact
For queries, reach out on 💼 **GitHub** → [SatyamInCode](https://github.com/SatyamInCode)


