pipeline {
    agent any
    stages {
        stage('build') {
            steps {	
                checkout([$class: 'GitSCM', branches: [[name: '*/myFirstPipeline']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: ' bb6b58d8-95ee-4709-966e-09d702139ebd', url: 'https://github.com/scotteverhart/myGitHubRepo.git']]])
                bat "git pull --all"
                bat "git checkout myFirstPipeline"
                bat 'c:/python27/python ./PythonProjects/src/TestModule1.py'
            	bat 'dir'
            	bat "mkdir output_${env.BUILD_NUMBER}"
                bat "cd output_${env.BUILD_NUMBER}"
                bat "copy *.txt output_${env.BUILD_NUMBER}"
                checkout([$class: 'GitSCM', branches: [[name: '*/development']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: ' bb6b58d8-95ee-4709-966e-09d702139ebd', url: 'https://github.com/scotteverhart/testJenkinsTarget.git']]])
                bat "git checkout development"
				withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'bb6b58d8-95ee-4709-966e-09d702139ebd', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD']]) {
				    bat 'git config --global user.name "scott everhart"'
				    bat 'git config --global user.email "scott.everhart1@gmail.com"'
				    bat "git pull origin development"
				    bat "git add *.txt"
				    bat "git tag -a \"jenkinsBuild_${env.BUILD_NUMBER}\" -m \"tag From Jenkins\""
				    bat "git commit -m \"From Jenkins Pipeline Build ${env.BUILD_NUMBER}\""
				    bat "git push --tags"
				}
            	input message: 'Approval required to begin gitTest build', ok: 'Approve', submitterParameter: 'ApprovingSubmitter'
            	build 'gitTest'
           	}
        }
    }
	post {
        always {
        	echo 'archiving files'
            archive '*.txt'
            echo 'archiving complete'
        }
    }
}