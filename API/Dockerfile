FROM python:3.9.7

# Copy local code into docker image
ADD ./ /miapi

# Change working directory to be the copied folder
WORKDIR /miapi

# Install code dependencies
RUN pip install -r requirements.txt

## This is the command that will be executed in "docker run <imagename>"
CMD [ "uvicorn", "main:app" ]
