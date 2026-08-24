# olmarkt

`olmarkt` is an early Python web application for a simple marketplace-style workflow. It uses server-rendered HTML templates, form handling, and MySQL-backed data access.

This repository is best viewed as an early portfolio project that shows Python web development basics and database connectivity. For job applications, it should sit behind stronger QA/data/API projects such as Lumina and future testing-focused repositories.

## Features

- Flask-style server-rendered pages
- User registration and login workflow
- Article/product creation and listing
- Search page for finding records by name
- MySQL database access through `pymysql`
- HTML templates and static assets

## Stack

- Python
- Flask
- PyMySQL
- bcrypt
- HTML/CSS templates
- MySQL

## Project Structure

```text
olmarkt/
├── main.py
├── mysql.py
├── db.py
├── config.py
├── requirements.txt
├── templates/
└── static/
```

## Configuration

Database credentials are read from environment variables in `config.py`.

Create a local `.env` or configure these variables in your hosting environment:

```text
OLMARKT_DB_HOST=your_database_host
OLMARKT_DB_USER=your_database_user
OLMARKT_DB_PASSWORD=your_database_password
OLMARKT_DB_NAME=your_database_name
```

Do not commit real database credentials or local `.env` files.

## Run Locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

A configured MySQL database is required for the app's database-backed routes.

## What This Demonstrates

- Python web application structure
- Template-based page rendering
- Basic authentication flow
- Form handling
- Database connection and query logic
- Repository hygiene improvements around credential handling

## Portfolio Notes

This project is useful as evidence of early Python/database practice, but it needs more polish before being a primary pinned repository. Recommended next improvements:

- Remove tracked `__pycache__` files from Git history/current branch
- Add tests for database helper functions where practical
- Add a schema or setup script for the expected MySQL tables
- Improve validation and error handling
- Replace global database config with a clearer application settings pattern
