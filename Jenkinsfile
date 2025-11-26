pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/iskilicaslan61/jenkinsfile-pipeline-project.git'
            }
        }

        stage('Kill old server') {
            steps {
                sh '''
                    echo "Killing old processes on port 3000..."
                    PID=$(lsof -t -i:3000) || true
                    if [ ! -z "$PID" ]; then
                        kill -9 $PID || true
                        echo "Killed process $PID"
                    else
                        echo "No process on port 3000"
                    fi
                '''
            }
        }

        stage('Start Python Server') {
            steps {
                sh '''
                    echo "Starting Python web server..."
                    nohup python3 python-welcome-page.py > server.log 2>&1 &
                    echo "Python server started on port 3000"
                '''
            }
        }
    }
}
