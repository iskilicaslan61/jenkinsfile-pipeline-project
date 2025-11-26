pipeline {
    agent any

    stages {
        
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/iskilicaslan61/jenkinsfile-pipeline-project.git'
            }
        }

        stage('Debug Workspace') {
            steps {
                sh '''
                    echo "Listing workspace contents:"
                    ls -la
                '''
            }
        }

        stage('Stop Old Server') {
            steps {
                sh '''
                    echo "Stopping old python server if running..."
                    pkill -f python-welcome-page.py || true
                '''
            }
        }

        stage('Start Python Server') {
            steps {
                sh '''
                    echo "Starting Python Web Server on port 3000..."
                    nohup python3 python-welcome-page.py > server.log 2>&1 &
                    sleep 2
                    echo "Server started."
                '''
            }
        }
    }

    post {
        success {
            echo "Build finished successfully. Server should be reachable now."
        }
        failure {
            echo "Build failed — check console log."
        }
    }
}
