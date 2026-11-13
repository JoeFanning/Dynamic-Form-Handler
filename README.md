# Dynamic Form Handler 📋⚡

A lightweight, backend application built to dynamically process, validate, and store different form submissions. Designed with **FastAPI** and backed by a **PostgreSQL** database on Render.

---

## 🚀 Features

* **Dynamic Submission Processing:** Accept and parse dynamic form structures without rigid schema constraints.
* **FastAPI Backend:** High-performance, asynchronous API framework with automatic interactive documentation.
* **PostgreSQL Database:** Secure, persistent storage for submissions using robust relational models.
* **Cloud-Ready:** Pre-configured for deployment platforms like Render.

---

## 🛠️ Tech Stack

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Python)
* **Database:** [PostgreSQL](https://www.postgresql.org/)
* **Server/Deployment:** [Uvicorn](https://pypi.org/project/uvicorn/), [Render](https://render.com/)

---

## 📦 Project Structure

├── main.py          # FastAPI app initialization and route registration

├── database.py      # SQLAlchemy engine, SessionLocal, and Base

├── models.py        # SQLAlchemy database models (e.g., FormSubmission)

└── crud.py          # Database query functions (Create, Read, Update, Delete)


**main.py**
(The Application Entrypoint)
What it does: Initializes the FastAPI application instance (app = FastAPI()), registers middleware, and hosts your API route handlers (endpoints like @app.get or @app.post).

Key responsibility: Acting as the traffic controller. It receives HTTP requests, calls the necessary functions from crud.py, validates data using schemas.py, and returns the final HTTP response to the client.

**database.py**
(The Connection Hub)
What it does: Initializes the database connection, configures the SQLAlchemy engine, and creates the session factory (SessionLocal).

Key responsibility: It also defines Base (which your database models inherit from) and provides the get_db() dependency generator function. This generator uses Python's yield statement to automatically handle opening a database session for a request and closing it when the request finishes—eliminating the need for manual try...finally blocks in your routes

**models.py**
(The Database Blueprint / ORM)
What it does: Defines your SQLAlchemy ORM (Object-Relational Mapping) models. These Python classes map directly to your database tables and columns (e.g., FormSubmission corresponding to a form_submissions table).

Key responsibility: Telling SQLAlchemy what your database schema looks like so it can translate Python code into SQL queries behind the scenes.

**crud.py**
(The Data Logic / Query Layer)
What it does: Stands for Create, Read, Update, Delete. This file contains pure database query functions (like get_all_submissions(db)) that interact with your session.

Key responsibility: Keeping database queries completely separate from your HTTP routing logic. If you need to fetch submissions from a background worker, a CLI script, or a different API endpoint, you can just call crud.get_all_submissions(db) instead of rewriting the query

## 🔗Links
(to see in browser current operational status or live status of Render backend engine: [https://dynamic-form-handler.onrender.com/](https://dynamic-form-handler.onrender.com/))

To see the Json contents of the Render database for all submitted forms: in your browser: https://dynamic-form-handler.onrender.com/api/submissions

To see a HTML version of the Render database for all submitted forms: https://joefanning.github.io/Dynamic-Form-Handler/all_forms_database_table.html

I also downloaded Dbeaver 26.2.4(https://dbeaver.io/download/) a free, open-source database management tool onto my computer to look at the database structure and information in detail on the same database on Render.

