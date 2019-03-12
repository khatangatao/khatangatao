#!/bin/bash
for line in $(cat requirements.pip)
do
  pip install $line
done
