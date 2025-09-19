# Use Python 3.13 slim image as base
FROM docker.arvancloud.ir/python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        gettext \
        && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Create directories for static and media files
RUN mkdir -p /app/staticfiles /app/static /app/media

# Expose port
EXPOSE 8000

# Run migrations and start Gunicorn
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput --clear && gunicorn RIML.wsgi:application --bind 0.0.0.0:8000 --workers 3"]
