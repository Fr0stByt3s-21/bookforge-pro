import streamlit as st
from bookforge_core import run_pipeline

st.title("📚 BookForge Pro")
topic = st.text_input("Enter Book Topic")
words = st.slider("Target Word Count", 10000, 100000, 30000)
audiobook = st.checkbox("Generate Audiobook?")
voice_id = st.text_input("ElevenLabs Voice ID", "21m00Tcm4TlvDq8ikWAM")
export_formats = st.multiselect("Export Formats", ["pdf", "epub", "md"], default=["pdf","epub"])

if st.button("Generate Book"):
    st.write("✅ Book creation in progress...")
    run_pipeline(topic, words, "yes" if audiobook else "no", export_formats, voice_id)
    st.success("✅ Book created! Check output folder.")
