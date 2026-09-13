import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="PlantBreeding AI",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 PlantBreeding AI")
st.subheader("AI Assistant for Plant Breeding Research")

st.write(
    "A simple research assistant for exploring plant traits "
    "and breeding strategies."
)

st.divider()

st.header("🌱 Plant information")

crop = st.selectbox(
    "Select a crop",
    ["Soybean", "Wheat", "Barley", "Corn"]
)

goal = st.selectbox(
    "Select a breeding goal",
    [
        "Drought resistance",
        "Higher yield",
        "Disease resistance",
        "Early maturity"
    ]
)

traits = {
    "Soybean": [
        "Plant height",
        "Root development",
        "Yield",
        "Flowering time",
        "Seed weight"
    ],
    "Wheat": [
        "Plant height",
        "Grain yield",
        "Disease resistance",
        "Spike length",
        "Maturity time"
    ],
    "Barley": [
        "Plant height",
        "Grain yield",
        "Drought tolerance",
        "Maturity time",
        "Protein content"
    ],
    "Corn": [
        "Plant height",
        "Ear size",
        "Yield",
        "Drought tolerance",
        "Maturity time"
    ]
}

st.header("🧬 Important traits")

selected_traits = st.multiselect(
    "Choose traits to analyse",
    traits[crop],
    default=traits[crop][:3]
)

st.divider()

if st.button("🔬 Generate research recommendation"):

    st.success("Research recommendation generated!")

    st.subheader("💡 Recommendation")

    if goal == "Drought resistance":
        recommendation = (
            f"For {crop}, focus on traits related to water-use efficiency, "
            "root development and yield stability under water stress."
        )

    elif goal == "Higher yield":
        recommendation = (
            f"For {crop}, compare varieties based on yield, plant architecture "
            "and reproductive traits."
        )

    elif goal == "Disease resistance":
        recommendation = (
            f"For {crop}, investigate disease resistance together with yield "
            "and plant development traits."
        )

    else:
        recommendation = (
            f"For {crop}, compare varieties with different maturity periods "
            "and evaluate their performance under local conditions."
        )

    st.write(recommendation)

    st.subheader("📊 Selected traits")

    if selected_traits:
        for trait in selected_traits:
            st.write(f"• {trait}")
    else:
        st.info("Please select at least one trait.")

    st.subheader("🧪 Suggested experiment")

    st.write(
        f"Compare several {crop} varieties under different environmental "
        f"conditions and measure the selected traits. The main breeding goal "
        f"should be **{goal.lower()}**."
    )

st.divider()

st.caption(
    "PlantBreeding AI — educational prototype for plant breeding research."
)
