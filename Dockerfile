# Use the Ubuntu 22.04 base image
FROM ubuntu:22.04


# Define an argument for Azure CLI version
ARG AZCLI_VERSION=2.55.0

# Update package lists and install required packages
RUN apt-get update \
    && apt-get install -y \
        curl \
        gnupg \
        lsb-release \
    && rm -rf /var/lib/apt/lists/*

# Download and install Microsoft's GPG key
RUN curl -sL https://packages.microsoft.com/keys/microsoft.asc | \
    gpg --dearmor | \
    tee /etc/apt/trusted.gpg.d/microsoft.gpg > /dev/null

# Set up Azure CLI repository
RUN AZ_REPO=$(lsb_release -cs) \
    && echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" | \
    tee /etc/apt/sources.list.d/azure-cli.list \
    && apt-get update \
    && apt-get install -y azure-cli=$AZCLI_VERSION-1~$AZ_REPO

# Set the entry point to bash
ENTRYPOINT [ "/bin/bash" ]
