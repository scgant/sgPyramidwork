import re
pattern1=re.compile('bc')
#string that we need to search
matcher=pattern1.finditer('bcaacbcba')
for match in matcher:
    print("bc Match is available at start index",match.start())
    print("bc Match is available at end index",match.end())
#    print("bc Match is available at group index",match.group())
    print('*'*30)

pattern1=re.compile('ps')
#string that we need to search
matcher=pattern1.finditer('pqprpstsp')
for match in matcher:
    print("ps Match is available at start index",match.start())
    print("ps Match is available at end index",match.end())
#    print("ps Match is available at group index",match.group())
    print('*'*30)

    pattern1=re.compile('az')
#string that we need to search
matcher=pattern1.finditer('acazczbzzcaz')
for match in matcher:
    print("az Match is available at start index",match.start())
    print("az Match is available at end index",match.end())
#    print("az Match is available at group index",match.group())
    print('*'*30)

pattern1=re.compile('ab')
#string that we need to search
matcher=pattern1.finditer('abaababa')
for match in matcher:
    print("ab Match is available at start index",match.start())
    print("ab Match is available at end index",match.end())
#    print("ab Match is available at group index",match.group())
    print('*'*30)

#=======================Question 9==================================

import re
pattern1=re.compile('bc')
#string that we need to search
matcher=pattern1.finditer('bcaacbcba')
for match in matcher:
    print("bc Match is available at start index",match.start())
    print("bc Match is available at end index",match.end())
    print("bc Match is available at group index",match.group())
    print('*'*30)

pattern1=re.compile('ps')
#string that we need to search
matcher=pattern1.finditer('pqprpstsp')
for match in matcher:
    print("ps Match is available at start index",match.start())
    print("ps Match is available at end index",match.end())
    print("ps Match is available at group index",match.group())
    print('*'*30)

    pattern1=re.compile('az')
#string that we need to search
matcher=pattern1.finditer('acazczbzzcaz')
for match in matcher:
    print("az Match is available at start index",match.start())
    print("az Match is available at end index",match.end())
    print("az Match is available at group index",match.group())
    print('*'*30)

pattern1=re.compile('ab')
#string that we need to search
matcher=pattern1.finditer('abaababa')
for match in matcher:
    print("ab Match is available at start index",match.start())
    print("ab Match is available at end index",match.end())
    print("ab Match is available at group index",match.group())
    print('*'*30)
