# Use the official Python image from the Docker Hub
FROM python:3.12.4-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Specify the command to run the app
CMD ["python", "-m", "hello_world.main"]
