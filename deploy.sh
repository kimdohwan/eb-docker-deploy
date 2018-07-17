#!/usr/bin/env bash


pipenv lock -r > requirements.txt
echo " Make requirements.txt"

git add requirements.txt
echo " Add requirements.txt"

git add .secret -f
echo " Add .secret"

#git add .media -f
#git add .static -f
#echo " Add .static"

eb deploy --profile eb-docker-deploy --staged
echo " Eb deploy"

git reset HEAD ./.secret/ requirements.txt
echo " Git reset HEAD"

rm requirements.txt
echo " Delete requirements"

eb open
echo " Open eb"
