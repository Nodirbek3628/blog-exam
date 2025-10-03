import json
from database import Base, engine, LocalSession
from models import User, Post, Comment

def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def load_demo_data():
    db = LocalSession()
    with open("demo_data.json", "r", encoding='utf-8') as f:
        data = json.load(f)

    # Users larni kriting
    for user in data.get("users", []):
        db.add(User(
            username=user["username"],
            email=user["email"]
        ))
    db.commit()

    # Posts larni kriting
    for post in data.get("posts", []):
        db.add(Post(
            title=post["title"],
            body=post["body"],
            user_id=post["user_id"]
        ))
    db.commit()

    # Comments larni kriting
    for comment in data.get("comments",[]):
        db.add(Comment(
            text=comment["text"],
            post_id=comment["post_id"],
            user_id=comment["user_id"]
            ))
    db.commit()

    db.close()

if __name__ == "__main__":
    init_db()
    load_demo_data()
    print("✅ Database initialized and demo data loaded!")
