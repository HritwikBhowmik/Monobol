# মনোবল (Monobol)

**Monobol** is a complete platform dedicated to our **mental health** and **community well-being**. It brings together **mood tracking**, **community support**, and **mental health services** in one place that helps us stay balanced, connected, and cared for.

---

## Team

**ShunnoLogic**

---

## Full-Stack Documentation

This document provides a comprehensive overview of Monobol's full-stack architecture, detailing the interactions between the frontend, Flask application (backend), database, and LLM engine.

### 1. Frontend

The frontend is responsible for presenting the user interface and handling all user interactions.

#### 1.1 Technologies

The frontend is built using modern JavaScript frameworks, with the specific choice based on project requirements and team expertise:

* **React:** A JavaScript library for building user interfaces.
* **Vue.js:** A progressive JavaScript framework for building user interfaces.
* **Svelte:** A compiler that turns components into tiny, highly efficient vanilla JavaScript.

#### 1.2 Interactions

The frontend communicates with the backend **Flask application** primarily through **RESTful API calls** to retrieve and send data.

---

### 2. Flask App (Backend)

The Flask application serves as the core backend, handling API requests, orchestrating database interactions, and managing communication with the LLM engine.

#### 2.1 Key API Endpoints

The Flask application exposes the following essential API endpoints:

| Endpoint | Description |
| :--- | :--- |
| `/api/db` | Handles all interactions with the underlying database API (e.g., retrieving mood logs, storing user data). |
| `/api/llm` | Manages communication with the LLM API for AI-powered features. |

#### 2.2 Technologies

* **Flask:** A lightweight WSGI web application framework written in Python.
* **REST Calls:** Standardized methods for communication between the frontend and backend systems.

---

### 3. Database

The application utilizes a robust database for persistent data storage.

#### 3.1 Technology

* **SQLite3:** A C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. It is commonly used for local storage and embedded applications.

#### 3.2 Integration

The Flask application manages all database interactions via the **`/api/db`** endpoint, enabling secure data retrieval, storage, and manipulation.

---

### 4. LLM Engine (AI Services)

The Large Language Model (LLM) engine is integrated to provide advanced language processing and AI-powered features for mental health support.

#### 4.1 Technologies

* **OpenAI API:** Provides access to various advanced AI models developed by OpenAI.
* **Gemini API:** A set of services and tools provided by Google for accessing and integrating their powerful Gemini family of large language models.

#### 4.2 Integration

The Flask application communicates with the selected API (e.g., OpenAI or Gemini) via the **`/api/llm`** endpoint to leverage the LLM for tasks such as natural language understanding, response generation, or personalized insights.

---

## Design & Specification

### High-Level Design (HDL) Diagram



### OpenAPI Specification (Swagger API)

The **OpenAPI Specification** will formally describe the Monobol RESTful API, providing a machine-readable and human-readable contract for its services. This specification will detail:

* **API Endpoints:** Paths and HTTP methods for all services.
* **Request/Response Schemas:** Data structures using JSON Schema for clear data handling.
* **Authentication Methods:** Specification for client authentication (e.g., API keys, OAuth2).
* **Parameters:** Descriptions of path, query, and header parameters.

This allows for the generation of interactive documentation (e.g., using **Swagger UI**), client SDKs, and server stubs.

### Postman Collection Overview

The Postman collection for Monobol provides a structured set of requests essential for development and testing:

* **Organization:** Requests are logically grouped into folders (e.g., **Database API**, **LLM API**).
* **Requests:** Individual requests for each endpoint (e.g., `POST /api/db/mood`, `GET /api/llm/generate-response`).
* **Configuration:** Includes **Environment Variables** for managing base URLs and tokens, and **Pre-request Scripts** for dynamic tasks like authentication.
* **Testing:** **Test Scripts** are included to validate API responses and ensure correct functionality.

###  HLD
![](https://github.com/HritwikBhowmik/Monobol/raw/master/assets/HLD.jpeg)
