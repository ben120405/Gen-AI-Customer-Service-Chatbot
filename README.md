**🤖 Gen AI Customer Service Chatbot**



**A collection of 6 AI-powered chatbot systems, covering real-world applications of Generative AI, NLP, and RAG (Retrieval-Augmented Generation).**







**🚀 Projects Included**:



&#x20;**1. Dynamic Knowledge Base Chatbot**:



**\* Automatically updates knowledge from new data sources**

**\* Uses \*\*FAISS vector database + embeddings\*\***

**\* Supports real-time document ingestion**



&#x20;**2. Multi-Modal Chatbot (Text + Image)**:



**\* Accepts \*\*text + image inputs\*\***

**\* Uses \*\*Gemini API for multimodal understanding\*\***

**\* Built with \*\*Streamlit UI\*\***



&#x20;**3. Medical Q\&A Chatbot**:



**\* Built using \*\*MedQuAD dataset (XML)\*\***

**\* Provides accurate medical answers**

**\* Uses \*\*semantic search + embeddings\*\***



&#x20;**4. arXiv Expert Chatbot**:



**\* Works on \*\*research paper dataset (JSON)\*\***

**\* Explains complex scientific topics**

**\* Uses \*\*RAG pipeline for knowledge retrieval\*\***



&#x20;**5. Sentiment-Aware Chatbot**:



**\* Detects \*\*user emotion (positive/negative/neutral)\*\***

**\* Responds accordingly**

**\* Improves conversational experience**



&#x20;**6. Multilingual Chatbot**:



**\* Supports multiple languages**

**\* Performs \*\*language detection + translation\*\***

**\* Provides responses in user's preferred language**



&#x20;**🧠 Tech Stack**:



**\* \*\*Python\*\***

**\* \*\*LangChain\*\***

**\* \*\*FAISS (Vector Database)\*\***

**\* \*\*HuggingFace Embeddings\*\***

**\* \*\*Google Gemini API\*\***

**\* \*\*Streamlit\*\***

**\* \*\*Pandas / NumPy\*\***



&#x20;**📁 Project Structure**:





**Gen-AI-Customer Service Chatbot/**

**│**

**├── apps/                # All chatbot projects**

**│   ├── 1\_dynamic\_kb/**

**│   ├── 2\_multimodal/**

**│   ├── 3\_medical/**

**│   ├── 4\_arxiv\_expert/**

**│   ├── 5\_sentiment/**

**│   └── 6\_multilingual/**

**│**

**├── shared/              # Reusable modules**

**│   ├── utils/**

**│   ├── embeddings/**

**│   └── llm/**

**│**

**├── requirements.txt**

**├── README.md**

**└── .env.example**





**⚙️ Setup Instructions**:



&#x20;

**1. Clone the repository**



**bash**

**git clone https://github.com/YOUR\_USERNAME/ai-chatbot-suite.git**

**cd ai-chatbot-suite**



&#x20;

**2. Create virtual environment**



**bash**

**python -m venv venv**

**venv\\Scripts\\activate    # Windows**



&#x20;

**3. Install dependencies**



**bash**

**pip install -r requirements.txt**





**4. Add API Key**



**Create a `.env` file:**



**GOOGLE\_API\_KEY=your\_api\_key\_here**





**5. Run any project**



**Example:**



**bash**

**cd apps/2\_multimodal**

**streamlit run app.py**





**📊 Datasets**:



**Datasets are not included due to size.**



**You can download from:**



**\* MedQuAD → https://github.com/abachaa/MedQuAD**

**\* arXiv Dataset → https://www.kaggle.com/datasets/Cornell-University/arxiv**





&#x20;**🎯 Key Learnings**:



**\* Built end-to-end \*\*RAG-based systems\*\***

**\* Worked with \*\*vector databases (FAISS)\*\***

**\* Implemented \*\*multimodal AI (text + image)\*\***

**\* Designed \*\*scalable chatbot architectures\*\***

**\* Integrated \*\*real-world APIs (Gemini)\*\***





**📌 Future Improvements**:



**\* Unified chatbot interface**

**\* Deployment on cloud (AWS / Render)**

**\* Add authentication system**

**\* Improve UI/UX**





&#x20;**👨‍💻 Author**:



**\*\*Benin Dbritto\*\***





**If you like this project**

**Give it a ⭐ on GitHub!**



