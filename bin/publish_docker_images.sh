#!/usr/bin/env bash

cd "$(dirname "$0")"

REPO=khatangatao

echo "Pushing build project into repo ${REPO}..."

for var in "$@"
do
    echo "Push $var..."
    docker push ${REPO}/khatangatao_$var:`cat ./version_$var`
done

echo "Complete!"
