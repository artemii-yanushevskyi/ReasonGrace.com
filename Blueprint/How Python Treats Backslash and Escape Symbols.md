
```
>>> s = "\\" str(s)
'\\'
>>> print(s)
\
>>> s="\n" print(s)
                                                                                                                                            
                                                                                                                                            
>>>                                                                                                                                         
>>> s="ab\\cd" print(s)
ab\cd
>>> s.replace("\\", "\\\\")
'ab\\\\cd'
>>> print(s)
ab\cd  
```

Even ```bash``` treats \s unpredictably *for me*.
