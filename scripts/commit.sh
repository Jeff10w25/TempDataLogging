#!/bin/sh
DELAY=5
cd TempDataLogging
sleep $DELAY
git add excel/
sleep $DELAY

git commit -m "Regular auto-commit"
sleep $DELAY
git pull --autostash
sleep $DELAY
git config --global --unset htpps.proxy
sleep $DELAY
git push origin main