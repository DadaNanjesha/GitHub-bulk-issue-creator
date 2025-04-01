# 🚀 GitHub Issue Creator

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) 
[![Build Status](https://img.shields.io/github/actions/workflow/status/DadaNanjesha/GitHub-issue-creator/python-app.yml?branch=main)](https://github.com/DadaNanjesha/GitHub-issue-creator/actions)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://create-bulk-issues-on-git.streamlit.app/)
[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-%E2%9D%A4-red)](https://github.com/sponsors/DadaNanjesha)

### 📌 Automate your GitHub Issue creation effortlessly!

Tired of manually creating GitHub issues? The **GitHub Issue Creator** is a Python-based tool designed to automate this process, saving you valuable time and ensuring efficient task tracking. Whether you're managing a personal project or a large open-source repository, this tool is your go-to solution.

✨ **Explore the App:** [Try Live Demo](https://create-bulk-issues-on-git.streamlit.app/) ✨ - Try it out now on Streamlit! 

#### Note : If you are using the Streamlit App, Please provide your GitHub credentials in the sidebar and token with complete access.
---

## 🚀 Features

<div class="features-grid">

✅ **CSV Bulk Upload** - Create 100+ issues in minutes  
✅ **CLI Interface** - Perfect for CI/CD pipelines  
✅ **Template Support** - Predefined issue structures  
✅ **GitHub API v3** - Secure integration  
✅ **Label Management** - Comma-separated tags  
✅ **Open Source** - MIT Licensed  

</div>

### 🌟 Ideal for:
- Setting up **project structures** 📁
- Writing **unit tests** 🧪
- Automating **CI/CD pipelines** ⚙️
- Managing **API integrations** 🌐
- Handling **documentation tasks** 📝

---

## 🛠️ Installation Guide

### 📌 Prerequisites
Ensure you have:
- **Python 3.6+** → [Download Python](https://www.python.org/downloads/)
- **Git** → [Download Git](https://git-scm.com/downloads)

### 📥 Clone the Repository
```
git clone https://github.com/DadaNanjesha/GitHub-issue-creator.git
cd GitHub-issue-creator
```

### 📦 Install Dependencies
```
pip install -r requirements.txt
```
---

## 📂 Project Structure

```
GitHub-issue-creator/                  # Root directory
│
├── config/                            # Configuration files
│   └── config.py                      # GitHub repository settings & authentication
│
├── issues/                            # Predefined issue templates
│   ├── issues_list.py                 # List of issues to be created
│
├── tests/                             # Unit tests
│   └── test_github_api.py             # Test cases for GitHub API integration
│
├── utils/                             # Utility scripts.
│   └── github_api.py                  # GitHub API interaction functions
│
├── main_csv.py                        # Script for CSV-based API issue creation
├── main_list.py                       # Script for list-based API issue creation
├── .env                               # environment variables file
├── requirements.txt                   # List of dependencies
└── README.md                          # Project documentation

```

---

## 🚀 Usage

### 1️⃣ **Set Up Configuration**
1. Place file in root directory as shown below:
   ```
   .env
   ```
2. Open `.env` and add your **GitHub repository** details and **personal access token**:
   ```
   USERNAME=your_github_username
   REPO=your_repo_name
   TOKEN=your_github_token
   ```

### 2️⃣ **Run the Tool**
#### **Option 1: Create Issues from a List**
Execute the following command to generate issues from a predefined list:
```
python main_list.py
```
The script reads predefined issues from `issues/issues_list.py` and creates them automatically.

#### **Option 2: Create Issues from a CSV**
Execute the following command to generate issues from a CSV file:
```
python main_csv.py
```
---

### 📝 **CSV File Integration**

You can now create issues faster using a **CSV file**. Here’s the required structure for the CSV file:

### 📝 CSV Format Guide

| Column     | Required | Description                | Example                      |
|------------|----------|----------------------------|------------------------------|
| **title**  | ✅ Yes    | Issue title                | `Fix login page UI bug`      |
| **body**   | ✅ Yes    | Detailed description       | `Update button colors...`    |
| **labels** | ✅ Yes    | Comma-separated tags       | `bug,ui,high-priority`       |
| **assignee**| ❌ No     | GitHub username            | `DadaNanjesha`  

### **How to Use the CSV File**

1. Create a file named `issues.csv` in the root directory of the project.
2. Add your issues in the above format.
3. Run the following command to create issues from the CSV file:
   ```
   python main_csv.py
   ```

---

## 🤝 **Open-Source & Community-Friendly**

🎉 welcome contributions from the community! Follow these steps to contribute:

1. **Fork the Repository**  
2. **Create a Feature Branch** (`git checkout -b feature-branch`)  
3. **Commit Your Changes** (`git commit -m "Added new feature"`)  
4. **Push to Your Branch** (`git push origin feature-branch`)  
5. **Open a Pull Request** 🚀  

💡 If you're planning major changes, **open an issue first** to discuss your proposal.

---
## 📜 License

This project is licensed under the **[MIT License](LICENSE)**.

---

## 📬 Contact

For any questions, issues, or feature requests, feel free to:  
- Open an issue in this repository 🛠️    

---

### 🔥 Key Improvements:

✅ **Streamlit App Integration** - Try the app directly via the new link!
✅ **CSV File Integration** – Added support for creating issues faster using a CSV file.  
✅ **Sponsorship Section** – Encourages users to sponsor the project for further development.  
✅ **More engaging introduction** – Makes the project sound exciting and valuable.  
✅ **Clearer structure & formatting** – Uses emojis, sections, and highlights for better readability.  
✅ **More details on usage & contribution** – Helps first-time users get started quickly.  
✅ **Better "Why Use This?" section** – Explains the benefits concisely.  
✅ **Enhanced readability** – Proper code blocks, file structures, and bold text for clarity.  

---
### 🎯 Further development in pipeline
- Customizing the UI. 
- Optimization if required.
- Can include new features for better user experience.
---

## **[🤝 Support This Project ](https://github.com/sponsors/DadaNanjesha)** 

If you find this project helpful, consider sponsoring it to support further development:

- Add new features 🚀
- Improve documentation 📚
- Fix bugs 🐛
- Maintain the project 🛠️

---
<div align="center"> <h3>⭐ Star This Repository</h3> <p>If you find this project useful, please consider starring it and also you can 💖 Sponsor!</p>
🎯 Happy Coding! 🚀
</div> 

