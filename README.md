# 🚀 Resume Analyzer & Job Finder

An AI-powered resume analysis and job search guidance application built with **Streamlit**, **CrewAI**, and **Google Gemini AI**. This multi-agent system provides comprehensive resume feedback, improvements, and personalized job search strategies.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.28+-red.svg)
![CrewAI](https://img.shields.io/badge/crewai-v0.126+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

### 📊 **Resume Analysis**
- **Comprehensive Feedback**: Detailed analysis with quality scoring (0-100)
- **Section Detection**: Identifies present and missing resume sections
- **Quality Assessment**: Evaluates well-written sections and areas for improvement
- **Actionable Suggestions**: Specific recommendations for enhancement

### ✅ **Resume Improvement**
- **AI-Powered Enhancement**: Automatically improves resume content
- **Grammar & Clarity**: Fixes language issues and improves readability
- **Professional Formatting**: Optimizes structure and presentation
- **Download Feature**: Get your improved resume as a DOCX file

### 💼 **Job Search Guidance**
- **Personalized Recommendations**: Job titles tailored to your profile
- **Company Suggestions**: Top companies in your field
- **Platform Guidance**: Best job boards and websites for your industry
- **Networking Tips**: Industry-specific networking strategies

### 🔧 **Technical Features**
- **Multi-format Support**: Upload PDF or DOCX resumes
- **Real-time Processing**: Instant AI analysis and feedback
- **User-friendly Interface**: Clean, intuitive Streamlit UI
- **Error Handling**: Robust error management with helpful messages

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/resume-analyzer.git
cd resume-analyzer
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables
1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Get your Gemini API key:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Click "Create API Key"
   - Copy your API key

3. Edit `.env` file and add your API key:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```

### Step 4: Run the Application
```bash
streamlit run main.py
```

The application will open in your browser at `http://localhost:8501`

## 📋 Requirements

Create a `requirements.txt` file with the following dependencies:

```txt
streamlit
python-docx
pymupdf
crewai
python-dotenv
langchain
langchain-google-genai
```

## 🚀 Usage

### 1. **Upload Your Resume**
- Click "Upload Resume (PDF or DOCX)"
- Select your resume file
- Supported formats: PDF, DOCX

### 2. **Analyze & Get Feedback**
- Click "🚀 Analyze & Find Jobs"
- Wait for AI processing (usually 30-60 seconds)

### 3. **Review Results**
- **Resume Feedback**: JSON analysis with scores and suggestions
- **Improved Resume**: Enhanced version of your resume
- **Job Search Guidance**: Personalized career advice

### 4. **Download Improved Resume**
- Click "⬇️ Download Improved Resume"
- Save the enhanced DOCX file

## 🏗️ Architecture

The application uses a **multi-agent AI system** powered by CrewAI:

### **Agent 1: Professional Resume Advisor**
- **Role**: Resume analysis expert
- **Task**: Analyze resume structure, content, and quality
- **Output**: JSON feedback with scores and suggestions

### **Agent 2: Resume Rewriting Expert**
- **Task**: Improve resume based on feedback
- **Output**: Enhanced resume text

### **Agent 3: Job Research Expert**
- **Task**: Provide job search guidance
- **Output**: Personalized career advice and strategies

## 📁 Project Structure

```
resume-analyzer/
│
├── main.py                 # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── .env                   # Your API keys (create this)
├── README.md              # This file
└── improved_resume.docx   # Generated improved resume (auto-created)
```

## 🔧 Configuration

### Environment Variables
- `GEMINI_API_KEY`: Your Google Gemini API key (required)

### Customization Options
You can modify the following in `main.py`:
- **AI Model**: Change `gemini/gemini-1.5-flash` to other Gemini models
- **Temperature**: Adjust creativity level (0.0-1.0)
- **Agent Roles**: Customize agent descriptions and tasks
- **Output Format**: Modify expected outputs and formatting

## 🐛 Troubleshooting

### Common Issues

#### **"Missing GEMINI_API_KEY" Error**
- Ensure `.env` file exists in the project root
- Verify your API key is correctly set in `.env`
- Check that your API key is valid and active

#### **"Could not parse JSON feedback" Warning**
- This is handled gracefully - raw output will be shown
- Usually resolves on retry
- Check your internet connection

#### **Package Installation Errors**
- Try using a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  pip install -r requirements.txt
  ```

#### **Slow Processing**
- Resume analysis typically takes 30-60 seconds
- Ensure stable internet connection
- Large resumes may take longer to process

### **Getting Help**
If you encounter issues:
1. Check the error messages in the Streamlit interface
2. Review the terminal output for detailed error logs
3. Ensure all dependencies are correctly installed
4. Verify your API key is valid and has sufficient quota

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Setup
```bash
# Clone your fork
git clone https://github.com/yourusername/resume-analyzer.git
cd resume-analyzer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your API keys to .env

# Run the application
streamlit run main.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[CrewAI](https://github.com/joaomdmoura/crewAI)** - Multi-agent AI framework
- **[Streamlit](https://streamlit.io/)** - Web application framework
- **[Google Gemini](https://ai.google.dev/)** - Large language model
- **[PyMuPDF](https://pymupdf.readthedocs.io/)** - PDF processing
- **[python-docx](https://python-docx.readthedocs.io/)** - DOCX file handling

## 📞 Support

If you find this project helpful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs via GitHub Issues
- 💡 Suggesting new features
- 🤝 Contributing to the codebase

---

**Built with ❤️ by [Pratham Dixit](https://github.com/yourusername)**

*Transform your resume with AI-powered insights and land your dream job!*
