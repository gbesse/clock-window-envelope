from .common import integer, unique_ids

def merge(intervals):
    result=[]
    for a,b in sorted(intervals):
        integer(a,-10**12,10**12);integer(b,-10**12,10**12)
        if a>=b: raise ValueError('window')
        if result and a<=result[-1][1]:result[-1][1]=max(result[-1][1],b)
        else:result.append([a,b])
    return result

def intersect(a,b):
    out=[];i=j=0
    while i<len(a) and j<len(b):
        lo=max(a[i][0],b[j][0]);hi=min(a[i][1],b[j][1])
        if lo<hi:out.append([lo,hi])
        if a[i][1]<b[j][1]:i+=1
        else:j+=1
    return out

def run(data):
    parties=data['parties']
    if not 1<=len(parties)<=100:raise ValueError('parties')
    unique_ids(parties);safe=None;nominal=None;details=[]
    for p in parties:
        if len(p['windows'])>1000:raise ValueError('windows')
        windows=merge(p['windows']);low,high=p['offset']
        integer(low,-10**12,10**12);integer(high,-10**12,10**12)
        if low>high:raise ValueError('offset')
        eroded=[[a-low,b-high] for a,b in windows if a-low<b-high]
        nominal=windows if nominal is None else intersect(nominal,windows)
        safe=eroded if safe is None else intersect(safe,eroded)
        details.append({'id':p['id'],'robust_windows':eroded})
    return {'robust_windows':safe,'nominal_windows':nominal,'witness_time':safe[0][0] if safe else None,'parties':details,'interval_semantics':'half_open; local_time = reference_time + offset'}
