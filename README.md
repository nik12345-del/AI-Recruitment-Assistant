# 🤖 AI Recruitment Assistant

An AI-powered Recruitment Assistant built using **Streamlit**, **Groq LLM**, **FAISS**, and **Sentence Transformers**. This application helps job seekers improve their resumes, discover suitable jobs, prepare for interviews, and receive personalized career guidance through an intelligent AI assistant.

---

## 🚀 Features

- 📄 Resume Analysis (ATS Score)
- 🎯 Job Description Matching
- 💼 AI-Based Job Recommendation
- 🛠 Skill Gap Analysis
- 📚 Personalized Learning Roadmap
- 💡 AI Project Recommendations
- 🎤 Interview Question Generator
- 📝 Resume Improvement Suggestions
- 🔍 Semantic Search using FAISS
- 🤖 Groq LLM Integration
- 📊 Interactive Dashboard with Streamlit

---

## 🛠 Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI & NLP
- Groq API
- Llama 3.3 70B Versatile
- Sentence Transformers
- FAISS
- Transformers

### Data Processing
- Pandas
- NumPy
- Scikit-learn

### Visualization
- Plotly
- Matplotlib

### Document Processing
- PyMuPDF
- Python-docx

---

## 📂 Project Structure

```
AI-Recruitment-Assistant/
│
├── app.py
├── requirements.txt
├── .env
│
├── utils/
│   ├── resume_parser.py
│   ├── resume_analyzer.py
│   ├── job_matcher.py
│   ├── project_recommender.py
│   ├── interview_generator.py
│   ├── learning_path.py
│   └── vector_store.py
│
├── data/
│
├── assets/
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/nik12345-del/AI-Recruitment-Assistant.git
```

```bash
cd AI-Recruitment-Assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a **.env** file

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## ☁️ Deployment

### Streamlit Community Cloud
1. Create a new app at https://streamlit.io/cloud.
2. Connect your GitHub repo.
3. Set the app path to `app.py`.
4. Add a secret for `GROQ_API_KEY` in the Cloud settings.
5. Deploy.

### Heroku
1. Install the Heroku CLI.
2. Run:

```bash
heroku login
heroku create your-app-name
git push heroku main
```

3. Set the environment variable:

```bash
heroku config:set GROQ_API_KEY=YOUR_API_KEY
```

4. Open the app:

```bash
heroku open
```

> Note: The repo already includes `Procfile`, `runtime.txt`, and `.streamlit/config.toml` for Heroku/Streamlit deployment.

---

## 🧠 How It Works

1. Upload Resume
2. Enter Job Description
3. AI extracts resume information
4. Resume is compared with Job Description
5. ATS Score is generated
6. Missing skills are identified
7. Personalized project recommendations are generated
8. AI suggests interview questions
9. Learning roadmap is created

---

## 📈 Future Enhancements

- User Authentication
- Resume Builder
- PDF Report Generation
- Recruiter Dashboard
- Candidate Ranking System
- Company Recommendation Engine
- Voice-based Interview Assistant
- Multi-language Support

---

## 📸 Screenshots

> Add screenshots of your application here.

Example:

```
screenshots/
│
├── home.png
├── ats_score.png
├── recommendations.png
└── interview_questions.png
```

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 👩‍💻 Author

**Nikita Dubey**

B.Tech – Artificial Intelligence & Data Science

Yeshwantrao Chavan College of Engineering, Nagpur

GitHub:
https://github.com/nik12345-del

---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

---

## 📄 License

This project is developed for educational and research purposes.
