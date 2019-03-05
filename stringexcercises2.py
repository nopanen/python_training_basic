# coding=UTF8
foo1 = foo2 = "Anomalocaris"
foo3 = "Waging on the purple drone"
foo4 = "Superficial"
foo5 = foo6 = "There truly is a dazzling bright world out there, waiting for us to explore"
foo7 = "91342391"
foo8 = "-== Warning! ==-"
foo9 = "-== Error! ==-"
foo10 = "–== Success! ==–"
foo11 = "Changing your dog for a bird? Some dog-lover you are."
foo12 = "Being bold has some uses."
foo13 = "–== Error! ==–"
foo14 = "abraham lincoln"
foo15 = "rEaDaBlE"
foo16 = "first word is capitalized"
foo17 = "a loooooooooooooooooooong word?"
foo18 = foo20 = "100000000000000000000000000000000000000000"
foo19 = "Something out of nothing? I really doubt we can do it anytime soon.."
foo21 = "what,if,we,have,no,choice?...."

print foo1.index("o")
print foo2.index("r")
print foo3.rfind("on")
print foo4.rfind("z")
print foo5.split(",")[1].index("a")
print foo6.split(",")[0].rindex("a")
print foo7[3:5]
print foo8[4:11]
print foo9[:9]
print foo10[6:]
print foo11.replace("dog", "cat")
print foo12.replace("o", "a", 1)
print foo13.upper()
print foo14.title()
print foo15.lower()
print foo16.capitalize()
print foo17.count("o")
print foo18.count("0")
print foo19.split("?")[0].count("n")
print foo20.rpartition("10")[1] + foo20.rpartition("10")[2].replace("0", "9")
print foo21.replace(",", " ").capitalize().rstrip(".")
