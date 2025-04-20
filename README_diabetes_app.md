
# 🧬 Diabetes Prediction App (Streamlit)

A simple web app built with **Streamlit** that predicts whether a person is likely to have diabetes, based on health features such as age, BMI, cholesterol, and more.

This project is perfect for learning:
- Machine learning (logistic regression)
- Building a frontend using Streamlit
- Saving/loading models with `joblib`
- Using VS Code + Git + Python environments

---

## 🚀 Features
- Clean web interface (Streamlit)
- Slider & dropdown inputs for user data
- Real-time prediction using a trained model
- Built fully in Python

---

## 📁 Project Structure

```
diabetes_streamlit_app/
├── app.py                # Main Streamlit web app
├── train_model.py        # ML training script (Logistic Regression)
├── model.pkl             # Trained model (saved using joblib)
├── requirements.txt      # Dependencies
└── README.md             # You're reading this!
```

---

## 📊 Dataset Used
- `load_diabetes()` from `sklearn.datasets`
- 442 samples with 10 baseline variables
- Target (a continuous value) was binarized: 
  - `> 140` → diabetic (1)
  - `<= 140` → non-diabetic (0)

---

## ✅ Setup Instructions

### 🔹 1. Clone or Download
```bash
git clone https://github.com/your-username/diabetes_streamlit_app.git
cd diabetes_streamlit_app
```

### 🔹 2. (Optional but Recommended) Create a Virtual Environment
Using Anaconda:
```bash
conda create -n diabetes_env python=3.9
conda activate diabetes_env
```

Or using `venv`:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 🔹 3. Install Dependencies
```bash
pip install -r requirements.txt
```

If you don’t have a requirements.txt yet, install manually:
```bash
pip install streamlit scikit-learn pandas joblib
```

---

### 🔹 4. Train the Model
```bash
python train_model.py
```
This saves a trained logistic regression model as `model.pkl`

### 🔹 5. Run the Web App
```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`.

---

## 🧠 Troubleshooting: What Went Wrong & How I Solved It

### ❌ Issue:
```
streamlit : The term 'streamlit' is not recognized as the name of a cmdlet...
```

### ✅ Fix:
This happened because VS Code didn't recognize my Conda environment properly. Here's how I solved it:

1. Opened **Anaconda Prompt**
2. Activated my environment manually:
   ```bash
   conda activate r_env
   ```
3. Then launched VS Code from that prompt:
   ```bash
   code .
   ```

That ensured VS Code recognized `conda`, `streamlit`, and all packages.

✅ Lesson: If `streamlit` or `conda` isn’t recognized in VS Code, launch it from Anaconda Prompt with the right environment activated.

---

## 📦 Example Requirements.txt
```txt
streamlit
scikit-learn
pandas
joblib
```

Generate it with:
```bash
pip freeze > requirements.txt
```

---

## 📷 Screenshot (Optional)

You can add a screenshot of your app here:
```markdown
![Demo Screenshot](screenshot.png)
```

---

## 💡 Future Improvements
- Deploy to [Streamlit Cloud](https://streamlit.io/cloud)
- Add model accuracy display
- Store user input history

---

## 🧑‍💻 Author
Built by [Your Name] as part of a Streamlit learning journey. Inspired by solving a real beginner challenge from zero.

---

## 📜 License
MIT License

# ctrl + shift + P and select Python: Select Interpreter
