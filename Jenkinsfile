pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/vikas-j-v/calc-app.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Lint Code') {
            steps {
                sh './venv/bin/flake8 calculator.py --max-line-length=100 || true'
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/bin/pytest calc_test.py --junitxml=report.xml'
            }
        }

        stage('Build Package') {
            steps {
                sh './venv/bin/python -m py_compile calc.py'
                echo 'Build successful — calc.py compiled.'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying calculator app...'
                sh 'mkdir -p /tmp/deploy && cp calc.py /tmp/deploy/'
                echo 'Deployment complete.'
            }
        }
    }

    post {
        always {
            junit 'report.xml'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs.'
        }
    }
}