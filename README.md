# Andarun

[فارسی](README.fa.md)

Andarun is an invite-only, text-only social network built with Django. It runs on a single server with no dependency on outside services, so it keeps working on a country's domestic network when international internet access is cut.

The name means "inside" in Persian; the andarun was the private inner quarter of a traditional Persian house.

> **Status:** early development (v1, phase 1.1: accounts). Not ready for real users or for production deployment.

## Why

During nationwide shutdowns in Iran, as in November 2019 and June 2025, international traffic stops while servers inside the country can still be reached on the domestic network. Services that rely on email or SMS verification, foreign CDNs, web fonts or third-party APIs are the first to break. Andarun avoids all of them: accounts are a username and a password, every asset is served by the application itself, and new members join by invitation instead of email confirmation.

## Status

| Area | Status |
| --- | --- |
| Project setup; settings read from the environment, `SECRET_KEY` required, `DEBUG` off by default | Done |
| Custom user model: username login, usernames limited to `[a-z0-9_]{3,20}` and stored in lowercase | Done |
| Admin for the custom user model | Done |
| Login, logout and password change | Next |
| Invite-only sign-up, approved by the member who sent the invitation | Next |
| Profiles, text posts, comments, likes, follows, feed, search, notifications | Planned for v1 |
| Direct and group messages, then end-to-end encryption | Planned for v2 |

The full plan, with exit criteria for each phase, is in [ROADMAP.md](ROADMAP.md).

## Design principles

- **No email, no phone numbers.** An account is a username and a password. Invitations replace email verification.
- **No outside services at runtime.** No external fonts, CDNs, analytics or APIs; everything is served from the same server.
- **Strict usernames.** Lowercase Latin letters, digits and underscores only, which rules out look-alike Persian and Arabic characters.
- **Fail closed.** The application does not start without a `SECRET_KEY`, and `DEBUG` stays off unless it is turned on explicitly.
- **Text only in v1.** No uploads means no media storage, no image processing and a smaller attack surface.

## Tech stack

- Python 3.12, Django 6.1
- SQLite for development; PostgreSQL planned for production
- python-dotenv for configuration
- Docker planned for deployment

## Getting started

Requires Python 3.12.

macOS and Linux:

```bash
git clone https://github.com/sepehrkhasto/andarun.git
cd andarun
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Windows (PowerShell):

```powershell
git clone https://github.com/sepehrkhasto/andarun.git
cd andarun
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

Generate a secret key and put it in `.env` in place of `change-me`:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Then create the database and an admin account, and start the development server:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The admin is at <http://127.0.0.1:8000/admin/>.

## Configuration

All settings come from environment variables, loaded from `.env` in development.

| Variable | Required | Default | Notes |
| --- | --- | --- | --- |
| `SECRET_KEY` | Yes | none | The application will not start without it. |
| `DEBUG` | No | `False` | `1`, `true` or `yes` turns it on. |
| `ALLOWED_HOSTS` | No | empty | Comma-separated, for example `localhost,127.0.0.1`. |

## Tests

```bash
python manage.py test
```

There are no tests yet. Every phase in the roadmap lists its own tests as an exit criterion, starting with accounts.

## Project structure

```text
andarun/
├── config/       settings, URLs, WSGI and ASGI entry points
├── accounts/     custom user model and admin; sign-up and invitations come next
├── social/       profiles, posts, comments and follows (v1)
├── chat/         direct messages (v2)
├── groups/       group conversations (v2)
├── templates/    project-wide templates
├── static/       project-wide static files
└── manage.py
```

## Security

Please report vulnerabilities privately, as described in [SECURITY.md](SECURITY.md), and not in public issues.

## Roadmap

- **v1:** a text-only social network: accounts and invitations, profiles, posts, comments, likes, follows, feed, search, notifications, and deployment with Docker.
- **v2:** direct and group messages, then end-to-end encryption.
- **v3:** mobile clients and real-time updates with Django Channels.
- **v4:** images and object storage.

Details and progress: [ROADMAP.md](ROADMAP.md).

## About this project

Andarun is my main Django learning project, and I write all of its code by hand. Issues and suggestions are welcome.

## License

No license has been chosen yet, so all rights are reserved for now.
