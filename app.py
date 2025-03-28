import streamlit as st
import openai
from dotenv import load_dotenv
import os
import time

# Load API Key
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Page Config
st.set_page_config(page_title="AI Business Analysis Assistant", page_icon="📊")

# --- Header ---
st.title("📊 AI Business Analysis Assistant")
st.markdown("Use AI to extract structured insights, business needs, and action plans from natural business input.")

# --- Input Section ---
with st.container():
    st.subheader("📝 Business Input")
    st.markdown("Paste any business challenge, stakeholder note, or idea you'd like analyzed.")
    user_input = st.text_area("What do you want help with?", height=200, placeholder="E.g., Our delivery process has frequent delays, and customer satisfaction is dropping...")

# --- Analyze Button ---
analyze = st.button("🔍 Generate Insights")

# --- AI Output Section ---
if analyze and user_input:
    with st.spinner("Analyzing your input..."):
        prompt = f"""You're a professional Business Analyst. Given the business input below, generate a clear and structured analysis including:

1. Business Requirements
2. Stakeholder Requirements
3. Key Tasks to perform
4. Recommended Analysis Techniques

Make the output readable and actionable, suitable for use in meetings or reports.

Input: {user_input}
"""

        try:
            start = time.time()
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                timeout=20
            )
            result = response.choices[0].message.content

            st.markdown("---")
            st.subheader("📄 Insight Summary")
            st.markdown(result)
            print("AI response time:", time.time() - start)

        except Exception as e:
            st.error(f"An error occurred while generating insights: {e}")

# --- Footer ---
st.markdown("---")
st.markdown(
    "<small>💡 Built with Python, Streamlit & OpenAI | Developed by an aspiring Business Analyst</small>",
    unsafe_allow_html=True
)
