vowel = [ 'a' , 'e' , 'i' , 'o' , 'u']
User = input("Enter the sentence : ").lower()
vow_count = 0
cons_count = 0
space = 0
digits = 0
other = 0
for i in User:
    if i == " ":
        space+=1
    elif i.isdigit():
        digits += 1
    elif i.isalpha():
        if i in vowel:
            vow_count+=1
        else:
            cons_count+=1
    else:
        other +=1

print(f"Vowel = {vow_count}\nConsonants = {cons_count}\nspace = {space}\nDigits = {digits}\nOthers ={other}") 
