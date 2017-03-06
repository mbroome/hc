#!/bin/sh

date >> /tmp/lights.log
curl -XPOST -d "state=0" http://localhost:8080/api/state/nodeid/6/childid/0 >>/tmp/lights.log

