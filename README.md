# scot-cicd

I got off scot CI/CD. This repo name is terrible, I am very sorry, but basically it contains a bunch of scripts to go along with my [T2'23](https://t2.fi/)
talk about deception in CI/CD environments. 

Each folder contains a different capability:
* ghrunner_docker - This contains code to launch a Docker container that attaches to a GitHub repo as a self-hosted runner and alerts on actions
* gitlab_token - This contains code to create and alert on token GitLab personal access tokens
* ssh_key_token - This contains scripts to create and alert on SSH key usage
* github_auditor - This contains code to audit a GitHub enterprise audit log to look for usage of tokened PATs


