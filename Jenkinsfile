pipeline {
    agent any
    
    stages{
        stage("Clone Code"){
            steps{
                echo "Cloning the code"
                git url:"https://github.com/MHamzaGhani/Jenkins.git",branch: "master"
                
            }
        }
        
        stage("Build"){
            steps {
                echo "building the image"
                // sh "docker build -t fast_pipeline_image ."
                
            }
            
        }
        
        stage("Run"){
            
            steps{
                echo "run the image"
                sh "docker run -d -p 8000:8000 fast_pipeline_image"
                
            }
        }
        
    }
    
    
    
    
}