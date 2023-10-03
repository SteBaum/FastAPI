FROM ubuntu:20.04
# Install python
RUN apt-get update && apt-get install python3 python3-pip -y
# Copy file
COPY FastAPI_file.py requirements.txt ./
# Install requirements
RUN python3 -m pip install -r requirements.txt
# Run application
CMD ["python3", "-m", "uvicorn", "FastAPI_file:app", "--host", "0.0.0.0", "--port", "8080"]