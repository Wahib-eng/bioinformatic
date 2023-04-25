#create an MSA by loading an alignment file with the AlignIO module

from Bio import AlignIO
align = AlignIO.read("opuntia.aln", "clustal")
print(align)
adet=len(align)
print(adet)
for record in align:
    print("%s %i" % (record.id, len(record)))
print(align[0].id)
print(align[-1].id)
print(align[:, 1])
print(align[:, :10])
print(align[:, :10] + align[:, -10:])
