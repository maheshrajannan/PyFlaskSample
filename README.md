unset DOCKER_HOST
unset DOCKER_TLS_VERIFY
unset DOCKER_TLS_PATH

Maheshs-MBP-3:PyFlaskSample2 maheshrajannan$ docker build -t myimage .
Sending build context to Docker daemon  67.58kB
Step 1/9 : FROM python:3.6.6-alpine
 ---> a78e257617d1
Step 2/9 : COPY src /app
 ---> Using cache
 ---> 64deeaa0244f
Step 3/9 : WORKDIR /app
 ---> Using cache
 ---> ad714ac04efc
Step 4/9 : RUN apk update && apk add libressl-dev libffi-dev gcc musl-dev
 ---> Using cache
 ---> 72e80a0ff6c8
Step 5/9 : RUN pip3 install -r requirements.txt
 ---> Using cache
 ---> 193a19f7077a
Step 6/9 : RUN python3 -m nltk.downloader punkt
 ---> Using cache
 ---> 41891844c4f4
Step 7/9 : EXPOSE 5000
 ---> Using cache
 ---> 6c410679cd1f
Step 8/9 : ENTRYPOINT ["python3"]
 ---> Using cache
 ---> f4380733849a
Step 9/9 : CMD ["analyse.py"]
 ---> Running in d29eed13770f
Removing intermediate container d29eed13770f
 ---> 0d53764fd009
Successfully built 0d53764fd009
Successfully tagged myimage:latest
Maheshs-MBP-3:PyFlaskSample2 maheshrajannan$ docker run -d -p 5000:5000 myimage
7183e177e7cbc2a790ae3ef134f2b541ac224989821b01f4d481877925e7b6be
Maheshs-MBP-3:PyFlaskSample2 maheshrajannan$ docker ps
CONTAINER ID        IMAGE               COMMAND                CREATED             STATUS              PORTS                    NAMES
7183e177e7cb        myimage             "python3 analyse.py"   4 seconds ago       Up 3 seconds        0.0.0.0:5000->5000/tcp   priceless_hermann
Maheshs-MBP-3:PyFlaskSample2 maheshrajannan$ 
