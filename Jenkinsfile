pipeline {
    agent any

    parameters {
        string(name: 'PERSON', defaultValue: 'Jenkins', description: 'Who should I say hello to?')

        text(name: 'BIOGRAPHY', defaultValue: '', description: 'Enter some information about the person')

        booleanParam(name: 'TOGGLE', defaultValue: true, description: 'Toggle this value')

        choice(name: 'CHOICE', choices: ['Start', 'Stop'], description: 'Pick something')

    }
    stages {
        stage('Example') {
            steps {
                echo "Hello ${params.PERSON}"

                echo "Biography: ${params.BIOGRAPHY}"

                echo "Toggle: ${params.TOGGLE}"

                echo "Choice: ${params.CHOICE}"
            }
        }
        stage('Python Script') {
            steps {
                withCredentials([aws(credentialsId: "760451896171", accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                    sh 'python3 script.py ${CHOICE}'
                }
            }
        }
    }
}
