#!/bin/sh

F=`dirname $0`/../../bin/activate
BINDIR=`dirname $0`/../bin

. $F

$BINDIR/onoff.py --sensor 6:0 --state off

