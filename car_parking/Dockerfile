# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /parking


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# # Copy the current directory contents into the container at /app
# ADD . /parking
#
# # Install the dependencies
# RUN pip install -r requirements.txt
#
# # run the command to start uWSGI
# CMD ["uwsgi", "app.ini"]

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .