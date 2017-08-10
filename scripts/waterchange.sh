#!/bin/sh

date >> /tmp/waterchange.log
curl http://localhost:8080/api/scene/run/zone2 >>/tmp/waterchange.log
sleep 10
curl http://localhost:8080/api/scene/run/zone3 >>/tmp/waterchange.log
sleep 10
curl http://localhost:8080/api/scene/run/zone4 >>/tmp/waterchange.log
sleep 10
curl http://localhost:8080/api/scene/run/zone5 >>/tmp/waterchange.log
sleep 10
curl http://localhost:8080/api/scene/run/zone6 >>/tmp/waterchange.log

