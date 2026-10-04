import json,glob,statistics as st,re,csv
R='/home/bizzroids/Desktop/code/research-facility/research/ai-youtube-video-titles'
rows={r['video_id']:r for r in csv.DictReader(open(R+'/videos.csv'))}
V=[]
for f in glob.glob(R+'/phase-6/raw/*.json'):
    d=json.load(open(f)); r=rows.get(d['id'])
    if not r or not d.get('view_count'): continue
    v=d['view_count']; l=d.get('like_count') or 0; c=d.get('comment_count') or 0
    V.append(dict(id=d['id'],t=d['title'],ch=d['channel'],v=v,l=l,c=c,lr=l/v if v else 0,cr=c/v if v else 0,
      vpd=float(r['views_per_day'] or 0),tpl=r['template'],ang=r['angle'],ind=r['industry'],dur=d.get('duration') or 0))
print('n',len(V), 'with likes', sum(1 for x in V if x['l']>0))
# channel-relative outperformance
from collections import defaultdict
bych=defaultdict(list)
for x in V: bych[x['ch']].append(x['v'])
for x in V:
    vs=bych[x['ch']]; x['rel']= x['v']/st.median(vs) if len(vs)>=3 else None
med=lambda a:st.median(a) if a else float('nan')
VL=[x for x in V if x['v']>=1000 and x['l']>0]
mvpd=med([x['vpd'] for x in VL]); mlr=med([x['lr'] for x in VL])
print('median vpd',round(mvpd),'median like rate %.4f'%mlr, 'median comment rate %.5f'%med([x['cr'] for x in VL]))
for x in VL:
    hv=x['vpd']>=mvpd; hl=x['lr']>=mlr
    x['q']={(1,1):'SWEET',(1,0):'BAIT',(0,1):'GEM',(0,0):'DEAD'}[(hv,hl)]
from collections import Counter
print(Counter(x['q'] for x in VL))
# like-rate vs views correlation (spearman-ish via rank)
def rank(a):
    s=sorted(range(len(a)),key=lambda i:a[i]); r=[0]*len(a)
    for k,i in enumerate(s): r[i]=k
    return r
import math
def spear(a,b):
    ra,rb=rank(a),rank(b); n=len(a); ma=sum(ra)/n; mb=sum(rb)/n
    num=sum((x-ma)*(y-mb) for x,y in zip(ra,rb)); return num/math.sqrt(sum((x-ma)**2 for x in ra)*sum((y-mb)**2 for y in rb))
print('spearman vpd~likerate %.2f'%spear([x['vpd'] for x in VL],[x['lr'] for x in VL]))
print('\nBY ANGLE: n | med vpd | med likerate | med commentrate | med rel-to-channel | %SWEET %BAIT')
for g in sorted(set(x['ang'] for x in VL)):
    s=[x for x in VL if x['ang']==g]; rel=[x['rel'] for x in s if x['rel']]
    print(f"{g:12} {len(s):4} {med([x['vpd'] for x in s]):8.0f} {med([x['lr'] for x in s]):.4f} {med([x['cr'] for x in s]):.5f} {med(rel):5.2f} {100*sum(x['q']=='SWEET' for x in s)/len(s):4.0f}% {100*sum(x['q']=='BAIT' for x in s)/len(s):4.0f}%")
print('\nBY TEMPLATE (n>=8)')
for g in sorted(set(x['tpl'] for x in VL)):
    s=[x for x in VL if x['tpl']==g]
    if len(s)<8: continue
    rel=[x['rel'] for x in s if x['rel']]
    print(f"{g[:60]:60} {len(s):4} vpd {med([x['vpd'] for x in s]):7.0f} lr {med([x['lr'] for x in s]):.4f} cr {med([x['cr'] for x in s]):.5f} rel {med(rel):5.2f} sweet {100*sum(x['q']=='SWEET' for x in s)/len(s):3.0f}% bait {100*sum(x['q']=='BAIT' for x in s)/len(s):3.0f}%")
json.dump(VL,open('vl.json','w'))
