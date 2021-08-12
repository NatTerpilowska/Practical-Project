pipeline{
    agent any
    environment{
        URI = credentials("DATABASE_URI")
        DOCKERHUB_CREDENTIALS = credentials("DOCKERHUB_CREDENTIALS")
    }
    stages{
        stage('Install Dependencies'){
            steps{
                sh "bash scripts/setup.sh"

            }
        }
        stage('Test App'){
            steps{
                sh "bash scripts/test.sh"
            }
        }
        stage('Build Images'){
            steps{
                sh "bash scripts/build.sh"
            }
        }
        stage('Configure VMs'){
            steps{
                sh "bash scripts/config.sh"
            }
        }
        stage('Deploy Stack'){
            steps{
                "bash scripts/deploy.sh"
            }
        }
    }
}