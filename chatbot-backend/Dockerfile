# Use a Python base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code to the container
COPY . /app/

# Expose port 5000 for the Flask app
EXPOSE 5000

# Command to run the backend server
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
