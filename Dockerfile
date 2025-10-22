# Use the official Python 3.12 slim image as a base
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt first (allows Docker to cache dependencies)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the code into the container
COPY . .

# Set entrypoint to run the calculator script
ENTRYPOINT ["python", "calculator.py"]
