#!/bin/sh
cd TempDataLogging/Excel
git add --all

timestamp() {
  date +"at 10:30 PM"
}

git commit -am "Regular auto-commit $(timestamp)"
git push origin main