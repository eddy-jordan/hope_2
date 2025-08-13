# Atlantic Express – Django + HTML/CSS Integration

A beginner-friendly structure that serves your HTML/CSS pages from Django templates, with static assets inside the app. Follow this guide to run and develop locally.

## What’s inside
- Django app: `shipping`
- Templates: `shipping/templates/shipping/*.html`
  - Home page: `index.html` (copied from `hope/index0.html`)
  - Tracking search: `tracking.html` (copied from `hope/index2.html`)
  - Tracking details: `track.html` (copied from `hope/transit.html`, wired to data)
  - Login: `login.html` (copied from `hope/index.html`)
  - Signup: `signup.html`
  - About: `about.html` (copied from `hope/about.html`)
- Static assets: `shipping/static/shipping/*` (`style.css`, `images/`)
- Routes: `/`, `/tracking/`, `/track/<id>/`, `/login/`, `/signup/`, `/about/`

## Prerequisites
- Python 3.10+
- pip

## Setup
```bash
cd hope_2
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://localhost:8000`.

## Seed a sample package (optional)
```bash
source .venv/bin/activate
python manage.py shell -c "from shipping.models import Package; Package.objects.update_or_create(tracking_id='56890783976255373837', defaults=dict(from_location='Lagos', to_location='Abuja', status='in_transit'))"
```

## Project structure
```text
shipping/
  templates/shipping/
    base.html
    index.html
    tracking.html
    track.html
    login.html
    signup.html
    about.html
  static/shipping/
    style.css
    images/
      pic1.png pic2.jpg pic3.jpg
```

## How the pages map
- `/` renders `index.html` (track form + nav)
- `/track/?tracking_id=...` redirects to `/track/<id>/`
- `/track/<id>/` renders `track.html`
- `/login/`, `/signup/` render auth pages
- `/about/` renders the static About page

## Common tasks
- Edit styles in `shipping/static/shipping/style.css`
- Edit templates in `shipping/templates/shipping/*.html`
- Add URLs in `shipping/urls.py` and views in `shipping/views.py`

## Notes for beginners
- Use `{% load static %}` and `{% static 'shipping/style.css' %}` for assets
- Use `{% url 'route_name' %}` instead of hardcoding links
- Don’t commit `.venv/` or `db.sqlite3` (see `.gitignore`)

## Running on Windows (PowerShell)
```powershell
cd hope_2
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Open `http://localhost:8000` in your browser.

## Next steps
- Improve styling with Bootstrap classes or Tailwind
- Extract reusable nav/footer into `base.html`
- Add model fields for richer tracking updates

