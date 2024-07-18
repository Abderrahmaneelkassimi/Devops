pipeline {
agent any
stages {
    stage ('GIT Checkout'){
        steps {
            git changelog: false, poll: false, url: 'https://github.com/Tasfiq23/Devops_assessment_2.git'
        }
    }
    
    stage('build') {
  steps {
   '''
    echo 'Building'
    sh 'python3 operations.py'
    sh 'python3 calc.py'

    
   '''
  }
}
    stage ('Test'){
        steps {
            sh 'python3 -m unit-test.py'
        }
    }
}
}
