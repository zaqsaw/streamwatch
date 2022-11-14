FROM ubuntu:22.04
RUN apt-get -qq update && \
    apt-get install -y python3 && \
    apt install -y python3-pip && \
    apt-get clean
RUN pip3 install virtualenv
ADD app /app
WORKDIR /app
RUN ./setup_venv.sh
ENTRYPOINT ./run_in_venv.sh

