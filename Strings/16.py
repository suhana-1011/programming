# class Vending_machine:

#     def Update_cart(self,name,qty):
#         if name in self.cart:
#             self.cart[name]=qty
#         else:
#             if name in self.all_products:
#                 self.cart[name]=qty
#             else:
#                 print("item not available")
    
#     def Total_bill(self):
#         print("total bill breakup")
#         total=0
#         for k,v in self.cart.items():
#             print(k,"-",v,"*",self.all_products[k],
#                   "=",v* self.all_products[k])
#             total==v*

'''Create a class and it should contains a methodslike add items display then update items then del items
when the object is created need to create an empty dictionary automatically and perform all the above methods on that dictionary'''
# class MYCLASS:
#     def __init__(self):
#         self.d1={}
#     def add_items(self,k,v):
#         if k not in self.d1:
#             self.d1[k]=v
#         else:
#             print("Key already Exists")
#     def display(self):
#         print(self.d1)
#     def update_items(self,k,v):
#         if k in self.d1:
#             self.d1[k]=v
#     def delete_items(self,k):
#         if k in self.d1:
#             del self.d1[k]
#         else:
#             print("Key does not Exists")

# obj=MYCLASS()
# obj.display()
# obj.add_items('one',10)
# obj.add_items('two',20)
# obj.add_items('three',30)
# obj.add_items('four',50)
# obj.display()
# obj.update_items('four',40)
# obj.display()
# obj.delete_items('three')
# obj.display()
# obj.add_items('three',30)
# obj.display()

'''WAP to encode and decode'''


# morse_code={
#     '0':'-----',
#     '1':'.----',
#     '2':'..---',
#     '3':'...--',
#     '4':'....-',
#     '5':'.....',
#     '6':'-....',
#     '7':'--...',
#     '8':'---..',
#     '9':'----.',
#     '10':'-----'
#     }
# number_morse_code={morse:code for code,morse in morse_code.items()}

# def encode_the_numberr(num_str):
#     res=""
#     for code in num_str:
#         if code in morse_code:
#             res += morse_code[code]
#         else:
#             return "Number not matching"
#     return res
# def decode_the_morse_code(morsecode):
#     res=""
#     codes = morsecode.split()
#     for code in codes:
#         if code in number_morse_code:
#             res += number_morse_code
#         else:
#             return "Invalid morse code"
#     return res
# print(encode_the_numberr('111234'))

# print("Enter the morse code with 5 chars only anfter give space and 5 chars \n")
# print("Morse code must be either - or ")
# code = input('Enter Morse Code:')
# print(decode_the_morse_code(code))
''' Create a class by name vending machie it shoul contain methods like add items,displayitems,updateitems and total bills  
# when the object is created an emoty cart should create automatically and we need to pass dictionary items as follows 
#    coded  '''

class VENDINGMACHINE:
    all_pro={
      'Bingo':20,
      'Cole':35,
      'oreo':30,
      'jimjam':40,
      'dietcoke':60,
      'chikki':10,
      'redbull':200
    }
    
    Cart={}
    def __init__(self):
        self.Cart={}


    def additems(self,k,v):
        if k not in self.d1:
            self.Cart[k]=v
        else:
            print("item exists cart")
    def display(self):
        print(self.Cart)


    def updateitems(self,k,v):
        if k in self.Cart:
            self.Cart[k]=v


    def deleteitems(self,k):
        if k in self.Cart:
            del self.Cart[k]
        else:
            print("Key does not Exists")
    def checkitems(self,k,v):
        if k in self.Cart:
            print(self.Cart[k])
        else:
            print("Item Does not exists in cart")

    def Totalbill(self,k,v,q):
        self.q=q
        for k in self.Cart:
            self.total=v*q
print(input("enter quantity and price(v):" ))
print(f"Total:{self.total}")