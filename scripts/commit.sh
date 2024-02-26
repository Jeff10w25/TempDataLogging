#!/bin/sh
cd TempDataLogging/excel
git add --all

timestamp() {
  date +"at 10:30 PM"
}

git config --global --unset htpps.proxy
git commit -am "Regular auto-commit $(timestamp)"
git push origin main