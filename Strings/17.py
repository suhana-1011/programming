'''
wap to design a functionality for railway dept, create a class and
it should contains a methods like get_train_name(train_no), 
get_train_total_seats(train_no), get_train_for_theday(day),toatl_collection(
general=215,sleeper=105,ac=76)
Accept the train details as follows
{'train_no:52319,
'train_name':'chennai express',
'starting':'banglore',
'end':'chennai',
'days_of_run':[''mon','wed','fri','sun']
'seats_available:{'general':250,sleeper:150,ac:100}
'price':{'general':250,sleeper:800,ac:2000}
}
'''
TRAINS=[
    {
        'train_no':52319,
        'train_name':'chennai express',
        'starting':'banglore',
        'end':'chennai',
        'days_of_run':['mon','wed','fri','sun'],
        'seats_available':{'general':250,'sleeper':150,'ac':100},
        'price':{'general':250,'sleeper':800,'ac':2000}
    },

    {
        'train_no':23451,
        'train_name':'vasco-da-gama',
        'starting':'banglore',
        'end':'Goa',
        'days_of_run':['mon','tue','wed','thur','fri','sat','sun'],
        'seats_available':{'general':280,'sleeper':190,'ac':140},
        'price':{'general':750,'sleeper':900,'ac':2450}
    },

    {
        'train_no':45671,
        'train_name':'Hampi express',
        'starting':'Hospete',
        'end':'bellary',
        'days_of_run':['mon','wed','thur','fri','sat','sun'],
        'seats_available':{'general':290,'sleeper':780,'ac':1500},
        'price':{'general':750,'sleeper':890,'ac':3400}
    }
]

class railway_dept:
     def get_train_name(self,trainno):
          for train in TRAINS:
               if train['train_no']==trainno:
                    return train['train_name']
               return "no trains available"
          
     def get_total_seats_avail(self,trainno):
          pass
       
     
     def get_train_for_theday(delf,day):
          result=[]
          for trains in TRAINS:
               if day in train['days_of_run']:
                    result.append(train['train_name'])
                    return result
           
     def get_toatl_collection(self,trainno,**kwargs):
          for train in TRAINS:
               if train['train_no']==trainno:
                    print(train['train_name'])
                    for k,v in kwargs.items():
                         print(k,"-",v,"*",train['price']
                               [k],"=",v *train['price'][k])
                         
r1=railway_dept()
# print(r1.get_train_name(78581))
# print(r1.get_trains_fot_theday('tue'))
r1.get_total_collection(23451,general=215,sleeper=105,ac=76 )



               
          
         












