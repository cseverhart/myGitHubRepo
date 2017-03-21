pipeline {
    agent any
    stages {
        stage('build') {
            steps {
            		checkout([$class: 'GitSCM', branches: [[name: '*/myFirstPipeline']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '7d589385-d9d8-4006-9571-e70538886a93', url: 'https://github.com/scotteverhart/myGitHubRepo.git']]])
                	bat 'c:/python27/python ./PythonProjects/src/TestModule1.py'
            		bat 'dir'
            		input message: 'Enter your name', ok: 'Click Me', submitterParameter: 'ApprovingSubmitter'
            		echo "Approved by " $ApprovingSubmitter
           	}
        }
    }
	post {
        always {
        	echo "archiving files"
            archive '*.txt'
            echo "archiving complete"
        }
    }
}