# মনোবল (Monobol)

Welcome to **মনোবল (Monobol)**, a full-stack web application dedicated to improving physical and **Monobol**, with a primary focus on mental well-being.

---

## 🛠️ Tech Stack & Architecture

This project uses a 4-tier, full-stack architecture, ensuring a clean separation of concerns between the user interface, business logic, data storage, and artificial intelligence.

### 1. Frontend
* **Description:** Responsible for rendering the user interface (UI) and handling all user interactions.
* **Technologies:** Built using a modern JavaScript framework. The specific choice depends on project needs:
    * [**React**](https://reactjs.org/): A JavaScript library for building user interfaces.
    * [**Vue.js**](https://vuejs.org/): A progressive, incrementally-adoptable JavaScript framework.
    * [**Svelte**](https://svelte.dev/): A radical new approach to building user interfaces by compiling components to highly efficient vanilla JavaScript.
* **Communication:** Interacts with the backend by making RESTful API calls to the Flask application.

### 2. Backend (Flask App)
* **Description:** A lightweight Python backend that serves as the central hub, handling API requests, processing business logic, and acting as a mediator between the frontend, database, and LLM engine.
* **Technology:** [**Flask**](https://flask.palletsprojects.com/)
* **Core Endpoints:**
    * `/api/db`: Handles all database operations (CRUD).
    * `/api/llm`: Manages all communication with the external LLM APIs.

### 3. Database
* **Description:** Used for persistent data storage (e.g., user data, application state, etc.).
* **Technology:** [**SQLite3**](https://www.sqlite.org/index.html)
* **Integration:** Accessed securely via the `/api/db` endpoint in the Flask app. Its lightweight, serverless nature makes it ideal for development and small-to-medium scale applications.

### 4. LLM Engine
* **Description:** Provides advanced AI and natural language processing capabilities to power the application's core features.
* **Technologies:**
    * [**OpenAI API**](https://openai.com/api/): Provides access to models like GPT-4, GPT-3.5, etc.
    * [**Google Gemini API**](https://ai.google.dev/): Provides access to Google's next-generation family of models.
* **Integration:** Accessed via the `/api/llm` endpoint, abstracting the AI logic from the main application.

---

## 🏗️ Web Application Architecture with Gemini LLM

The diagram below illustrates the flow of information between the different components of the application.

```mermaid
graph TD
    %% Define Nodes
    subgraph "Clients"
        A[fa:fa-users Frontend <br> (React/Vue/Svelte)]
    end

    subgraph "Infrastructure"
        B[fa:fa-network-wired Application Load Balancer]
    end

    subgraph "Application Layer (Backend)"
        C(fa:fa-server Python Flask)
        subgraph C [Python Flask]
            C1[fa:fa-database Database API <br> (/api/db)]
            C2[fa:f-fa-comment-dots Chatbot API <br> (/api/llm)]
        end
    end

    subgraph "Data & AI"
        D[fa:fa-database SQLite3 Database]
        E[fa:fa-robot LLM Engine <br> (Gemini/OpenAI)]
    end

    %% Define Links
    A --> B
    B --> C
    C1 --> D
    C2 --> E
