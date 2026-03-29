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
                bat 'for /f "tokens=*" %%i in (\'docker ps -q\') do docker stop %%i'
                bat 'for /f "tokens=*" %%i in (\'docker ps -aq\') do docker rm %%i'
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
                bat '''
                powershell Compress-Archive -Path * -DestinationPath "complete-%DATE:~10,4%-%DATE:~4,2%-%DATE:~7,2%.zip"
        '''
    }
}
    }
}