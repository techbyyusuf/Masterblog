from flask import Flask, redirect, render_template, request, url_for
from blog_data import fetch_post_by_id, load_posts, update_posts, save_posts

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


@app.route('/delete/<int:post_id>', methods= ['POST'])
def delete(post_id):
    blog_posts = load_posts()
    updated_posts = [post for post in blog_posts if post["id"] != post_id]
    save_posts(updated_posts)
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods= ['GET', 'POST'])
def update(post_id):
    post = fetch_post_by_id(post_id)
    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        author = request.form.get("author")
        title = request.form.get('title')
        content = request.form.get('content')

        updated_post = {
            "id": post_id,
            "author": author,
            "title": title,
            "content": content
        }

        update_posts(updated_post,post_id)

        return redirect(url_for('index')) # Redirect back to index

    return render_template('update.html', post=post)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)