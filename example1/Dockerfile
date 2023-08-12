# Use the official Ubuntu 20.04 image as the base
FROM ubuntu:20.04

# Update package lists and install Python 3 and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Set environment variables
ENV APP_HOME /app
WORKDIR $APP_HOME

# Copy application files
COPY app.py $APP_HOME/app.py
COPY config.ini $APP_HOME/config.ini

# Install Flask
RUN pip3 install Flask

# Expose port 80
EXPOSE 80

# Specify the command to run the application
CMD ["python3", "app.py"]

# In this example, let's assume you have a file named app.py that contains a simple Flask web application, and a configuration file named config.ini.
# The Dockerfile installs Python 3, copies your application files and configuration, installs the Flask library, exposes port 80, and sets the command to run your Flask application.

# To build the Docker image using this Dockerfile, navigate to the directory containing the Dockerfile and your application files, and then run the following command:
# docker build -t my-flask-app .

# This command will build the Docker image using the current directory (.) as the build context and tag it as my-flask-app.
# After the build is complete, you can run a container from the image using:
# docker run -p 8080:80 my-flask-app

# The command basically tells docker that it's going to run an image file, sets the ports (8080 is the port to show the app on
# and 80 is the flask server's port) and then provides the actual image file name.

# This maps port 8080 on your host machine to port 80 in the container, allowing you to access your Flask application in a web browser using http://localhost:8080.
# Remember that this is a simplified example, and in a real-world scenario, you might have more complex requirements and configurations.
