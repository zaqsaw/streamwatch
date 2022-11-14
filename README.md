# streamwatcher

A simple application that queries a stream and downloads streams when they are live.

Build the docker image:
`./build.sh`

Setup the application settings in `docker/app/config.ini`

Run the docker container and download a stream to /tmp/stream.mp4
`./run {mount_directory}`

