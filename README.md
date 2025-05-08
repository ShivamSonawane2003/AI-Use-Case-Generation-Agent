# 🧠 AI Use Case Generator

A GenAI-powered tool that suggests AI applications tailored to specific industries or company descriptions. This app uses Hugging Face's `LaMini-Flan-T5-783M` model and is built with Streamlit for an interactive UI experience.

## 🚀 Features

- Generate internal AI use case suggestions based on input text.
- Simple, intuitive web interface.
- Uses a transformer-based language model for relevant results.
- Ideal for brainstorming GenAI tools for business use.

## 🛠 Tech Stack

- **Frontend:** Streamlit  
- **Model:** Hugging Face - LaMini-Flan-T5-783M  
- **Language:** Python  
- **API Calls:** Hugging Face Inference API

## 📂 Project Structure

```
├── AI_Use_Case_Generator.ipynb  # Jupyter notebook for development and testing
├── app.py                       # Streamlit web app
├── final_report.md              # Example use case report (e.g., retail industry)
├── requirements.txt             # Dependencies
└── README.md                    # Project documentation
```

## 🧪 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-use-case-generator.git
cd ai-use-case-generator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Hugging Face API

Open `app.py` and replace the value of `HF_TOKEN` with your Hugging Face API token:

```python
HF_TOKEN = "your_huggingface_api_token_here"
```

### 4. Run the App

```bash
streamlit run app.py
```

## 📊 Example Use Case: Retail Industry

From the included report:
- **Use Case Example:** AI-powered customer service chatbots
- **Relevant Datasets:**
  - [Predictive Maintenance Dataset - Kaggle](https://www.kaggle.com/datasets/stephanmatzka/predictive-maintenance-dataset-ai4i-2020)
  - [Machine Predictive Maintenance - Kaggle](https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification)

## 🤖 Model Information

Model used: [`MBZUAI/LaMini-Flan-T5-783M`](https://huggingface.co/MBZUAI/LaMini-Flan-T5-783M)

## 🔐 Security Note

> ⚠️ **Do not share your Hugging Face API token publicly.** Consider using environment variables or a `.env` file to manage secrets.

## 🙌 Acknowledgments

- Hugging Face for the model and API platform.
- Streamlit for simplifying the UI build process.
