# SSH key token

This folder contains scripts to create users on a server along with keys that when used trigger an alert

## Creating a decoy key

You'll need to `pip3 install faker` on the target server to install the dependency.

With the whole repo on the target server, run `./create_ssh_token.sh EMAIL_TO_ALERT` and it will:
* Create a new user based on a faker username that cannot login (shell is /usr/sbin/nologin)
* Create an SSH keypair for that user and set that public key in their authorized_hosts file
* Create a canarytoken web-bug that alerts the user
* Adds an entry to /etc/ssh/sshrc that if the user trying to login is the decoy user, fire the alert