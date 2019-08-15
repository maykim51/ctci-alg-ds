'''
CTCI 7.2. Call Center: 

Imagine you have a call center with three levels of employees: respondent, manager, and director. 
An incoming telephone call must be first allocated to a respondent who is free. 
If the respondent can't handle the call, he or she must escalate the call to a manager. 
If the manager is not free or not able to handle it, then the call should be escalated to a director. 

Design the classes and data structures for this problem. 
Implement a method dispatchCall() which assigns a call to the first available employee. 

'''
class CallHandler:
  #employess
  LEVEL = 3
  NUM_RESPONDENTS = 10
  NUM_MANAGERS = 5
  NUM_DIRECTORS = 3 

  '''
  list of employees
  employeelevels[0] = respondents
  employeelevels[1] = managers
  employeelevels[2] = directors
  '''  
  employeelevels = []
  
  '''
  call queue per level
  callqueue[0] = respondents
  callqueue[1] = managers
  callqueue[2] = directors
  '''  
  callqueue = []  
  
  def __init__(self):
    #TODO
    pass 
  
  # def getHandlerForCall(call:Call): #-> return employee
  #   pass
  
  # def dispatchCall(caller):
  #   call = Call(caller)
  
  
  
  ### WIP
  ##