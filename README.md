# Automated-Python-News-Scraper-AI
A high-performance automated Python news intelligence pipeline that retrieves, summarizes, and delivers top tech news from Hacker News and utilizes the BART Transformer model for real-time abstractive summarization and email delivery.

## The Mission
In an era of information overload, this project serves as a personalized "AI Editor." It doesn't just find links; it reads the articles for you and delivers a concise, human-like briefing directly to your inbox.

## Technical Architecture: Tools & Libraries

This project integrates several industry-standard libraries, each chosen for a specific role in the data lifecycle:

| Tool / Library | Role | The "Why" |
| :--- | :--- | :--- |
| **Requests** | Data Retrieval | Handles the HTTP handshake to fetch raw HTML from the web. |
| **BeautifulSoup4** | Web Scraping | Parses the HTML DOM to isolate specific news headlines and links. |
| **Newspaper3k** | Content Extraction | Uses advanced heuristics to "clean" articles, removing ads/navbars to find the core body text. |
| **Transformers** | AI Logic | The backbone of the project; uses the **BART** (Bidirectional and Auto-Regressive Transformers) model architecture. |
| **PyTorch (Torch)** | Deep Learning Engine | Provides the mathematical tensor operations required for the Transformer model to "think." |
| **SMTPLib** | Communication | Interfaces with Gmail’s SMTP servers using SSL encryption for secure mail delivery. |
| **Dotenv** | Security | Decouples sensitive credentials from the source code using Environment Variables. |


## 🧠 The AI Pipeline (BART Model)
Unlike simple "extractive" scripts that just copy the first three sentences of an article, this engine uses **Abstractive Summarization**. 
* **The Process:** The text is tokenized into numerical vectors, processed through a 1.6GB neural network, and decoded back into English.
* **The Result:** A synthesized "Synopsis" that understands context and rewrites the news in a condensed format.

## ⚙️ Setup & Installation

### 1. Environment Configuration
Ensure you have Python 3.10+ installed. Clone the repository and install the dependencies:
```bash
pip install requests beautifulsoup4 transformers torch newspaper3k lxml_html_clean python-dotenv
