def median (lst):
    lst=sorted(lst)
    if len(lst)%2!=0:
      return lst[int((len(lst)-1)/2)]
    else:
      return ( lst[int(len(lst)/2)-1]+lst[int(len(lst)/2)])/2
   
