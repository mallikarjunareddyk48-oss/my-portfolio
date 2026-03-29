import streamlit as st
import google.generativeai as genai
import PIL.Image

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Malli | AI Architect", page_icon="👨‍💻", layout="wide")

# --- 2. SETUP GEMINI AI ---
# API Key ని Streamlit Secrets నుండి తీసుకుంటుంది
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    else:
        st.error("Error: Gemini API Key is missing. Please add it to Streamlit Secrets.")
except Exception as e:
    st.error(f"Error configuring Gemini: {e}")

# --- 3. PROFESSIONAL CSS ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
    }
    h1, h2, h3 { font-family: 'Helvetica Neue', sans-serif; color: white; }
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px; border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)
    st.title("Mallikarjuna Reddy")
    st.write("📍 **ECE Student & AI Innovator**")
    st.markdown("---")
    st.write("📧 mallikarjunareddyk48@gmail.com") 
    st.write("🔗 [LinkedIn Profile](https://www.linkedin.com/in/k-malli-karjuna-reddy-ba2a54314)")
    st.info("Status: Open to Work")

# --- 5. HERO SECTION ---
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("# 👋 Hello, I'm Mallikarjuna Reddy")
    st.markdown("### I Architect **Secure AI Systems**.")
    st.write("I build business solutions using 'Active Defense' strategies and Rapid Prototyping.")

with col2:
    st.image("https://img.freepik.com/free-vector/programming-concept-illustration_114360-1351.jpg")

st.markdown("---")

# --- 6. PROJECTS ---
st.markdown("## 🏆 Featured Project: Netra AI")
st.markdown("""
<div class="glass-card">
    <h3>👁️ Active Defense System</h3>
    <p>Netra AI is a <b>counter-measure security system</b> designed to detect human error.</p>
    <p>
        💰 <b>Real Problem. Real Scale.</b><br>
        According to NPCI and the Indian Cyber Crime Coordination Centre (I4C), Indians lost over
        <b>₹485 crore to UPI fraud in FY 2023-24</b> — and the number is rising steeply in 2025.
        A single case from <b>Hyderabad, Telangana (2025)</b> saw a victim lose <b>₹11 lakh</b>
        to a <b>fake customer-care screen-share scam</b>: attackers posed as bank support,
        convinced the victim to install a remote-access app, then silently drained the UPI account.
    </p>
    <p>
        🧠 <b>How Netra AI stops it:</b><br>
        Netra AI monitors live screen activity and flags unauthorised remote-access sessions in
        real time — the exact attack vector used in 67% of reported UPI fraud cases
        (screen-share / remote-control exploits). By catching human error <i>before</i> the
        transaction is authorised, Netra AI becomes the last line of defence that banks and
        payment apps currently lack.
    </p>
    <hr style="border-color: rgba(255,255,255,0.15);">
    <table style="width:100%; color:white;">
        <tr>
            <td>💰 Amount lost (single case)</td>
            <td><b>₹11 lakh — Hyderabad, 2025</b></td>
        </tr>
        <tr>
            <td>📍 State / City</td>
            <td><b>Telangana / Hyderabad</b></td>
        </tr>
        <tr>
            <td>🎯 Attack method</td>
            <td><b>Fake customer-care + screen-share remote access</b></td>
        </tr>
        <tr>
            <td>📊 National scale (FY 2024)</td>
            <td><b>₹485 crore lost across India (NPCI / I4C)</b></td>
        </tr>
    </table>
    <p style="margin-top:12px; font-size:0.85em; opacity:0.7;">
        Sources: NPCI Annual Report FY2023-24 · Indian Cyber Crime Coordination Centre (I4C) ·
        Telangana Cyber Security Bureau press releases
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- 7. REAL GEMINI AI CHATBOT 🤖 ---
st.markdown("## 🤖 Chat with Netra AI")
st.write("I am a real AI. Ask me anything about Malli's skills!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        # System Prompt
        persona = """
        You are Netra AI, a professional portfolio assistant for Mallikarjuna Reddy.
        KEY INFO:
        - Name: Mallikarjuna Reddy (Malli).
        - Role: ECE Student & AI Developer.
        - Skills: Python, Streamlit, Cyber Security, IoT, Hardware Logic.
        - Pricing: Prototypes start at ₹4000.
        """
        vision_model_chat = genai.GenerativeModel('gemini-pro')
        response = vision_model_chat.generate_content(persona + "\nUser Question: " + prompt)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        
    except Exception as e:
        st.error(f"AI Error: {e}")

# --- 8. SMART ECE PROJECT: AI VISION (Live Camera) ---
st.markdown("---")
st.markdown("## 📷 Smart ECE: Component Scanner")
st.write("Scan any electronic component (Resistor, IC, Sensor) using your camera or upload a photo!")

# Option to choose Input Method
input_method = st.radio("Choose Input Method:", ("📷 Live Camera", "📂 Upload Image"), horizontal=True)

image_data = None

if input_method == "📷 Live Camera":
    # Camera Input
    camera_image = st.camera_input("Take a picture of the component")
    if camera_image is not None:
        image_data = camera_image
        
elif input_method == "📂 Upload Image":
    # File Uploader with UNIQUE KEY to prevent errors
    uploaded_file = st.file_uploader("Upload Component Image...", type=["jpg", "png", "jpeg"], key="unique_uploader_key")
    if uploaded_file is not None:
        image_data = uploaded_file

# --- AI ANALYSIS LOGIC ---
if image_data is not None:
    # 1. Show the Image
    image = PIL.Image.open(image_data)
    st.image(image, caption="Analyzed Image", use_column_width=True)
    
    # 2. Analyze Button
    if st.button("🔍 Identify Component"):
        try:
            with st.spinner("Netra AI is scanning circuitry..."):
                vision_model = genai.GenerativeModel('gemini-1.5-flash')
                
                vision_prompt = """
                You are an expert Electronics Engineer. Analyze this image.
                1. Identify the electronic component shown (e.g., Arduino, Resistor, Capacitor, IC).
                2. Explain its main function briefly.
                3. Provide a pin configuration or value if visible.
                
                If not an electronic component, say "⚠️ Not an electronic component."
                """
                
                response = vision_model.generate_content([vision_prompt, image])
                st.success("✅ Identification Complete!")
                st.markdown(response.text)
                
        except Exception as e:
            st.error(f"AI Error: {e}")

# --- 9. CONTACT FORM ---
st.markdown("---")
st.markdown("## 📬 Contact Me")
with st.form("contact_form"):
    c_name = st.text_input("Your Name")
    c_email = st.text_input("Your Email")
    c_msg = st.text_area("Message")
    if st.form_submit_button("🚀 Send Message"):
        st.success("Message sent successfully!")
