# ImgPic

ImgPic is a Django-based image-sharing web application. Users can create an account (or sign in with Google via OAuth), upload images with a heading, browse all uploaded images, and manage their own uploads from a personal profile page.

---

## Features

- **User authentication** – register, log in, and log out using [django-allauth](https://django-allauth.readthedocs.io/), with support for both username/e-mail and **Google OAuth 2.0** sign-in.
- **Image gallery** – a public home page that displays every uploaded image in a responsive three-column grid.
- **Upload images** – authenticated users can upload an image file together with a short heading.
- **Profile page** – users can view only their own uploads, then edit the heading/image or delete a photo directly from that page.
- **Automatic user profiles** – a `UserProfile` record (including an optional bio and Google profile-picture URL) is created automatically whenever a new user registers.
- **Django admin** – the `Imgs` model is registered so administrators can manage all images through the built-in admin panel.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Web framework | Django 5 |
| Authentication | django-allauth (local + Google OAuth 2.0) |
| Database | SQLite (default, swap for PostgreSQL in production) |
| Media storage | Local filesystem (`media/` directory) |
| Static files | Local filesystem (`static/` directory) |
| Front-end | Plain HTML + CSS (Google Fonts) |

---

## Project Structure

```
ImgPic---Django-allauth/
├── config/                  # Main Django app
│   ├── migrations/          # Database migrations
│   ├── templates/
│   │   ├── account/         # allauth login / signup / logout pages
│   │   ├── socialaccount/   # Google OAuth confirmation page
│   │   └── config/          # App templates (list, form, delete, profile)
│   ├── adapter.py           # Custom allauth adapter
│   ├── admin.py             # Admin registration
│   ├── apps.py
│   ├── models.py            # UserProfile + Imgs models
│   ├── tests.py
│   └── views.py             # Class-based views (List, Create, Update, Delete)
├── imgpic/                  # Django project package
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── static/
│   └── config/
│       └── header_bg.jpg    # Header background image
├── media/                   # Uploaded images (created at runtime)
├── manage.py
├── db.sqlite3               # Default SQLite database
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.10 or newer
- `pip`
- A Google Cloud project with an OAuth 2.0 Client ID and Client Secret (only required for Google sign-in)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/abdullah-alfahim/ImgPic---Django-allauth.git
cd ImgPic---Django-allauth

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. Create a superuser (optional, needed for the admin panel)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

The application will be available at **http://127.0.0.1:8000/**.

### Configuring Google OAuth (optional)

1. Go to the [Google Cloud Console](https://console.cloud.google.com/) and create an OAuth 2.0 Client ID.
2. Set the authorised redirect URI to `http://127.0.0.1:8000/accounts/google/login/callback/`.
3. Log in to the Django admin panel at `/admin/`.
4. Under **Sites**, update the default site to `127.0.0.1:8000`.
5. Under **Social Applications**, add a new application:
   - Provider: `Google`
   - Client ID: *your Google Client ID*
   - Secret key: *your Google Client Secret*
   - Assign it to the default site.

---

## URL Overview

| URL | View | Description |
|---|---|---|
| `/` | `ImgListView` | Public image gallery (home page) |
| `/add/` | `ImgCreateView` | Upload a new image (login required) |
| `/update/<pk>/` | `ImgUpdateView` | Edit an existing image |
| `/delete/<pk>/` | `ImgDeleteView` | Delete an image |
| `/user_images/` | `UserImgListView` | Current user's profile / uploaded images |
| `/accounts/` | allauth | Login, signup, logout, Google OAuth |
| `/admin/` | Django admin | Site administration |

---

## Models

### `UserProfile`
Extends the built-in user model with an optional `bio` and a `google_profile_picture_url`. Created automatically via a `post_save` signal on every new user.

### `Imgs`
Stores each uploaded image with a `heading`, `date` (auto-set on creation), the `image` file, and a foreign key to the owning user.

---

## Design Reference

The initial UI design mockup can be viewed on Canva:  
[View design](https://www.canva.com/design/DAGsRdfhVeY/QYt1q_SomB5JNr_bP2LlUw/edit?utm_content=DAGsRdfhVeY&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

---

## License

This project is open source and available for personal and educational use.
