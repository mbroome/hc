#!/bin/sh

date >> /tmp/zone3-wc.log
curl http://localhost:8080/api/scene/run/zone3 >>/tmp/zone3-wc.log

