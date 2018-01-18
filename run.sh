#!/bin/bash

VERSION="0.1.0"

# Build the docker container
docker build -t haystax-twitter-api-frontend:$VERSION .

# Run the docker container, and assign the port to host it externally (in a local environment)
docker run -d -p 5000:5000 haystax-twitter-api-frontend:$VERSION