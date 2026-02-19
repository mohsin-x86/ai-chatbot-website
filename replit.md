# replit.md

## Overview

This is a simple AI Customer Support Chatbot built with Flask (Python). It provides a web-based chat interface where users can type messages and receive automated responses based on keyword matching. Chat history is persisted to a SQLite database. The bot handles basic queries about pricing, services, and contact information using rule-based logic (no AI/ML models involved).

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend (Flask / Python)
- **`app.py`** — The main entry point. Runs a Flask web server on port 5000 with two routes:
  - `GET /` — Serves the chat UI (HTML page)
  - `POST /chat` — Accepts a JSON body with a `message` field, passes it to the chatbot logic, saves the exchange to SQLite, and returns the bot's response as JSON.
- **`chatbot_logic.py`** — Contains the `get_response()` function which uses simple keyword matching (if/elif) to generate responses. There is no NLP, ML, or external AI API involved. This is the main place to expand bot intelligence.

### Frontend
- **`template/index.html`** — Single-page chat interface with vanilla HTML/CSS/JavaScript. Uses `fetch()` to POST messages to `/chat` and appends responses to the chat box.
  - **Known issue:** The template directory is named `template/` but Flask expects `templates/` (plural) by default. This will cause a runtime error unless corrected or Flask is configured with `template_folder='template'`.
  - **Known issue:** The Enter key event listener is attached inside `sendMessage()`, which means it gets re-attached on every send. It should be moved outside the function.
- **`static/style.css`** — Basic styling for the chat container and message display.

### Data Storage
- **SQLite** (`database.db`) — Used to persist chat history. The `chats` table has two columns:
  - `user` (TEXT) — The user's message
  - `bot` (TEXT) — The bot's response
- The table is created on-the-fly with `CREATE TABLE IF NOT EXISTS` inside `save_message()`. There is no migration system or ORM.

### Key Architectural Decisions
1. **Rule-based responses over AI/ML**: Simple keyword matching keeps the project lightweight with zero external API dependencies. The tradeoff is very limited conversational ability.
2. **SQLite for storage**: Chosen for simplicity — no database server needed. Works well for a single-user or low-traffic prototype but won't scale for concurrent writes.
3. **No frontend framework**: Vanilla JS keeps things simple but limits UI sophistication. No message history is loaded on page refresh despite being saved to the database.
4. **No authentication**: The app is completely open — no user accounts or session management.

## External Dependencies

### Python Packages
- **Flask** — Web framework (listed in `requirements.txt`)
- **sqlite3** — Built-in Python module for SQLite database access (no additional install needed)

### External Services
- None. The application is entirely self-contained with no third-party API calls, no external databases, and no authentication providers.

### Running the Application
- Install dependencies: `pip install -r requirements.txt`
- Start the server: `python app.py`
- The app serves on `http://0.0.0.0:5000`