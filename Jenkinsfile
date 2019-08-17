pipeline {
    agent any
    stages {
         stage('start_pipeline') {
            steps {
                sh 'echo "Start Pipeline"'
            }
         }
         stage('scm_checkout') {
            steps {	
                checkout([$class: 'GitSCM', branches: [[name: '*/Development']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '40c21658-7efb-48d6-a1cb-865bd192e63b', url: 'https://github.com/scotteverhart/myGitHubRepo.git']]])
            }
         }

         stage('Run_python') {
            steps {
                sh 'python ./PythonProjects/src/TestModule1.py'
            	sh "ls -alF"
            	sh "cd"
            	sh "mkdir output_${env.BUILD_NUMBER}"
                sh "cd output_${env.BUILD_NUMBER}"
                sh "cd"
                sh "cp *.txt output_${env.BUILD_NUMBER}"
                sh "ls -alF"
                sh "ls -alF"
             }
          }
          stage('scm_push') {
steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/development']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '40c21658-7efb-48d6-a1cb-865bd192e63b', url: 'https://github.com/scotteverhart/testJenkinsTarget.git']]])
                sh "git checkout development"
				withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'bb6b58d8-95ee-4709-966e-09d702139ebd', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD']]) {
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
            archiveArtifacts '*.txt'
            echo 'archiving complete'
        }
    }
}
