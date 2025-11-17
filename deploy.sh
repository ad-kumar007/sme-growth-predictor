#!/bin/bash
# Quick deployment script for SME Growth Predictor

echo "🚀 SME Growth Predictor - Deployment Script"
echo "==========================================="
echo ""

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
echo "Checking prerequisites..."

if ! command_exists docker; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

if ! command_exists docker-compose; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "✅ Prerequisites check passed"
echo ""

# Create .env if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file from .env.example..."
    cp .env.example .env
    echo "✅ .env file created"
    echo "⚠️  Please update .env with your configuration"
    echo ""
fi

# Ask user what to do
echo "Select deployment option:"
echo "1) Local Docker deployment"
echo "2) Build for production"
echo "3) Stop all services"
echo "4) View logs"
echo ""
read -p "Enter option (1-4): " option

case $option in
    1)
        echo ""
        echo "🐳 Starting local Docker deployment..."
        docker-compose up --build
        ;;
    2)
        echo ""
        echo "🏗️  Building for production..."
        docker-compose -f docker-compose.yml build
        echo "✅ Build complete"
        echo ""
        echo "To deploy to cloud:"
        echo "- Backend: Push to Render/Railway"
        echo "- Frontend: Push to Vercel/Netlify"
        echo ""
        echo "See DEPLOYMENT.md for detailed instructions"
        ;;
    3)
        echo ""
        echo "🛑 Stopping all services..."
        docker-compose down
        echo "✅ Services stopped"
        ;;
    4)
        echo ""
        echo "📋 Viewing logs..."
        docker-compose logs -f
        ;;
    *)
        echo "Invalid option"
        exit 1
        ;;
esac
