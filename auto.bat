python -m venv venv
call venv/Scripts/activate.bat
pip install -r requirement.txt
@REM gunicorn main:app --workers 4 --worker-class
uvicorn main:app --reload --port 8000 --host 0.0.0.0 --workers 4 
REM End of auto.bat
