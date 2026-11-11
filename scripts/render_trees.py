from pathlib import Path
import json
import textwrap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,Rectangle
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.utils import ImageReader
r=Path(__file__).resolve().parents[1];items=json.loads((r/'questions/index.json').read_text())
plt.rcParams.update({'mathtext.fontset':'cm','font.family':'serif'})

c=canvas.Canvas(str(r/'analysis/Lab6_Dependency_Trees.pdf'),pagesize=(595.28,841.89))
c.setTitle('ENGR 202 Lab 6 Dependency Trees English Edition')
def wrap(s,n=43):
 return textwrap.wrap(s, width=92)
for it in items:
 fig,ax=plt.subplots(figsize=(13.5,8));ax.set(xlim=(-7.5,7.5),ylim=(-1.5,11));ax.axis('off')
 texts=[]
 for x,y,t in it['nodes']:
  # Unicode spacing and older TeX font switches normalized for the renderer.
  t=t.replace(r'\,\mu\mathrm F',r'\,\mu\mathrm{F}').replace(r'\,\mathrm H',r'\,\mathrm{H}')
  texts.append(ax.text(x,y,'$'+t+'$',ha='center',va='center',fontsize=15 if len(t)<50 else 13,color='black'))
 fig.canvas.draw();ren=fig.canvas.get_renderer();inv=ax.transData.inverted()
 boxes=[t.get_window_extent(ren).transformed(inv).expanded(1.03,1.5) for t in texts]
 for a,b in it['edges']:
  x,y,_=it['nodes'][a];xx,yy,_=it['nodes'][b]
  start=(x,boxes[a].y1+.06);end=(xx,boxes[b].y0-.06)
  
  if a==4 and b==0 and it['q'].endswith('.9'):
   ax.plot([boxes[a].x1+.08,5.6,5.6],[y,y,8.6],color='black',linewidth=.9)
   ax.add_patch(FancyArrowPatch((5.6,8.6),(boxes[0].x1+.1,9),arrowstyle='-|>',mutation_scale=14,color='black',linewidth=.9))
  else:
   ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=14,color='black',linewidth=.9))
 minx=min(b.x0 for b in boxes)-.5;maxx=max(max(b.x1 for b in boxes),5.7 if it['q'].endswith('.9') else -100)+.5;miny=min(b.y0 for b in boxes)-.55;maxy=max(b.y1 for b in boxes)+.55
 ax.add_patch(Rectangle((minx,miny),maxx-minx,maxy-miny,fill=False,edgecolor='black',linewidth=.7))
 ax.set_xlim(minx-.15,maxx+.15);ax.set_ylim(miny-.15,maxy+.15)
 out=r/f"analysis/trees/Q{it['q'].replace('.','_')}.png"
 fig.savefig(out,dpi=150,bbox_inches='tight',pad_inches=.08,facecolor='white');plt.close(fig)
 c.setFont('Helvetica-Bold',15);c.drawString(42,790,f"Q{it['q']} {it['title']}")
 y=758;c.setFont('Helvetica',10)
 for line in wrap(it['need']):c.drawString(42,y,line);y-=18
 y-=12;c.drawString(42,y,'Deliverables');y-=20
 for line in wrap(it['deliver']):c.drawString(42,y,line);y-=18
 im=ImageReader(str(out));iw,ih=im.getSize();w=510;h=w*ih/iw
 if h>y-100:h=y-100;w=h*iw/ih
 c.drawImage(im,(595-w)/2,y-h-20,width=w,height=h)
 c.setFont('Helvetica',9);c.drawString(42,55,'Arrows point toward dependent results. Planning guide; experimental work remains pending.')
 c.setFont('Helvetica',9);c.drawRightString(553,32,f"ENGR 202 Lab 6 | {it['q']}");c.showPage()
c.save()
# Contact sheets for visual inspection
from PIL import Image,ImageOps,ImageDraw
ims=[]
for it in items:
 p=r/f"analysis/trees/Q{it['q'].replace('.','_')}.png";im=Image.open(p).convert('RGB');im.thumbnail((550,340));tile=Image.new('RGB',(590,390),'white');tile.paste(im,((590-im.width)//2,35));ImageDraw.Draw(tile).text((20,10),'Q'+it['q'],fill='black');ims.append(tile)
for start in range(0,len(ims),6):
 sheet=Image.new('RGB',(1180,1170),'#dddddd')
 for i,im in enumerate(ims[start:start+6]):sheet.paste(im,((i%2)*590,(i//2)*390))
 sheet.save(r/f'analysis/contact_{start//6}.png')
print('Rendered',len(items),'trees')
