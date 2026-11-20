pipeline{
  agent any
  stages{
    stage('Test'){
      steps{
        echo'Checking python application'
        bat'python -m py compile app.py'
      }
    }
    stage('Run Application'){
      steps{
        bat'python app.py'
      }
    }
  }
  post{
    success{
      echo'CI Pipeline completed successfully'
    }
    failure{
      echo'CI Pipeline failed'
    }
  }
}
