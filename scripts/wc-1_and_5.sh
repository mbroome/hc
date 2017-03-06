#!/bin/sh

date >> /tmp/zone1-5-wc.log
curl http://localhost:8080/api/scene/run/zone1 >>/tmp/zone1-5-wc.log
curl http://localhost:8080/api/scene/run/zone5 >>/tmp/zone1-5-wc.log

