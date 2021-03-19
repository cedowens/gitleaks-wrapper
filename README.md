# gitleaks-wrapper
Simple wrapper around gitleaks to enumerate publicly facing github repos for teh specified org and then run gitleaks against each in search of exposed secrets/keys. This saves some time from having to manually re-run gitleaks against each of an org's repos.

This simple script basically checks api.github.com/repos/[companyname] in order to find an org's repos.

Steps:

1. Download and build gitleaks: https://github.com/zricethezav/gitleaks

2. Download this python script and place it in the same directory that you built gitleaks in step #1 above.

3. Run this script and pass the company name into the -c option. Example:

> python3 github-repo-searcher.py -c [ExampleCompany] -u [ExampleUser]

4. Results will be returned to stdout

-----------------------
