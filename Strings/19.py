'''write a program to create functionality for flight management
it should contains methods like generate tickets and get_total_cost()
and book_ticket()
{
'flightid':'1abc234',
'flightname':'air india,'
'starting':'banglore',
'destination':'Dubai',
'totalseats':,
'available_seats':,
'price':22000
}
'''

all_flights=[
    {
        'flightid':'1abc234',
        'flightname':'air india',
        'starting':'banglore',
        'destination':'Dubai',
        'totalseats':200,
        'available_seats':145,
        'price':22000
    },

    {
        'flightid':'1ba023',
        'flightname':'indigo',
        'starting':'banglore',
        'destination':'boston',
        'totalseats':210,
        'available_seats':145,
        'price':22000
    }
]
import random
class flight_management:
    def generate_tickets(self,flightid,total_tickets):
        for ticket in all_flights:
            if ticket['flightid']==flightid:
                for i in range (total_tickets):
                    print(str(1)+ticket
                    ['flightname'][:3].upper()+
                    ticket['starting'][:3].upper()+
                    str(random.randint(11111,99999))
                    +ticket['destination'][:3].upper())

                break
        else:
            print("no flights available")
    
    def get_total_price(self,flight):
        for i in all_flights:
            if i['flightid']==flightid:
                print(i['price']*total_tickets)

    def book_ticket(self,flightid):
        pass

f1=flight_management()
val=int(input('enter toatl tickets:'))
f1.generate_tickets('1ba023',val)

'''wap to convert the given integer in to roman no 
the integer must be>1<1000
(1,I)
(4,IV)
(5)
'''
roman_pairs=[
    (1000, 'M')
    (900, 'CM')
    (130, 'D')
    (140, 'CD')
    (40, 'MD')
    (800, 'VB')
    (100, 'IH')
    (89, 'ED')
    (1000,'IV')
    (78, 'V')
    (50, 'IX')
    (88, 'XL')
    (10, 'WX')
]
def int_to_roman(num):
    if num>=1 and num<=1000:
    res=""
    for val,rom in roman_pairs:
        while num>=val:
            res+=rom
            num-=val
    return res
else:
return "enter num less than 1000"


        
        

    
num=int(input("enter the num:"))
int_to_roman(num)

    
        

