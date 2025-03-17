import streamlit as st

st.set_page_config(
    page_title="For Emina",
    page_icon="🐱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Title and divider
st.markdown("""
    <h1 style="text-align: center;">👋 Hello Emina</h1>
    <hr style="border: 2px solid #CCCCCC;">
""", unsafe_allow_html=True)

# Simplified CSS that focuses only on what's needed
st.markdown("""
    <style>
        /* Make everything centered */
        .stApp {
            max-width: 100%;
            text-align: center;
        }

        /* Button styling */
        .stButton > button {
            font-size: 24px !important;
            padding: 15px 30px !important;
            border-radius: 10px !important;
            background-color: #333333 !important;
            color: white !important;
            border: 2px solid #555555 !important;
            cursor: pointer !important;
            display: block !important;
            margin: 0 auto !important;
        }

        /* Text message styling */
        .message {
            text-align: center !important;
            font-size: 22px !important;
            color: #CCCCCC !important;
            margin: 20px 0 !important;
        }
        
        /* Center all content */
        .element-container {
            display: flex !important;
            justify-content: center !important;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "show_content" not in st.session_state:
    st.session_state.show_content = False

# Toggle function
def toggle_content():
    st.session_state.show_content = not st.session_state.show_content

# Simple centered button
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.button("🐱", on_click=toggle_content)

# Show message and image only if session state is True
if st.session_state.show_content:
    st.markdown("<p class='message'>I wish you a nice week and a lot of luck!</p>", unsafe_allow_html=True)
    
    # Create a centered layout for the image
    left_col, center_col, right_col = st.columns([1, 2, 1])
    with center_col:
        st.image("cat.jpg", width=280, use_column_width=True)