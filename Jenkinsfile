pipeline{
    agent any
    stages{
        stage('Checkout') {
            steps {
                checkout...
            }
        }
                                
        stage('Build'){
            steps {
                git branch https://github.com/ShayaneGonzalez/crud_luiza_code/tree/develop_shayane
            }
                                
        }
                                
        stage('Test'){
            steps{
                echo 'The job has been tested'
            }
        }

        stage('Production'){
            steps{
                echo 'The job has been put in production'
                }
        }
        }
        }