# Start from a small official Python image
FROM python:3.12-slim

# Set the working folder inside the container
WORKDIR /app

# Install dependencies first (faster rebuilds)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# The app listens on port 5000
EXPOSE 5000

# Command to start the app
CMD ["python", "app.py"]
