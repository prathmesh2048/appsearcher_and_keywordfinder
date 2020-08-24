'''def recommended_key(urls, keys):
    if len(urls) > 2:
        del urls[2:]
    elif len(urls) == 1:
        urls = ['', '']

    if len(keys) > 2:
        del keys[2:]
    elif len(keys) == 1:
        keys = ['', '']

    def common_elements(list1, list2):
        result = []
        for element in list1:
            if element in list2:
                result.append(element)
        return result

    if a or b:
        result = common_elements(a, b)
    else:
        result = []
    # print(result)
    dic1 = {}

    if len(result) >= 3:
        for i in result:
            a.remove(i)
            b.remove(i)
        dic1 = {urls[0]: b, urls[1]: a}
    # print(dic1)
    return dic1
'''

'''a = ['dota 2 stats', 'dota 2', 'statistics', ' dota', 'guides']
b = ['dota 2 stats', 'dota 2', 'statistics', ]
keys = [a,b]
urls = ['https://www.dotabuff.com/', 'https://stratz.com/']
print(recommended_key(urls, keys))'''