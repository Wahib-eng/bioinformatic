

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment

a1 = SeqRecord(Seq("AAAAC"), id="Alpha")
b1 = SeqRecord(Seq("AAA-C"), id="Beta")
c1 = SeqRecord(Seq("AAAAG"), id="Gamma")
a2 = SeqRecord(Seq("GT"), id="Alpha")
b2 = SeqRecord(Seq("GT"), id="Beta")
c2 = SeqRecord(Seq("GT"), id="Gamma")

left = MultipleSeqAlignment([a1, b1, c1],

annotations={"tool": "demo", "name": "start"},

column_annotations={"stats": "CCCXC"})

right = MultipleSeqAlignment([a2, b2, c2],

annotations={"tool": "demo", "name": "end"},
column_annotations={"stats": "CC"})

print("Left alignment:\n",left)
print("right alignment:\n",right)

combined = left + right
print("combined alignment:\n",combined)

print("Left alignment:\n",len(left))
print("right alignment:\n",len(right))
print("combined alignment:\n",len(combined))
print(combined.annotations)
print(combined.column_annotations)
