#!/usr/bin/python
import subprocess
import paramiko
from snowboy import snowboydecoder

server='192.168.1.55'
server_port=5249
username="alarm"
password="wxg"
audio_file="/home/alarm/bin_data/success.wav"

def text_run(text):

    hit=False

    if 'radio' in text:
        if 'play' in text:
            if '1' in text or 'one' in text:
                run('ls')
                run("mplayer -ao pulse 'http://lhttp.qingting.fm/live/5022340/64k.mp3'")
                hit=True
            elif '2' in text or 'two' in text:
                run("mplayer -ao pulse 'http://lhttp.qingting.fm/live/275/64k.mp3'")
                hit=True
            else:
                pass
        elif 'stop' in text:
            run('killall mplayer');
            hit=True
    if 'speaker' in text or 'speak' in text:
        if 'open' in text:
            subprocess.call(['pacmd', 'set-default-sink', 'combined'])
            hit=True
        elif 'stop' in text:
            pass
    if 'music' in text:
        if 'play' in text:
            run('mocp -p')
            hit=True
        elif 'stop' in text:
            run('mocp -P')
            hit=True

    if hit:
        snowboydecoder.play_audio_file(audio_file)
    return hit

def run(cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server,port=server_port, username=username, password=password)
    return ssh.exec_command("nohup "+cmd+" > /dev/null 2>&1 &")

def test_connect():
    i,r,e = run('ls -l')
    print(r.readlines())

def main():
    test_connect()

if __name__ == "__main__":
    main()
