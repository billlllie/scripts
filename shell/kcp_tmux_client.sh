#!/bin/bash
TMUX_BIN="<path to tmux>"
UDP_SPEEDER_BIN="<path to udp speeder>"
KCP_CLIENT_BIN="<path to kcp>"
SERVER_IP="server ip"
SERVER_SPEEDER_PORT="speeder port"
SERVER_KCP_PORT="kcp port"
LOCAL_SPEEDER_PORT="local speeder port"
LOCAL_KCP_PORT="local kcp port"
SPEEDER_ARGS="-f 2:4"
KCP_ARGS="-key 'your password here' -crypt salsa20 -nocomp -datashard 2 -parityshard 2 -mtu 1350 -sndwnd 512 -rcvwnd 2048 -dscp 46 -mode fast3"


set -e
$TMUX_BIN new -s kcp -d
$TMUX_BIN rename-window -t "kcp:0" service
$TMUX_BIN send -t "kcp:service" "$UDP_SPEEDER_BIN -c -r$SERVER_IP:$SERVER_SPEEDER_PORT -l0.0.0.0:$LOCAL_SPEEDER_PORT $SPEEDER_ARGS" Enter
$TMUX_BIN split-window -v -t "kcp:service"
$TMUX_BIN send -t "kcp:service" "$KCP_CLIENT_BIN -l :$LOCAL_KCP_PORT -r $SERVER_IP:$SERVER_KCP_PORT $KCP_ARGS" Enter

echo "KCP in Tmux is up."