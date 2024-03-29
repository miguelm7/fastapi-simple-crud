from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4 as uuid

from helpers import read_json_data, save_json_data

app = FastAPI()

# posts = []

# Post model
class Post(BaseModel):
    """
    Model class for posts
    """
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published : bool = False

@app.get("/")
def read_root():
    return {"Welcome" : "Welcome to my REST API"}

@app.get("/posts")
def get_posts():
    posts = read_json_data("data")
    return posts

@app.get("/posts/{post_id}")
def get_post(post_id: str):
    posts = read_json_data("data")
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not Found")

@app.post("/posts")
def create_post(post: Post):
    posts = read_json_data("data")
    post.id = str(uuid())
    posts.append(post.model_dump())
    save_json_data("data",posts)
    return posts[-1]

@app.delete("/posts/{post_id}")
def delete_post(post_id: str):
    posts = read_json_data("data")
    for idx, post in enumerate(posts):
        if post["id"] == post_id:
            deleted_post = posts.pop(idx)
            save_json_data("data",posts)
            return {"successfully deleted" : deleted_post} 
    raise HTTPException(status_code=404, detail="Post not Found")

@app.put("/posts/{post_id}")
def update_post(post_id: str, updated_post: Post):
    posts = read_json_data("data")
    for idx, post in enumerate(posts):
        if post["id"] == post_id:
            posts[idx]["title"] = updated_post.title
            posts[idx]["content"] = updated_post.content
            posts[idx]["author"] = updated_post.author
            save_json_data("data",posts)
            return {"successfully updated" : posts[idx]}
    raise HTTPException(status_code=404, detail="Post not Found")