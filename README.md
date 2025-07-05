# 📝 Simple Blog API with FastAPI

This is a simple CRUD (Create, Read, Update, Delete) API built with **FastAPI** to simulate a blog system. It uses an **in-memory list of dictionaries** to store posts and exposes RESTful endpoints to interact with the data.

---

## 🚀 Features

- ✅ Fetch all blog posts
- ✅ Fetch a single post by UUID
- ✅ Create a new post
- ✅ Update an existing post
- ✅ Delete a post
- ✅ Organized endpoints and clean project structure
- ✅ Integrated Postman collection for testing

---

## 🧠 Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/) – High-performance Python web framework
- [Pydantic](https://docs.pydantic.dev/) – Data validation and settings management
- [Uvicorn](https://www.uvicorn.org/) – ASGI server for running FastAPI apps
- [Postman](https://www.postman.com/) – API testing and documentation

---

## 📂 Project Structure

simple_blog_api/
├── app/
│ └── main.py # Main FastAPI application
├── postman/
│ ├── simple_blog_api.postman_collection.json
├── README.md
└── requirements.txt

---

## 📦 Requirements

- Python 3.8+
- FastAPI
- Uvicorn

Install dependencies:

```bash
pip install -r requirements.txt


---

| Method | Endpoint      | Description                      |
| ------ | ------------- | -------------------------------- |
| GET    | `/api`        | API home with route instructions |
| GET    | `/posts`      | Get all blog posts               |
| GET    | `/posts/{id}` | Get a single post by UUID        |
| POST   | `/posts`      | Create a new post                |
| PUT    | `/posts/{id}` | Update an existing post          |
| DELETE | `/posts/{id}` | Delete a post by UUID            |


---

📌 Sample Request Payloads
✅ Create a Post

POST /posts
{
  "title": "Learning FastAPI",
  "content": "FastAPI is super fast and easy to use!",
  "author": "Maziidev"
}

✅ Update a Post


PUT /posts/{id}
{
  "title": "Updated Title",
  "content": "Updated content body",
  "author": "Godswill"
}


❌ Error Handling
404 Not Found – When a post ID does not exist

405 Method Not Allowed – If the wrong HTTP method is used

422 Unprocessable Entity – Validation errors from missing/invalid input


---
👨‍💻 Author
Godswill Nathaniel (maziidev)
Backend & AI Engineer | Web3 Enthusiast
