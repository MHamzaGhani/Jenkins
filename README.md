# Chicago Crime Rate Prediction with Facebook Prophet

This repository contains code for building a predictive model using Facebook Prophet to forecast crime rates in Chicago. Additionally, a FastAPI application has been developed to expose an endpoint for users to upload their data and input the number of months for which they want to predict crime rates. Dockerization and Jenkins pipeline automation have also been implemented for easy deployment and continuous integration.

## Getting Started

### Prerequisites

- Python 3.x
- Docker
- Jenkins (for automation)
- FastAPI (Python library)

### Installation

1. **Clone this repository:**

    ```bash
    https://github.com/MHamzaGhani/Jenkins.git
    ```

2. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Build the Docker image:**

    ```bash
    docker build -t chicago-crime-prediction .
    ```

4. **Start the FastAPI application:**

    ```bash
    docker run -d -p 8000:8000 chicago-crime-prediction
    
    ```

## Usage

### 1. File Upload Endpoint

You can upload your data file to the following endpoint:
POST http://localhost:8000/upload


This endpoint allows you to upload your dataset, which will be used for crime rate prediction.

### 2. Endpoint for Crime Rate Prediction

Once you have uploaded your data using the `/upload` endpoint, you can access the endpoint for crime rate prediction at:
POST http://localhost:8000/predict


This endpoint allows you to specify the number of months for which you want to predict crime rates based on the uploaded data.

### 3. Jenkins Pipeline

The Jenkins pipeline has been set up to automate the deployment process. Whenever changes are pushed to the main branch, Jenkins will trigger a build and deployment of the Docker container, ensuring that the latest version of the application is always available.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add feature-name'`.
4. Push to your fork: `git push origin feature-name`.
5. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the Facebook Prophet team and the FastAPI community for their excellent tools and documentation, which made this project possible.



