# Use an official Python runtime as a parent image
FROM python:3.11.2-slim-bullseye

# Define environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

# Install git
RUN apt-get update && apt-get install -y git

# Set the working directory in the container
WORKDIR /code

# Clone the repository
ARG GITHUB_REPO_URL
RUN git clone ${GITHUB_REPO_URL} /code

# Install any needed packages specified in requirements.txt
COPY ./requirements.txt /code
RUN pip install --upgrade pip && pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

