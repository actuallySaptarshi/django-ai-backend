# Django AI Backend

<p align="center">
<img src="https://img.shields.io/badge/django-green?style=for-the-badge&logo=django" alt="Django" />
<img src="https://img.shields.io/badge/ollama-black?style=for-the-badge&logo=ollama" alt="Ollama" />
<img src="https://img.shields.io/badge/python-gold?style=for-the-badge&logo=python" alt="Python" />
</p>

A robust Django-based backend designed to power AI-driven applications. This project serves as a foundational boilerplate featuring a dedicated API for AI interactions, a homepage interface, and a custom Tailwind CSS theme. This project is intented to be used with a frontend framework (Eg: Flutter, React etc.) for the performance, features, security & reliability of Django alongwith a beautiful frontend library with the communications happening using REST Api.

## 📂 Project Structure

The project is organized into modular applications:

  * **`api/`**: Handles the RESTful API endpoints, likely serving as the interface for AI model interactions and data processing.
  * **`homepage/`**: Manages the frontend landing page and user-facing views.
  * **`theme/`**: Contains the frontend styling configuration, utilizing Tailwind CSS for a modern, responsive UI.
  * **`django_ai_backend/`**: The main project configuration directory (settings, URLs, WSGI).

## 🛠️ Tech Stack

  * **Framework:** Django
  * **API:** Django Rest Framework (DRF)
  * **Styling:** Tailwind CSS (via `django-tailwind`)
  * **Database:** SQLite (Default) / Extensible to PostgreSQL
  * **Language:** Python 3.x

## 🚀 Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

  * Python 3.8+ installed
  * Node.js & npm (required for Tailwind CSS generation)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/actuallySaptarshi/django-ai-backend.git
    cd django-ai-backend
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Python dependencies:**
    *(Note: If a `requirements.txt` is missing, install the core packages manually)*

    ```bash
    pip install django djangorestframework django-tailwind django-browser-reload
    ```

4.  **Install Tailwind CSS dependencies:**
    This project appears to use `django-tailwind`. You need to install the Node.js dependencies for the theme.

    ```bash
    python manage.py tailwind install
    ```

5.  **Apply Database Migrations:**

    ```bash
    python manage.py migrate
    ```

6.  **Create a Superuser (Optional):**

    ```bash
    python manage.py createsuperuser
    ```

## 🏃‍♂️ Usage

To run the development server, you will likely need two terminals if using Tailwind CSS (one for Django, one for the Tailwind watcher).

**Terminal 1: Django Server**

```bash
python manage.py runserver
```

Access the application at:

  * **Homepage:** `http://127.0.0.1:8000/`
  * **API Root:** `http://127.0.0.1:8000/api/`
  * **Admin Panel:** `http://127.0.0.1:8000/admin/`

Based on the code provided in `api/views.py`, here is a structured **API Usage** section for your README. It details how to interact with the Chat endpoint, manage conversation history, and handle the prerequisites.

-----

## 🔌 API Usage

This backend is designed to handle AI logic and chat storage, allowing frontend frameworks (React, Flutter, etc.) to integrate easily without managing the AI model connection directly.

**Base URL:** `http://127.0.0.1:8000/api/` (Default local development)

### 1\. AI Chat Endpoint (`http://127.0.0.1:8000/api/chat/`)

**Class:** `Chat`
**Method:** `POST`

This endpoint acts as a gateway to a local Ollama instance (defaulting to the `gemma3` model). It handles two scenarios: starting a new chat and continuing an existing one.

#### A. Start a New Conversation

To begin a new session, send the message history without an ID. The server will generate a unique `id` for tracking.

**Request:**

```json
{
    "messages": [
        {
            "role": "user",
            "content": "Hello, who are you?"
        }
    ]
}
```

**Response:**

```json
{
    "message": {
        "role": "assistant",
        "content": "I am an AI assistant powered by Gemma 3. How can I help you?"
    },
    "id": 1  // Save this ID to continue the conversation later
}
```

#### B. Continue a Conversation

To maintain context, include the `id` received from the previous response and append the full message history (including the AI's previous replies).

**Request:**

```json
{
    "id": 1,
    "messages": [
        {
            "role": "user",
            "content": "Hello, who are you?"
        },
        {
            "role": "assistant",
            "content": "I am an AI assistant powered by Gemma 3. How can I help you?"
        },
        {
            "role": "user",
            "content": "Can you help me write Python code?"
        }
    ]
}
```

**Response:**

```json
{
    "message": {
        "role": "assistant",
        "content": "Yes, I can certainly help you with Python code! What specifically do you need?"
    },
    "id": 1
}
```

### 2\. Test Endpoint (`http://127.0.0.1:8000/api/test/`)

**Class:** `Test`
**Method:** `POST`

A simple health-check endpoint to verify that the serializer is receiving data correctly.

**Request:**

```json
{
    "field1": "Test Data"
}
```

**Response:**

```json
{
    "message": "Data Recieved successfully",
    "Body": {
        "field1": "Test Data"
    }
}
```

-----

### ⚠️ Important Prerequisites

Ensure the following are set up before using the API:

1.  **Ollama Running Locally:** The view explicitly calls `http://localhost:11434/api/chat`. Ensure Ollama is installed and running on port 11434.

2.  **Model Availability:** The code is hardcoded to use the `gemma3` model. You must pull this model in your local Ollama instance:
    ```bash
    ollama pull gemma3
    ```

3.  **Changing Model:** You can change the model from `/api/views.py` in `chat_model`

## 🤝 Contributing

Contributions are welcome\! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Commit your changes (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature/YourFeature`).
5.  Open a Pull Request.

## 📄 License
<p align="center">
This project is open source (MIT License).
</p>
