from flask import Flask, redirect, render_template, request, url_for
from blog_data import load_posts, save_posts

app = Flask(__name__)

@app.route('/')
def index():
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        author = request.form.get("author")
        title = request.form.get('title')
        content = request.form.get('content')

        blog_posts = load_posts()

        new_post = {
            "id": max(post["id"] for post in blog_posts) + 1 if blog_posts else 1,
            "author": author,
            "title": title,
            "content": content
        }

        blog_posts.append(new_post)
        save_posts(blog_posts)

        return redirect(url_for('index'))
    return render_template('add.html')



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)