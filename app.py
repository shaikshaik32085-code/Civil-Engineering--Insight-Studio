import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image
from google import genai
import time

# Load environment variables
load_dotenv()

# Configure Gemini API
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# --- Page Config ---
st.set_page_config(
    page_title="Civil Engineering Insight Studio",
    page_icon="🏗️",
    layout="wide"
)

# --- Stylish CSS UI Enhancement ---
st.markdown("""
    <style>
    /* Background and Font */
    .stApp {
        background: radial-gradient(circle at top left, #1a1c2c, #0d0e14);
        color: #e0e0e0;
    }
    
    /* Heading Style */
    .main-title {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        letter-spacing: -1px;
        background: linear-gradient(90deg, #ffffff, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
    }

    /* Glassmorphism Cards */
    .stCard {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 25px;
        backdrop-filter: blur(10px);
    }

    /* Button Styling */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #2563eb, #1d4ed8);
        border: none;
        color: white;
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: bold;
        width: 100%;
        transition: 0.3s;
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);
    }
    
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1 class='main-title'>🏗️ Civil Engineering Insight Studio</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 1.1rem; margin-top: -10px;'>Precision Structural Analysis & Engineering Intelligence</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Layout ---
left_col, right_col = st.columns([1, 1.2], gap="large")

with left_col:
    st.markdown("### 🛠️ Investigation Parameters")
    
    with st.expander("📝 Analysis Configuration", expanded=True):
        user_text = st.text_input(
            "Observation Focus:", 
            placeholder="Identify structural defects, material type, etc."
        )
        
        uploaded_file = st.file_uploader(
            "Upload Site Documentation (JPG/PNG)", 
            type=["jpg", "png", "jpeg"]
        )

    if uploaded_file:
        st.markdown("### 📸 Asset Preview")
        image = Image.open(uploaded_file)
        st.image(image, use_container_width=True, caption="Site Reference Data")

with right_col:
    st.markdown("### 🧠 AI Diagnostic Engine")
    
    if st.button("Generate Insight Report"):
        if uploaded_file and user_text:
            # Professional Animation
            with st.status("Initializing Structural Neural Engine...", expanded=True) as status:
                st.write("🔹 Scanning image geometry...")
                time.sleep(1)
                st.write("🔹 Analyzing material fatigue points...")
                time.sleep(1)
                st.write("🔹 Comparing against ISO standards...")
                
                try:
                    # Setup image data
                    image_data = [{"mime_type": uploaded_file.type, "data": uploaded_file.getvalue()}]
                    
                    # Professional prompt
                    expert_prompt = f"Analyze this as a senior structural engineer. Focus: {user_text}. Format: Professional Report."
                    
                    response = client.models.generate_content(
                        model="models/gemini-2.0-flash",
                        contents=[expert_prompt, image_data[0]]
                    )
                    
                    status.update(label="Analysis Complete!", state="complete", expanded=False)
                    
                    # Display Results in a Clean Card
                    st.success("✅ Technical Report Ready")
                    st.markdown("---")
                    st.markdown(response.text)
                    
                    # Save / Export
                    st.download_button("📥 Download Official Report", response.text, "Civil_Insight_Report.txt")

                except Exception as e:
                    st.error(f"Analysis Error: {e}")
        else:
            st.error("❗ Action Needed: Please provide both an image and an observation prompt.")

# --- Footer ---

st.markdown("<br><hr><p style='text-align: center; color: #64748b;'>© 2026 Engineering Insight Studio | AI-Driven Excellence</p>", unsafe_allow_html=True)
