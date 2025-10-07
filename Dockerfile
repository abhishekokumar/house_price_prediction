FROM python:3.9-slim

WORKDIR /app

# Install system dependencies + nginx + curl for healthcheck
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    nginx \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY client ./client/
COPY model ./model/
COPY Server ./Server/

# Configure nginx using EC2-style configuration
RUN echo 'server { \
    listen 80; \
    server_name _; \
    root /app/client; \
    index app.html; \
    \
    location /api/ { \
        rewrite ^/api(.*) $1 break; \
        proxy_pass http://127.0.0.1:5000; \
        proxy_set_header Host $host; \
        proxy_set_header X-Real-IP $remote_addr; \
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; \
        proxy_set_header X-Forwarded-Proto $scheme; \
        add_header Access-Control-Allow-Origin *; \
    } \
}' > /etc/nginx/sites-available/default

# Log to stdout/stderr
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

# Expose HTTP port
EXPOSE 80

# Health check for backend API
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:80/api/health || exit 1

# Copy start script to run Flask in background and nginx in foreground
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Start Flask and nginx
CMD ["/app/start.sh"]
