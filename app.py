import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Prompt Evaluation Playground",
    page_icon="🧠",
    layout="wide"
)

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ------------------------
# Session State
# ------------------------

if "prompt_a" not in st.session_state:
    st.session_state.prompt_a = ""

if "prompt_b" not in st.session_state:
    st.session_state.prompt_b = ""

# ------------------------
# Header
# ------------------------

st.title("🧠 Prompt Evaluation Playground")
st.caption("Compare prompts before spending API tokens.")

left, right = st.columns(2)

with left:
    st.subheader("Prompt A")
    prompt_a = st.text_area(
        "",
        key="prompt_a",
        height=220,
        placeholder="Paste Prompt A here..."
    )

with right:
    st.subheader("Prompt B")
    prompt_b = st.text_area(
        "",
        key="prompt_b",
        height=220,
        placeholder="Paste Prompt B here..."
    )

st.divider()

# ------------------------
# Criteria
# ------------------------

st.subheader("Evaluation Criteria")

accuracy = st.checkbox("Accuracy", value=True)
reasoning = st.checkbox("Reasoning", value=True)
structure = st.checkbox("Structure", value=True)
creativity = st.checkbox("Creativity")
safety = st.checkbox("Safety")
readability = st.checkbox("Readability")

criteria = []

if accuracy:
    criteria.append("Accuracy")

if reasoning:
    criteria.append("Reasoning")

if structure:
    criteria.append("Structure")

if creativity:
    criteria.append("Creativity")

if safety:
    criteria.append("Safety")

if readability:
    criteria.append("Readability")

st.divider()

col1, col2 = st.columns(2)

with col1:
    evaluate = st.button(
        "🚀 Evaluate",
        use_container_width=True,
        type="primary"
    )

with col2:
    clear = st.button(
        "🗑️ Clear",
        use_container_width=True
    )

# ------------------------
# Clear
# ------------------------

if clear:
    st.session_state.prompt_a = ""
    st.session_state.prompt_b = ""
    st.rerun()

# ------------------------
# Evaluate
# ------------------------

if evaluate:

    if not prompt_a.strip():
        st.error("Prompt A is empty.")
        st.stop()

    if not prompt_b.strip():
        st.error("Prompt B is empty.")
        st.stop()

    if len(criteria) == 0:
        st.error("Please select at least one criterion.")
        st.stop()

    with st.spinner("Evaluating prompts..."):

        response = client.responses.create(
            model="gpt-5-mini",
            input=f"""
Bandingkan Prompt A dan Prompt B.

Prompt A:
{prompt_a}

Prompt B:
{prompt_b}

Gunakan kriteria berikut:
{", ".join(criteria)}

Berikan hasil dalam format markdown.

# 🏆 Winner
(Prompt A / Prompt B)

# 📊 Score
- Accuracy
- Reasoning
- Structure
- Creativity
- Safety
- Readability

# 🔍 Analysis

## Prompt A
- Kelebihan
- Kekurangan

## Prompt B
- Kelebihan
- Kekurangan

## Kesimpulan
Jelaskan prompt mana yang lebih baik dan alasannya.
"""
        )

    st.success("✅ Evaluation completed!")

    st.markdown(response.output_text)

    with st.expander("📄 Input Summary"):

        st.markdown("### Prompt A")
        st.write(prompt_a)

        st.markdown("### Prompt B")
        st.write(prompt_b)

        st.markdown("### Evaluation Criteria")
        st.write(", ".join(criteria))
