import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image(r"web_app2\hoyasala.jpg")


with col2:
    st.title("About Hoyasala")
    content = """
    The Hoysaleshvara temple in the village of Halebidu, in the southwestern Indian state of Karnataka, is one of the most sculpturally elaborate buildings in South Asia. Dancing images of gods, goddesses, and celestial beings—carved in high relief into locally sourced blocks of schist used to build the temple—enliven the dynamically zigzagging exterior walls. Processions of elephants, cavalries of horses, and visual narratives wrap their way around the structure, beckoning viewers to follow along. From afar, the temple appears as a vast expanse of sculpture. Up close, the minutely carved details of its walls draw you in, filling your field of vision."""
    st.info(content)

st.info("Below you can find some of the apps I have built in Python.Feel free to contact me!")

