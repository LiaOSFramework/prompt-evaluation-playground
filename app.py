import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Prompt Evaluation Playground",
    page_icon="🧠",
    layout="wide"
)

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🧠 Prompt Evaluation Playground")
st.caption("Compare prompts before spending API tokens.")

left, right = st.columns(2)

with left:
    st.subheader("Prompt A")
    prompt_a = st.text_area(
        "",
        height=220,
        placeholder="Paste Prompt A here..."
    )

with right:
    st.subheader("Prompt B")
    prompt_b = st.text_area(
        "",
        height=220,
        placeholder="Paste Prompt B here..."
    )

st.divider()

criteria = st.multiselect(
    "Evaluation Criteria",
    [
        "Accuracy",
        "Reasoning",
        "Structure",
        "Creativity",
        "Safety",
        "Readability"
    ],
    default=["Accuracy","Reasoning","Structure"]
)

if st.button("Evaluate"):
    st.success("UI Ready")
    st.info("Evaluator backend will be connected later.")

    st.subheader("Prompt A")
    st.write(prompt_a if prompt_a else "_No prompt provided._")

    st.subheader("Prompt B")
    st.write(prompt_b if prompt_b else "_No prompt provided._")

    st.subheader("Selected Criteria")
    st.write(criteria)
