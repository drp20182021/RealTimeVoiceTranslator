import streamlit as st
from ui import main_page, translate_page
from interactions import handle_translation


def render_page():
    if "page" not in st.session_state:
        st.session_state.page = "main"

    if st.session_state.page == "main":
        main_page()
    else:
        translate_page(handle_translation)


if __name__ == "__main__":
    render_page()
