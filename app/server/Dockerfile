FROM python:3.10

# Create a virtual environment and activate it
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Set the working directory
WORKDIR /flask-deploy

# Copy the project files into the container
COPY . /flask-deploy

# Install project dependencies using pip and the requirements.txt file
RUN pip install -r requirements.txt

# Install Gunicorn with Gevent
RUN pip install gunicorn[gevent]

# Expose the required port
EXPOSE 5000

# Start the application with Gunicorn
CMD ["gunicorn", "--worker-class", "gevent", "--workers", "8", "--bind", "0.0.0.0:5000", "wsgi:app", "--max-requests", "10000", "--timeout", "5", "--keep-alive", "5", "--log-level", "info"]
