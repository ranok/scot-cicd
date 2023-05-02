# GitLab token

This folder contains information about tokening a GitLab instance (self-hosted primarily)

## Instance prep

This [diff](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/119326/diffs?commit_id=a24964c42ac68213a9015e6f2f327c8461c7b8ff) is needed to improve the timeliness
of alerts. If it is not applied, alerts for a specific token will only fire once every 24 hours.

## Creating tokens

The script gitlab.py will generate tokens provided a GitLab instance base URL (e.g. https://git.r4n0k.com), target user id (e.g., 2), and GitLab PAT that has admin
 permissions to generate tokens, and a token name. 

## Detecting usage

The code in gitlab-lambda.py can be run periodically (set to every 2 min) in a AWS Lambda with the BASE_URL, CT_URL, PULL_UID, and tc variables updated. This 
will check for a token that has been used recently and issue a GET to the canarytokens URL with the tokenname as a path param. If you create a web-bug token, then
use that token id as the token name, this will allow you to get a canarytoken alert for GitLab usage.