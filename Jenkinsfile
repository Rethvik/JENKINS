pipeline {
    agent { docker { image 'python:3.11' } }
    stages {
        stage('Build') {
            steps {
                echo 'Build Stage'
            }
        }
        stage('Run python file'){
            steps{
                sh 'python index.py'
            }
        }
    }
}
