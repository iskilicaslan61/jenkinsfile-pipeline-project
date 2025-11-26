pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/iskilicaslan61/jenkinsfile-pipeline-project.git'
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
