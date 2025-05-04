# Brand Blog Website

A clean, responsive brand blog website built with Flask, featuring a homepage, blog listings, about and contact pages with an in-memory data store.

## Features

- Homepage with a short intro and recent blog posts
- Blog page showing multiple posts
- About page with company story and team information
- Contact page with social media links and contact form
- Responsive and minimal HTML/CSS using Bootstrap
- Python Flask backend serving HTML templates

## Tech Stack

- Python (Flask)
- HTML/CSS (Bootstrap with Replit dark theme)
- In-memory list for blog posts (no database required)

## Local Setup Instructions

1. Clone the repository to your local machine:
```
git clone <repository-url>
cd brand-blog
```

2. Create a virtual environment:
```
python -m venv venv
```

3. Activate the virtual environment:
   - On Windows:
   ```
   venv\Scripts\activate
   ```
   - On macOS/Linux:
   ```
   source venv/bin/activate
   ```

4. Install the required packages:
```
pip install flask==2.3.3 email-validator==2.0.0 flask-sqlalchemy==3.0.5 gunicorn==23.0.0
```

5. Run the application:
```
python main.py
```

6. Open your browser and navigate to `http://127.0.0.1:5000`

## Project Structure

```
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── scripts.js
├── templates/
│   ├── about.html
│   ├── base.html
│   ├── blog.html
│   ├── blog_post.html
│   ├── contact.html
│   └── index.html
└── main.py
```

## Development

To modify the blog posts, edit the `blog_posts` list in `main.py`.

For styling changes, modify the CSS in `static/css/styles.css` or use Bootstrap classes directly in the HTML templates.

## License

This project is available for personal and commercial use.