# 🛡️ CodeGuardian

> AI-Powered Code Analysis and Review Platform

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange.svg)](https://openai.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📖 Table of Contents

- [Introduction](#-introduction)
- [Key Features](#-key-features)
- [Project Structure](#-project-structure)
- [Technical Architecture](#-technical-architecture)
- [Supported Languages](#-supported-programming-languages)
- [API Endpoints](#-api-endpoints)
- [Installation & Setup](#-installation--setup)
- [AI Integration](#-ai-integration-details)
- [Security Features](#-security-features)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)

---

## 🎯 Introduction

**CodeGuardian** is a full-stack web application that provides intelligent code analysis and review using OpenAI's GPT models. The system offers comprehensive code quality assessment, security analysis, performance optimization suggestions, and best practices recommendations across multiple programming languages.

Whether you're looking for a quick feedback loop or an in-depth code review, CodeGuardian leverages state-of-the-art AI to bridge the gap between automated linting and human code review.

---

## 📁 Project Structure

```
Code_Guardian/
├── project/
│   ├── app.py                      # Flask backend server
│   ├── requirements.txt            # Python dependencies
│   ├── static/
│   │   ├── script.js              # Frontend JavaScript
│   │   └── style.css              # Styling and design
│   ├── templates/
│   │   └── index.html             # Main web interface
│   └── utils/
│       ├── code_analyzer.py       # AI code analysis logic
│       ├── prompt_templates.py    # GPT prompt engineering
│       └── schemas.py             # Data validation schemas
├── .env.example                    # Environment variables template
├── .gitignore                      # Git ignore rules
├── Readme.md                       # Project documentation
├── SETUP_GUIDE.md                 # Detailed setup instructions
└── TODO.md                        # Development roadmap
```

---

## 🏗️ Technical Architecture

### Backend System

- **Framework:** Flask 2.3+ (Python web framework)
- **AI Integration:** OpenAI API (GPT-4 and GPT-3.5 Turbo)
- **Prompt Framework:** Structured templates with expert personas
- **API Structure:** RESTful endpoints with JSON responses
- **Validation:** Pydantic schemas for type-safe data handling

### Core Components

- **app.py:** Main Flask application with route definitions and server configuration
- **code_analyzer.py:** Handles OpenAI API interactions and response parsing
- **prompt_templates.py:** Contains engineered prompts for different analysis types
- **schemas.py:** Pydantic models for request/response validation

### Frontend System

- **Technology:** Pure HTML5, CSS3, and Vanilla JavaScript
- **Styling:** Modern gradient design with responsive layout
- **Icons:** Font Awesome for visual elements
- **Responsive Design:** Mobile-first approach with flexbox and media queries

---

## ✨ Key Features

### 🔍 Analysis Types

#### 1. **Comprehensive Review**
- Overall code quality scoring (0-100)
- Detailed issue identification and categorization
- Quality metrics across five dimensions:
  - 📚 **Readability:** Code clarity and structure
  - 🔧 **Maintainability:** Long-term code sustainability
  - 🔒 **Security:** Vulnerability assessment
  - ⚡ **Performance:** Efficiency and optimization
  - 📝 **Documentation:** Code comments and clarity

#### 2. **Quick Feedback**
- Rapid analysis using GPT-3.5 Turbo
- 2-3 key improvement points
- Instant actionable suggestions
- Ideal for iterative development

#### 3. **Security Analysis**
- Comprehensive vulnerability assessment
- Security anti-pattern detection
- OWASP compliance checking
- Detailed remediation guidance

#### 4. **Performance Analysis**
- Bottleneck identification
- Algorithm complexity evaluation
- Optimization opportunities
- Resource usage analysis

### 🎨 User Experience

- **Real-time code editing** with syntax highlighting
- **Multiple programming language support** (11 languages)
- **Customizable review focus areas**
- **Interactive results display** with severity ratings
- **Export functionality** for review documentation
- **Responsive design** for desktop and mobile devices

---

## 💻 Supported Programming Languages

<table>
  <tr>
    <td>🐍 Python</td>
    <td>☕ Java</td>
    <td>🟨 JavaScript</td>
  </tr>
  <tr>
    <td>📘 TypeScript</td>
    <td>⚙️ C++</td>
    <td>🔵 C</td>
  </tr>
  <tr>
    <td>🟣 C#</td>
    <td>🐘 PHP</td>
    <td>💎 Ruby</td>
  </tr>
  <tr>
    <td>🔷 Go</td>
    <td>🦀 Rust</td>
    <td></td>
  </tr>
</table>

### 🎯 Review Focus Areas

- 🐛 **Bugs & Errors** - Logic issues and runtime errors
- 🔒 **Security Vulnerabilities** - Security flaws and threats
- ⚡ **Performance Issues** - Bottlenecks and inefficiencies
- 🎨 **Code Style** - Formatting and conventions
- ✅ **Best Practices** - Industry standards and patterns

---

## 🤖 AI Integration Details

### Prompt Engineering

The system uses sophisticated prompt templates with carefully crafted components:

#### **Expert Personas**
- 👨‍💻 Senior Software Engineer (15+ years experience)
- 🛡️ Cybersecurity Specialist
- ⚡ Performance Optimization Expert

#### **Structured Output**
- Enforced JSON response format for consistency
- Standardized scoring metrics (0-100 scale)
- Categorized issue tracking with severity levels

#### **Context Awareness**
- Language-specific best practices
- Focus area prioritization
- Balanced feedback (positive + constructive)

### Model Configuration

| Configuration | Value | Purpose |
|--------------|-------|---------|
| **Primary Model** | GPT-4 | Comprehensive analysis with deep insights |
| **Secondary Model** | GPT-3.5 Turbo | Quick feedback for rapid iteration |
| **Temperature** | 0.1 - 0.3 | Deterministic and consistent responses |
| **Max Tokens** | 1000 - 4000 | Varies based on analysis complexity |

---

## 🔌 API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | API information and welcome message |
| `/health` | GET | Service status and health check |
| `/review` | POST | Comprehensive code analysis (GPT-4) |
| `/quick-feedback` | POST | Rapid code feedback (GPT-3.5 Turbo) |
| `/security-analysis` | POST | Security-focused review |
| `/performance-analysis` | POST | Performance optimization suggestions |

### Request Format

```json
{
  "code": "your code here",
  "language": "python",
  "focus_areas": ["bugs", "security", "performance"]
}
```

### Response Format

```json
{
  "overall_score": 85,
  "summary": "Code analysis summary...",
  "issues": [
    {
      "severity": "high",
      "type": "security",
      "description": "Issue description...",
      "suggestion": "How to fix..."
    }
  ],
  "metrics": {
    "readability": 90,
    "maintainability": 85,
    "security": 75,
    "performance": 88,
    "documentation": 70
  }
}
```

---

## 🚀 Installation & Setup

### Prerequisites

Before you begin, ensure you have:

- ✅ **Python 3.8+** installed on your system
- ✅ **OpenAI API Key** ([Get one here](https://platform.openai.com/api-keys))
- ✅ **Modern web browser** (Chrome, Firefox, Safari, or Edge)
- ✅ **Git** for cloning the repository

### Quick Start Guide

#### Step 1: Clone the Repository

```bash
git clone https://github.com/Muhammad-Roshaan-Idrees/Code_Guardian.git
cd Code_Guardian
```

#### Step 2: Environment Configuration

1. Copy the `.env.example` file to create your `.env` file:
   ```bash
   # Windows
   copy .env.example .env
   
   # Linux/Mac
   cp .env.example .env
   ```

2. Open the `.env` file and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_actual_api_key_here
   FLASK_PORT=5000
   FLASK_ENV=development
   ```

#### Step 3: Backend Setup

```bash
# Navigate to project directory
cd project

# (Optional but recommended) Create a virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the Flask backend server
python app.py
```

The backend API will start on `http://localhost:5000`

#### Step 4: Frontend Access

Open a new terminal window:

```bash
# Navigate to project directory
cd project

# Start a simple HTTP server
python -m http.server 8000
```

The frontend will be available at `http://localhost:8000`

**Alternative:** Simply open `project/templates/index.html` directly in your browser.

#### Step 5: Verification

1. ✅ Check backend health: Open `http://localhost:5000/health` in your browser
2. ✅ Access the application: Open `http://localhost:8000` (or the HTML file directly)
3. ✅ The status indicator should show "Connected" if everything is working correctly

### 🐛 Troubleshooting

<details>
<summary><b>Issue: "OPENAI_API_KEY environment variable is required"</b></summary>

**Solution:** Ensure you've created the `.env` file in the root directory with your API key.
</details>

<details>
<summary><b>Issue: "Port already in use"</b></summary>

**Solution:** 
- For backend: Change `FLASK_PORT` in `.env` to a different port (e.g., 5001)
- For frontend: Use a different port: `python -m http.server 8001`
</details>

<details>
<summary><b>Issue: Frontend shows "Disconnected"</b></summary>

**Solution:** 
1. Verify backend is running on port 5000
2. Visit http://localhost:5000/health to confirm
3. Check browser console for CORS errors
</details>

For more detailed setup instructions, see [SETUP_GUIDE.md](SETUP_GUIDE.md).

---

## 🔒 Security Features

CodeGuardian implements multiple layers of security to protect your code and data:

### Security Measures

| Feature | Implementation | Purpose |
|---------|---------------|---------|
| **CORS Configuration** | Cross-Origin Resource Sharing | Controlled API access from authorized domains |
| **Input Validation** | Pydantic schemas | Request parameter sanitization and type checking |
| **Error Handling** | Graceful degradation | Prevents information leakage through error messages |
| **API Key Security** | Environment variables | Secure credential storage outside source code |
| **Rate Limiting** | Request throttling | Prevents abuse and excessive API usage |

### Best Practices

- 🔐 API keys are stored in environment variables, never in code
- 🚫 The `.gitignore` file prevents committing sensitive data
- ✅ All user inputs are validated before processing
- 🛡️ Error messages don't expose internal system details

---

## 📊 Performance Characteristics

| Metric | Value | Notes |
|--------|-------|-------|
| **Response Time** | 2-10 seconds | Depends on code complexity and analysis type |
| **Concurrent Users** | Single-threaded | Flask development server (production deployment recommended) |
| **Memory Usage** | Efficient | Optimized prompt handling and response parsing |
| **Scalability** | Modular | Architecture designed for easy horizontal scaling |

### Performance Tips

- Use **Quick Feedback** for faster results (GPT-3.5 Turbo)
- Use **Comprehensive Review** for detailed analysis (GPT-4)
- Optimize code snippets to < 500 lines for best results
- Consider batch processing for multiple files

---

## 🎨 User Experience Highlights

### Frontend Interface

- 🎨 **Clean, modern design** with gradient aesthetics
- ⏱️ **Real-time feedback** with loading indicators and progress bars
- 📱 **Responsive layout** optimized for desktop and mobile devices
- ✨ **Interactive elements** with smooth hover effects and animations
- 🌙 **Professional color scheme** with excellent contrast and readability

### Key User Flows

1. **Code Input** → Syntax highlighting and real-time validation
2. **Language Selection** → Dropdown with 11 programming languages
3. **Focus Area Customization** → Checkbox selection for targeted analysis
4. **AI Analysis** → Progress indication with status updates
5. **Results Display** → Structured output with severity ratings and color coding
6. **Export Functionality** → Download reviews as formatted documentation

---

## 🎓 Technical Innovations

CodeGuardian showcases several innovative approaches:

- **🧠 Advanced Prompt Framework** - Structured templates with expert personas for consistent AI responses
- **⚡ Multi-Model Strategy** - GPT-4 for depth and accuracy, GPT-3.5 for speed and efficiency
- **🔒 Type-Safe Validation** - Pydantic schemas ensure reliable data handling
- **🛡️ Graceful Degradation** - Fallback mechanisms maintain service during API issues
- **📊 Comprehensive Metrics** - Five-dimensional quality scoring system

---

## 🚀 Future Enhancements

### Planned Features

#### Phase 1: User Management
- 👤 **User Authentication** - Secure login and registration
- 📊 **Review History** - Track and revisit past analyses
- 🎯 **Personalized Recommendations** - AI learns from your preferences

#### Phase 2: Advanced Analysis
- 📦 **Batch Processing** - Analyze multiple files simultaneously
- 🔄 **Continuous Integration** - GitHub/GitLab integration
- 📁 **Project-wide Analysis** - Full repository scanning

#### Phase 3: Collaboration
- 👥 **Team Features** - Shared workspaces and collaborative reviews
- 💬 **Comments & Discussions** - Thread-based code conversations
- 📈 **Analytics Dashboard** - Team metrics and insights

#### Phase 4: Customization
- 📝 **Custom Rule Sets** - Organization-specific guidelines
- 🎨 **Custom Themes** - Branding and personalization
- 🔌 **Plugin System** - Extensible architecture

### Technical Roadmap

| Milestone | Features | Timeline |
|-----------|----------|----------|
| **v1.1** | Database integration, user preferences | Q1 2024 |
| **v1.2** | Caching layer, improved response times | Q2 2024 |
| **v2.0** | Microservices architecture, scalability | Q3 2024 |
| **v2.1** | WebSocket support, real-time features | Q4 2024 |

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Ways to Contribute

- 🐛 **Report Bugs** - Submit detailed issue reports
- 💡 **Suggest Features** - Share your ideas for improvements
- 📝 **Improve Documentation** - Help make docs clearer and more comprehensive
- 🔧 **Submit Pull Requests** - Contribute code improvements

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Contact & Support

- **Repository:** [github.com/Muhammad-Roshaan-Idrees/Code_Guardian](https://github.com/Muhammad-Roshaan-Idrees/Code_Guardian)
- **Issues:** [Report a bug or request a feature](https://github.com/Muhammad-Roshaan-Idrees/Code_Guardian/issues)
- **Documentation:** [Setup Guide](SETUP_GUIDE.md) | [TODO List](TODO.md)

---

## 🎉 Conclusion

**CodeGuardian** represents a significant advancement in automated code quality assessment. By leveraging state-of-the-art AI models with sophisticated prompt engineering, it provides developers with actionable insights that bridge the gap between automated linting and human code review.

### Why Choose CodeGuardian?

- ✅ **AI-Powered Intelligence** - Leverages GPT-4 for expert-level code reviews
- ✅ **Multi-Language Support** - Works with 11 popular programming languages
- ✅ **Comprehensive Analysis** - Covers security, performance, style, and best practices
- ✅ **Developer Friendly** - Clean UI, easy setup, and intuitive workflow
- ✅ **Open Source** - Free to use, modify, and extend

The modular architecture ensures maintainability and extensibility, while the user-friendly interface makes advanced code analysis accessible to developers of all skill levels. This project demonstrates the practical application of AI in software development workflows, offering tangible productivity improvements and code quality enhancements for development teams.

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ by the CodeGuardian Team

</div>
