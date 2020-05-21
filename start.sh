#!/usr/bin/env bash
# shellcheck disable=SC2164
cd /home/caner/ryu-mininet/kafka_2.12-2.4.0
gnome-terminal --tab -x bin/zookeeper-server-start.sh config/zookeeper.properties
sleep 5
gnome-terminal --tab -x bin/kafka-server-start.sh config/server.properties
gnome-terminal --tab -x docker run -it --rm --privileged -e DISPLAY \
             -v /tmp/.X11-unix:/tmp/.X11-unix \
             -v /lib/modules:/lib/modules \
              iwaseyusuke/ryu-mininet -p 8080:8080 -p 6653:6653