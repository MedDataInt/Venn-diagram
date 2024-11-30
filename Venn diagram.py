### Visualization 
### venn diagram 

# basic
from bioinfokit import visuz
visuz.venn(vennset=(1595,133,196,522,789,96,133), vennlabel = ('Human', 'Mouse', 'CellLine'))
# note: order the set in (100,010,110,001,101,011,111) format


# change default colors
visuz.venn(vennset=(1595,133,196,522,789,96,133), vennlabel = ('Human', 'Mouse', 'CellLine'),
venncolor=('#ff6347', '#008000', '#FF00FF'))

# change default transparency 
visuz.venn(vennset=(1595,133,196,522,789,96,133), vennlabel = ('Human', 'Mouse', 'CellLine'),
venncolor=('#ff6347', '#008000', '#FF00FF'), vennalpha=0.9)

