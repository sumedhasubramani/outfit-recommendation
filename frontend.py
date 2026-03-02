import streamlit as st
import requests
import os

st.set_page_config(page_title="Outfit Generator 👕", layout="centered")

st.title("AI Outfit Recommendation System 👗✨")
st.caption("Personalized outfits based on weather, style & age")

# ---------------- MAPPINGS ---------------- #

weather_label = st.selectbox(
    "Weather 🌦️",
    ["Sunny 🌞", "Humid 💧", "Winter ❄️", "Moderate 🌤️", "Rainy 🌧️"]
)

weather_map = {
    "Sunny 🌞": "sunny",
    "Humid 💧": "humid",
    "Winter ❄️": "winter",
    "Moderate 🌤️": "moderate",
    "Rainy 🌧️": "rainy"
}
weather = weather_map[weather_label]

style_label = st.selectbox(
    "Style 👔",
    ["Casual", "Sporty", "College Formal", "Office Semi Formal",
     "Office Formal", "Classy", "Minimal", "Ethnic"]
)
style = style_label.lower()

gender_label = st.selectbox(
    "Gender 🧍",
    ["Male 👦", "Female 👩"]
)

gender_map = {
    "Male 👦": "male",
    "Female 👩": "female"
}
gender = gender_map[gender_label]

age_group = st.selectbox(
    "Age Group 🎯",
    ["20-35", "35-50"]
)

# ---------------- BUTTON ---------------- #

if st.button("Generate Outfit ✨"):
    payload = {
        "weather": weather,
        "style": style,
        "gender": gender,
        "age_group": age_group
    }

    try:
       from recommender import recommend_outfit

result = recommend_outfit(weather, style, gender, age_group)
        


            if "message" in result:
                st.warning(result["message"])
            else:
                st.success("Recommended Outfit 👌")

                st.markdown(f"**Top:** {result['top']}")
                st.markdown(f"**Bottom:** {result['bottom']}")
                st.markdown(f"**Footwear:** {result['footwear']}")
                st.markdown(f"**Style:** {result['style'].title()}")
                st.markdown(f"**Age Group:** {result['age_group']}")

                if result["image_path"]:
                    st.image(
                        result["image_path"],
                        caption="Suggested Look 👀",
                        width=350
                    )
                else:
                    st.info("Image not found 📷")

    except Exception as e:
        st.error("Backend server is not running ❌")



