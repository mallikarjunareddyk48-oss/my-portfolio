import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Malli | AI Architect", page_icon="👨‍💻", layout="wide")

# --- 2. PROFESSIONAL CSS (Glassmorphism Design) ---
st.markdown("""
    <style>
    /* Main Background - Dark Blue Professional Gradient */
    .stApp {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
    }
    
    /* Headlines */
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
        color: #ffffff;
    }
    
    /* Glassmorphism Cards (అద్దం లాంటి బాక్సులు) */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
        height: 100%;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #00d2ff 0%, #3a7bd5 100%);
        color: white;
        border: none;
        padding: 10px 24px;
        border-radius: 8px;
        font-weight: bold;
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (Contact Info) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)
    st.title("Mallikarjuna Reddy")
    st.write("📍 **ECE Student & AI Innovator**")
    st.markdown("---")
    st.write("📧 mallikarjunareddyk48@gmail.com")")
    st.write("🔗 [LinkedIn Profile](https://www.linkedin.com/in/k-malli-karjuna-reddy-ba2a54314)")
    st.write("🐙 [GitHub Profile](#)")
    st.markdown("---")
    st.info("Status: Open to Work")

# --- 4. HERO SECTION (Main Intro) ---
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("# 👋 Hello, I'm Mallikarjuna reddy")
    st.markdown("### I Architect **Secure AI Systems** & **Rapid Web Products**.")
    st.write("""
    I am an Electronics Engineer (ECE) bridging the gap between **Hardware Logic** and **Software Intelligence**.
    I don't just write code; I build business solutions using 'Active Defense' strategies and Rapid Prototyping.
    """)
    st.write("**Specialization:** `Python` `Streamlit` `Cyber Security` `IoT`")

with col2:
    st.image("https://img.freepik.com/free-vector/programming-concept-illustration_114360-1351.jpg", caption="AI & Security Developer")

st.markdown("---")

# --- 5. CORE COMPETENCIES (నీ కొత్త స్కిల్స్ సెక్షన్) ---
st.markdown("## ⚡ Core Competencies & Services")
st.write("Leveraging advanced technology to solve complex business problems.")

# Columns for the skills
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="glass-card">
        <h3>🚀 AI Product Development</h3>
        <p style='font-size: 14px; opacity: 0.8;'><b>Focus: Rapid Prototyping (MVP)</b></p>
        <p>I transform abstract concepts into <b>deployable market-ready applications</b>. Specializing in high-speed development cycles (24-Hours) to reduce time-to-market.</p>
        <hr style='border-color: rgba(255,255,255,0.1); margin: 10px 0;'>
        <p><b>Tech Stack:</b> Streamlit, Generative AI, Python</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="glass-card">
        <h3>🛡️ Cybersecurity Architecture</h3>
        <p style='font-size: 14px; opacity: 0.8;'><b>Focus: Active Defense Strategy</b></p>
        <p>Designing robust security frameworks. I implement <b>'Offensive Defense'</b> mechanisms (Honeypots) to identify and neutralize threats in real-time, going beyond simple firewalls.</p>
        <hr style='border-color: rgba(255,255,255,0.1); margin: 10px 0;'>
        <p><b>Tech Stack:</b> AES-256, PyCryptodome, Network Forensics</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="glass-card">
        <h3>⚙️ Algorithmic Automation</h3>
        <p style='font-size: 14px; opacity: 0.8;'><b>Focus: Business Logic Optimization</b></p>
        <p>Engineering intelligent bots to automate repetitive workflows. I build custom scripts that integrate APIs (Stock data, Crypto, Messaging) to drive <b>operational efficiency</b>.</p>
        <hr style='border-color: rgba(255,255,255,0.1); margin: 10px 0;'>
        <p><b>Tech Stack:</b> Telegram API, Pandas, Cloud Functions</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- 6. FEATURED STARTUP (Netra AI) ---
st.markdown("## 🏆 Featured Project: Netra AI")

col_a, col_b = st.columns([1, 1])

with col_a:
    st.image("https://media.istockphoto.com/id/1329766943/photo/digital-padlock-icon-cyber-security-network-and-data-protection-technology-on-virtual.jpg?s=612x612&w=0&k=20&c=N_2eM4BwA9d4Q8c1H4f3h3h4h3h4h3h4", use_column_width=True)

with col_b:
    st.markdown("""
    <div class="glass-card">
        <h3>👁️ Active Defense System</h3>
        <p>Netra AI is a <b>counter-measure security system</b> designed to detect human error.</p>
        <ul>
            <li><b>Problem:</b> Traditional firewalls can't stop phishing/human mistakes.</li>
            <li><b>Solution:</b> A Honeypot-based trap that tracks hacker IP & Location.</li>
            <li><b>Status:</b> Prototype Ready & Tested.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    if st.button("View Live Demo"):
        st.toast("Redirecting to Netra AI Demo...")

st.markdown("---")

# --- 7. CONTACT FORM ---
st.markdown("## 📬 Let's Build Something Great")

with st.form("contact_form"):
    c_name, c_email = st.columns(2)
    with c_name:
        st.text_input("Your Name")
    with c_email:
        st.text_input("Your Email")
    
    st.text_area("How can I help you?")
    
    submit = st.form_submit_button("🚀 Send Message")
    if submit:
        st.success("Thank you! I will get back to you within 2 hours.")

        st.balloons()
