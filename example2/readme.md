# Building
This will build the Ubuntu 20.04 image alongside an SSH server. Reminder that regardless of if a container has SSH or not, you can still access it's terminal by manually executing bash as such:
<code>docker run -it image_name /bin/bash</code>
This should open the terminal through Docker directly, not as if it was it's own independent server.

In this example:

1. The Dockerfile starts with the official Ubuntu 20.04 image.
2. It updates the package lists and installs the SSH server (openssh-server).
3. The DEBIAN_FRONTEND=noninteractive environment variable is set to prevent interactive prompts during package installation.
4. After installing the SSH server, unnecessary package caches are cleaned to reduce the image size.
5. Password authentication for SSH is enabled (for demonstration purposes; in real scenarios, you'd likely use key-based authentication for better security).
6. The root password is set to "password" (again, for demonstration purposes).
7. Port 22 is exposed to allow SSH connections.
8. The SSH server is started in the foreground using the <code>CMD</code> instruction.

To build the Docker image, run the following command:
<code>docker build -t ubuntu-ssh:20.04 .</code>

Once the image is built, you can run a container from it using the following command:
<code>docker run -d -p 2222:22 --name my-ssh-container ubuntu-ssh:20.04</code>

See example1's readme.md file for more information.
