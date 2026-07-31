# 🤖 AI Project Charter Generator

Generate professional AI-powered Project Charters in seconds using **Google Gemini AI** and **Streamlit**.

This application helps project managers, business analysts, startup teams, and students quickly generate structured Project Charters from a project name and description.

---

# 🌐 Live Demo

**Application:** https://ai-project-charter-generator.streamlit.app

> **Note:** This application is hosted on **Streamlit Community Cloud**. If it has been inactive for some time, the first visit may take **30–60 seconds** while the server wakes up. After that, the application loads normally.

---

# ✨ Features

- 🤖 AI-powered Project Charter generation using Google Gemini
- 📋 Professional PMBOK-inspired Project Charter structure
- 📄 Export generated charter as PDF
- ⚡ Clean and responsive Streamlit interface
- 🔒 Secure API key management using Streamlit Secrets
- ☁️ Cloud deployment with Streamlit Community Cloud

---

# 📌 Generated Project Charter Includes

- Project Overview
- Business Need
- Project Objectives
- Project Scope
- In Scope
- Out of Scope
- Key Stakeholders
- Major Deliverables
- Estimated Timeline
- Assumptions & Constraints
- Estimated Budget (ROM)
- Key Risks
- Project Manager Authority
- Success Criteria
- Sponsor Approval

---

# 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- ReportLab
- python-dotenv

---

# 📁 Project Structure

```text
AI-Project-Charter-Generator/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── assets/
└── .env (Local only)
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/gopichand-7/AI-Project-Charter-Generator.git
```

Move into the project directory

```bash
cd AI-Project-Charter-Generator
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install the required packages

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

For Streamlit deployment, add the following to **Streamlit Secrets**:

```toml
GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 💼 Use Cases

- Project Managers
- Business Analysts
- Product Managers
- Startup Teams
- Students
- PMO Teams
- Freelancers

---

# 🚀 Future Improvements

- DOCX Export
- Editable Generated Content
- Multiple Charter Templates
- Organization Branding
- Risk Matrix
- Timeline Visualization

---

# 👨‍💻 Author

**Gopichand Kollapattu**

GitHub: https://github.com/gopichand-7

---

# 📄 License

This project is licensed under the MIT License.
