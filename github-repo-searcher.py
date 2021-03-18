import requests
import re
import optparse
from optparse import OptionParser
import sys
import subprocess
import os

if ((len(sys.argv) < 3 or len(sys.argv) > 5) and '-h' not in sys.argv):
    print("Usage: %s {-c <company_name> | -u <user_name>}" % sys.argv[0])
    sys.exit(1)

parser = OptionParser()
parser.add_option("-c", "--company", help="company to search git repo for")
parser.add_option("-u", "--user", help="user to search git repo for")
(options, args) = parser.parse_args()

company = options.company
user = options.user
owner = (company or user)

if company is not None:
    url = "https://api.github.com/orgs/%s/repos" % company
else:
    url = "https://api.github.com/users/%s/repos" % user

response = requests.get(url)

response2 = response.text

response3 = re.findall(r'\"https://github.com/%s/[0-9a-zA-Z-]{2,}"'%owner,response2)

response4 = set(response3)

total = len(response4)

print("Total of %s repos:" % str(total))

print("=======================")

for each in response4:
    print(each)

print("=======================")

print("[+] Running git-leaks check on each repo found...")

for each in response4:
    print("\033[33m[+] Scanning repo: %s\033[0m" % each)
    cmd = "./gitleaks -v --repo-url=%s"%each
    os.system(cmd)
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    
