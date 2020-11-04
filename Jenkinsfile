#!groovy

pipeline {
    agent {
        node {
            label 'jenkins-dynamic-worker-gcp'
        }
    }
    options {
        timeout(time: 3, unit: 'MINUTES')
        timestamps()

        // Since we use docker for our integration tests, root may have ownership of some folder.
        // We need to force jenkins to use a custom build step for checking out the project so
        // that we can run a chown on this directory before cleaning it.
        skipDefaultCheckout true
    }
    stages {
        stage('Test') {
            steps {
                sh '''
                    python $WORKSPACE/hello.py
                '''
            }
        }
    }
}
