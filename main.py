import os, time

listofEmail = []
def prettyPrint():
  os.system("clear")
  print("listofEmail")
  print()
  counter = 1
  for email in listofEmail:
    print(f"{counter}: {email}")
    counter += 1
  time.sleep(1)

def spam(max):
  for i in range(0,max):
    print(f"""
    Email {i+1}
    
Dear {listofEmail[i]}
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.
Love and hugs,
Ian Spammington III""")
    time.sleep(1)
    os.system("clear")

while True:
  print()
  print("SPAMMER Inc.")
  print()
  menu = input("1. Add email\n2: \033[33mRemove email\n\033[0m3. Show emails\n4. \033[31mGet SPAMMING\n\033[0m> ")
  if menu == "1":
    email = input("Email > ")
    listofEmail.append(email)
  elif menu == "2":
    email = input("Email > ")
    if email in listofEmail:
      listofEmail.remove(email)
  elif menu == "3":
    prettyPrint()
  elif menu == "4":
    spam(10)
  time.sleep(1)
  os.system("clear")
