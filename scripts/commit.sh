#!/bin/sh
cd TempDataLogging
git add excel/

timestamp() {
  date +"at 10:30 PM"
}

DELAY=10

git commit -am "Regular auto-commit $(timestamp)"
sleep $DELAY
git config --global --unset htpps.proxy
sleep $DELAY
git push origin main