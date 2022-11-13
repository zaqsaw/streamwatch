FROM ubuntu:22.04
WORKDIR /app
RUN apt-get -qq update && \
    apt-get install -y ffmpeg && \
    apt-get clean
COPY m3u8_request.sh .
ENV M3U8=""
ENV NAME="stream"
ENV EXT="mp4"
ENTRYPOINT ./m3u8_request.sh ${M3U8} ${NAME} ${EXT}

