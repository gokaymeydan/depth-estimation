// Jenkinsfile for Poetry and Docker project
pipeline {
    agent any

    environment {
        // Jenkins agent'ın PATH'ine poetry'nin bin dizinini ekle
        PATH = "${env.HOME}/.local/bin:${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/gokaymeydan/depth-estimation.git', branch: 'main'
            }
        }

        stage('Setup Poetry') {
            steps {
                script {
                    sh 'python3 --version'
                    sh '''
                    if ! command -v poetry &> /dev/null
                    then
                        echo "Poetry could not be found, installing..."
                        curl -sSL https://install.python-poetry.org | python3 -
                    else
                        echo "Poetry is already installed."
                    fi
                    '''
                    sh 'poetry --version'
                }
            }
        }

        stage('Install All Dependencies') {
            steps {
                sh 'poetry install'
            }
        }

        stage('Lint and Format Check') {
            steps {
                // isort ile import sıralamasını kontrol et
                echo 'Checking import order with isort...'
                sh 'poetry run isort . --check-only'

                // black ile kod formatını kontrol et
                echo 'Checking code format with black...'
                sh 'poetry run black . --check'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Poetry kullanan güncel Dockerfile ile imajı oluştur
                    def appImage = docker.build("gokaymeydan/depth-estimation:${env.BUILD_NUMBER}")
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished. Cleaning up workspace...'
            cleanWs()
        }
    }
}