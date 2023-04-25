
# load an MSA from a file using a list of SeqRecord objects

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment

a = SeqRecord(Seq("AAAACGT"), id="Alpha")
b = SeqRecord(Seq("AAA-CGT"), id="Beta")
c = SeqRecord(Seq("AAAAGGT"), id="Gamma")

align = MultipleSeqAlignment([a, b, c],
                             annotations={"tool": "demo"},
                             column_annotations={"stats": "CCCXCCC"})

print(align)
