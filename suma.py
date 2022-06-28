inputtext1 = Element("inputtext1")
inputtext2 = Element("inputtext2")

output = Element("output")

def clear(*args, **kwargs):
    inputtext1.clear()
    inputtext2.clear()
    output.clear()

def suma(*args, **kwargs):
    totalsuma = int(inputtext1.value) + int(inputtext2.value)
    output.write(totalsuma)
