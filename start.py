"""
Start both FastAPI and Streamlit servers for local development.
Usage: python start.py
"""

import subprocess
import sys
import time
import os

def main():
    print("=" * 60)
    print("🛡️  SheShield AI – Starting Services")
    print("=" * 60)

    # Start FastAPI backend
    print("\n🚀 Starting FastAPI backend on http://localhost:8000")
    api_process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "api:app", "--reload", "--host", "0.0.0.0", "--port", "8000"],
        cwd=os.path.dirname(os.path.abspath(__file__)),
    )
    time.sleep(2)

    # Start Streamlit frontend
    print("🚀 Starting Streamlit frontend on http://localhost:8501")
    st_process = subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", "app.py", "--server.port", "8501"],
        cwd=os.path.dirname(os.path.abspath(__file__)),
    )

    print("\n" + "=" * 60)
    print("✅ Services Running:")
    print("   📡 API:      http://localhost:8000")
    print("   📡 API Docs: http://localhost:8000/docs")
    print("   🌐 Frontend: http://localhost:8501")
    print("=" * 60)
    print("\nPress Ctrl+C to stop all services.\n")

    try:
        api_process.wait()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down...")
        api_process.terminate()
        st_process.terminate()
        api_process.wait()
        st_process.wait()
        print("👋 Goodbye!")


if __name__ == "__main__":
    main()
