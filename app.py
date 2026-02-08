import streamlit as st
import langchain_helper

st.title("🍽️ Restaurant Name Generator")

cuisine = st.sidebar.selectbox(
    "Pick a Cuisine",
    (
        'Indian', 'Italian', 'Chinese', 'Mexican', 'Japanese', 'Thai',
        'French', 'Spanish', 'Greek', 'Mediterranean', 'Korean',
        'Vietnamese', 'Lebanese', 'Turkish', 'Moroccan', 'Ethiopian',
        'American', 'Southern', 'Tex-Mex', 'Brazilian', 'Peruvian',
        'Argentinian', 'German', 'British', 'Irish', 'Russian',
        'Ukrainian', 'Polish', 'Hungarian', 'Austrian', 'Swiss',
        'Portuguese', 'Caribbean', 'Jamaican', 'Cuban', 'Hawaiian',
        'Filipino', 'Indonesian', 'Malaysian', 'Singaporean',
        'Nepalese', 'Tibetan', 'Sri Lankan', 'Bengali', 'Punjabi',
        'Rajasthani', 'Gujarati', 'Hyderabadi', 'Mughlai',
        'Awadhi', 'Kashmiri'
    )
)

if cuisine:
    with st.spinner("Generating restaurant concept..."):
        response = langchain_helper.generate_restaurant_name_and_items(cuisine)

    st.header(response["restaurant_name"])
    st.subheader("Menu")
    st.markdown(response["menu_items"])
