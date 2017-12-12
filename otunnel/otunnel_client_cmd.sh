#!/usr/bin/env bash

chmod +x otunnel
./otunnel connect 106.14.248.127:10099 -s longlongsecret -t r:192.168.2.184:22::20080 >> otunnel.log 2>&1 &
