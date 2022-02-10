def hello():
    print("heelo there")

hello()

#passing value

def pas_func(greet):
    print(greet.isupper())
    print(greet.upper())
    print("{} how are you?".format(greet) )

greet="yoooss"
pas_func(greet)