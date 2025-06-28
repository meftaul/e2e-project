# Steps to run the Streamlit app(Manual Approach):

1. Ensure you have Python installed on your system.
2. Install the required packages by running:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the Streamlit app by executing:
   ```bash
   streamlit run app.py --server.port=8080 --server.address=0.0.0.0
   ```
4. Open your web browser and navigate to `http://localhost:8501` to view the app.


# Steps to run the Streamlit app(Docker Approach):

1. Ensure you have Docker installed on your system.
2. Build the Docker image by running:
   ```bash
   docker build -t meftaul/housing-app:v0.0.1 .
   ```
3. Run the Docker container with the following command:
   ```bash
   docker run -p 8080:8080 meftaul/housing-app:v0.0.1
   ```
4. Open your web browser and navigate to `http://localhost:8080` to view the app.

# Steps to run the from Docker registry:

1. Ensure you have Docker installed on your system.
2. Pull the Docker image from the registry:
3. ```bash
   docker pull meftaul/housing-app:v0.0.1
   ```
4. Run the Docker container with the following command:
   ```bash
   docker run -p 8080:8080 meftaul/housing-app:v0.0.1
   ```
5. Open your web browser and navigate to `http://localhost:8080` to view the app.