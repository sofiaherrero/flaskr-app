# Use Python 3
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# RUN export FLASK_ENV=development this export won't persist across images (each Dockerfile directive will generate an intermediate container, committed into an intermediate image: that image won't preserve the exported value) but ENV will persist
ENV FLASK_APP flaskr
ENV FLASK_ENV development 

RUN ["python", "-m", "flask", "init-db"] 

ENTRYPOINT ["python"]

# Bind to the 0.0.0.0 IP address for the web server to accept connections originating from outside of the container (instead of 127.0.0.1 which is inside the container)
CMD ["-m", "flask", "run", "-h", "0.0.0.0"] 