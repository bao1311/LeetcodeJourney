class Solution:
    def countMentions(self, n: int, events: List[List[str]]) -> List[int]:
        '''
        1 1 1
        '''
        res = [0] * n
        cur = 0
        frozen = defaultdict(int)
        for e in events:
            if e[0] == "OFFLINE":
                e[0] = 1
            else:
                e[0] = 2
        events.sort(key=lambda x:(int(x[1]),x[0])) 
        for e in events:
            if e[0] == 1:
                e[0] = "OFFLINE"
            else:
                e[0] = "MESSAGE"
        print(events)
        for e,t,id in events:    
            ids = []
            if e == "MESSAGE":
                if id == "ALL":
                    res = [k + 1 for k in res]
                elif id == "HERE":
                    for i,k in enumerate(res):
                        if frozen[i] <= int(t):
                            res[i] = k + 1        
                else:
                    a = id.split(' ')
                    for p in a:
                        ids.append(int(p[2:]))
                    for l in ids:
                        res[l] += 1 
            else:
                frozen[int(id)] = int(t) + 60
                

        print('res',res)
        return res
