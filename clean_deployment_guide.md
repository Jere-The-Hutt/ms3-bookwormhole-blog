# Deployment

## Live Application
The Bookwormhole blog is deployed on Heroku: [View Live Site](https://jeres-bookwormhole-blog-a8e9a55f8d36.herokuapp.com/)

## Prerequisites
- Heroku account
- Cloudinary account
- GitHub repository

## Heroku Deployment

### 1. Create Heroku App
```bash
# Via Heroku CLI (optional)
heroku create your-app-name
```
Or create via Heroku Dashboard.

### 2. Add Database
Add **Heroku Postgres** add-on through the Heroku Dashboard.

### 3. Configure Environment Variables
Set these config vars in Heroku Settings:
```
DATABASE_URL=<automatically-set-by-postgres-addon>
SECRET_KEY=<your-django-secret-key>
CLOUDINARY_URL=<your-cloudinary-url>
DEBUG=False
PORT=8000
```

### 4. Connect to GitHub
1. In Heroku Dashboard → Deploy tab
2. Connect to your GitHub repository
3. Choose manual deployments from `main` branch

### 5. Initial Database Setup
Run in Heroku Console:
```bash
python manage.py migrate
python manage.py createsuperuser
```

## Required Project Files

### Procfile
```
web: gunicorn bookwormhole.wsgi
```

### requirements.txt
Ensure all dependencies are listed:
```bash
pip freeze > requirements.txt
```

### settings.py Configuration
```python
import os
import dj_database_url

if os.path.isfile("env.py"):
    import env

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

# Cloudinary Configuration
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}

# Static Files (WhiteNoise + Cloudinary)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

## Local Development Setup

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/bookwormhole.git
cd bookwormhole
```

### 2. Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Environment Variables
Create `env.py`:
```python
import os

os.environ["SECRET_KEY"] = "your-local-secret-key"
os.environ["CLOUDINARY_URL"] = "your-cloudinary-url"
os.environ["DEBUG"] = "True"
# DATABASE_URL not needed for local SQLite
```

### 4. Database Setup
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Services Used

| Service | Purpose | Configuration |
|---------|---------|---------------|
| **Heroku** | App hosting | Manual deployment from GitHub |
| **Heroku Postgres** | Production database | Automatic DATABASE_URL |
| **Cloudinary** | Media file storage | CLOUDINARY_URL config var |
| **WhiteNoise** | Static file serving | Django middleware |
| **GitHub** | Code repository | Connected to Heroku |

## Fork & Contribute

### Fork Repository
1. Click **Fork** on the [GitHub repository](https://github.com/yourusername/bookwormhole)
2. Clone your fork: `git clone https://github.com/YOUR-USERNAME/bookwormhole.git`

### Make Contributions
1. Create feature branch: `git checkout -b feature-name`
2. Make changes and commit: `git commit -m "Add feature"`
3. Push to your fork: `git push origin feature-name`
4. Submit pull request

---

**Need help?** Check the [GitHub Issues](https://github.com/yourusername/bookwormhole/issues) or create a new one.