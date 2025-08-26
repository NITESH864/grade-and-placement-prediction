# course recommendation system
# import essential library
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import LabelEncoder 
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings('ignore')

# load and preprocess the data
df=pd.read_excel("MIS Data.xlsx")
df.columns=df.columns.str.strip().str.replace(" ","_").str.replace("-","_")
df['College']=df['College'].fillna('Not Provided')
df['Branch']=df['Branch'].str.strip().str.title()
df['Course']=df['Course'].str.strip().str.title()
df['Subject']=df['Subject'].str.strip().str.title()

# Encode Features and train ML model for prediction
features=['Branch','College','Course','Year']
target='Subject'
df_ml=df.dropna(subset=features+[target])  
encoders={}

for col in features+[target]:
    le=LabelEncoder()
    df_ml[col]=le.fit_transform(df_ml[col])
    encoders[col]=le
X=df_ml[features]
y=df_ml[target] 
model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X,y)

def predict_subjects_ml(branch,college,course,year,top_n=3):
    input_df=pd.DataFrame([[branch,college,course,year]],columns=features)
    for col in features:
        input_df[col]=encoders[col].transform(input_df[col])
    probs=model.predict_proba(input_df)[0]
    top_indices=np.argsort(probs)[::-1][:top_n]
    subject_names=encoders[target].inverse_transform(top_indices)    
    return list(zip(subject_names,probs[top_indices]))

# Streamlit UI
st.title("Course Recommendation System")
st.markdown("Get top recommended course based on your Branch, College ,Course and Year")

# Sidebar Input
branches=sorted(df['Branch'].dropna().unique())
colleges=sorted(df['College'].dropna().unique())
courses=sorted(df['Course'].dropna().unique())
years=sorted(df['Year'].dropna().unique())

selected_branch=st.selectbox("Select Branch",branches)
selected_college=st.selectbox("Select College",colleges)
selected_course=st.selectbox("Select Course",courses)
selected_year=st.selectbox("Select Year",years)

button=st.button("Recommend Subject (ML-Based)")
if button:
    ml_recommendations=predict_subjects_ml(selected_branch,selected_college,selected_course,selected_year)
    st.subheader("ML-Based Recommended Subjects")
    for i,(subject,score) in enumerate(ml_recommendations,1):
        st.markdown(f"{i}. **{subject}** - Confidence : {score:.2f}")