#from Item import Item
#from dayOfWeekFinder import DaysOfWeek

#neccissary Item functions
class Item: 
    _object = None
    _next = None
    _prev = None
    _iter = None
    
    def __init__(self, obj = None):
        self.object = obj
    
    def append(self, obj):
        if self._object == None:
            self._object = obj
            newItem = self
        else: 
            last = self.last()
            newItem = Item(obj)
            newItem._prev = last
            newItem._object = obj
            last._next = newItem
        return newItem
        
    def first(self): 
        iter = self
        while True:
            if iter._prev == None:
                break
            iter = iter._prev 
        return iter
        
    def last(self):
        iter = self 
        while True:
            if iter._next == None: 
                break
            iter = iter._next
        return iter
        
    def showList(self):
        iter = self.first()
        while iter._next is not None:
            print(iter._object)
            iter = iter._next
        print(iter._object)
#end        
        
#functions for finding the day of the week

class DaysOfWeek:
    _daysOfWeek = Item()
    #_daysOfWeek.clear()
    _daysOfWeek = _daysOfWeek.append('Monday')
    _daysOfWeek = _daysOfWeek.append('Tuesday')
    _daysOfWeek = _daysOfWeek.append('Wednsday')
    _daysOfWeek = _daysOfWeek.append('Thursday')
    _daysOfWeek = _daysOfWeek.append('Friday')
    _daysOfWeek = _daysOfWeek.append('Saturday')
    _daysOfWeek = _daysOfWeek.append('Sunday')
    _daysOfWeek = _daysOfWeek.first()
    #_daysOfWeek.showList()
    _iter_ = _daysOfWeek.first()
    
    print(f'The week starts on {_iter_._object}') 
    
    def tommorrow(self):
        iter = self._iter_
        if iter._next == None:
            iter = self._daysOfWeek.first()
            #print(f'Iter is back at {iter._object}')
            self._iter_ = iter
        else:
            iter = iter._next
            #print(f'Iter is at {iter._object}')
            self._iter_ = iter
        return iter
        
    def yesterday(self):
        iter = self._iter_
        if iter._prev == None:
            iter = self._daysOfWeek.last()
           #print(f'Iter is back at {iter._object}')
            self._iter_ = iter
        else:
            iter = iter._prev
            #print(f'Iter is at {iter._object}')
            self._iter_ = iter
        return iter
        
    def blastToThePast(self, int):
        if int >= 1:
           for _ in range(0, int):
               iter = self.yesterday()
           return iter
        else:
            print('0 is invalid')
        
    def backToTheFuture(self, int):
        if int >= 1:
            for _ in range(0, int):
                iter = self.tommorrow()
            return iter
        else:
            print('0 is invalid')
            
    def pastIncident(self, int):
        for _ in range(0, int):
            incident = int(input('Enter days without incident: '))
        
        if int >= 1:
           for _ in range(0, int):
               iter = self.yesterday()
           return iter
        else:
            print('0 is invalid')
#end


#functional UI

def pastIncident():
    #pastIncident functions
    def incidentDay():
        
        while True:
            try:
                value = int(input('Enter days without accident: '))
                test = 1/(abs(value) + value)
                break
            except Exception:
                print('Only positive integers accepted')
            
        #if value >= 0:
        day = DaysOfWeek()
        weekday = day.blastToThePast(value)
        print(' ')
        print('=' * 40)
        print(f'The day {value} day(s) ago from Monday was {weekday._object}')
        print('=' * 40)
        print(' ')
        #else:
            #print('Negative values invalid')
    def singleIncidents():
        while True:
            try:
                repeat = int(input('Number of incidents weekdays to be found: '))
                test = 1/(abs(repeat) + repeat)
                break
            except Exception:
               print('Only positive integers accepted')
            
        for x in range(0, repeat):	
            incidentDay()
            
    def multipleIncidents():
        #incidentList = Item()
        incidentList2 = []
        count = 1
        incidentDaysList = Item()
        while True:
            try:
                incident = int(input('Enter days without incident one by one (enter any letter(s) or [ENTER] to stop): '))
                test = 1/(abs(incident) + incident)
                #incidentList = incidentList.append(incident)
                incidentList2.append(incident)
                sumof = sum(incidentList2)
                day = DaysOfWeek()
                weekday = day.blastToThePast(sumof)
                print(' ')
                print('=' * 40)
                print(f'Incident {count} occured on {weekday._object}')
                print('=' * 40)
                print(' ')
                incidentDaysList.append(weekday._object)
                count += 1
            except ValueError:
                #incidentList.showList()
                print(f'Days without incident values: {incidentList2}')
                break
            except ZeroDivisionError:
                print('Negative values are invalid')
        sumof = sum(incidentList2)
        print(f'Value Total: {sumof}')
        print(f'values entered: {count - 1}')
        incidentDaysList.showList()
    
    #past Incident option selection
    
    print()
    print('Weekday Finding Tool\n')

    print('=' * 40)
    print('1. Single Incident values')

    print('2. Multiple Incident Values')
    print('=' * 40)
    print()
    while True:
        try:
            option = int(input('Enter 1 or 2 to continue...\n'))
            if option == 1 or option == 2:
                break
            else:
                error = 1/0
        except Exception:
            print('Only number 1 or 2 accepted\n')
    if option == 1:
        singleIncidents()
    if option == 2:
        multipleIncidents()

pastIncident()
