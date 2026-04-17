# 🤖 Gen-AI-Customer Service Chatbot

A collection of **6 AI-powered chatbot systems** , covering real-world applications of **Generative AI, NLP, and RAG (Retrieval-Augmented Generation)**.

---

## 🚀 Projects Included

### 1. Dynamic Knowledge Base Chatbot

* Automatically updates knowledge from new data sources
* Uses **FAISS vector database + embeddings**
* Supports real-time document ingestion

---

### 2. Multi-Modal Chatbot (Text + Image)

* Accepts **text + image inputs**
* Uses **Gemini API for multimodal understanding**
* Built with **Streamlit UI**

---

### 3. Medical Q&A Chatbot

* Built using **MedQuAD dataset (XML)**
* Provides accurate medical answers
* Uses **semantic search + embeddings**

---

### 4. arXiv Expert Chatbot

* Works on **research paper dataset (JSON)**
* Explains complex scientific topics
* Uses **RAG pipeline for knowledge retrieval**

---

### 5. Sentiment-Aware Chatbot

* Detects **user emotion (positive/negative/neutral)**
* Responds accordingly
* Improves conversational experience

---

### 6. Multilingual Chatbot

* Supports multiple languages
* Performs **language detection + translation**
* Provides responses in user's preferred language

---

## 🧠 Tech Stack

* **Python**
* **LangChain**
* **FAISS (Vector Database)**
* **HuggingFace Embeddings**
* **Google Gemini API**
* **Streamlit**
* **Pandas / NumPy**

---

## 📁 Project Structure

```
ai-chatbot-suite/
│
├── apps/                # All chatbot projects
│   ├── 1_dynamic_kb/
│   ├── 2_multimodal/
│   ├── 3_medical/
│   ├── 4_arxiv_expert/
│   ├── 5_sentiment/
│   └── 6_multilingual/
│
├── shared/              # Reusable modules
│   ├── utils/
│   ├── embeddings/
│   └── llm/
│
├── requirements.txt
├── README.md
└── .env.example
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-chatbot-suite.git
cd ai-chatbot-suite
```

---

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate    # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add API Key

Create a `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

---

### 5. Run any project

Example:

```bash
cd apps/2_multimodal
streamlit run app.py
```

---

## 📊 Datasets

Datasets are not included due to size.

You can download from:

* MedQuAD → https://github.com/abachaa/MedQuAD
* arXiv Dataset → https://www.kaggle.com/datasets/Cornell-University/arxiv

---

## 🎯 Key Learnings

* Built end-to-end **RAG-based systems**
* Worked with **vector databases (FAISS)**
* Implemented **multimodal AI (text + image)**
* Designed **scalable chatbot architectures**
* Integrated **real-world APIs (Gemini)**

---

## 📌 Future Improvements

* Unified chatbot interface
* Deployment on cloud (AWS / Render)
* Add authentication system
* Improve UI/UX

---

## 👨‍💻 Author

**Benin Dbritto**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
