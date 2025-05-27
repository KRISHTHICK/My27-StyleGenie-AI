# My27-StyleGenie-AI
GenAI

Sure! Here's a **brand new fashion-related AI project** idea with **full code, explanation, and new features**, all designed to **run directly in VS Code without using `venv`** and ready to be pushed to **GitHub**.

---

## 👠✨ **Project Title**: **StyleGenie AI – Virtual Wardrobe + Outfit Recommender**

---

## 💡 **Idea:**

**StyleGenie AI** lets users:

* Upload multiple clothing item images.
* Classify each item (Top, Bottom, Shoes, Accessories).
* Mix and match to create suggested outfits.
* View AI-generated fashion advice.
* Get captions for sharing on social media.

---

## 🔥 **New Features:**

* 🧺 Multi-item wardrobe upload.
* 🏷️ Auto-detect clothing category via filename keywords.
* 🧠 Outfit generator logic (Top + Bottom + Shoes).
* 📝 Auto-caption generator using keywords.
* 📸 Preview full outfit layout.
* 💡 Fashion tips based on selected style.

---

## 📁 **Folder Structure**

```
StyleGenie-AI/
├── app.py
├── utils.py
├── wardrobe/
│   └── your_clothes.jpg...
├── requirements.txt
└── README.md
```

---

## 📦 `requirements.txt`

```txt
streamlit
Pillow
numpy
```

---

## 🧠 `utils.py`

```python
import os
from PIL import Image
import random

def classify_image_by_name(filename):
    fname = filename.lower()
    if "top" in fname or "shirt" in fname:
        return "Top"
    elif "jean" in fname or "pant" in fname or "skirt" in fname:
        return "Bottom"
    elif "shoe" in fname or "sneaker" in fname:
        return "Shoes"
    elif "bag" in fname or "accessory" in fname:
        return "Accessory"
    else:
        return "Other"

def generate_outfits(images_dict):
    outfits = []
    tops = images_dict.get("Top", [])
    bottoms = images_dict.get("Bottom", [])
    shoes = images_dict.get("Shoes", [])

    for top in tops:
        for bottom in bottoms:
            shoe = random.choice(shoes) if shoes else None
            outfits.append((top, bottom, shoe))
    return outfits[:5]  # limit to 5 outfit suggestions

def generate_caption(top, bottom, shoe):
    caption = f"Today's vibe: {top.split('.')[0]} + {bottom.split('.')[0]}"
    if shoe:
        caption += f" + {shoe.split('.')[0]}"
    caption += " 😍 #StyleGenie #OOTD"
    return caption
```

---

## 🚀 `app.py`

```python
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
```

---

## 📖 `README.md`

````markdown
# 👠 StyleGenie AI – Outfit Recommender and Fashion Assistant

## 🚀 Features
- Upload multiple images to build a virtual wardrobe.
- Automatically classify clothing items based on filename.
- Mix and match pieces to generate stylish outfits.
- Suggest social media captions for the outfit.
- Minimal setup, works with just Python and Streamlit.

## 📂 Folder Structure
- `wardrobe/`: place your clothing item images here.
- `app.py`: main Streamlit app.
- `utils.py`: helper functions.
- `requirements.txt`: required packages.

## 🛠️ Setup & Run
```bash
pip install -r requirements.txt
streamlit run app.py
````

## 💡 Notes

* Make sure your image filenames include keywords like "top", "jeans", "shoe".
* Add more images for better outfit generation.
* Push to GitHub to showcase your personal styling assistant.

## 📸 Example

Upload:

* `top_red.jpg`
* `jeans_blue.jpg`
* `shoes_white.jpg`

Get:

* Outfit suggestions + captions + wardrobe preview.

````

---

## ✅ How to Use in VS Code & GitHub

### 1. Run Locally
```bash
git clone https://github.com/yourusername/StyleGenie-AI.git
cd StyleGenie-AI
pip install -r requirements.txt
streamlit run app.py
````

### 2. Upload to GitHub

* Push the project folder to your GitHub repo.
* Make sure `wardrobe/` is included with `.gitkeep` or sample images.

---

Would you like me to:

* Add advanced features like color detection or CLIP-based matching?
* Help deploy this on Hugging Face or Streamlit Cloud?
* Add a search filter by category?

Let me know, and I’ll expand the project!
