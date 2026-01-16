# Lung Cancer Prediction ML Application

A modern web application for lung cancer risk assessment using machine learning.

## Features

- **Modern UI**: Clean, step-by-step assessment form
- **ML-Powered**: Uses scikit-learn for lung cancer prediction
- **Responsive Design**: Works on desktop and mobile devices
- **Docker Ready**: Complete containerization for easy deployment

## Quick Start

### Prerequisites
- Python 3.9+
- Docker (optional)

### Local Development
```bash
# Clone the repository
git clone <repository-url>
cd Lung-Cancer-Prediction-ML

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Visit: http://localhost:5000

### Docker Deployment

#### Using Docker Compose (Recommended)
```bash
# Build and run with Docker Compose
docker-compose up --build

# Run in background
docker-compose up --build -d

# View logs
docker-compose logs -f
```

#### Using Docker
```bash
# Build the image
docker build -t lung-cancer-prediction .

# Run the container
docker run -p 5000:5000 lung-cancer-prediction
```

### Production Deployment

The application is configured for production deployment with:
- **Gunicorn WSGI server** for handling multiple requests
- **Health checks** for container orchestration
- **Non-root user** for security
- **Auto-restart** policies

## Deployment Options

### Heroku
```bash
# Install Heroku CLI, then:
heroku create your-app-name
git push heroku main
```

### AWS ECS
```bash
# Build and push to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account>.dkr.ecr.us-east-1.amazonaws.com
docker build -t lung-cancer-prediction .
docker tag lung-cancer-prediction:latest <account>.dkr.ecr.us-east-1.amazonaws.com/lung-cancer-prediction:latest
docker push <account>.dkr.ecr.us-east-1.amazonaws.com/lung-cancer-prediction:latest
```

### Google Cloud Run
```bash
# Build and deploy
gcloud run deploy lung-cancer-prediction --source . --platform managed --region us-central1
```

### DigitalOcean App Platform
1. Connect your GitHub repository
2. Select "Deploy from GitHub"
3. The app will be auto-detected and deployed

## Application Structure

```
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml   # Docker Compose setup
├── templates/           # HTML templates
│   ├── index.html      # Main assessment form
│   └── result.html     # Result display
└── *.pkl              # Trained ML models
```

## Technology Stack

- **Backend**: Flask, Python 3.9
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **ML**: scikit-learn, pandas, numpy
- **Server**: Gunicorn
- **Container**: Docker

## Environment Variables

- `FLASK_ENV`: Set to "production" for production deployment
- `PORT`: Port number (default: 5000)

## Health Check

The application includes health checks at `/` endpoint for container orchestration.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License

## Disclaimer

This application is for educational and informational purposes only. The results should not be considered as medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical concerns.