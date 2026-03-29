pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t inventory-api .'
            }
        }

      stage('Clean Old Containers') {
            steps {
                bat '''
                docker container prune -f
        '''
    }
}
        stage('Run Container') {
            steps {
                bat 'docker run -d -p 8000:8000 inventory-api'
            }
        }

       stage('Run Tests') {
            steps {
        bat 'npm install -g newman'
        bat 'cd tests && npx newman run postman_collection.json'
    }
}
       stage('Stop Container') {
            steps {
        bat '''
        for /F "tokens=*" %%i in ('docker ps -q') do docker stop %%i
        '''
    }
}

       stage('Create Zip') {
    steps {
        script {
            def timestamp = new Date().format("yyyy-MM-dd_HH-mm-ss")
            bat "powershell Compress-Archive -Path * -DestinationPath complete-${timestamp}.zip"
        }
    }
}
    }
}