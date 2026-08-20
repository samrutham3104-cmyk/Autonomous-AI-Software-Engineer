# 🤖 Autonomous AI Software Engineer

A Python-based multi-agent software engineering platform that automates multiple stages of the software development lifecycle.

## 🚀 Overview

The system takes a software requirement from a user and processes it through a sequence of specialized agents:

User Requirement
↓
🧠 Planner Agent
↓
🏗️ Architect Agent
↓
💻 Coding Agent
↓
🧪 Testing Agent
↓
🔍 Review Agent
↓
🔧 Repair Agent
↓
🛡️ Security Agent
↓
✅ Verification Agent
↓
📦 Generated Project

## ✨ Features

- 🧠 Automated project planning
- 🏗️ Software architecture generation
- 💻 Automated project generation
- 🧪 Automated pytest testing
- 🔍 Static code review
- 🔧 Basic automated code repair
- 🛡️ Security scanning
- ✅ Final project verification
- 🔗 End-to-end agent orchestration

## 🧩 Agents

### 🧠 Planner Agent
Converts the user's requirement into a development plan.

### 🏗️ Architect Agent
Creates the proposed software architecture and project structure.

### 💻 Coding Agent
Generates the initial project structure and source files.

### 🧪 Testing Agent
Runs automated tests using pytest.

### 🔍 Review Agent
Performs static analysis of Python source code.

### 🔧 Repair Agent
Applies controlled automatic repairs to detected issues.

### 🛡️ Security Agent
Scans source code for common security risks.

### ✅ Verification Agent
Combines testing, review, security, and project-structure results into a final verification status.

## 🛠️ Technology Stack

- Python
- OpenAI API
- Pytest
- Python AST
- Regular Expressions
- Multi-Agent Architecture
- Git & GitHub

## 📁 Project Structure

```text
Autonomous-AI-Software-Engineer/
│
├── main.py
├── planner_agent.py
├── architect_agent.py
├── coder_agent.py
├── testing_agent.py
├── review_agent.py
├── repair_agent.py
├── security_agent.py
├── verification_agent.py
│
├── generated_projects/
├── requirements.txt
├── README.md
├── .gitignore
└── .env