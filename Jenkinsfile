pipeline {
    agent { docker { image 'python:3.11' } }
    environment{
        NAME='RETHVIK'
    }
    parameters{
        text(name:'age',defaultValue:15,description:'Options to select age')
        booleanParam(name:'OK',defaultValue:true,description:'I will say what in my mind')
    }
    stages {
        stage('Build') {
            steps {
                echo 'Build Stage'
                echo "user ${NAME}"
            }
        }
        stage('Run python file'){
            steps{
                script{
                    if ${params.OK}
                    {
                        sh 'python index.py 21'
                    }
                    else{
                        sh 'python index.py'
                    }
                }
            }
        }
    }
}
