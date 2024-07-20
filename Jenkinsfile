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
   		 sh 'python3 operations.py'
					 
     }
  }
    stage ('Test'){
        steps {
            sh 'python3 -m unit-test'
	    
        }
    }
}
}
