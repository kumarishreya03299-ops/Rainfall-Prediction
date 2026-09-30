# 🌧️ Rainfall Prediction System
A Machine Learning project that predicts whether rain is expected tomorrow based on weather conditions.

## 📌 Project Overview
This project uses Machine Learning to predict tomorrow's rainfall using different weather features.
The model takes the following inputs:
- Temperature
- Humidity
- Wind Speed
- Precipitation
- Cloud Cover
- Pressure

The target variable is:
- `Rain Tomorrow`

Where:
- `0` = No Rain
- `1` = Rain

## 🤖 Machine Learning Model

### Algorithm Used

**Logistic Regression**
This is a classification problem because the model predicts two possible outcomes: Rain or No Rain.

## 📊 Model Performance
The model achieved approximately:
**90.92% Accuracy**

The model was evaluated using:
- Accuracy
- Confusion Matrix
- Classification Report
- Precision
- Recall
- F1-score

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook
- Streamlit
- Pickle

## 📁 project files
```text
Rainfall-Prediction/
│
├── Rainfall_Prediction.ipynb
├── rainfall.csv
├── model.pkl
├── app.py
└── README.md
```

# 🌐 Streamlit Web App
The trained Machine Learning model is connected to a Streamlit web application.
The app allows users to enter weather details and predicts:
🌧️ Rain is expected tomorrow
or
☀️ No rain is expected tomorrow
It also displays the Rain Probability (%).

# 🚀 How to Run
Install the required libraries: 

```bash
pip install pandas numpy scikit-learn matplotlib streamlit 
```
Run the Streamlit application: 

```bash
streamlit run app.py
```

# 📓 Jupyter Notebook
The complete Machine Learning workflow was developed in Jupyter Notebook, including:
1. Loading the dataset
2. Data exploration
3. Feature selection
4. Train-test split
5. Logistic Regression
6. Prediction
7. Model evaluation
8. Confusion Matrix
9. Classification Report
10. Saving the trained model

# 🔮 Future Improvements
1. Real-time weather API integration
2. Location-based prediction
3. Multi-day rainfall prediction
4. Advanced Machine Learning models
5. Interactive weather charts
6. Cloud deployment

# 👩‍💻 Author
Shreya Kumari
