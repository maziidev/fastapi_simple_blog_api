from typing import Optional, List
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from uuid import UUID, uuid4

app = FastAPI()

# Input model (used for creating and updating)
class PostCreate(BaseModel):
    title: str
    content: str
    author: Optional[str] = "Admin"

# Simulated database (now a list of dicts)
all_posts: List[dict] = [
    {
        "id": uuid4(),
        "title": "Understanding APIs",
        "content": "APIs allow different systems to communicate.",
        "author": "MD"
    },
    {
        "id": uuid4(),
        "title": "Intro to Docker",
        "content": "Docker helps you containerize applications.",
        "author": "Admin"
    }
]

# Home route
@app.get("/api", status_code=status.HTTP_200_OK)
def home():
    return {
        "message": "Welcome to our API",
        "routes": {
            "GET /posts": "List all posts",
            "GET /posts/{id}": "Get a single post by ID",
            "POST /posts": "Create a new post",
            "PUT /posts/{id}": "Update an existing post",
            "DELETE /posts/{id}": "Delete a post"
        }
    }

# Get all posts
@app.get("/posts", status_code=status.HTTP_200_OK)
def get_all_posts():
    return {"data": all_posts}

# Get post by ID
@app.get("/posts/{id}", status_code=status.HTTP_200_OK)
def get_post(id: UUID):
    for post in all_posts:
        if post["id"] == id:
            return {"post_detail": post}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

# Create a new post
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreate):
    new_post = {
        "id": uuid4(),
        **post.model_dump()
    }
    all_posts.append(new_post)
    return {"data": new_post}

# Update an existing post
@app.put("/posts/{id}", status_code=status.HTTP_200_OK)
def update_post(id: UUID, post_data: PostCreate):
    for idx, existing_post in enumerate(all_posts):
        if existing_post["id"] == id:  # No need to str() if both are UUIDs
            updated_post = {
                "id": id,  # Reuse provided ID for consistency
                **post_data.model_dump()
            }
            all_posts[idx] = updated_post
            return {"data": updated_post}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")



# Delete a post
@app.delete("/posts/{id}", status_code=status.HTTP_200_OK)
def delete_post(id: UUID):
    for idx, post in enumerate(all_posts):
        if str(post["id"]) == str(id):  # Force string comparison
            all_posts.pop(idx)
            return {"message": "Post deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

