import streamlit as st
from google import genai
from PIL import Image

# Page setup
st.set_page_config(
    page_title="KrushiAI",
    page_icon="🌱"
)

# Gemini AI client
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# Title
st.title("🌱 KrushiAI")
st.subheader("AI-Based Crop Health Assistant")

st.write(
    "Upload a crop-leaf image and KrushiAI will use AI "
    "to provide a preliminary crop health assessment."
)

# Crop selection
crop = st.selectbox(
    "🌾 Select your crop",
    ["Tomato", "Potato", "Rice", "Wheat", "Cotton"]
)

# Image upload
image = st.file_uploader(
    "📷 Upload a leaf image",
    type=["jpg", "jpeg", "png"]
)

if image is not None:

    img = Image.open(image)

    st.image(
        img,
        caption="Uploaded crop image",
        use_container_width=True
    )

    if st.button("🤖 Analyze Crop"):

        with st.spinner("AI is analyzing the crop... 🌱"):

            prompt = f"""
You are KrushiAI, an agricultural crop health assistant.

Analyze this image of a {crop} leaf.

Give a simple, farmer-friendly response containing:

1. Crop identified
2. Whether the leaf appears healthy or shows signs of disease/stress
3. Possible disease or problem
4. Visible symptoms
5. Possible causes
6. Recommended next steps for the farmer
7. Prevention tips

Do not claim certainty from an image alone.
If the image is unclear, say that a clearer image is needed.
Keep the explanation simple and practical.
"""

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[prompt, img]
            )

        st.success("✅ Analysis completed!")

        st.markdown("### 🔍 KrushiAI Analysis")
        st.write(response.text)

        st.info(
            "💡 This is an AI-based preliminary assessment. "
            "For serious crop problems, consult an agricultural expert."
        )import streamlit as st
from google import genai
from PIL import Image

# Page setup
st.set_page_config(
    page_title="KrushiAI",
    page_icon="🌱"
)

# Gemini AI client
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# Title
st.title("🌱 KrushiAI")
st.subheader("AI-Based Crop Health Assistant")

st.write(
    "Upload a crop-leaf image and KrushiAI will use AI "
    "to provide a preliminary crop health assessment."
)

# Crop selection
crop = st.selectbox(
    "🌾 Select your crop",
    ["Tomato", "Potato", "Rice", "Wheat", "Cotton"]
)

# Image upload
image = st.file_uploader(
    "📷 Upload a leaf image",
    type=["jpg", "jpeg", "png"]
)

if image is not None:

    img = Image.open(image)

    st.image(
        img,
        caption="Uploaded crop image",
        use_container_width=True
    )

    if st.button("🤖 Analyze Crop"):

        with st.spinner("AI is analyzing the crop... 🌱"):

            prompt = f"""
You are KrushiAI, an agricultural crop health assistant.

Analyze this image of a {crop} leaf.

Give a simple, farmer-friendly response containing:

1. Crop identified
2. Whether the leaf appears healthy or shows signs of disease/stress
3. Possible disease or problem
4. Visible symptoms
5. Possible causes
6. Recommended next steps for the farmer
7. Prevention tips

Do not claim certainty from an image alone.
If the image is unclear, say that a clearer image is needed.
Keep the explanation simple and practical.
"""

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[prompt, img]
            )

        st.success("✅ Analysis completed!")

        st.markdown("### 🔍 KrushiAI Analysis")
        st.write(response.text)

        st.info(
            "💡 This is an AI-based preliminary assessment. "
            "For serious crop problems, consult an agricultural expert."
)
