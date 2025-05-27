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
