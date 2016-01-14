import win32com.client as win32

from sys import version_info
from datetime import datetime, timedelta, time



outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)


py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2
print("===================================================")
print("===================================================")
print("1.Пица \"НЕАПОЛИТАНА\" - доматен сос, кашкавал, риба тон, риган, лук")
print("2.Пица \"ПРИМАВЕРА\"  - доматен сос, кашкавал, гъби, риган, пресни чушки, царевица, лук, маслини")
print("3.Пица \"КАПРИЧОЗА\" - доматен сос, кашкавал, шунка, гъби, пресни чушки, риган")
print("4.Пица \"КАРИОЛА\" - доматен сос, кашкавал, бекон, лук, риган")
print("5.Пица \"ЛИБЪРТИ\" - доматен сос, кашкавал, кисели краставички, гъби, пресни чушки, риган, лук, маслини, пилешко филе")
print("6.Бяла пица \"ПОПАЙ\" - бял сос, кашкавал, спанак, риган, бяло сирене")
print("7.Бяла пица \"МАРГАРИТА\"  - бял сос, кашкавал, моцарела, риган")
print("8.Бяла пица \"МАРКО ПОЛО\" - бял сос, кашкавал, пилешко филе, гъби, маслини, лук, моркови, риган, топено сирене")
print("9.Бяла пица \"КУАТРО ФОРМАДЖИ\" - бял сос, кашкавал, синьо сирене, моцарела, бяло сирене, риган")
print("===================================================")



pizza_choosen = ""

while True:
    if py3:
       response = input("Please enter your choice :")
    else:
       response = raw_input("Please enter your choice: ")
    if response == "1":
       pizza_choosen = "Пица \"НЕАПОЛИТАНА\""
       break
    elif response == "2":
       pizza_choosen = "Пица \"ПРИМАВЕРА\""
       break
    elif response == "3":
       pizza_choosen = "Пица \"КАПРИЧОЗА\""	
       break
    elif response == "4":
       pizza_choosen = "Пица \"КАРИОЛА\""
       break
    elif response == "5":
       pizza_choosen = "Пица \"ЛИБЪРТИ\""
       break
    elif response == "6":
       pizza_choosen = "Бяла пица \"ПОПАЙ\""
       break
    elif response == "7":
       pizza_choosen = "Бяла пица \"МАРГАРИТА\""
       break
    elif response == "8":
       pizza_choosen = "Бяла пица \"МАРКО ПОЛО\""
       break
    elif response == "9":
       pizza_choosen = "Бяла пица \"КУАТРО ФОРМАДЖИ\""
       break
    
print ("you entered " + pizza_choosen) 

#mail.To = 'someone@domain.com'

now = datetime.now()
print("Ordering time = "+now.strftime("%H:%M"))
now =  now + timedelta(minutes=30)

subject = pizza_choosen+' , '+now.strftime("%H:%M")+', И-НОМЕР - ИМЕ 
print("Subject = "+ subject)

print("Mail To = "+ mail.To)
print("Subject = "+ subject)

input("Моля потвърдете")

mail.Subject = subject
mail.body = 'Благодаря'
mail.send
print("Sent")