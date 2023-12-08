# Penguin Species Prediction App with Docker

This project consists of a machine learning model to predict the species of penguins based on certain features. The model is served using a FastAPI server, and predictions can be made using a Streamlit client.

## Clone the Project

To clone the project, run the following command:

```bash
git clone https://github.com/cyriellebarailler26/mlops_docker.git
cd your-project
```

## Running the Application
### Using Docker Compose

You can use Docker Compose to build and run both the FastAPI server and the Streamlit client. Ensure you have Docker Compose installed.

```bash
docker-compose up --build
```

This command will build the Docker images and start the containers. The FastAPI server documentation will be accessible at http://localhost:8000/docs, and the Streamlit client will be accessible at http://localhost:8501.
