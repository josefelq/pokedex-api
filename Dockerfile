FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy project to app directory
COPY pokedex /app
WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt
RUN apt-get update && apt install -y netcat

# Copy entrypoint.sh
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Run entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
