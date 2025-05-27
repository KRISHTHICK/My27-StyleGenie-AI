import streamlit as st
from PIL import Image
import os
from utils import classify_image_by_name, generate_outfits, generate_caption

st.set_page_config(page_title="StyleGenie AI", layout="wide")
st.title("👠 StyleGenie AI – Your Smart Wardrobe Assistant")

WARDROBE_DIR = "wardrobe"
if not os.path.exists(WARDROBE_DIR):
    os.makedirs(WARDROBE_DIR)

st.sidebar.header("📸 Upload Your Clothing Items")
uploaded_files = st.sidebar.file_uploader("Upload multiple images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        with open(os.path.join(WARDROBE_DIR, file.name), "wb") as f:
            f.write(file.getbuffer())
    st.sidebar.success(f"Uploaded {len(uploaded_files)} items!")

images_dict = {"Top": [], "Bottom": [], "Shoes": [], "Accessory": [], "Other": []}

for file in os.listdir(WARDROBE_DIR):
    cat = classify_image_by_name(file)
    images_dict[cat].append(file)

st.subheader("🧺 Your Wardrobe Items")
for category, files in images_dict.items():
    if files:
        st.markdown(f"**{category}s:**")
        cols = st.columns(len(files))
        for i, file in enumerate(files):
            img = Image.open(os.path.join(WARDROBE_DIR, file))
            cols[i].image(img, width=100, caption=file)

st.subheader("👚 Suggested Outfits")
outfits = generate_outfits(images_dict)

if outfits:
    for i, (top, bottom, shoe) in enumerate(outfits):
        col1, col2, col3 = st.columns(3)
        col1.image(os.path.join(WARDROBE_DIR, top), caption="Top")
        col2.image(os.path.join(WARDROBE_DIR, bottom), caption="Bottom")
        if shoe:
            col3.image(os.path.join(WARDROBE_DIR, shoe), caption="Shoes")
        else:
            col3.write("👟 No shoes available")
        st.text_area("📸 Caption", generate_caption(top, bottom, shoe), height=70)

st.info("Tip: Rename files like `top_red.jpg`, `jeans_blue.jpg`, `shoes_white.png` for better category detection.")
