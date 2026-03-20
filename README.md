# FOSS Logic Engine – Intelligent Open Source Tool Recommender

---

## 🌍 Why This Project Exists (The Story)

As a student exploring different domains like coding, design, machine learning, and development, I often faced a recurring problem — choosing the right tool. Every time I started something new, I would spend hours searching online, comparing tools, reading blogs, and still feel unsure about what to pick.

Sometimes the tools I chose were too advanced for me, and I ended up feeling stuck. Other times, I picked very basic tools that limited my learning and growth. This constant confusion made me realize that the real problem was not the lack of tools, but the lack of guided decision-making.

I noticed that many students like me face the same issue. We don’t need more tools — we need the right tool at the right time, based on our skill level and goal.

That’s why I decided to build this project.

Instead of solving a random problem, I chose this because it directly impacts how students learn, build, and grow. This system acts like a simple assistant that understands what a user wants to do and recommends the most suitable open-source tool.

Through this project, I wanted to create something practical, scalable, and meaningful — a system that reduces confusion and helps people focus on learning and creating, rather than getting stuck at the starting point.

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


