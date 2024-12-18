# Use the official Python image as a base image
FROM python:3.9-slim

# Set environment variables to prevent Python from writing .pyc files and enable buffer flushing
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file if you have one, or manually install dependencies
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app code into the container
COPY . /app/

# Expose port 8080
EXPOSE 8080

# Run the Flask app
CMD ["python", "app.py"]
