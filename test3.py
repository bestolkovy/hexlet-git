def compare_version(version1, version2):
    ver1, ver2 = version1.split('.'), version2.split('.')
    v1 = [int(ver1[0]), int(ver1[1])]
    v2 = [int(ver2[0]), int(ver2[1])]
    if v1 > v2:
        print ('1')
    elif v1 < v2:
        print ('-1')
    else:
        print('0')


   
compare_version("6.55", "7.55")