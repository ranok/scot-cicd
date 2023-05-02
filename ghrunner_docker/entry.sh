#!/bin/bash

export ACTIONS_RUNNER_HOOK_JOB_STARTED=/prep_env.sh

while getopts e:r:t: flag
do
    case "${flag}" in
	e) EMAIL=${OPTARG};;
	r) REPO=${OPTARG};;
	t) TOKEN=${OPTARG};;
    esac
done

TURL=$(python3 /gen_token.py web "$EMAIL" "GitHub self-hosted runner for $REPO")
export CT_URL=$TURL

URL="https://github.com/$REPO"
/gh/actions-runner/config.sh --unattended --url $URL --token $TOKEN
/gh/actions-runner/run.sh



