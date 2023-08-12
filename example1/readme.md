# The Dockerfile

A Dockerfile is a text file that contains a set of instructions for building a Docker container image. It's used to define the environment and configuration needed to run an application within a container. The main parts of a Dockerfile include:

1. Base Image: The first line of a Dockerfile specifies the base image to start from. It defines the underlying operating system and environment for your application. For example, you might use an official Linux distribution or a specialized image tailored for your needs.
<code>FROM ubuntu:20.04</code>

2. Environment Setup: Subsequent lines in the Dockerfile involve setting up the environment for your application. This can include installing dependencies, setting environment variables, and creating directories.

<code>RUN apt-get update && apt-get install -y python3
ENV APP_HOME /app
WORKDIR $APP_HOME</code>

3. Copying Files: You can copy files from your local machine into the Docker image using the COPY instruction. This is commonly used to include application code and configuration files.

<code>COPY app.py $APP_HOME/app.py
COPY config.ini $APP_HOME/config.ini</code>

4. Running Commands: The RUN instruction allows you to run commands within the Docker image. This is often used for tasks like installing software, setting up databases, and configuring the system.

<code>RUN pip install Flask
RUN chmod +x $APP_HOME/app.py</code>

5. Exposing Ports: If your application listens on specific ports, you need to expose them to the host system using the EXPOSE instruction.

<code>EXPOSE 80</code>

6. Container Execution Command: The final step in the Dockerfile specifies how the container should be executed when it's run. This is done using the CMD instruction. It's important to note that the CMD instruction can be overridden when you start the container, allowing you to provide different execution commands without modifying the Dockerfile.

<code>CMD ["python3", "app.py"]</code>

Dockerfiles collectively define the building blocks and instructions for creating a container image that encapsulates your application along with its dependencies and configuration. Once the Dockerfile is ready, you can use the docker build command to create the container image, and the resulting image can then be used to run containers with consistent environments across different systems.

# Building

To build this example, try the following command:
<code>docker build -t my-docker-example .</code>
Breakdown:
1. <code>docker build</code> - This command is used to build a Docker image from a Dockerfile
2. <code>-t my-docker-example</code> - This flag specifies the name and an optional tag for the image. The optional tag in question is the version tag, used
   like "my-docker-example:1.0.0" or "my-docker-example:latest" if deploying your image as a consumer.
3. <code>.</code> - This specifies the build context, which is the directory containing the Dockerfile and any other files needed. The "." refers to the
   current directoy.

To run your built image, try the following command:
<code>docker run -p 8080:80 my-docker-example</code>
Breakdown:
1. <code>docker run</code> - This command is used to create and run a container from an existing Docker image.
2. <code>-p 8080:80</code> - This flag maps a port from the host to a port in the container. In this case, it takes port 80 (from the flask app
   inside the container) and maps it to port 8080 outside the container making it accessible from http://localhost:8080/.
3. <code>my-docker-example</code> - This is the name of the docker image you want to create a container from.
