import streamlit as st
import requests

# Hugging Face API details
API_URL = "https://api-inference.huggingface.co/models/MBZUAI/LaMini-Flan-T5-783M"
HF_TOKEN = "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"  # Replace with your valid token

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def query_huggingface(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 100,
            "temperature": 0.7,
            "top_p": 0.9,
            "do_sample": True
        }
    }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 403:
        return "Error: Forbidden. Check your token permissions."
    elif response.status_code == 404:
        return "Error: Model not found. Check the model name."
    elif response.status_code != 200:
        return f"Error: Received status code {response.status_code}"
    
    try:
        result = response.json()
        return result[0]["generated_text"]
    except Exception as e:
        return f"Failed to decode response: {e}"

# Streamlit UI
st.title("Suggested GenAI Tools")

industry_text = st.text_input("Enter industry or company description:", "ecommerce")

if st.button("Generate Suggestions"):
    prompt = f"""
Based on the following company or industry description, suggest a few internal GenAI tools such as:
- AI-powered document search
- Automated report generation
- Customer-facing chatbots

Industry Info: {industry_text}
"""
    result = query_huggingface(prompt)
    st.subheader("Output")
    st.write(result)