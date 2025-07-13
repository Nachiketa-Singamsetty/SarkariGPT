# SarkariGPT 🚀

**Decode. Simplify. Verify.**

A comprehensive AI-powered platform for simplifying government documents and verifying information from social media and messaging platforms.

## 🌐 Live Demo

**Try it now:** [https://sarkarigpt.onrender.com](https://sarkarigpt.onrender.com)

## ✨ Features

### 📄 Document Simplification
- **TL;DR Summary**: Get quick, concise summaries of complex government documents
- **Simple Summary**: Detailed yet easy-to-understand explanations
- **Actionable Checklist**: Step-by-step action items extracted from documents
- **PDF Support**: Upload and process PDF documents (coming soon)

### 🔍 Information Verification
- **Fake News Detection**: AI-powered classification of news authenticity
- **Fact Checking**: Cross-reference claims with verified sources
- **Source Attribution**: Get links to credible news articles
- **Confidence Scores**: Understand the reliability of predictions

## 🏗️ Architecture

- **Frontend**: Streamlit web application
- **Backend**: Flask API with AI/ML models
- **AI Models**: 
  - BART for document summarization
  - BERT for fake news detection
  - Gemma-2B for fact checking
- **External APIs**: SerpAPI for web search

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Nachiketa-Singamsetty/SarkariGPT.git
   cd SarkariGPT
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   SERPAPI_KEY=your_serpapi_key_here
   ```

5. **Run the application**
   ```bash
   chmod +x start.sh && ./start.sh
   ```
   
   Or run services separately:
   ```bash
   # Terminal 1 - Backend
   cd backend && python app.py
   
   # Terminal 2 - Frontend
   cd frontend && streamlit run app.py
   ```

6. **Access the application**
   - Frontend: http://localhost:8501
   - Backend API: http://localhost:5000

## 📖 Usage Guide

### Document Simplification
1. Navigate to the "Simplify Document" tab
2. Paste your government document text or upload a PDF
3. Click "Summarize"
4. View the TL;DR, detailed summary, and action checklist

### Information Verification
1. Navigate to the "Verify Info" tab
2. Paste the text you want to verify (e.g., WhatsApp message)
3. Click "Verify"
4. Review the fake news prediction and fact-checking results

## 🔧 API Endpoints

### Backend API (http://localhost:5000)

#### POST `/summarize`
Summarizes government documents.

**Request:**
```json
{
  "text": "Your government document text here..."
}
```

**Response:**
```json
{
  "tldr": "Brief summary",
  "simple_summary": "Detailed summary",
  "checklist": ["Action item 1", "Action item 2"]
}
```

#### POST `/detect_fake`
Detects fake news in text.

**Request:**
```json
{
  "text": "News text to verify..."
}
```

**Response:**
```json
{
  "label": "REAL/FAKE",
  "confidence": 0.95
}
```

#### POST `/fact_check`
Performs fact checking with web search.

**Request:**
```json
{
  "text": "Claim to fact check..."
}
```

**Response:**
```json
{
  "claim": "Original claim",
  "verdict": "✅ True/❌ False/🤷 Unverified",
  "evidence": [
    {
      "title": "Article title",
      "link": "Article URL",
      "snippet": "Article snippet"
    }
  ]
}
```

## 🛠️ Development

### Project Structure
```
SarkariGPT/
├── backend/
│   ├── app.py              # Flask API server
│   ├── summarizer.py       # Document summarization
│   ├── fake_detector.py    # Fake news detection
│   ├── fact_checker.py     # Fact checking service
│   └── utils/              # Utility functions
├── frontend/
│   ├── app.py              # Streamlit web app
│   ├── components/         # UI components
│   └── pages/              # Additional pages
├── requirements.txt        # Python dependencies
├── start.sh               # Startup script
└── README.md              # This file
```

### Adding New Features
1. Backend: Add new endpoints in `backend/app.py`
2. Frontend: Add new UI components in `frontend/`
3. Models: Add new AI models in respective backend modules

## 🌍 Deployment

### Render Deployment
1. Connect your GitHub repository to Render
2. Set environment variables:
   - `SERPAPI_KEY`: Your SerpAPI key
3. Use start command: `chmod +x start.sh && ./start.sh`

### Environment Variables
- `SERPAPI_KEY`: Required for fact checking functionality

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Hugging Face** for providing the AI models
- **SerpAPI** for web search capabilities
- **Streamlit** for the web framework
- **Flask** for the backend API

## 📞 Contact

- **GitHub**: [@Nachiketa-Singamsetty](https://github.com/Nachiketa-Singamsetty)
- **Project Link**: [https://github.com/Nachiketa-Singamsetty/SarkariGPT](https://github.com/Nachiketa-Singamsetty/SarkariGPT)

---

**Made with ❤️ for simplifying government information access** 