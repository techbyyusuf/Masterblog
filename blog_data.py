import json


DATA_FILE = 'data/data_structure.json'

def load_posts():
    with open(DATA_FILE, 'r') as file:
        blog_posts = json.load(file)
    return blog_posts


def save_posts(blog_posts):
    with open(DATA_FILE, "w") as file:
        json.dump(blog_posts, file)


if __name__ == "__main__":
    print(load_posts())