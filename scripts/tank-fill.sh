#!/bin/sh

date >> /tmp/tank-fill.log
curl -XPOST -d "state=1" http://localhost:8080/api/state/nodeid/6/childid/5 >>/tmp/tank-fill.log

