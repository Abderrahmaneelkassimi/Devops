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
   		 sh 'pip install pytest'
					 
     }
  }
    stage ('Test'){
        steps {
            sh 'pytest test_operations.py'
	    
        }
    }
}
}
