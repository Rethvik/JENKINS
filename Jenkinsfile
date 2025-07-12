df userScript
pipeline {
    agent { docker { image 'python:3.11' } }
    environment{
        NAME='RETHVIK'
    }
    parameters{
        text(name:'age',defaultValue:'15',description:'Enter your age')
        booleanParam(name:'OK',defaultValue:true,description:'I will say what in my mind')
    }
    stages {
        stage('init'){
            steps{
                script{
                    userScript = load "script.grrovy"
                }
            }
        }
        stage('Build') {
            steps {
                script{
                    userScript.greetUser()
                }
            }
        }
        stage('Run python file'){
            steps{
                    script{
                if(params.OK){
                        userScript.suggestUser()
                }
                    }
            }
        }
    }
}
