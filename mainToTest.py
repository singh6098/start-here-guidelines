
def mainToTest_fgetVar(i_num=0):
    try:
      if(i_num == None) or (type(i_num) == str):
        return "Wrong Type"
      else:
        num = i_num/16.00
        return num
    except Exception as Err:
       print(f"!!!! Unexpected {Err =}, {type(Err)=}")
       raise
