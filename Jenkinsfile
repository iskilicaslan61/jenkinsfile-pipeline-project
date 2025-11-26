pipeline {
    agent any

    environment {
        PYTHON_CMD = 'python3'
        SERVER_PORT = '3000'
        SCRIPT_NAME = 'python-welcome-page.py'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main', url: 'https://github.com/iskilicaslan61/jenkinsfile-pipeline-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Upgrading pip...'
                sh "${env.PYTHON_CMD} -m pip install --upgrade pip"
                // Uncomment if you have dependencies
                // sh "${env.PYTHON_CMD} -m pip install -r requirements.txt"
            }
        }

        stage('Run Python Server') {
            steps {
                script {
                    sh """
                        echo 'Stopping any existing Python server on port ${SERVER_PORT}...'
                        fuser -k ${SERVER_PORT}/tcp || true

                        echo 'Starting Python server in background...'
                        nohup setsid ${env.PYTHON_CMD} ${SCRIPT_NAME} > server.log 2>&1 &
                        sleep 2
                        echo 'Python server started. Logs: server.log'
                    """
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}
