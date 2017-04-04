pipeline {
    agent any
    stages {
        stage('scm_checkout') {
            steps {	
                checkout([$class: 'GitSCM', branches: [[name: '*/feature-test-1']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: ' bb6b58d8-95ee-4709-966e-09d702139ebd', url: 'https://github.com/scotteverhart/myGitHubRepo.git']]])
            }
         }
         stage('scm_repull') {
            steps {
                 bat "git pull --all"
                 bat "git checkout feature-test-1"
            }
         }
         stage('Run_python') {
            steps {
                bat 'c:/python27/python ./PythonProjects/src/TestModule1.py'
            	bat "dir"
            	bat "cd"
            	bat "mkdir output_${env.BUILD_NUMBER}"
                bat "cd output_${env.BUILD_NUMBER}"
                bat "cd"
                bat "copy *.txt output_${env.BUILD_NUMBER}"
                bat "dir"
             }
          }
          stage('scm_push') {
             steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/development']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: ' bb6b58d8-95ee-4709-966e-09d702139ebd', url: 'https://github.com/scotteverhart/testJenkinsTarget.git']]])
                bat "git checkout development"
				withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'bb6b58d8-95ee-4709-966e-09d702139ebd', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD']]) {
				    bat 'git config --global user.name "scott everhart"'
				    bat 'git config --global user.email "scott.everhart1@gmail.com"'
				    bat "git pull origin development"
				    bat "cd"
				    bat "copy \"${env.WORKSPACE}\\output_${env.BUILD_NUMBER}\\*.txt\" ."
				    bat "cd"
				    bat "git add output_${env.BUILD_NUMBER}\\*.txt"
				    bat "cd"
				    bat "git tag -a \"jenkinsBuild_${env.BUILD_NUMBER}\" -m \"tag From Jenkins\""
				    bat "cd"
				    bat "git commit -m \"From Jenkins Pipeline Build ${env.BUILD_NUMBER}\""
				    bat "git push --tags"
				}
		      }
		   }
		   stage('Approval') {
		      steps {
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