FROM python:3.8.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy project to app directory
COPY ./pokedex/requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt
RUN apt-get update && apt install -y netcat

# Copy entrypoint.sh and set permissions
COPY ./pokedex/entrypoint.sh .
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Copy project files
COPY ./pokedex .

# Run entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
