import streamlit as st
from google import genai
from PIL import Image

st.set_page_config(page_title="KrushiAI", page_icon="🌱")

# ⚙️ Settings
with st.sidebar:
    st.header("⚙️ Settings")

    language = st.selectbox(
        "🌐 Language",
        ["English", "Hindi", "Marathi"]
    )

    voice = st.toggle("🔊 Voice Output", value=False)

    st.divider()
    st.caption("🌱 KrushiAI")
    st.caption("AI-Based Crop Health Assistant")
    # 🎨 HOMEPAGE DESIGN
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f7fff4, #e8f6df);
}

h1, h2, h3 {
    color: #14532d;
}

.hero {
    padding: 35px 10px 25px 10px;
}

.hero-title {
    font-size: 52px;
    font-weight: 800;
    color: #14532d;
}
hero-title span {
    color: #58a942;
}

.hero-text {
    font-size: 20px;
    color: #374151;
}

.feature {
    background: rgba(255,255,255,0.8);
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #d9ebd0;
}
.badge {
    display: inline-block;
    background: #e1f4d8;
    color: #166534;
    padding: 8px 14px;
    border-radius: 20px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)
# 🌱 MAIN HOMEPAGE
st.markdown("""
<div class="hero">

<div class="badge">🌱 AI FOR SMART FARMING</div>

<div class="hero-title">
Smart Farming.<br>
<span>Healthy Future.</span> 🌿
</div>
<p class="hero-text">
Upload a crop-leaf image and get an AI-powered preliminary
health assessment with practical guidance for farmers.
</p>

</div>
""", unsafe_allow_html=True)

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]

crop = st.selectbox(
    "🌾 Select your crop",
    ["Tomato", "Potato", "Rice", "Wheat", "Cotton"]
)

image = st.file_uploader(
    "📷 Upload a leaf image",
    type=["jpg", "jpeg", "png"]
)

if image:
    img = Image.open(image)
    st.image(img, caption="Uploaded crop image", use_container_width=True)

    if st.button("🤖 Analyze Crop", use_container_width=True):

        prompt = f"""
You are KrushiAI, a farmer-friendly agricultural AI assistant.
Give the response in {language}.
Analyze this {crop} leaf image and give a PRELIMINARY visual assessment.

Use exactly these sections:

## 🌱 Crop Health Report

**Crop:** {crop}

**🩺 Health Status:** 
Choose: 🟢 Appears Healthy, 🟡 Possible Stress, or 🔴 Possible Disease.

**📊 Estimated Visible Affected Area:**
Estimate the percentage of the visible leaf area that appears affected.
Give a ONLY a whole-number percentage from 0 to 100 on the next line.
Example:
Affected Area: 20
This is only a visual estimate from the uploaded image and is NOT
a measurement of disease severity.

**🔬 Possible Problem**
Give the most likely possible problem. Do not claim certainty.

**👀 Visible Symptoms**
- List only symptoms visible in the image.

**💡 Possible Causes**
- Give simple possible causes.

**🌾 Recommended Actions**
1. Give practical next steps.
2. Give another useful step.
3. Say when to consult a local agricultural expert.
**🛡️ Prevention Tips**
- Give simple prevention advice.

**⚠️ Important Note**
State that this is an AI-based preliminary assessment and
cannot replace professional diagnosis.

Keep the answer simple, practical, and concise.
If the image is unclear, say that a clearer image is needed.
"""

        with st.spinner("🤖 KrushiAI is analyzing... 🌱"):
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=[prompt, img]
            )

        st.success("✅ Analysis completed!")
        st.markdown(response.text)
