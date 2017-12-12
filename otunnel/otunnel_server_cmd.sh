#!/usr/bin/env bash

chmod +x otunnel
./otunnel listen :10099 -s longlongsecret >> otunnel.log 2>&1 &
