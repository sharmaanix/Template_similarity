FROM python:3.8
RUN pip3 install pipenv
COPY . /app
WORKDIR /app
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pipenv install --system --skip-lock
ENTRYPOINT [ "python3" ]
CMD ["main.py"]