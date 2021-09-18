# Simple Shell Cleaner

## What is it?
A simple video downloader that downloads videos with the m3u8 extension. Example: video.m3u8.

## Available to

Linux

## How to Install

### Create (If it doesn't already exist) the .bash_aliases file on your home directory:
```
test -f ~/.bash_aliases && echo file already exists, please paste the next command. || touch ~/.bash_aliases
```
### Create a folder named shell_programs inside your home directory:
```
test -d ~/shell_programs && echo The folder already exists. Please, paste the next command. || mkdir ~/shell_programs
```
### Clone the M3u8 Video Downloader inside the shell_programs folder:
```
cd ~/shell_programs
git clone https://github.com/cryswerton/m3u8-video-downloader.git
```
### Create an alias in your .bash_aliases file:
```
echo "alias m3u8-get=\"~/shell_programs/m3u8-video-downloader/m3u8-downloader.h\"" >> ~/.bash_aliases
```
### Now just restart the terminal and it will work fine!