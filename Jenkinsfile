pipeline{
    agent any
    environment{
        DATABASE_URI = credentials("DATABASE_URI")
        DOCKERHUB_CREDENTIALS = credentials("DOCKERHUB_CREDENTIALS")
    }
    stages{
        stage('Install Dependencies'){
            steps{
                sh "bash scripts/setup.sh"

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
                sh "bash scripts/deploy.sh"
            }
        }
    }
}