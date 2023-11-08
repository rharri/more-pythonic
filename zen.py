import pprint
import this

print("", end="\n\n\n")
print("The Zen of Python is scrambled")
print(this.s, end="\n\n\n")

print("The encoding is stored in a dictionary")
pprint.pprint(this.d)
print("", end="\n\n\n")

print("For example, to unscramble the first letter...")
print(f"this.d.get(this.s[0]) = {this.d.get(this.s[0])}", end="\n\n\n")

unscrambled = "".join([this.d.get(c, c) for c in this.s])

print(unscrambled, end="\n\n\n")

print("" if copyright() else "", end="\n\n\n")

print("" if credits() else "", end="\n\n\n")

