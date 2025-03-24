# Use a base image with Python
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy your requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy your Flask app to the container
COPY . /app/

# Set environment variable for Flask (optional)
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Expose the port your Flask app is running on
EXPOSE 42055

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=42055"]
