# Use a minimal Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code from the terminology directory
COPY terminology /app/terminology

# Expose the port the app runs on
EXPOSE 8000

# Command to run the FastAPI application using environment variables
CMD ["sh", "-c", "uvicorn terminology.server.fhir_api:app --host ${OT_FHIR_LISTEN:-0.0.0.0} --port ${OT_FHIR_PORT:-8000}"]