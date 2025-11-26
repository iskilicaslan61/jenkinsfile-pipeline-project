pipeline {
    agent any

    environment {
        // Define Python version if needed, e.g., python3
        PYTHON_CMD = 'python3'
    }

    stages {
        stage('Checkout') {
            steps {
                // Clone your GitHub repository
                git branch: 'main', url: 'https://github.com/iskilicaslan61/jenkinsfile-pipeline-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // If you have dependencies, install them here (e.g., Flask, etc.)
                sh "${env.PYTHON_CMD} -m pip install --upgrade pip"
                // Example: sh "${env.PYTHON_CMD} -m pip install -r requirements.txt"
            }
        }

        stage('Run Python Server') {
            steps {
                // Run your Python script in background
                sh "${env.PYTHON_CMD} python-welcome-page.py &"
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}
