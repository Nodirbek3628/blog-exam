# from database import LocalSession
# import crud

# db = LocalSession()

# # Test: user qo‘shish
# user = crud.create_user(db, "Bob", "bob@example.com")
# print("Created User:", user.username)



# # Test: user postlari
# post = crud.create_post(db, 5, "Test post", "Bu post matni")
# print("User posts:", post.title)


# coment = crud.create_comment(db,)

# # Qolgan function larni ham shu yerda test qiling

from database import LocalSession
import crud

db = LocalSession()

# Test: user qo‘shish
user = crud.create_user(db, "Bob", "bob@example.com")
print("Created User:", user.username)

# Test: user post qo‘shish
post = crud.create_post(db, user.id, "Test post", "Bu post matni")
print("Created Post:", post.title)

# Test: user postlarini olish
posts = crud.get_user_posts(db, user.id)
print("User posts:", [p.title for p in posts])

# Test: comment qo‘shish
comment = crud.create_comment(db, user.id, post.id, "Bu comment matni")
print("Created Comment:", comment.text)

# Test: post comment count
count = crud.get_post_comment_count(db, post.id)
print("Comment count:", count)


latest = crud.get_latest_posts(db)
print("Latest posts:", [p.title for p in latest])

# Test: search by title
search = crud.search_posts_by_title(db, "Test")
print("Search result:", [p.title for p in search])


db.close()
