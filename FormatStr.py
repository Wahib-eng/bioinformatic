#Return the alignment as a string in specific format 

from Bio.Align import MultipleSeqAlignment
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

seq1 = Seq("ACTGCTAGCTAG")
seq2 = Seq("ACT-CTAGCTAG")
seq3 = Seq("ACTGCTAGATAG")

rec1 = SeqRecord(seq1, id="Alpha")
rec2 = SeqRecord(seq2, id="Beta")
rec3 = SeqRecord(seq3, id="Gamma")

records = [rec1, rec2, rec3]


align = MultipleSeqAlignment(records)

fasta_str = ""
for record in align:
    fasta_str += ">{}\n{}\n".format(record.id, record.seq)

phylip_str = "{} {}\n".format(len(records), len(records[0].seq))
for record in align:
    phylip_str += "{} {}\n".format(record.id, record.seq)

print(fasta_str)
print(phylip_str)
