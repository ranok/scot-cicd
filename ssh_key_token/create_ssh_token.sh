#!/bin/bash

# To be run (as root) on the target server
# Requires the faker python3 module to be installed

EMAIL=$1

USERNAME=$(python3 -c "import faker; fake = faker.Faker(); print(fake.user_name())")
TCURL=$(python3 ../ghrunner_docker/gen_token.py web "$EMAIL" "SSH login on $HOSTNAME")

echo "Creating user: $USERNAME"
useradd $USERNAME --shell /usr/sbin/nologin -m
mkdir -p /home/$USERNAME/.ssh
ssh-keygen -f /tmp/deploy_key -N ""
mv /tmp/deploy_key.pub /home/$USERNAME/.ssh/authorized_keys
chown -R $USERNAME:$USERNAME /home/$USERNAME/.ssh/

echo "Adding alerter to /etc/ssh/sshrc"
cat sshrc_snippet | sed -e "s/USERNAME/$USERNAME/" | sed -e "s%TOKEN%$TCURL%" >> /etc/ssh/sshrc

echo "Below is the SSH key to be used in SSH as $USERNAME@$HOSTNAME"
cat /etc/deploy_key