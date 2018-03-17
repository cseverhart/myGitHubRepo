pipeline {
    agent any
    stages {
         stage('scm_checkout') {
            steps {	
                checkout([$class: 'GitSCM', branches: [[name: '*/myFirstPipeline']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: ' 38927baa-2326-4b88-b640-a736577219fe', url: 'https://github.com/scotteverhart/myGitHubRepo.git']]])
            }
         }
         stage('scm_repull') {
            steps {
                 sh "git pull --all"
                 sh "git checkout myFirstPipeline"
            }
         }
         stage('Run_python') {
            steps {
                sh 'c:/python27/python ./PythonProjects/src/TestModule1.py'
            	sh "dir"
            	sh "cd"
            	sh "mkdir output_${env.BUILD_NUMBER}"
                sh "cd output_${env.BUILD_NUMBER}"
                sh "cd"
                sh "copy *.txt output_${env.BUILD_NUMBER}"
                sh "dir"
                sh "dir"
             }
          }
          stage('scm_push') {
             steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/development']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: ' 38927baa-2326-4b88-b640-a736577219fe', url: 'https://github.com/scotteverhart/testJenkinsTarget.git']]])
                sh "git checkout development"
				withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: '38927baa-2326-4b88-b640-a736577219fe', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD']]) {
				    sh 'git config --global user.name "scott everhart"'
				    sh 'git config --global user.email "scott.everhart1@gmail.com"'
				    sh "git pull origin development"
				    sh "cd"
				    sh "copy \"${env.WORKSPACE}\\output_${env.BUILD_NUMBER}\\*.txt\" ."
				    sh "cd"
				    sh "git add output_${env.BUILD_NUMBER}\\*.txt"
				    sh "cd"
				    sh "git tag -a \"jenkinsBuild_${env.BUILD_NUMBER}\" -m \"tag From Jenkins\""
				    sh "cd"
				    sh "git commit -m \"From Jenkins Pipeline Build ${env.BUILD_NUMBER}\""
				    sh "git push --tags"
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