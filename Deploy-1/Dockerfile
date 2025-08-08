# 1. Use the official Python image
FROM python:3.10-slim

# 2. Set a working directory inside the container
WORKDIR /app

# 3. Copy all project files into the container
COPY . .

# 4. Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expose the port your FastAPI app will run on
EXPOSE 8000

# 6. Command to run the FastAPI app with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
