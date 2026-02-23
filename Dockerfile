# Base Image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install system dependencies (important for ML apps)
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port
EXPOSE 8501

# Start FastAPI
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]