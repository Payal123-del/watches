Visit my Project:https://payal123-del.github.io/watches/index.html

Backend
-------

This project includes a simple Python Flask backend for the existing frontend files (`s.html`, `b.css`). The backend serves the static frontend and provides a few example API endpoints:

- `GET /api/products` — returns a sample product list
- `GET /api/products/<id>` — returns product details
- `POST /api/checkout` — accepts a JSON `cart` and returns a mock order id

Setup (Windows PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000/` in your browser to view the frontend.

Next steps

- Wire the frontend's JS to call the API endpoints (`/api/products`, `/api/checkout`).
- Replace the in-memory `PRODUCTS` list with a database as needed.
