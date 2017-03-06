#!/bin/sh

date >> /tmp/zone2-wc.log
curl http://localhost:8080/api/scene/run/zone2 >>/tmp/zone2-wc.log

