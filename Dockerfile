# Base image
FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app files
COPY . .

# Expose the port on which the app will run
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]