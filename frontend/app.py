import streamlit as st
import requests

BACKEND_URL = "http://localhost:5000"

st.set_page_config(page_title="SarkariGPT", layout="wide")
st.title("SarkariGPT")
st.markdown("**Decode. Simplify. Verify.**")

# Tabs for features
tab1, tab2 = st.tabs(["Simplify Document", "Verify Info"])

with tab1:
    st.header("Simplify Document")
    uploaded_file = st.file_uploader("Upload a PDF or paste text", type=["pdf", "txt"])
    text_input = st.text_area("Or paste your text here:")
    if st.button("Summarize"):
        text = text_input
        if uploaded_file is not None and uploaded_file.type == "application/pdf":
            st.warning("PDF extraction not implemented yet. Paste text to test.")
        if not text:
            st.error("Please provide text to summarize.")
        else:
            with st.spinner("Summarizing..."):
                resp = requests.post(f"{BACKEND_URL}/summarize", json={"text": text})
                if resp.ok:
                    data = resp.json()
                    st.success("Summarization complete!")
                    with st.expander("TL;DR"):
                        st.write(data.get("tldr", "-"))
                    with st.expander("Simple Summary"):
                        st.write(data.get("simple_summary", "-"))
                    with st.expander("Checklist"):
                        st.write("\n".join(data.get("checklist", [])))
                else:
                    st.error("Error from backend.")

with tab2:
    st.header("Verify Info")
    info_text = st.text_area("Paste a WhatsApp message or text to verify:")
    if st.button("Verify"):
        if not info_text:
            st.error("Please provide text to verify.")
        else:
            with st.spinner("Checking..."):
                resp1 = requests.post(f"{BACKEND_URL}/detect_fake", json={"text": info_text})
                resp2 = requests.post(f"{BACKEND_URL}/fact_check", json={"text": info_text})
                if resp1.ok and resp2.ok:
                    fake_data = resp1.json()
                    fact_data = resp2.json()
                    st.subheader("Prediction:")
                    st.write(f"Label: {fake_data.get('label', '-')}")
                    st.write(f"Confidence: {fake_data.get('confidence', '-')}")
                    st.subheader("Verified Articles:")
                    for art in fact_data.get("articles", []):
                        st.markdown(f"- [{art.get('title')}]({art.get('url')}) ({art.get('source')})\n> {art.get('summary')}")
                else:
                    st.error("Error from backend.") 