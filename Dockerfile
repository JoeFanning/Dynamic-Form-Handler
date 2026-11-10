# Use the official Python slim image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker caching
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose the port your app runs on (e.g., 5000 for Flask or 8000 for FastAPI)
EXPOSE 5000

# Command to run your application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
