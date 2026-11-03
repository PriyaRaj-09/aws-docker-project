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
