# Carbon Footprint Calculator (Flask)

A tiny web app to calculate and visualise carbon emissions from transport (km), electricity (kWh), and flights (hours).
Built on your original modules: `assessment3_backend.py` and `assessment3_visualization.py`.

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
# open http://localhost:5000
```

## Deploy to Render (recommended & free)

1. Create a **new private GitHub repo** and upload all files from this folder.
2. Go to Render.com → New → Web Service → connect your repo.
3. Use:
   - Environment: **Python**
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
4. Click **Create Web Service**. After deploy, you'll get a public URL you can put on your resume.

## Deploy to Railway (alternative)

1. Create a repo with these files.
2. Go to railway.app → New Project → Deploy from GitHub → select repo.
3. It will auto-detect, or set Start Command to `gunicorn app:app`.

## What the interviewer can do

- Visit your live URL.
- Enter numbers for distance (km), electricity (kWh) and flight hours.
- See total emissions + a bar chart.
- View the last 5 submissions saved to CSV.
