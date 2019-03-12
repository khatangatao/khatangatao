#!/usr/bin/env bash

cd "$(dirname "$0")"

REPO=hub.docker.com

echo "Starting build project..."

for var in "$@"
do
    echo "Build $var..."
    docker build -t ${REPO}/khatangatao_$var:`cat ./version_$var` -f ../docker/$var/Dockerfile ..
done

echo "Complete!"