#!/bin/bash

# Make a request to download a stream and save it to a file

m3u8=$1
pathname=$2
ext=$3
filename="${pathname}.${ext}"

echo ${m3u8}
echo ${pathname}
echo ${ext}
echo ${filename}

avoidOverwrite () {
	suffix=0
	while [ -f "${filename}" ]
	do
		filename="${pathname}-${suffix}.${ext}"
		((suffix++))
	done
}

encodeStream () {
	avoidOverwrite

	# Encode live stream or VOD (depending on the given URL)
	# Encoding is set to being perceptually lossless and good audio quality to avoid huge filesize
	ffmpeg -i "${m3u8}" -c:v libx264 -preset veryfast -crf 18 -c:a aac -b:a 128k "${filename}"

}

encodeStream
