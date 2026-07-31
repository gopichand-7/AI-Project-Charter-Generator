# 🤖 AI Project Charter Generator

An AI-powered Project Charter Generator built with **Streamlit** and **Google Gemini**. This application helps project managers, business analysts, students, and professionals generate structured, professional-quality project charters in seconds.

---

## 🚀 Features

- ✨ AI-powered Project Charter generation using Google Gemini
- 📋 Professional PMBOK-inspired charter structure
- 📄 Export as Markdown (.md)
- 📑 Export as professionally formatted multi-page PDF
- 🗓️ Automatic current date generation
- 🎯 Covers all key project charter sections
- ⚡ Clean and interactive Streamlit interface

---

## 📌 Project Charter Includes

- Project Overview
- Business Need
- Project Objectives
- Project Scope
- In Scope
- Out of Scope
- Key Stakeholders
- Major Deliverables
- High-Level Timeline
- Assumptions & Constraints
- Estimated Budget (ROM)
- Risks & Mitigation
- Project Manager & Authority
- Success Criteria
- Sponsor Approval

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- ReportLab
- python-dotenv

---

## 📂 Project Structure

```
AI-Project-Charter-Generator/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── .env (not included)
└── assets/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/gopichand-7/AI-Project-Charter-Generator.git
```

Go to the project directory

```bash
cd AI-Project-Charter-Generator
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📷 Screenshots

Add screenshots of your application inside the `assets` folder and reference them here.

Example:

```markdown
![Home Screen](assets/home.png)

![Generated Charter](assets/result.png)

![PDF Export](assets/pdf.png)
```

---

## 🎯 Use Cases

- Project Managers
- Business Analysts
- Students
- Startups
- Product Managers
- Freelancers
- PMO Teams

---

## 🌟 Future Improvements

- DOCX Export
- Multiple Charter Templates
- Editable Generated Content
- Organization Branding
- Risk Matrix
- Timeline Visualization

---

## 👨‍💻 Author

**Gopichand Kollapattu**

GitHub: https://github.com/gopichand-7

---

## 📜 License

This project is licensed under the MIT License.
