# Use a Python 3.12 image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Flask app and cracking script to the container
COPY app.py /app/app.py
COPY crack.py /app/crack.py

# Install Flask and other dependencies
RUN pip install --no-cache-dir flask

# Expose the port Flask will run on
EXPOSE 5050

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
ENV PATH="/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
ENV HOSTNAME=ed7471a94fda
ENV PYTHON_VERSION=3.12.12
ENV PYTHONUNBUFFERED=1

# Install additional dependencies if required
RUN pip install hashlib

# Command to run Flask app
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5050"]
