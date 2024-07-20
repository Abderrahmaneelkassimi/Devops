pipeline {
agent any
stages {
    stage ('GIT Checkout'){
        steps {
            echo "cheking out"
        }
    }
    
    stage('build') {
        steps {
   		 sh 'python3 operations.py'
					 
     }
  }
    stage ('Test'){
        steps {
            sh 'python3 -m test_operations'
	    
        }
    }
}
}
