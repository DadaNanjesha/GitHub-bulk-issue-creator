# 🚀 GitHub Issue Creator

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) 
[![Build Status](https://img.shields.io/github/actions/workflow/status/DadaNanjesha/GitHub-issue-creator/python-app.yml?branch=main)](https://github.com/DadaNanjesha/GitHub-issue-creator/actions)

### 📌 Automate your GitHub Issue creation effortlessly!

The **GitHub Issue Creator** is a Python-based tool designed to automate the process of creating GitHub issues in your repositories. Whether you're managing a personal project or a large open-source repository, this tool saves time and ensures that necessary tasks are tracked efficiently.

---

## 🧐 Why Use This?

✅ **Automate Repetitive Tasks** – Quickly create multiple issues at once.  
✅ **Customizable** – Modify issue templates to match your project needs.  
✅ **Seamless GitHub API Integration** – Automatically push issues to any repository.  
✅ **CSV File Integration** – Create issues faster using a CSV file.  
✅ **Open-Source & Community-Friendly** – Contribute, improve, and extend features!  

### 🚀 Ideal for:
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
```bash
git clone https://github.com/DadaNanjesha/GitHub-issue-creator.git
cd GitHub-issue-creator
```

### 📦 Install Dependencies
```bash
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
├── utils/                             # Utility scripts
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
   ```bash
   .env
   ```
2. Open `.env` and add your **GitHub repository** details and **personal access token**:
   ```env
   USERNAME=your_github_username
   REPO=your_repo_name
   TOKEN=your_github_token
   ```

### 2️⃣ **Run the Tool**
#### **Option 1: Create Issues from a List**
Execute the following command to generate issues from a predefined list:
```bash
python main_list.py
```
The script reads predefined issues from `issues/issues_list.py` and creates them automatically.

#### **Option 2: Create Issues from a CSV**
Execute the following command to generate issues from a CSV file:
```bash
python main_csv.py
```
---

### 📝 **CSV File Integration**

You can now create issues faster using a **CSV file**. Here’s the required structure for the CSV file:

#### **CSV File Structure**

| Column     | Description                                                                 | Example Value                                      |
|------------|-----------------------------------------------------------------------------|----------------------------------------------------|
| **title**  | The title of the issue.                                                     | `Set up initial project structure`                 |
| **body**   | The description of the issue.                                               | `Create the directory structure for the project...`|
| **labels** | A comma-separated list of labels (e.g., `"Backlog,Setup,Project Structure"`).| `"Backlog,Setup,Project Structure"`                |
| **assignee**| The GitHub username of the assignee (leave empty for no assignee).          | `DadaNanjesha`                                     |

#### **Example CSV File**

Save the following content as `issues.csv` in the root directory:

| title                                | body                                                                                       | labels                          | assignee      |
|--------------------------------------|--------------------------------------------------------------------------------------------|---------------------------------|---------------|
| Set up initial project structure     | Create the directory structure for the project, including `data/`, `scripts/`, and `tests/ folders`, and initialize a basic Python environment. | `"Backlog,Setup,Project Structure"` | DadaNanjesha  |
| Add API integration                  | Integrate the GitHub API to automate issue creation.                                       | `"Backlog,Feature,API Integration"` | DadaNanjesha  |

---

### **How to Use the CSV File**

1. Create a file named `issues.csv` in the root directory of the project.
2. Add your issues in the above format.
3. Run the following command to create issues from the CSV file:
   ```bash
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

## 💖 Sponsor This Project

If you find this project helpful, consider sponsoring it to support further development. Your sponsorship will help us:

- Add new features 🚀
- Improve documentation 📚
- Fix bugs 🐛
- Maintain the project 🛠️

👉 **[Sponsor this project](https://github.com/sponsors/DadaNanjesha)**

---

## 📜 License

This project is licensed under the **[MIT License](LICENSE)**.

---

## 📬 Contact

For any questions, issues, or feature requests, feel free to:  
- Open an issue in this repository 🛠️    

---

💡 **Star this repository** ⭐ 
if you find this project helpful!  

---

### 🔥 Key Improvements:

✅ **CSV File Integration** – Added support for creating issues faster using a CSV file.  
✅ **Sponsorship Section** – Encourages users to sponsor the project for further development.  
✅ **More engaging introduction** – Makes the project sound exciting and valuable.  
✅ **Clearer structure & formatting** – Uses emojis, sections, and highlights for better readability.  
✅ **More details on usage & contribution** – Helps first-time users get started quickly.  
✅ **Better "Why Use This?" section** – Explains the benefits concisely.  
✅ **Enhanced readability** – Proper code blocks, file structures, and bold text for clarity.  


---
### 🎯 Further development in pipeline
- Creating UI. 
- Optimization if required.
- Can include new features for better user experience.
---

🎯 Happy Coding! 🚀