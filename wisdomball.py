import random
import urllib.request

url = 'https://raw.githubusercontent.com/PiraTechnics/wisdomball/main/wisdom'
wisdom_list = urllib.request.urlopen(url).read().splitlines()

print("The Ball of Wisdom says:")

random_line = random.randint(0, len(wisdom_list)-1)
print(wisdom_list[random_line].decode('utf-8'))