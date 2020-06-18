import simplejson as json


#Dict(json)선언

data = {}
data['people'] = []
data['people'].append({
    'name':'Kim',
    'website':'naver.com',
    'from':'Seoul'
})
data['people'].append({
    'name':'Park',
    'website':'google.com',
    'from':'Busan'
})
data['people'].append({
    'name':'Lee',
    'website':'daum.net',
    'from':'Incheon'
})
# print(data)

#Dict(json) -> Str 

e = json.dumps(data,indent = 4)
# print(type(e))
# print(e)

#Str -> Dict(Json)
d = json.loads(e)
# print(type(d))
# print(d)

with open ('E:/Github/WebCrawling/Section_4/member.json','w')  as outfile:
    #http://jsoneditoronline.org/#left=local.yivido&right=local.wuyufo <-json sort 창
    outfile.write(e)

with open ('E:/Github/WebCrawling/Section_4/member.json','r')  as infile:
    r = json.loads(infile.read())
    print("=======")
    # print(type(r))
    # print(r)
    for p in r['people']:
        print('Name:'+p['name'])
        print('Website:'+p['website'])
        print('From:'+p['from'])
        print('')
        