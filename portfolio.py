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
    
    /* Glassmorphism Cards */
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
    st.write("📧 mallikarjunareddyk48@gmail.com") 
    st.write("🔗 [LinkedIn Profile](https://www.linkedin.com/in/k-malli-karjuna-reddy-ba2a54314)")
    st.write("🐙 [GitHub Profile](#)")
    st.markdown("---")
    st.info("Status: Open to Work")

# --- 4. HERO SECTION (Main Intro) ---
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("# 👋 Hello, I'm Mallikarjuna Reddy")
    st.markdown("### I Architect **Secure AI Systems** & **Rapid Web Products**.")
    st.write("""
    I am an Electronics Engineer (ECE) bridging the gap between **Hardware Logic** and **Software Intelligence**.
    I don't just write code; I build business solutions using 'Active Defense' strategies and Rapid Prototyping.
    """)
    st.write("**Specialization:** `Python` `Streamlit` `Cyber Security` `IoT`")

with col2:
    st.image("https://img.freepik.com/free-vector/programming-concept-illustration_114360-1351.jpg", caption="AI & Security Developer")

st.markdown("---")

# --- 5. CORE COMPETENCIES ---
st.markdown("## ⚡ Core Competencies & Services")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="glass-card">
        <h3>🚀 AI Product Development</h3>
        <p>I transform abstract concepts into <b>deployable market-ready applications</b> in 24 hours.</p>
        <p><b>Tech Stack:</b> Streamlit, Generative AI, Python</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="glass-card">
        <h3>🛡️ Cybersecurity Architecture</h3>
        <p>Designing robust security frameworks and <b>'Offensive Defense'</b> mechanisms (Honeypots).</p>
        <p><b>Tech Stack:</b> AES-256, PyCryptodome, Network Forensics</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="glass-card">
        <h3>⚙️ Algorithmic Automation</h3>
        <p>Engineering intelligent bots to automate repetitive workflows and integrate APIs.</p>
        <p><b>Tech Stack:</b> Telegram API, Pandas, Cloud Functions</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- 6. AI CHATBOT SECTION (NEW!) ---
st.markdown("## 🤖 Chat with Netra AI (Demo)")
st.write("Ask me about Malli's skills, pricing, or projects!")

# Chat History Setup
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input Logic
if prompt := st.chat_input("Type here (e.g., 'What are your skills?')..."):
    # 1. User Message Display
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. AI Logic (Smart Responses)
    response = "I am currently in Demo Mode. Please email Malli for details."
    
    p_lower = prompt.lower()
    
    if "hello" in p_lower or "hi" in p_lower:
        response = "Hello! I am **Netra AI**, Malli's virtual assistant. How can I help you?"
        
    elif "skill" in p_lower or "technology" in p_lower:
        response = "Malli is an expert in: \n- **Python & Streamlit** (Web Apps) \n- **Cyber Security** (AES-256, Honeypots) \n- **IoT & Electronics** (Arduino, Sensors)"
        
    elif "price" in p_lower or "cost" in p_lower or "charge" in p_lower:
        response = "Malli offers **Rapid Prototyping starting at just $50 (₹4000)**. The final price depends on the project complexity."
        
    elif "contact" in p_lower or "email" in p_lower or "hire" in p_lower:
        response = "You can hire him immediately! \n📧 Email: **mallikarjunareddyk48@gmail.com** \n🔗 Or use the Contact Form below."
        
    elif "netra" in p_lower:
        response = "**Netra AI** is Malli's flagship security project that uses active defense to trap hackers. It's built with Python."

    # 3. Assistant Message Display
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

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
    if st.form_submit_button("🚀 Send Message"):
        st.success("Thank you! I will get back to you within 2 hours.")
