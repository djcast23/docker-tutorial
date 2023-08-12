# Use the official Ubuntu 20.04 image as the base
FROM ubuntu:20.04

# Update package lists and install the SSH server
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y openssh-server && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Enable password authentication for SSH (for demonstration purposes)
RUN echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config

# Set the root password (for demonstration purposes)
RUN echo 'root:password' | chpasswd

# Expose port 22 for SSH
EXPOSE 22

# Start the SSH server
CMD ["/usr/sbin/sshd", "-D"]

# This example requires no additional files.
