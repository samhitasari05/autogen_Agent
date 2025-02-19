# Autogen Research Paper Summarization Assistant

## 📌 Overview
This project is an AI-powered research assistant that automates the process of fetching, summarizing, and analyzing research papers using **Microsoft's Autogen framework**. The system integrates with **Google Scholar** and **ArXiv** to retrieve relevant papers and provides insights through intelligent AI agents. The user interacts with the tool via a **Streamlit-based UI**, where they can input a research topic and receive summarized insights.

## 🔥 Features
- **Automated Paper Fetching**: Retrieves at least five research papers from Google Scholar and ArXiv.
- **AI-based Summarization**: Uses Autogen's assistant agent to summarize key points from each paper.
- **Paper Analysis**: Highlights the **advantages and disadvantages** of each paper.
- **Alternative Topic Suggestions**: Suggests three closely related topics if fewer than five papers are found.
- **Streamlit UI**: Provides an interactive interface for users to search and explore insights.
- **Error Handling**: Addresses common issues such as SSL errors, API restrictions, and compatibility concerns.

## 🏗️ Folder Structure
```bash
📂 Autogen-Research-Assistant
│── 📄 README.md  # Documentation
│── 📄 requirements.txt  # Dependencies
│── 📂 src
│   ├── 📄 main.py  # Streamlit UI
│   ├── 📄 agents.py  # AI agent logic
│   ├── 📄 data_loader.py  # Google Scholar & ArXiv integration
│   ├── 📄 agents.py  # Autogen summarization module
```

## 🚀 Installation & Setup
### Prerequisites
Ensure you have **Python 3.10+** installed.

### Step 1: Clone the Repository
```sh
git clone https://github.com/samhitasari05/Autogen-Research-Assistant.git
cd Autogen-Research-Assistant
```

### Step 2: Install Dependencies
```sh
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables
Create a `.env` file in the root directory and add your API keys (if needed for Google Scholar or ArXiv access).
```env
SCHOLAR_API_KEY=your_google_scholar_api_key
ARXIV_API_KEY=your_arxiv_api_key
```

### Step 4: Run the Application
```sh
streamlit run src/main.py
```

## 🛠️ Technologies Used
- **Autogen** (Microsoft AI Agent Framework)
- **LangChain** (LLM orchestration)
- **Scholarly** (Google Scholar integration)
- **Python-dotenv** (Environment variables management)
- **Streamlit** (User Interface)
- **ArXiv API** (Paper retrieval)

## 🧐 Example Usage
1. Open the Streamlit app.
2. Enter a research topic (e.g., "Natural Language Processing in Healthcare").
3. The system fetches relevant papers and summarizes them.
4. View summarized insights along with key takeaways and alternative topics.

## 🐞 Troubleshooting & Debugging
- **SSL Errors**: Ensure Python is updated and SSL certificates are correctly installed.
- **Model Compatibility Issues**: The project works best with Python 3.10.
- **API Rate Limits**: Google Scholar API might impose restrictions; try a different query or use proxies.

## 💡 Future Improvements
- Expand paper sources to include IEEE and Springer.
- Improve topic clustering for better recommendations.
- Implement a database to store past searches and summaries.

## 🤝 Contributing
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push to the branch and submit a pull request.

## 📜 License
This project is licensed under the MIT License. Feel free to use and modify it for educational or research purposes.

## 📬 Contact
For questions or suggestions, feel free to connect with me on **GitHub: [samhitasari05](https://github.com/samhitasari05)**.
