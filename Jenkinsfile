pipeline {
    agent any

    environment {
        IMAGE_NAME = "enterprise-rag"
        DOCKER_HUB = "saitejakorla"
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/Saitej-04/Enterprise-RAG-Assistant.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_HUB/$IMAGE_NAME:latest .'
            }
        }

        stage('Login Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $DOCKER_HUB/$IMAGE_NAME:latest'
            }
        }

        stage('Deploy Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }

    }

    post {
        success {
            echo 'Deployment Successful!'
        }

        failure {
            echo 'Deployment Failed!'
        }
    }
}