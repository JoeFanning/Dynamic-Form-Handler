# Dynamic Form Handler 📋⚡

A lightweight, robust backend application built to dynamically process, validate, and store different form submissions. Designed with **FastAPI** and backed by a **PostgreSQL** database.

---

## 🚀 Features

* **Dynamic Submission Processing:** Accept and parse dynamic form structures without rigid schema constraints.
* **FastAPI Backend:** High-performance, asynchronous API framework with automatic interactive documentation.
* **PostgreSQL Database:** Secure, persistent storage for submissions using robust relational models.
* **Cloud-Ready:** Pre-configured for deployment platforms like Render.

---

## 🛠️ Tech Stack

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Python)
* **Database:** PostgreSQL
* **Server/Deployment:** Uvicorn, Render

---

## 📦 Project Structure

```text
├── main.py               # Application entry point & FastAPI setup
├── requirements.txt      # Python dependencies
├── index.html            # A sample form to use on your website or connect to it here using url
└── README.md             # Project documentation


(to see in browser current operational status or live status of Render backend engine: https://dynamic-form-handler.onrender.com/)

(to see in browser contents of the database on Render: https://dynamic-form-handler.onrender.com/api/submissions)

I also downloaded Dbeaver 26.2.4(https://dbeaver.io/download/) a free, open-source database management tool onto my computer to look at the database structure and information in detail on the same database on Render.
