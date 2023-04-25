
#Iterate over alignment rows as SeqRecord objects.

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment

seq1 = Seq("ACTGCTAGCTAG")
seq2 = Seq("ACT-CTAGCTAG")
seq3 = Seq("ACTGCTAGATAG")

records = [SeqRecord(seq1, id="Alpha"),
           SeqRecord(seq2, id="Beta"),
           SeqRecord(seq3, id="Gamma")]

align = MultipleSeqAlignment(records, annotations={"gap_char": "-"})

for record in align:
    print(record.id)
    print(record.seq)
