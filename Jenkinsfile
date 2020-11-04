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
         stage('Checkout SCM') {
            steps {
                // Because root could have taken over permissions inside a target folder
                sh 'sudo chown -R jenkins:jenkins ${WORKSPACE}'

                // This will ensure that all environment properties from a checkout() call
                // will be set correctly on this process (ie: GIT_BRANCH, GIT_URL).
                // Normally jenkins will handle this for us, but since the 'skipDefaultCheckout' option is set the
                // environment variables must be set explicitly.
                //
                // Checkout and set environment variables properly:
                // https://issues.jenkins-ci.org/browse/JENKINS-45198
                script {
                    checkout(scm).each { k,v -> env.setProperty(k, v) }
                }
            }
        }
        stage('Test') {
            steps {
                sh '''
                ls
                    python hello.py
                '''
            }
        }
    }
}
