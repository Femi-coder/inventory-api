pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t inventory-api .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 8000:8000 inventory-api'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'cd tests && newman run postman_collection.json'
            }
        }

        stage('Stop Container') {
            steps {
                bat 'docker ps -q | for /f %i in (\'more\') do docker stop %i'
            }
        }

        stage('Create Zip') {
            steps {
                bat 'powershell Compress-Archive -Path * -DestinationPath complete-%DATE%-%TIME%.zip'
            }
        }
    }
}