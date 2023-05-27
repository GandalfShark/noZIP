"""
creates a ban list of common words to be added to /etc/hosts
while this is not a good solution it is BTN (better than nothing)
You are best to block all .zip domains at your router. But this could help
if you have a computer you use on public wifi or at school.
simply copy and paste the contents of banzip.txt to the hosts file
list of words from: https://www.desiquintans.com/nounlist
"""
words = []
with open('nouns.txt', 'r') as f:
    for line in f:
        words.append(line.strip('\n'))
# make the list array
with open('banzip.txt', 'a') as ban:
    for word in words:
        ban.write(f'172.0.0.1 {word}.zip #loopback ban of zip TLD\n')
# write the list to ban via loopback address
