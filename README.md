# ESN Vote System

A lightweight, secure, and anonymous voting system built for my student association (ESN ULB Brussels).

## 🔍 Overview

ESN Vote System lets you:
- Run internal votes with strong anonymity guarantees
- Use public/private key cryptography to ensure one vote per person
- Dynamically open/close votes and visualize results in real time
- Prevent double voting and preserve voter privacy

## 🧠 Motivation

As Communication Manager at ESN ULB, I realized that most voting platforms were paid or lacked transparency. Inspired by a recent cryptography course, I built this tool to offer a free, secure, and open-source alternative adapted to our needs.

## ⚙️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Security:** Python cryptography library (key generation, signature verification)
- **Containerization:** Docker
- **Visualization:** Chart.js

## 🚀 How to Run

```bash
git clone https://github.com/yourusername/esn-vote-system
cd esn-vote-system
docker-compose up --build
