# Technical Documentation: Job Platform Engine

**Project Repository:** [ManideepK007/job-platform](https://github.com/ManideepK007/job-platform)

-----

## 1\. Project Overview


The **Job Platform Engine** is a robust backend system designed to bridge the gap between job seekers and recruiters. It serves as a centralized hub for managing career opportunities, streamlining the application process, and providing a scalable infrastructure for professional networking.

This project exists to demonstrate a production-ready approach to handling relational data, user authentication, and multi-entity workflows within a modern web architecture.

-----

## 2\. Problem Statement

Traditional job boards often suffer from fragmented data management and high friction in the application pipeline. Recruiters struggle with disorganized applicant tracking, while candidates face a "black hole" during the application lifecycle.

This system addresses these issues by providing:

  * **Structured Data Integrity:** Ensuring job postings and applications maintain strict relational consistency.
  * **Scalable Architecture:** A modular design that allows for the addition of features like AI-driven matching or advanced analytics without re-engineering the core.

-----

## 3\. Key Features

  * **User Role Differentiation:** Distinct workflows for Job Seekers (profile/application management) and Recruiters (job posting/applicant tracking).
  * **Dynamic Job Lifecycle:** Real-time job posting, status updates, and archive capabilities.
  * **Application Tracking System (ATS):** Centralized dashboard for managing candidate statuses.
  * **Persistent Auth:** Secure session management for persistent user states.

-----

## 4\. System Architecture

The project follows the **Model-View-Controller (MVC)** architectural pattern, specifically utilizing the **Application Factory Pattern** in Flask. This ensures that the application is modular, testable, and capable of supporting multiple configurations (development, testing, production).

-----

## 5\. Core Logic / Workflow

1.  **Authentication Phase:** Users register and authenticate, with credentials securely hashed and sessions managed via Flask-Login.
2.  **Job Discovery/Creation:** \* *Recruiters* define job parameters (title, description, requirements) which are committed to PostgreSQL.
      * *Seekers* query the database for active listings.
3.  **Application Pipeline:** Users submit profiles against specific Job IDs. This creates a relational link in the `applications` table.
4.  **Feedback Loop:** Recruiters update application statuses, triggering state changes visible to the seeker.

-----

## 6\. Tech Stack

| Technology | Role | Selection Justification |
| :--- | :--- | :--- |
| **Language:** Python 3.13 | Core Language | Chosen for its extensive ecosystem and rapid development capabilities. |
| **Framework:** Flask | Web Framework | A micro-framework that offers high flexibility and modularity for building RESTful services. |
| **Database:** PostgreSQL | Database | Provides ACID compliance and superior handling of complex relational data. |
| **ORM/ODM:** SQLAlchemy | ORM | Abstracts raw SQL, preventing injection vulnerabilities and simplifying data modeling. |
| **Architecture:** Flask-Migrate | Versioning | Handles database schema migrations (Alembic) without data loss. |

-----

## 7\. Database Design

The schema is built on a relational foundation to ensure that deletions (e.g., a recruiter deleting a profile) are handled via cascading rules or protected constraints.

  * **Users Table:** Stores hashed credentials, roles (Seeker/Recruiter), and metadata.
  * **Jobs Table:** Stores job metadata, linked to a specific Recruiter ID.
  * **Applications Table:** A junction table linking `UserID` to `JobID`, storing the status and timestamp of the application.

-----

## 8\. Folder Structure Overview

```bash
job-platform/
├── app/
│   ├── models.py          # SQLAlchemy Schema Definitions
│   ├── routes.py          # View Controllers & API Endpoints
│   ├── auth/              # Authentication Logic & Blueprints
│   └── templates/         # UI Layouts (if SSR is used)
├── migrations/            # DB Schema version control
├── config.py              # Environment & App configurations
├── main.py                # WSGI Entry Point
└── requirements.txt       # Dependency Manifest
```

-----

## 9\. Setup & Installation Guide

1.  **Environment Setup:**
    ```bash
    python -m venv venv
    source venv/bin/activate  (or if it is on Windows:) venv\Scripts\activate
    pip install -r requirements.txt
    ```
2.  **Database Configuration:**
    Ensure PostgreSQL is running and update the `SQLALCHEMY_DATABASE_URI` in your `.env` or `config.py`.
3.  **Migrations:**
    ```bash
    flask db upgrade
    ```
4.  **Execution:**
    ```bash
    python main.py
    ```

-----

## 10\. Edge Cases & Error Handling

  * **Database Connection Failure:** The app uses a global error handler to catch connection timeouts and provide a user-friendly 503 error.
  * **Unauthorized Access:** Decorators protect Recruiter-only routes, redirecting unauthorized seekers to the login portal.
  * **Duplicate Applications:** Unique constraints prevent a single user from applying to the same job multiple times.

-----

## 11\. Limitations

  * **Real-time Notifications:** Current status updates require a page refresh.
  * **File Storage:** Resume uploads are stored locally rather than in a cloud bucket (S3), limiting horizontal scalability.

-----

## 12\. Future Improvements

  * **Search Optimization:** Implementation of Elasticsearch for full-text job searching.
  * **Containerization:** Dockerizing the application for consistent deployment across environments.
  * **API Layer:** Moving toward a decoupled Vue.js/React frontend utilizing a JWT-based REST API.

-----