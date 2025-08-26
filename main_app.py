import streamlit as st

# ================== PAGE CONFIG ==================
st.set_page_config(page_title="🚀 Softpro Project Launcher", page_icon="💻", layout="wide")

# ================== CUSTOM CSS ==================
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top left, #0f2027, #203a43, #2c5364);
    color: #e0e0e0;
    font-family: 'Segoe UI', sans-serif;
}

h1 {
    text-align: center;
    color: #00adb5;
    font-size: 42px;
    margin-bottom: 10px;
}

hr {
    border: 1px solid #00adb5;
    margin: 30px 0;
}

.project-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(0,173,181,0.3);
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    transition: 0.3s ease-in-out;
    box-shadow: 0 4px 10px rgba(0,0,0,0.4);
    min-height: 180px;      /* ✅ Smaller card height */
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin: 15px;           /* ✅ Equal gap between all cards */
}
.project-card:hover {
    transform: scale(1.05);
    background: rgba(0,173,181,0.1);
    box-shadow: 0 0 20px #00adb5;
}

.project-card h2 {
    color: #00adb5;
    font-size: 20px;
}

.launch-btn {
    display: inline-block;
    margin-top: 10px;
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
    color: #ffea00;
    border: none;
    border-radius: 10px;
    text-decoration: none;
    transition: 0.3s;
}
.launch-btn:hover {
    background: linear-gradient(135deg,#007a7c,#00adb5);
    box-shadow: 0 0 12px #00adb5, 0 0 18px #00adb5;
    color: #fff176;
}
</style>
""", unsafe_allow_html=True)

# ================== TITLE ==================
st.markdown("<h1>🚀 Softpro Project Launcher Dashboard</h1>", unsafe_allow_html=True)
st.write("")

# ================== PROJECT CARDS ==================
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
        <div class="project-card">
            <h2>📚 Course Recommendation System</h2>
            <p>Smart AI system to recommend best courses for students.</p>
            <a class="launch-btn" href="http://localhost:8501" target="_blank">▶ Launch</a>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="project-card">
            <h2>📊 Business Forecast System</h2>
            <p>ML powered forecasting for sales & trends.</p>
            <a class="launch-btn" href="http://localhost:8502" target="_blank">▶ Launch</a>
        </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2, gap="large")

with col3:
    st.markdown("""
        <div class="project-card">
            <h2>📈 Language vs Placement Correlation</h2>
            <p>Analyze the relation of programming languages with placement rates.</p>
            <a class="launch-btn" href="http://localhost:8503" target="_blank">▶ Launch</a>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class="project-card">
            <h2>🔍 Student Performance Prediction</h2>
            <p>Predict students’ grades & placement chances.</p>
            <a class="launch-btn" href="http://localhost:8504" target="_blank">▶ Launch</a>
        </div>
    """, unsafe_allow_html=True)

# ================== FOOTER ==================
st.markdown("<hr>", unsafe_allow_html=True)
st.info("⚠ Make sure CRS (8501), BFS (8502), LVPC (8503), and SPP (8504) are running before launching 🚀")
