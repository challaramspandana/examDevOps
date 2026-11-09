pipeline{
    agent any
        stages{
            stage('Build the docker application'){
                steps{
                    echo 'Building the application'
                    bat 'docker build -t myapp .'
                }
            }
            stage('Running the Docker Application'){
                steps{
                    echo 'Running the application'
                    bat 'docker rm -f mycontainer || exit 0'
                    bat 'docker run -p 5000:5000 myapp'
                }
            }
            stage('Testing the Application'){
                steps{
                    echo 'Testing the application'
                    bat 'curl http://localhost:5000'
                }
            }
            
        }
        post{
            success{
                echo 'Application is running'
            }
            failure{
                echo 'Application is not running'
            }
        }
    }
