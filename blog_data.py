import json


DATA_FILE = 'data/data_structure.json'

def load_posts():
    with open(DATA_FILE, 'r') as file:
        blog_posts = json.load(file)
    return blog_posts


def save_posts(blog_posts):
    with open(DATA_FILE, "w") as file:
        json.dump(blog_posts, file)


def fetch_post_by_id(post_id):
    blog_posts = load_posts()
    for post in blog_posts:
        if post["id"] == post_id:
            return post
    return None

def update_posts(updated_post, post_id):
    blog_posts = load_posts()
    for i, post in enumerate(blog_posts):
        if post["id"] == post_id:
            blog_posts[i]= updated_post
            break
    save_posts(blog_posts)


if __name__ == "__main__":
    print(load_posts())