class User:
    user_id = str
    username = str
    email = str
    password = str
    first_name = str

class comments:
    comment_id = str
    post_id = str
    user_id = str
    content = str
    created_at = str
    updated_at = str
    likes = int
    is_deleted = bool