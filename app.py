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
    with st.spinner("Evaluating..."):

        response = client.responses.create(
            model="gpt-5-mini",
            input=f"""
Bandingkan Prompt A dan Prompt B.

Prompt A:
{prompt_a}

Prompt B:
{prompt_b}

Nilai berdasarkan:
{", ".join(criteria)}

Berikan output dalam format markdown:

## Winner
(Prompt A / Prompt B)

## Score
- Accuracy:
- Reasoning:
- Structure:
- Creativity:
- Safety:
- Readability:

## Analysis
Jelaskan kelebihan dan kekurangan masing-masing prompt.
"""
        )

    st.markdown(response.output_text)

 st.subheader("Prompt A")
    st.write(prompt_a if prompt_a else "_No prompt provided._")

    st.subheader("Prompt B")
    st.write(prompt_b if prompt_b else "_No prompt provided._")

    st.subheader("Selected Criteria")
    st.write(criteria)
