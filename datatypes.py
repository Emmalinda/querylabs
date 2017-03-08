def data_type(n):

  if isinstance(n,str):
    #print("entered string, the length is:")
    return len(n)
  
  elif isinstance(n,bool):
    #print("this is boolean")
    return n
  
  elif isinstance(n, int):
    num=100
  
    if n<num:
      return "less than 100"
    elif n>num:
      return "more than 100"
      #print("this is integer")	

  elif isinstance(n, list):
    if len(n)>2:
      return n[2]
    else:
      return None
  
  elif n is None:
    return "no value"