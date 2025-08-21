
import os
import sys
import subprocess
import uvicorn

if __name__ == "__main__":
    # Activate virtual environment if present
    venv_activate = os.path.join("venv", "Scripts", "activate_this.py")
    if os.path.exists(venv_activate):
        print("🔄 Activating virtual environment...")
        with open(venv_activate) as f:
            exec(f.read(), {'__file__': venv_activate})

    # Prevent __pycache__ creation globally
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
    sys.dont_write_bytecode = True

    # Get mode from command-line argument, default to 'dev'
    mode = sys.argv[1] if len(sys.argv) > 1 else "dev"
    os.environ["APP_ENV"] = mode

    print(f"🚀 Running FastAPI app via run.py in {mode} mode...")

    app_path = "app.main:app"
    reload = mode == "dev"

    uvicorn.run(app_path, host="127.0.0.1", port=8000, reload=reload)
