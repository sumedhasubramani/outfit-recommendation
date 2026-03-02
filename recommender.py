import pandas as pd
import os
import random

DATASET_PATH = "outfits.csv"

def load_dataset():
    return pd.read_csv(DATASET_PATH)

def recommend_outfit(weather, style, gender, age_group):
    df = load_dataset()

    # Exact match (MOST IMPORTANT)
    filtered = df[
        (df["weather"] == weather) &
        (df["style"] == style) &
        (df["gender"] == gender) &
        (df["age_group"] == age_group)
    ]

    if filtered.empty:
        return {"message": "No suitable outfit found"}

    outfit = filtered.sample(1).iloc[0]

    image_path = outfit["image_path"]
    if not os.path.exists(image_path):
        image_path = None

    return {
        "top": outfit["top"],
        "bottom": outfit["bottom"],
        "footwear": outfit["footwear"],
        "style": outfit["style"],
        "gender": outfit["gender"],
        "age_group": outfit["age_group"],
        "image_path": image_path
    }
