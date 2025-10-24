# 📘 Grade and Placement Prediction  

A Machine Learning based project that predicts **student grades** and **placement outcomes** using academic and demographic data. This project demonstrates how ML models can be applied in **EdTech** to improve student performance tracking and career planning.  

---

## 🚀 Features  
- Predicts **student grades** from academic data.  
- Predicts **placement outcomes** (whether a student will get placed).  
- Built with **Python, Pandas, Scikit-Learn and Streamlit** (for app interface).  
- Includes trained models (`.pkl` files) for instant predictions.  
- Well-documented dataset and preprocessing pipeline.  

---------

## 🗂️ Project Structure  
```
📂 softpro_edtech/
 ┣ 📓 Grade Prediction.ipynb       # Jupyter Notebook for model training
 ┣ 📄 main.py, main_app.py         # ML App scripts
 ┣ 📄 main2.py, main3.py, main4.py
 ┣ 📊 MIS Data.xlsx                # Sample academic data
 ┣ 📊 softpro_student_data.csv     # Student dataset
 ┣ 📊 student_placement_data.csv   # Placement dataset
 ┣ 📦 student_performance_model.pkl  # Trained model
 ┣ 📦 grade_encoder.pkl              # Encoder for grades
 ┣ 📦 technology_encoder.pkl         # Encoder for tech skills
```

---

## ⚙️ Installation  

Clone the repository:  
```bash
git clone https://github.com/your-username/grade-and-placement-prediction.git
cd grade-and-placement-prediction
```

Create and activate a virtual environment:  
```bash
python -m venv venv
source venv/bin/activate   # for Linux/Mac
venv\Scripts\activate      # for Windows
```

Install dependencies:  
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage  

Run Jupyter Notebook (for training & analysis):  
```bash
jupyter notebook
```

Run the Streamlit App (for predictions):  
```bash
streamlit run main_app.py
```

---

## 📊 Dataset  
- **softpro_student_data.csv** → used for grade prediction.  
- **student_placement_data.csv** → used for placement prediction.  
- Preprocessing includes **encoding categorical values** (grades, technologies, etc.).  

---

## 📈 Model  
- Algorithms used: **Logistic Regression, Random Forest, Decision Trees**.  
- Final selected model: **Random Forest** (highest accuracy).  
- Trained models are stored as `.pkl` files for reuse.  

---

## 🔮 Future Scope  
- Add **Deep Learning models (ANN, LSTM)**.  
- Create **real-time dashboards** for students & faculty.  
- Deploy as a **mobile/web app** for educational institutions.  

---

## 🤝 Contributing  
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.  

---

## 📜 License  
This project is licensed under the **MIT License**.  
