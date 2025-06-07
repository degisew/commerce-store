# Commerce Store

<div align="center">

<!-- ![Project Logo](https://via.placeholder.com/150x150/0066cc/ffffff?text=LOGO) -->

**A back-end e-commerce API built with Python, Django, and PostgreSQL.**

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.x-green.svg)](https://djangoproject.com)
[![Docker](https://img.shields.io/badge/Docker-20.10+-blue.svg)](https://docker.com)

**Contact**: [degisew.mengist21@gmail.com](mailto:degisew.mengist21@gmail.com) | [LinkedIn](https://linkedin.com/in/degisew-mengist)

</div>

## Overview

A back-end e-commerce API built with Python, Django, and PostgreSQL. It includes endpoints for creating, retrieving, updating, and deleting products, as well as for managing orders, customers, carts, and their items.

**Key Features**:

- Secure JWT authentication and role-based access control.
- Containerized deployment with Docker.
- Products Catalog management.
- Shopping Cart and Orders management.

<!-- **Links**:

- **Portfolio**: [Portfolio](https://degisew-portfolio.netlify.com)
- **GitHub**: [GitHub](https://github.com/degisew)
- **LinkedIn**: [LinkedIn](https://linkedin.com/in/degisew-mengist) -->

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [API Reference](#api-reference)
- [Architecture](#architecture)
  <!-- - [Testing](#testing) -->
- [Deployment](#deployment)

## Quick Start

```bash
# Clone the repo
git clone https://github.com/degisew/commerce-store.git
cd commerce-store

# Run with Docker
docker-compose up --build

# OR run locally
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements/dev.txt
python manage.py runserver
```

**Access**: [http://localhost:8000/api/v1/docs](http://localhost:8000/api/v1/docs) for API docs.

## Project Structure

```bash
├── apps/                 # Custom Apps collection
├── config/               # Project Configurations
├── docker
│     └── dev/
│          └── Dockerfile # Django API Dockerfile for development environment
├── docs/                 # Documentation files
├── requirements/         # requirements.txt files collection
├── .env                  # Environment variables (you will create this)
├── compose.yaml          # Docker Compose configuration file
└── README.md             # This README file
```

## Setup

<details>
<summary><strong>Show Setup Details</strong></summary>

### Prerequisites

- Python 3.10+
- Docker 20.10+ & Docker Compose 1.29+
- PostgreSQL 14+ (for local setup)
- Git 2.30+

### Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/degisew/commerce-store.git
   cd commerce-store
   ```

2. **Configure Environment**:

   ```bash
   Create a .env file with-in your root project directory and store secure values.
   ```

   Example `.env`:

   ```bash
   # Database
   POSTGRES_USER=your_db_user
   POSTGRES_PASSWORD=your_db_password
   POSTGRES_DB=your_db_name

   # Django
   SECRET_KEY=your_secret_key
   DB_USER=your_database_user

   # Optional: pgAdmin
   PGADMIN_DEFAULT_EMAIL=admin@example.com
   PGADMIN_DEFAULT_PASSWORD=your_pgadmin_password
   ```

3. **Run the Application**:
   - **Docker (Recommended)**:

     ```bash
     docker-compose up --build
     ```

   - **Local Development**:

     ```bash
     python -m venv venv
     source venv/bin/activate
     pip install -r requirements/dev.txt
     python manage.py runserver
     ```

4. **Access Services**:
   - API: [http://localhost:8000](http://localhost:8000)
   - API Docs: [http://localhost:8000/api/v1/docs](http://localhost:8000/api/v1/docs)
   - pgAdmin (if included): [http://localhost:8001](http://localhost:8001)

</details>

## API Reference

<details>
<summary><strong>Show API Reference</strong></summary>

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/store/products` | GET | List all available products |
| `/api/v1/core/users` | GET | List Registered accounts |
| `/api/v1/store/collections` | GET | List all Product Categories |


**Full Docs**: [http://localhost:8000/api/v1/docs](http://localhost:8000/api/v1/docs)

</details>

## Architecture

**Tech Stack**:

- **Backend**: Django, and Django Rest Framework for RESTful APIs
- **Database**: PostgreSQL
- **DevOps**: Docker, Docker-compose

<!-- ## Testing

<details>
<summary><strong>Show Testing Details</strong></summary>

```bash
# Run tests With coverage
docker compose exec api pytest

- 85%+ test coverage with `pytest` and `coverage.py`.
- Includes unit tests (models, utilities) and integration tests (API endpoints).
```

</details> -->

## Deployment

<details>
<summary><strong>Show Deployment Details</strong></summary>

### Production

```bash

# Run with Docker Compose
docker-compose -f compose.prod.yaml up -d
```

### Environment Variables

```bash
DB_USER=your_database_user
REDIS_URL=redis://host:6379/0
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=your-domain.com
```

</details>

## License

MIT License. See [LICENSE](LICENSE).

<div align="center">

**⭐ Star this repo if you found it useful!**

Built by [Degisew Mengist](https://github.com/degisew)

[⬆ Back to Top](#commerce-store)

</div>
