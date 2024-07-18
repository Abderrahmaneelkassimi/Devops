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
   		 sh 'python3 -m venv venv'
		 
     }
    stage ('Test'){
        steps {
            sh 'python3 -m unit-test'
	     def testResult = sh(script: '''#!/bin/bash
                        source venv/bin/activate
                        python3 -m unittest discover -s . -p "test*.py"
                    ''', returnStatus: true, label: 'Running Tests')
                    
                    if (testResult != 0) {
                        error 'Unit tests failed'
                    }
        }
    }
}
}
