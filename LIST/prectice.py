# String
naam = "Ritik"

# ------------------ Case Methods ------------------

print(naam.upper())        # Sabhi letters UPPERCASE -> RITIK
print(naam.lower())        # Sabhi letters lowercase -> ritik
print(naam.capitalize())   # Pehla letter capital -> Ritik
print(naam.title())        # Har word ka pehla letter capital -> Ritik
print(naam.swapcase())     # Upper ko lower aur lower ko upper -> rITIK
print(naam.casefold())     # Lowercase ka advanced version -> ritik

# ------------------ Search Methods ------------------

print(naam.find("t"))      # Pehla index batata hai -> 2
print(naam.rfind("i"))     # Last occurrence ka index -> 3
print(naam.index("R"))     # Character ka index -> 0
print(naam.count("i"))     # Kitni baar character aaya -> 2

# ------------------ Check Methods ------------------

print(naam.startswith("Ri"))   # True
print(naam.endswith("ik"))     # True
print(naam.isalpha())          # Sirf letters? -> True
print(naam.isalnum())          # Letters + Numbers? -> True
print(naam.isdigit())          # Sirf digits? -> False
print(naam.isnumeric())        # Numeric? -> False
print(naam.isdecimal())        # Decimal digits? -> False
print(naam.islower())          # Lowercase? -> False
print(naam.isupper())          # Uppercase? -> False
print(naam.istitle())          # Title case? -> True
print(naam.isspace())          # Sirf spaces? -> False
print(naam.isascii())          # ASCII characters? -> True
print(naam.isidentifier())     # Variable name ban sakta hai? -> True
print(naam.isprintable())      # Printable? -> True

# ------------------ Replace & Modify ------------------

print(naam.replace("R", "V"))   # R ko V se replace -> Vitik
print(naam.strip())             # Left & Right spaces remove
print(naam.lstrip())            # Left spaces remove
print(naam.rstrip())            # Right spaces remove

# ------------------ Split & Join ------------------

line = "Python Java C++"

print(line.split())             # Space ke hisaab se list
print(line.split("a"))          # 'a' ke hisaab se split

list1 = ["Python", "Java", "C++"]
print("-".join(list1))          # Python-Java-C++

# ------------------ Alignment ------------------

print(naam.center(20))          # Center align
print(naam.ljust(20))           # Left align
print(naam.rjust(20))           # Right align
print(naam.zfill(10))           # Zero fill -> 00000Ritik

# ------------------ Partition ------------------

email = "ritik@gmail.com"

print(email.partition("@"))     # ('ritik', '@', 'gmail.com')
print(email.rpartition("@"))    # Right partition

# ------------------ Formatting ------------------

age = 20

print("My name is {}".format(naam))      # format()
print(f"My name is {naam}")              # f-string

# ------------------ Encoding ------------------

print(naam.encode())            # Bytes me convert

# ------------------ Translate ------------------

table = str.maketrans("R", "V")
print(naam.translate(table))    # Ritik -> Vitik

# ------------------ Expand Tabs ------------------

text = "Python\tJava"
print(text.expandtabs(20))      # Tab ko spaces me convert

# ------------------ Slicing ------------------

print(naam[0])      # R
print(naam[-1])     # k
print(naam[1:4])    # iti
print(naam[::-1])   # kitiR (Reverse)

# ------------------ Length ------------------

print(len(naam))    # String ki length -> 5