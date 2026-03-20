# FOSS Logic Engine – Intelligent Open Source Tool Recommender

---

## 🌍 Why This Project Exists (The Story)

While working on different projects, we often faced a common problem — choosing the right tool. There are thousands of free and open-source tools available, but finding the one that matches both the task and the user’s skill level is confusing and time-consuming.

Beginners often pick tools that are too complex, while experienced users sometimes end up using tools that limit their capabilities. This gap between **user needs and tool selection** inspired me to build a system that can guide users intelligently.

FOSS Logic Engine was created to simplify this decision-making process by recommending the most suitable open-source tool based on what the user wants to do and how experienced they are.

---

## 📌 Overview

FOSS Logic Engine is a full-stack web application that helps users discover the most suitable free and open-source software (FOSS) based on their requirements and experience level.

It acts as a **decision-making assistant**, reducing confusion and helping users quickly find the right tool.

---

## 🎯 Problem Statement

Users struggle to:
- Identify the right tool for their task
- Balance simplicity vs advanced features
- Navigate the overwhelming number of available tools

---

## 🧠 Solution Approach

The system uses a structured **decision-based recommendation model**:

1. User selects:
   - Genre (task type)
   - Difficulty level
2. System queries MongoDB dataset
3. Matches tools based on:
   - Exact genre
   - Closest difficulty level
4. Returns the best possible recommendation

---

## ⚙️ Tech Stack

### Backend
- FastAPI (Python)
- MongoDB
- Pydantic

### Frontend
- HTML
- CSS (Modern UI)
- JavaScript (Fetch API)

### Tools
- Uvicorn
- Git & GitHub

---


