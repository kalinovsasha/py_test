#!/bin/bash

/bin/nice -n +17 /usr/bin/rsync -a --exclude 'tmp' --remove-source-files /mnt/natlogs/nat root@192.168.1.1:/mnt/netflow
/bin/nice -n +17 /usr/bin/rsync -a --exclude 'tmp' --remove-source-files /mnt/natlogs/dns root@192.168.1.1:/mnt/netflow