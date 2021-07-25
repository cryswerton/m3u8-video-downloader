#! /bin/bash

COMMAND="ffmpeg"

# check if the ffmpeg command is installed on the system.
command -v $COMMAND >/dev/null 2>&1 || { echo >&2 "I require $COMMAND but it's not installed.  Aborting."; exit 1; }

# check if the argument string is empty.
if [ -z "$1" ]
  then
    echo "No argument supplied"
    exit
fi

# download the m3u8 video by passing its link as argument.
ffmpeg -protocol_whitelist file,http,https,tcp,tls,crypto -i "$1" -c copy video.mp4
