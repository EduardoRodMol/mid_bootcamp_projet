FROM python:3.9.7

# Copy local code into docker image
ADD ./ /miapi

# Change working directory to be the copied folder
WORKDIR /miapi

# Install code dependencies
RUN pip install -r requirements.txt

## This is the command that will be executed in "docker run <imagename>"
ENV PORT=8080

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]
