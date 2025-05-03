# 📰 Flask Blog Project

This is a simple blog application built with Flask. It demonstrates core web development concepts like routing, templating, form handling, and data storage using JSON.

---

## 🚀 Features

- View all blog posts
- Add a new blog post
- Update existing posts
- Delete posts with confirmation
- Custom error pages for 404 and 500
- Basic CSS styling

---

## 📁 Project Structure

```
/your_project/
├── app.py
├── blog_data.py
├── data/
│   └── data_structure.json
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   ├── add.html
│   ├── update.html
│   ├── 404.html
│   └── 500.html
```

---

## 📦 Requirements

- Python 3.x
- Flask

Install Flask with:

```bash
pip install flask
```

---

## 🧠 How It Works

- Blog posts are stored in `data/data_structure.json` as a list of dictionaries.
- Each post has an `id`, `title`, `author`, and `content`.
- CRUD operations (Create, Read, Update, Delete) are supported via HTML forms.
- Data is read/written to the JSON file using helper functions in `blog_data.py`.

---

## 🛠️ Running the App

```bash
python app.py
```

Then open your browser and go to:

```
http://localhost:5000/
```

---

## ✍️ To-Do Ideas

- Add login/logout
- Markdown support for content
- Flash messages on actions
- Pagination or search

---

## 💡 Author

Built as part of a Flask learning exercise.

Feel free to fork and modify!
