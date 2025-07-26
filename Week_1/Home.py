import streamlit as st

st.set_page_config(page_title="Main Page", page_icon="🤖", layout="centered")
st.title("Welcome to the Multi-Page Streamlit App!")
st.write("Use the sidebar to navigate between pages.")

pages = {
    "📧 Email Draft": "1_Email_Draft_Generator",
    "🗒️ Meeting Notes": "2_Meeting_Notes_Summarizer",
}

for page_name, page_display_name in pages.items():
    col = st.columns([1, 2, 1])[1]  # Center the button
    with col:
        # Use markdown for a larger button-like appearance
        if st.button(f"**{page_name}**", use_container_width=True):
            st.switch_page(f"pages/{page_display_name}.py")
