# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirement file & install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Cloud Run expects the app to listen on $PORT
ENV PORT=8080

# Command to run the web server
CMD ["gunicorn", "-b", "0.0.0.0:8080", "main:app"]
