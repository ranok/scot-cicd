# Docker container for a GitHub self-hosted runner token

This folder contains the Dockerfile needed to build a Docker container to act as a deception GitHub self-hosted runner. 
It will establish a connection with GitHub, listen for jobs assigned to self-hosted runners, and alert the creator of the attempt before 
failing job execution (before the possibly-malicious job is run).

## Building

`docker build . -t ghrunner`

## Running

`docker run -r ghrunner -e "EMAIL_TO_ALERT" -r "ORG/REPO" -t "GITHUB_REPO_TOKEN"`

Where the email is the address you want alerts sent to, ORG/REPO is the Github organization/user and repo name (e.g., this is ranok/scot-cicd), 
and the token is found on the [self-hosted runner creation page](https://github.com/ORG/REPO/settings/actions/runners/new)

If you want to reclaim your TTY, you can run the docker command with `-d` to have it ru in detatched mode.

You should be able to see the runner appear on the [repo runners setting page]((https://github.com/ORG/REPO/settings/actions/runners/)
