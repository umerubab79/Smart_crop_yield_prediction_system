from pathlib import Path

folders = [
    "backend/app/routers",
    "backend/app/models",
    "backend/app/schemas",
    "backend/app/services",
    "backend/app/database",
    "backend/app/ml",
    "frontend/pages",
    "dataset",
    "reports",
    "docs"
]

files = [
    "backend/app/main.py",
    "backend/requirements.txt",
    "frontend/Home.py",
    "frontend/pages/Login.py",
    "frontend/pages/Register.py",
    "frontend/pages/Dashboard.py",
    "frontend/pages/Prediction.py",
    "frontend/pages/Result.py",
    "frontend/pages/History.py",
    "README.md"
]

for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)

for file in files:
    Path(file).touch(exist_ok=True)

print("Project structure created successfully!")