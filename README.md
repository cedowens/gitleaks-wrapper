# gitleaks-wrapper
Simple wrapper around gitleaks to enumerate publicly facing github repos and then run gitleaks against each in search of exposed secrets/keys.

Steps:

1. Download and build gitleaks: https://github.com/zricethezav/gitleaks

2. Download this python script and place it in the same directory that you built gitleaks in step #1 above.

3. Run this script and pass the company name into the -c option. Example:

> python3 github-repo-searcher.py -c ExampleCompany

4. Results will be returned to stdout

-----------------------
