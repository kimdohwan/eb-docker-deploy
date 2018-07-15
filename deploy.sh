#!/usr/bin/env bash


pipenv lock -r > requirements.txt
echo " make requirements.txt"

git add requirements.txt
echo " git add requirements.txt"

git add .secret -f
echo " Git add .se cret"

git add .media -f
git add .static -f

eb deploy --profile eb-docker-deploy --staged
echo " Eb deploy"

git reset HEAD
echo " Git reset HEAD"

rm -rf requirements.txt
echo " Delete requirements"

eb open
echo " Open"
