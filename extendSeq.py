from Bio.Align import MultipleSeqAlignment
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

align = MultipleSeqAlignment([])
seq1 = SeqRecord(Seq("ACTGCTAGCTAG"), id="Alpha")
seq2 = SeqRecord(Seq("ACT-CTAGCTAG"), id="Beta")
seq3 = SeqRecord(Seq("ACTGCTAGATAG"), id="Gamma")
align.extend([seq1, seq2, seq3])
print(align)
