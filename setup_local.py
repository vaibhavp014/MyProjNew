"""
Setup script to help with local environment setup.
Run this script to export the required files for local development.
"""

import os
import shutil
import zipfile
from pathlib import Path

def create_zip_archive():
    """Create a zip archive of the project files for local development."""
    
    # Create a directory to hold files for zipping
    export_dir = Path("export_for_local")
    if export_dir.exists():
        shutil.rmtree(export_dir)
    export_dir.mkdir()
    
    # Create directories
    for directory in ["static/css", "static/js", "templates"]:
        path = export_dir / directory
        path.mkdir(parents=True, exist_ok=True)
    
    # Copy main.py
    shutil.copy("main.py", export_dir / "main.py")
    
    # Copy templates
    template_files = ["base.html", "index.html", "blog.html", "blog_post.html", "about.html", "contact.html"]
    for file in template_files:
        shutil.copy(f"templates/{file}", export_dir / "templates" / file)
    
    # Copy static files
    static_css_files = ["styles.css"]
    for file in static_css_files:
        shutil.copy(f"static/css/{file}", export_dir / "static/css" / file)
    
    static_js_files = ["scripts.js"]
    for file in static_js_files:
        shutil.copy(f"static/js/{file}", export_dir / "static/js" / file)
    
    # Copy README.md
    shutil.copy("README.md", export_dir / "README.md")
    
    # Create requirements.txt for local development
    with open(export_dir / "requirements.txt", "w") as f:
        f.write("""flask==2.3.3
email-validator==2.0.0
flask-sqlalchemy==3.0.5
gunicorn==23.0.0
""")
    
    # Create a zip file
    with zipfile.ZipFile("brand_blog_local.zip", "w") as zipf:
        for root, _, files in os.walk(export_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(
                    file_path, 
                    os.path.relpath(file_path, export_dir)
                )
    
    # Clean up
    shutil.rmtree(export_dir)
    
    print("Created brand_blog_local.zip for local development")
    print("Instructions for use:")
    print("1. Download the zip file")
    print("2. Extract it to your local machine")
    print("3. Follow the setup instructions in README.md")

if __name__ == "__main__":
    create_zip_archive()