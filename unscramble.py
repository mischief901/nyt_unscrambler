import sys
import getopt
import bisect

def main(letters, center) :
  words = open("/usr/share/dict/american-english", "r")
  for word in words :
    word = word.lower().strip()
    
    if center not in word :
      continue
    if len(word) < 4 :
      continue
    
    lets = "".join(sorted(set(word)))

    valid = True
    for l in lets :
      if l not in letters :
        valid = False
    if valid :
      print(word)

if __name__ == "__main__" :
  args = sys.argv
  letters = "".join(sorted(args[1].lower()))
  center = args[2].lower()
  if len(letters) is not 7 or len(center) is not 1 :
    exit(1)
  print(letters)
  print(center)
  main(letters, center)
  
