# CSIT327-G5-Lao-ErosJohn-FirstDjango

## Student Information

- **Full name:** Eros John Lao
- **Section:** G5

## Run Locally

1. Clone the repository and enter the project folder:

   ```powershell
   git clone https://github.com/ErosJohn8888/CSIT327-section-Lao-ErosJohn-FirstDjango.git
   cd CSIT327-section-Lao-ErosJohn-FirstDjango
   ```

2. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies and initialize the database:

   ```powershell
   pip install -r requirements.txt
   python manage.py migrate
   ```

4. Start the development server:

   ```powershell
   python manage.py runserver 127.0.0.1:8080
   ```

5. Open <http://127.0.0.1:8080/> in a browser.

The checked-in Django secret key fallback is for local development only. Set
`DJANGO_SECRET_KEY` to a private value when deploying the project.
