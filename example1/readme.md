## Dockerfile

```Dockerfile
# Use an official Ubuntu 20.04 image as the base
FROM ubuntu:20.04

# Update package lists and install Python 3
RUN apt-get update && apt-get install -y python3

# Set an environment variable for the application's home directory
ENV APP_HOME /app

# Set the working directory
WORKDIR $APP_HOME

# Copy the application code and configuration files
COPY app.py $APP_HOME/app.py
COPY config.ini $APP_HOME/config.ini

# Install Flask framework
RUN pip install Flask

# Make the application script executable
RUN chmod +x $APP_HOME/app.py

# Expose port 80 for the application
EXPOSE 80

# Define the command to run the application
CMD ["python3", "app.py"]
