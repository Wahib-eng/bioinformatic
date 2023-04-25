from Bio import AlignIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
align = AlignIO.read("opuntia.aln", "clustal")
print(align)
print(len(align))
dummy = SeqRecord(Seq("N"*156), id="dummy")
align.append(dummy)
print(align)
print(len(align))
