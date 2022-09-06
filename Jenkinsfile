pipeline {
    agent any
    triggers {
        cron('18 10 6 9 *')
    }
    parameters {
        string(name: 'PERSON', defaultValue: 'Jenkins', description: 'Who should I say hello to?')

        text(name: 'BIOGRAPHY', defaultValue: '', description: 'Enter some information about the person')

        booleanParam(name: 'TOGGLE', defaultValue: true, description: 'Toggle this value')

        choice(name: 'CHOICE', choices: ['One', 'Two', 'Three'], description: 'Pick something')

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
                sh 'python3 script.py'
            }
        }
    }
}
