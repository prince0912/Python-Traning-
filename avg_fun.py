def avrg(first, *rests):
    return (first+sum(rests))/(1+len(rests))
print(avrg(1,2))
