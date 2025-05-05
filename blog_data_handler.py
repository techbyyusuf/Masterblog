import json
import os

DATA_FILE = 'data/data_structure.json'

def load_posts():
    """
    Load all blog posts from the JSON file.

    Returns:
        list: A list of blog post dictionaries.
    """
    try:
        if not os.path.exists(DATA_FILE):
            return []

        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading posts: {e}")
        return []


def save_posts(blog_posts):
    """
    Save the given list of blog posts to the JSON file.

    Args:
        blog_posts (list): List of blog post dictionaries to be saved.
    """
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(blog_posts, file, indent=4)  # formatted JSON
    except IOError as e:
        print(f"Error saving posts: {e}")


def fetch_post_by_id(post_id):
    """
    Fetch a single blog post by its ID.

    Args:
        post_id (int): The ID of the blog post to retrieve.

    Returns:
        dict or None: The blog post dictionary if found, otherwise None.
    """
    blog_posts = load_posts()
    for post in blog_posts:
        if post["id"] == post_id:
            return post
    return None


def update_posts(updated_post, post_id):
    """
    Update an existing blog post by its ID.

    Args:
        updated_post (dict): The updated blog post data.
        post_id (int): The ID of the post to update.
    """
    blog_posts = load_posts()
    for i, post in enumerate(blog_posts):
        if post["id"] == post_id:
            blog_posts[i] = updated_post
            break
    save_posts(blog_posts)


if __name__ == "__main__":
    print(load_posts())
