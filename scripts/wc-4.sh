#!/bin/sh

date >> /tmp/zone4-wc.log
curl http://localhost:8080/api/scene/run/zone4 >>/tmp/zone4-wc.log

