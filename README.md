 #ai Knowledge Assistant

This is a Django-based backend system for an AI-powered Knowledge Assistant. It provides a secure REST API for managing articles and questions and integrates with OpenAI to answer questions based on existing knowledge.

---

##  Features

- JWT Authentication
-  Article and Question Management (CRUD)
-  Ask Questions using OpenAI API (gpt-3.5-turbo)
- Search, Filter, and Pagination
- PostgreSQL 
- Role-based Permissions

---

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Auth**: Simple JWT
- **AI Integration**: OpenAI GPT
- **Database**: PostgreSQL (Prod)
- **Filtering**: django-filter
- **Pagination**: Custom + DRF Pagination

---

##  Setup Instructions

### 1. Clone the project

```bash
git clone https://github.com/nada232/ai-knowledge-assistant.git
cd ai-knowledge-assistant/backend
```

### 2. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```


### 4. Create `.env` file

Create a `.env` file in the root of the `backend/` folder:

```env
SECRET_KEY=your-django-secret-key
OPENAI_API_KEY=your-openai-api-key

DB_NAME=knowledge_db
DB_USER=nada
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (for Admin access)

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

---

## API Endpoints

### Auth

- `POST /api/auth/token/` – Get access and refresh token

### Articles

- `GET /api/articles/` – List articles
- `POST /api/articles/` – Create article (authenticated)
- `GET /api/articles/?search=keyword` – Search in title/content/tags
- `GET /api/articles/?tags=AI` – Filter by tags
- `GET /api/articles/?page=2` – Pagination

### Questions

- `POST /api/ask/` – Ask a question and get AI response (authenticated)
- `GET /api/stats/` – Get article/question stats + recent questions

