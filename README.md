# Dynamic Form Handler 📋⚡

A lightweight, backend application built to dynamically process, validate, and store different form submissions. Designed with **FastAPI** and backed by a **PostgreSQL** database.

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
│
├── main.py          # FastAPI app initialization and route registration
├── database.py      # SQLAlchemy engine, SessionLocal, and Base
├── models.py        # SQLAlchemy database models (e.g., FormSubmission)
├── schemas.py       # Pydantic models for request/response validation
└── crud.py          # Database query functions (Create, Read, Update, Delete)

**database.py** (The Connection Hub)
What it does: Initializes the database connection, configures the SQLAlchemy engine, and creates the session factory (SessionLocal).

Key responsibility: It also defines Base (which your database models inherit from) and provides the get_db() dependency generator function. This generator uses Python's yield statement to automatically handle opening a database session for a request and closing it when the request finishes—eliminating the need for manual try...finally blocks in your routes

models.py (The Database Blueprint / ORM)
What it does: Defines your SQLAlchemy ORM (Object-Relational Mapping) models. These Python classes map directly to your database tables and columns (e.g., FormSubmission corresponding to a form_submissions table).

Key responsibility: Telling SQLAlchemy what your database schema looks like so it can translate Python code into SQL queries behind the scenes.


(to see in browser current operational status or live status of Render backend engine: https://dynamic-form-handler.onrender.com/)

(to see in browser contents of the database on Render: https://dynamic-form-handler.onrender.com/api/submissions)

I also downloaded Dbeaver 26.2.4(https://dbeaver.io/download/) a free, open-source database management tool onto my computer to look at the database structure and information in detail on the same database on Render.
