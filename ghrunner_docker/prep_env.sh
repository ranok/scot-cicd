#!/bin/bash

echo "Preparing environment for GithHub action(s)"
#stty -echo
wget -q $CT_URL > /dev/null
#stty echo
echo "Unable to prepare environment!"
exit 1
