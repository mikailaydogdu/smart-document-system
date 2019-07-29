import hashlib


def Kodlar(xtable, type):
    qry = xtable.objects.all().filter(type=type)
    xlist = []
    for i in qry.values_list('id', 'title'):
        xlist.append(i)
    return xlist


def generate_sha(file):
    sha = hashlib.sha1()
    file.seek(0)
    while True:
        buf = file.read(104857600)
        if not buf:
            break
        sha.update(buf)
    sha1 = sha.hexdigest()
    file.seek(0)
    return sha1

def generate_md5(file):
    md5 = hashlib.md5()
    file.seek(0)
    while True:
        buf = file.read(104857600)
        if not buf:
            break
        md5.update(buf)
    md5 = md5.hexdigest()
    file.seek(0)
    return md5
