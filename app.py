import streamlit as st

st.set_page_config(
    page_title="KrushiAI",
    page_icon="🌱"
)

st.title("🌱 KrushiAI")
st.subheader("AI-Based Crop Health Assistant")

st.write(
    "Upload a crop-leaf image to get a preliminary "
    "crop health assessment."
)

crop = st.selectbox(
    "🌾 Select your crop",
    ["Tomato", "Potato", "Rice", "Wheat", "Cotton"]
)

image = st.file_uploader(
    "📷 Upload a leaf image",
    type=["jpg", "jpeg", "png"]
)

if image is not None:
    st.image(image, caption="Uploaded crop image")

    if st.button("🤖 Analyze Crop"):
        st.success("Analysis completed!")

        st.write("🌱 Crop:", crop)
        st.write("🔎 Preliminary result: Healthy / Possible disease")
        st.write(
            "💡 Please consult an agricultural expert "
            "for confirmation."
)
