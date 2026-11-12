# AWS + Linux + Docker Project

A Flask web app with a visitor counter, deployed on an AWS EC2 Ubuntu server using Docker Compose.

## Architecture
Browser → Nginx (port 80) → Flask app (port 5000) → Redis

## Tech Stack
- **AWS EC2** – Ubuntu Linux server
- **Docker & Docker Compose** – containerization
- **Nginx** – reverse proxy
- **Flask (Python)** – web app
- **Redis** – stores the visit count

## How to Run
```bash
git clone https://github.com/<your-username>/aws-docker-project.git
cd aws-docker-project
docker compose up -d --build
```
Then open `http://<server-ip>` in a browser.

## CI/CD Pipeline (GitHub Actions)
Every push to `main` automatically deploys to the EC2 server.

**Flow:** git push → GitHub Actions → SSH into EC2 → git pull → docker compose up --build → restart Nginx → health check

- Server details and SSH key are stored as encrypted **GitHub Secrets**
- A health check on `/health` retries for ~30 seconds
- If the app doesn't come up healthy, the pipeline **fails** and prints the app's error logs
