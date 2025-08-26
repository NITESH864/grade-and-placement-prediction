import streamlit as st
                                            #    run :-  streamlit run main_app.py port --server.port 8500
                                            # streamlit run  main.py --server.port 8501 
# --- Dark Mode Styling ---                     
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #e0e0e0;
    }
    button[kind="primary"] {
        background-color: #00adb5;
        color: white;
        border-radius: 12px;
        padding: 20px 40px;
        font-size: 22px;
        transition: 0.3s;
    }
    button[kind="primary"]:hover {
        background-color: #007a7c;
        box-shadow: 0 0 15px #00adb5, 0 0 25px #00adb5;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1 style='text-align: center; color: #00adb5;'>🚀 Softpro Project Launcher Dashboard</h1>", unsafe_allow_html=True)
st.write("")

# --- Static Buttons using Columns ---
col1, col2 = st.columns(2)

with col1:
    if st.button("📚 Course Recommendation System"):
        st.markdown("[Open Project](http://localhost:8501)", unsafe_allow_html=True)

with col2:
    if st.button("📊 Business Forecast System"):
        st.markdown("[Open Project](http://localhost:8502)", unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    if st.button("📈 Language Vs. Placement Correlation"):
        st.markdown("[Open Project](http://localhost:8503)", unsafe_allow_html=True)

with col4:
    if st.button("🔍 Student Performance Prediction"):
        st.markdown("[Open Project](http://localhost:8504)", unsafe_allow_html=True)


# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
st.info("Make sure CRS (8501), BFS (8502), LVPC (8503), and SPP (8504) are running before launching them 🚀.")