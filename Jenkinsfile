pipeline {
    agent { docker { image 'node:16-alpine' } }
    stages {
        stage('building') {
            steps {
                sh 'node --version'
            }
        }
    }
}
