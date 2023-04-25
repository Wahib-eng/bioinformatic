from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment
a = SeqRecord(Seq("AAAACGT"), id="Alpha")
b = SeqRecord(Seq("AAA-CGT"), id="Beta")
c = SeqRecord(Seq("AAAAGGT"), id="Gamma")
d = SeqRecord(Seq("AAAACGT"), id="Delta")
e = SeqRecord(Seq("AAA-GGT"), id="Epsilon")
align = MultipleSeqAlignment([a, b, c])
print(align)
align.extend([d, e])
print(align)
