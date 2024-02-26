#!/bin/sh
cd TempDataLogging
git add excel/

timestamp() {
  date +"at 10:30 PM"
}

git commit -am "Regular auto-commit $(timestamp)"
git config --global --unset htpps.proxy
git push origin main