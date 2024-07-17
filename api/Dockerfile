FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . .

# Expose the port on which the Flask app runs
EXPOSE 5000

# Set environment variables
COPY .env .env

# Set the entry point to run the Flask app
CMD ["python", "main.py"]
