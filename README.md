# Premium Digital Notice Board

Full-stack Django website for schools and colleges.

## Run on Windows

```powershell
cd premium_notice_board
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/

## First setup
1. Login at `/admin/`.
2. Add departments and categories.
3. Open Dashboard → Branding to add institution name, logo and contact details.
4. Publish notices from the dashboard.

## Keep data from the old project
Copy `db.sqlite3` from the old folder only if its database schema matches. The safer option is to use this as a fresh premium version.
