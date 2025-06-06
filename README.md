# Bookwormhole

**Bookwormhole** is a full-stack Django blog application for sharing and discovering book reviews across multiple genres. Designed with readers and writers in mind, the site allows users to browse detailed reviews, leave comments, and send in their book suggestions to the site owner. Admins can manage posts through a secure backend, with future plans for genre-based filtering and improved content navigation. The project demonstrates key Django features including authentication, models, templates, and deployment to Heroku.

![Bookwormhole mockup](static/images/ms3-bookwormhole-mockup.png)

## Table of Contents

- [Project Goals](#project-goals)
- [User Experience](#user-experience)
- [Database](#database)
- [Design](#design)
- [Technologies Used](#technologies-used)
- [Development Methodology](#development-methodology)
- [Features](#features)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Code Attribution](#code-attribution)
- [Original Development](#original-development)
- [Tools and Resources](#tools-and-resources)
- [Acknowledgments](#acknowledgments)

---

## Project Goals

### User Goals

- Discover in-depth book reviews.
- Browse reviews by genre.
- Engage with content through comments.

### Site Owner Goals

- Provide a platform for sharing analytical book reviews.
- Maintain a clean and user-friendly interface.
- Encourage user interaction and feedback.

---

## User Experience

### Target Audience

- Book enthusiasts seeking detailed analyses.
- Readers interested in diverse genres.
- Individuals looking for a community of like-minded readers.

### User Requirements and Expectations

- Easy navigation across the site.
- Clear categorization of reviews.
- Responsive design for various devices.

## User Stories

| User Type | Story | Acceptance Criteria |
|-----------|--------|-------------------|
| **Reader** | Browse reviews by genre | Can filter posts by genre categories |
| **Reader** | Comment on reviews | Can leave comments when logged in |
| **Admin** | Create reviews | Can draft and publish book reviews |
| **Admin** | Moderate content | Can approve/reject comments |

**Complete tracking**: [Bookwormhole Blog Project Board](https://github.com/users/Jere-The-Hutt/projects/12)

## Database

### Entity Relationship Diagram

![Database ERD](static/images/bookwormhole_database_erd.jpeg)

### Database Schema Overview

The Bookwormhole application uses a PostgreSQL database with six core entities designed to support a comprehensive book review platform:

#### Core Models

**User** (Django built-in)
- Handles authentication and links to posts as authors and comments as commenters

**Post** (Book Reviews)  
- Main content entity storing book reviews with title, body, excerpt, featured image, and publication status (draft/published)
- Links to User (author) and Genre, supports multiple Comments

**Genre**
- Categorizes book reviews by literary genre (name, slug fields)
- One-to-many relationship with Posts

**Comment**
- User comments on book reviews with moderation system (requires approval before display)
- Links to both Post and User (commenter)

**Contact**
- Stores book recommendation submissions from users (standalone entity)
- Fields: name, email, book details, message, timestamp

**About**
- Site information content (typically single record)
- Manages the About page content with profile image and description

#### Key Relationships
- **User → Posts**: One-to-many (author relationship)
- **User → Comments**: One-to-many (commenter relationship)  
- **Genre → Posts**: One-to-many (categorization)
- **Post → Comments**: One-to-many (review discussions)
- **Contact & About**: Standalone entities for site management

---

## Design

### Design Choices

- Minimalist layout focusing on content readability.
- Emphasis on textual content with supportive imagery.

### Color

- Neutral tones to reduce eye strain and enhance readability.
  ![Coolors Palette](static/images/bookwormhole-coolors-palette.png)

### Fonts

- Carta-Marina (sans-serif) for headings to convey a literary feel.
- Basic-Sans (sans-serif) for body text for clarity.

### Structure

#### Before Logging In
- Access to all reviews and the About page.
- Options to register or log in.

#### After Logging In
- Ability to comment on reviews.
- Ability to log out.


### Wireframes

**index.html**
  ![index wireframe](static/images/index.html.png)

**post_detail.html**
  ![post_detail wireframe](static/images/post_detail.html.png)

**about.html**
  ![about wireframe](static/images/about.html.png)

**genre_posts.html**
  ![genre_posts wireframe](static/images/genre_posts.html.png)

---

## Technologies Used

### Languages

- HTML, CSS, JavaScript, Python

### Frameworks

- Django 5, Bootstrap 5

### Database

- PostgreSQL

### Tools

- Git, GitHub, Heroku, Cloudinary

### Supporting Libraries and Packages

- `dj-database-url`, `gunicorn`, `django-allauth`, `crispy-forms`, etc.

---

## Development Methodology

### Agile Development
The project utilized an iterative Agile approach with GitHub Projects for task management and progress tracking.

### User Stories and Issues
Requirements were captured as user stories and converted into GitHub Issues with acceptance criteria, enabling clear traceability from concept to implementation.

### Project Tracking
Development progress was managed through a Kanban board for visibility into task status and workflow.

[View Project Board](https://github.com/users/Jere-The-Hutt/projects/12)

---

## Features

### Landing Page
![Index 1](static/images/bookwormhole_features_index_01.png)
![Index 2](static/images/bookwormhole_features_index_02.png)
- Bookwormhole hero image.
- Reviews are listed with excerpts and paginated for easier browsing.

### Review Detail Page
![Post detail](static/images/bookwormhole_features_post_detail_01.png)
![Comments](static/images/bookwormhole_features_post_detail_02.png)
- Full review content.
- Comment section for user engagement.

### User Account Management
![Sign in](static/images/bookwormhole_features_auth_01.png)
![Sign up](static/images/bookwormhole_features_auth_02.png)
![Log out](static/images/bookwormhole_features_auth_03.png)
- Registration and authentication.

### Navigation
![Navbar logged in](static/images/bookwormhole_features_navbar_01.png)
![Navbar logged out](static/images/bookwormhole_features_navbar_02.png)
- Responsive navbar with links to Home, About, Register, and Login.

### Custom 404 page
![Custom 404](static/images/bookwormhole-custom_404.png)
- A styled error page appears if a user lands on a missing page, with buttons to go back or return home.

### Future Features

- User-submitted reviews.
- Rating system for reviews.
- Enhanced search functionality.
- Genre page so user can browse posts by genres.
- Social Authentication

---

## Testing

### Code Validation
All Python code in this project was tested for PEP8 compliance using the PEP8 Online Checker [CI Python Linter](https://pep8ci.herokuapp.com/). Each file was individually reviewed, including models, views, forms, and the main manage.py script. No PEP8 errors or warnings were found, ensuring that the code adheres to standard Python style guidelines and maintains readability and consistency throughout the project.

### Lighthouse

**index.html**:

  ![index lighthouse score](static/images/bookwormhole-lighthouse-index.png)

**post_detail.html**

  ![post_detail lighthouse score](static/images/bookwormhole-lighthouse-post_detail.png)

**about.html**

  ![about lighthouse score](static/images/bookwormhole-lighthouse-about.png)

**genre_posts.html**

  ![genre_posts lighthouse score](static/images/bookwormhole-lighthouse-genre_posts.png)


### HTML Validation

**index.html**:

  ![index HTML Validation](static/images/bookwormhole-html-validation-index.png)

**post_detail.html**

  ![post_detail HTML Validation](static/images/bookwormhole-html-validation-post_detail.png)

**about.html**

  ![about HTML Validation](static/images/bookwormhole-html-validation-about.png)

**genre_posts.html**

  ![genre_posts HTML Validation](static/images/bookwormhole-html-validation-genre_posts.png)

### CSS Validation

![style CSS Validation](static/images/bookwormhole-css-validation.png)

### WAVE Web Accessibility Evaluation

No accessibility errors were detected using the WAVE tool, aside from a few contrast warnings related to minor meta text and default link styles. These did not impact overall readability or usability, so they were not prioritized for correction.

![WAVE Index](static/images/bookwormhole_wave_index.png)
![WAVE Post Detail](static/images/bookwormhole_wave_post_detail.png)

---

## Bugs

### Known Bugs

- **Flake8 warning in `settings.py`:**
  ```text
  F401: 'env' imported but unused
  ```
  This warning appears because env.py is imported to allow for environment variable loading during development, but not explicitly used elsewhere in settings.py. This can be safely ignored, or suppressed if preferred.

### Fixed Bugs

- **Static Files Issue in Production**

    During deployment to Heroku, the app initially served outdated styles because the `staticfiles/` directory contained old versions of the CSS. This happened because the static files were previously committed to the repository before `.gitignore` was properly configured.

    **Cause**

    - `staticfiles/` had been committed to Git before it was added to `.gitignore`.
    - `collectstatic` was not run consistently or was generating outdated content.
    - Heroku served outdated cached files due to missing configuration.

    **Resolution**

    1. Removed `staticfiles/` from Git:
   ```
   git rm -r --cached staticfiles/
   ```
    2. Ensured staticfiles/ is listed in .gitignore.

    3. Ran collectstatic to regenerate the correct static assets:
    ```
    python manage.py collectstatic
    ```
    4. Added the following to settings.py to enable proper static file versioning and compression in production:
    ```
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    ```

    This setting ensures that Django appends unique hashes to static file names (e.g. style.38a4510b6b64.css) so browsers always load the most up-to-date version, avoiding cache issues. It also compresses files to improve performance on Heroku.

- **Cloudinary serving all images over HTTP instead of HTTPS**

    Cloudinary was serving all images over HTTP instead of HTTPS, causing mixed content warnings and potential security issues in production.

    **Cause**

    - Cloudinary's default configuration doesn't force HTTPS delivery.

    **Resolution**

    Added ```secure=True``` to the Cloudinary configuration in ```settings.py```:
    ```
    cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET'),
    secure=True  # Forces HTTPS for all image URLs
    )
    ```
    All Cloudinary image URLs now automatically use HTTPS, resolving mixed content issues and ensuring secure image delivery.

- **HTML Validation Error: "No p element in scope but a p end tag seen"**

    HTML validation was failing due to nested paragraph tags in the post_detail.html template.
    ![Post detail HTML Validation Error](static/images/bookwormhole-html-validation-post_detail-error.png)

    **Cause** 
    
    The post.body content (which already contained properly formatted HTML with <p> tags) was being wrapped in an additional <p class="post-body"> tag, creating invalid nested paragraph elements.
    
    **Resolution**

    - Replaced ```<p class="post-body">``` wrapper with ```<div class="post-body">``` in the post content section
    - Updated comment rendering to use {{ comment.body | safe }} instead of | linebreaks
    - Consolidated multiline class attributes in comment templates
    - Changed empty comment state message from <p> to <div> tag

    Template now passes HTML validation and renders correctly across all browsers.

---

## Deployment

### Live Application

The Bookwormhole blog is deployed on Heroku: [View Live Site](https://jeres-bookwormhole-blog-a8e9a55f8d36.herokuapp.com/)

## Prerequisites
- Python 3.8+ installed
- Git installed
- GitHub account
- Heroku account
- Cloudinary account
- Code Institute database access (for students)

## Create Repository and Local Workspace

### 1. Create a new GitHub repository
1. Go to github.com and create a new repository
2. Do not initialize with a README (you'll create one locally)
3. Copy the repository URL for the next step

### 2. Set up your local project directory
Open your terminal in your project folder and run:

```bash
# Initialize git and create initial README
echo "# ms3-bookwormhole-blog" >> README.md
git init
git add README.md
git commit -m "Initial commit"
git branch -M main

# Connect to your GitHub repository (replace with your actual repo URL)
git remote add origin https://github.com/Jere-The-Hutt/ms3-bookwormhole-blog.git
git push -u origin main
```

### 3. Set up virtual environment and install dependencies

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Create essential project files

Before deploying, ensure you have these files:

**Procfile** (create in root directory):
```
web: gunicorn bookwormhole.wsgi
```

**requirements.txt** (update with current dependencies):
```bash
pip freeze > requirements.txt
```

### 5. Configure environment variables for local development

Create `env.py` in your root directory:

```python
import os

os.environ["SECRET_KEY"] = "your-local-secret-key-here"
os.environ["CLOUDINARY_URL"] = "cloudinary://your-cloudinary-url"
os.environ["DEBUG"] = "True"
# DATABASE_URL not needed for local SQLite
```

**Important**: Add `env.py` to your `.gitignore` file to prevent committing sensitive information:

```bash
echo "env.py" >> .gitignore
```

### 6. Push all changes to GitHub

```bash
git add .
git commit -m "Add project files and configuration"
git push origin main
```

## Heroku Deployment

### 1. Create Heroku application
1. Log in to your Heroku dashboard
2. Click "New" → "Create new app"
3. Choose a unique app name
4. Select your region
5. Click "Create app"

### 2. Set up PostgreSQL database
This project uses a PostgreSQL database provided by Code Institute. Contact your course provider for database credentials, or set up your own PostgreSQL instance.

### 3. Configure environment variables
In your Heroku app dashboard, go to Settings → Config Vars and add:

```
DATABASE_URL=your-postgresql-database-url
SECRET_KEY=your-production-secret-key
CLOUDINARY_URL=cloudinary://your-cloudinary-credentials
DEBUG=False
```

**Generating a SECRET_KEY**: You can generate a secure key using Python:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 4. Connect to GitHub and deploy
1. Go to the Deploy tab in your Heroku dashboard
2. Select "GitHub" as deployment method
3. Connect your GitHub account and search for your repository
4. Connect to the repository
5. Choose "Manual deploy" from the main branch
6. Click "Deploy Branch"

### 5. Set up the database
After successful deployment, open the Heroku Console (More → Run console) and run:

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Collect static files
If you encounter static file issues, run:

```bash
python manage.py collectstatic --noinput
```

## Local Development Setup

### 1. Clone the repository

```bash
git clone https://github.com/Jere-The-Hutt/ms3-bookwormhole-blog.git
cd ms3-bookwormhole-blog
```

### 2. Set up virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure local environment variables

Create `env.py` in the root directory:

```python
import os

os.environ["SECRET_KEY"] = "your-local-secret-key"
os.environ["CLOUDINARY_URL"] = "your-cloudinary-url"
os.environ["DEBUG"] = "True"
# Local development uses SQLite - no DATABASE_URL needed
```

### 4. Set up local database

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Your local development server will be available at `http://127.0.0.1:8000/`

## Services Used

| Service | Purpose | Configuration |
|---------|---------|---------------|
| **Heroku** | Application hosting | Manual deployment from GitHub |
| **PostgreSQL** | Production database | DATABASE_URL environment variable |
| **Cloudinary** | Media file storage | CLOUDINARY_URL configuration |
| **WhiteNoise** | Static file serving | Django middleware for Heroku |
| **GitHub** | Code repository | Version control and deployment source |

## Troubleshooting

### Common Issues

**Static files not loading in production:**
- Ensure `STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'` is in settings.py
- Run `python manage.py collectstatic` in Heroku console

**Database connection errors:**
- Verify DATABASE_URL is correctly set in Heroku config vars
- Ensure migrations have been run: `python manage.py migrate`

**Environment variable errors:**
- Double-check all config vars are set in Heroku
- Ensure `env.py` is not committed to Git (check `.gitignore`)

## Fork & Contribute

### Fork this repository

1. Click **Fork** on the [Bookwormhole repository](https://github.com/Jere-The-Hutt/ms3-bookwormhole-blog)
2. Clone your fork: `git clone https://github.com/YOUR-USERNAME/ms3-bookwormhole-blog.git`

### Make contributions

1. Create a feature branch: `git checkout -b feature-name`
2. Make your changes and commit: `git commit -m "Add feature description"`
3. Push to your fork: `git push origin feature-name`
4. Submit a pull request to the original repository
---

## Code Attribution

## External Sources and References

### Code Institute Walkthrough Project
- **Source**: "I Think Therefore I Blog" walkthrough project
- **Usage**: Used as reference for project setup and structure
- **Components Used**: 
  - About model, views, and forms
  - Post model, views, and forms
  - Comment model, views, and forms
- **Files Influenced**: Overall project architecture, configuration, and core blog functionality
- **Modifications**: Adapted and modified for this project's specific requirements

### Starter Code Templates
- **Source**: Code Institute walkthrough project base templates
- **Files**: 
  - `base.html` & `post_detail.html` - Base template structure (significantly modified)
  - `style.css` - Initial styling framework (extensively customized)
- **Modifications**: Both files have been considerably modified and extended to meet project requirements

### Django Model Reference
- **Source**: "Django 5 By Example" book
- **Usage**: Referenced for initial model creation and database design
- **Integration**: Combined with Code Institute walkthrough approach
- **Modifications**: Models adapted and extended for project-specific functionality

## Original Development
- **Genre Model**: Independently designed and implemented genre categorization system
- **Contact Form**: Independently developed contact form functionality (similar function to walkthrough but original implementation)
- All other custom views, templates, JavaScript functionality, additional styling, and project-specific features represent original development work building upon the referenced foundations.

## Tools and Resources

- **Balsamiq** - Wireframe creation and user interface planning
- **Lucidchart** - Database Entity Relationship Diagram (ERD) design
- **Coolors** - Color palette generation and selection
- **Adobe Fonts** - Typography and web font resources
- **Unsplash** - Stock images and visual content
- **Favicon.io** - Favicon generation and optimization
- **ChatGPT** - Content generation for book reviews and troubleshooting guidance
- **Claude (Anthropic)** - README documentation refinement

## Acknowledgments
- My mentor Spencer Barriball for guidance and his fantastic pancake tips
- My classmate Daniel Rydell for his help with the "Cloudinary serving all images over HTTP instead of HTTPS" issue
- Code Institute for educational resources and starter templates
- "Django 5 By Example" for comprehensive Django guidance
- [Django Software Foundation](https://docs.djangoproject.com/) and contributors for the Django framework and documentation 
