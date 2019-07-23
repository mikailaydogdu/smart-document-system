def Kodlar(xtable, type):
    qry = xtable.objects.all().filter(type=type)
    xlist = []
    for i in qry.values_list('id', 'title'):
        xlist.append(i)
    return xlist
