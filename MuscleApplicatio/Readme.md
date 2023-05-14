1 Introduction

MUSCLE is a program for creating multiple alignments of amino acid or nucleotide sequences. A range of options is provided that give you the choice of optimizing accuracy, speed, or some compromise between the two. Default parameters are those that give the best average accuracy in our tests. Using versions current at the time of writing, my tests show that MUSCLE can achieve both better average accuracy and better speed than CLUSTALW or T‑Coffee, depending on the chosen options. Many command line options are provided to vary the internals of the algorithm; some of these will primarily be of interest to algorithm developers who wish to better understand which features of the algorithm are important in different circumstances.

#2 Quick Start


The MUSCLE algorithm is delivered as a command-line program called muscle. If you are running under Linux or Unix you will be working at a shell prompt. If you are running under Windows, you should be in a command window (nostalgically known to us older people as a DOS prompt). If you don't know how to use command-line programs, you should get help from a local guru.

#1 Introduction
MUSCLE is a program for creating multiple alignments of amino acid or nucleotide sequences. A range of options is provided that give you the choice of optimizing accuracy, speed, or some compromise between the two. Default parameters are those that give the best average accuracy in our tests. Using versions current at the time of writing, my tests show that MUSCLE can achieve both better average accuracy and better speed than CLUSTALW or T‑Coffee, depending on the chosen options. Many command line options are provided to vary the internals of the algorithm; some of these will primarily be of interest to algorithm developers who wish to better understand which features of the algorithm are important in different circumstances.

#2 Quick Start


The MUSCLE algorithm is delivered as a command-line program called muscle. If you are running under Linux or Unix you will be working at a shell prompt. If you are running under Windows, you should be in a command window (nostalgically known to us older people as a DOS prompt). If you don't know how to use command-line programs, you should get help from a local guru.

2.1 Installation


Copy the muscle binary file to a directory that is accessible from your computer. That's it—there are no configuration files, libraries, environment variables or other settings to worry about. If you are using Windows, then the binary file is named muscle.exe. From now on muscle should be understood to mean "muscle if you are using Linux or Unix, muscle.exe if you are using Windows".

#2.2 Making an alignment
Make a FASTA file containing some sequences. (If you are not familiar with FASTA format, it is described in detail later in this Guide.) For now, just to make things fast, limit the number of sequence in the file to no more than 50 and the sequence length to be no more than 500. Call the input file seqs.fa. (An example file named seqs.fa is distributed with the standard MUSCLE package). Make sure the directory containing the muscle binary is in your path. (If it isn't, you can run it by typing the full path name, and the following example command lines must be changed accordingly). Now type:

 

muscle -in seqs.fa -out seqs.afa

 

You should see some progress messages. If muscle completes successfully, it will create a file seqs.afa containing the alignment. By default, output is created in "aligned FASTA" format (hence the .afa extension). This is just like regular FASTA except that gaps are added in order to align the sequences. This is a nice format for computers but not very readable for people, so to look at the alignment you will want an alignment viewer such as Belvu, or a script that converts FASTA to a more readable format. You can also use the –clw command-line option to request output in CLUSTALW format, which is easier to understand for people. If muscle gives an error message and you don't know how to fix it, please read the Troubleshooting section.

 

The default settings are designed to give the best accuracy, so this may be all you need to know.

2.3 Large alignments
If you have a large number of sequences (a few thousand), or they are very long, then the default settings of may be too slow for practical use. A good compromise between speed and accuracy is to run just the first two iterations of the algorithm. On average, this gives accuracy comparable to T-Coffee and speeds much faster than CLUSTALW. This is done by the option –maxiters 2, as in the following example.

 

muscle -in seqs.fa -out seqs.afa -maxiters 2

2.4 Faster speed
The –diags option enables an optimization for speed by finding common words (6-mers in a compressed amino acid alphabet) between the two sequences as seeds for diagonals. This is related to optimizations in programs such as BLAST and FASTA: you get faster speed, but sometimes lower average accuracy. For large numbers of closely related sequences, this option works very well.

 

If you want the fastest possible speed, then the following example shows the applicable options for proteins.

 

muscle -in seqs.fa -out seqs.afa -maxiters 1 -diags -sv -distance1 kbit20_3

 

For nucleotides, use:

 

muscle -in seqs.fa -out seqs.afa -maxiters 1 -diags

 

At the time of writing, muscle with these options is faster than any other multiple sequence alignment program that I have tested. The alignments are not bad, especially when the sequences are closely related. However, as you might expect, this blazing speed comes at the cost of the lowest average accuracy of the options that muscle provides.

2.5 Huge alignments
If you have a very large number of sequences (several thousand), or they are very long, then the kbit20_3 option may cause problems because it needs a relatively large amount of memory. Better is to use the default distance measure, which is roughly 2× or 3× slower but needs less memory, like this:

 

muscle -in seqs.fa -out seqs.afa -maxiters 1 -diags1 -sv

2.6 Accuracy: caveat emptor
Why do I keep using the clumsy phrase "average accuracy" instead of just saying "accuracy"? That's because the quality of alignments produced by MUSCLE varies, as do those produced other programs such as CLUSTALW and T-Coffee. The state of the art leaves plenty of room for improvement. Sometimes the fastest speed options to muscle give alignments that are better than T-Coffee, though the reverse will more often be the case. With challenging sets of sequences, it is a good idea to make several different alignments using different muscle options and to try other programs too. Regions where different alignments agree are more believable than regions where they disagree.

2.7 Pipelining
Input can be taken from standard input, and output can be written to standard output. This is the default, so our first example would also work like this:

 

muscle < seqs.fa > seqs.afa

2.8 Refining an existing alignment
You can ask muscle to try to improve an existing alignment by using the –refine option. The input file must then be a FASTA file containing an alignment. All sequences must be of equal length, gaps can be specified using dots "." or dashes "–". For example:

 

muscle -in seqs.afa -out refined.afa -refine

2.9 Using a pre-computed guide tree
The –usetree option allows you to provide your own guide tree. For example,

 

muscle -in seqs.fa -out seqs.afa -usetree mytree.phy

 

The tree must by in Newick format, as used by the Phylip package (hence the .phy extension). The Newick format is described here:

 

        http://evolution.genetics.washington.edu/phylip/newicktree.html

 

WARNING. Do not use this option just because you believe that you have an accurate evolutionary tree for your sequences. The best guide tree for multiple alignment is not in general the correct evolutionary tree. This can be understood by the following argument. Alignment accuracy decreases with lower sequence identity. It follows that given a set of profiles, the two that can be aligned most accurately will tend to be the pair with the highest identity, i.e. at the shortest evolutionary distance. This is exactly the pair selected by the nearest-neighbor criterion which MUSCLE uses by default. When mutation rates are variable, the evolutionary neighbor may not be the nearest neighbor. This explains why a nearest-neighbor tree may be superior to the true evolutionary tree for guiding a progressive alignment.

 

You will get a warning if you use the –usetree option. To disable the warning, use ­–usetree_nowarn instead,

e.g.:

 

muscle -in seqs.fa -out seqs.afa -usetree_nowarn mytree.phy

2.10 Profile-profile alignment
A fundamental step in the MUSCLE algorithm is aligning two multiple sequence alignments. This operation is sometimes called "profile-profile alignment". If you have two existing alignments of related sequences you can use the –profile option of MUSCLE to align those two sequences. Typical usage is:

 

muscle -profile -in1 one.afa -in2 two.afa -out both.afa

 

The alignments in one.afa and two.afa, which must be in aligned FASTA format, are aligned to each other, keeping input columns intact and inserting columns of gaps where needed. Output is stored in both.afa.

 

MUSCLE does not compute a similarity measure or measure of statistical significance (such as an E-value), so this option is not useful for discriminating homologs from unrelated sequences. For this task, I recommend Sadreyev & Grishin's COMPASS program.

2.11 Adding sequences to an existing alignment
To add a sequence to an existing alignment that you wish to keep intact, use profile-profile alignment with the new sequence as a profile. For example, if you have an existing alignment existing_aln.afa and want to add a new sequence in new_seq.fa, use the following commands:

 

muscle -profile -in1 existing_aln.afa -in2 new_seq.fa -out combined.afa

 

If you have more than one new sequences, you can align them first then add them, for example:

 

muscle -in new_seqs.fa -out new_seqs.afa

muscle -profile -in1 existing_aln.afa -in2 new_seqs.fa -out combined.afas

2.12 Sequence clustering
The first stage in MUSCLE is a fast clustering algorithm. This may be of use in other applications. Typical usage is:

 

muscle -cluster -in seqs.fa -tree1 tree.phy -maxiters 1

 

The sequences will be clustered, and a tree written to tree.phy. Options –weight1, –distance1, –cluster1 and –root1 can be applied if desired. Note that by default, UPGMA clustering is used. You can use

 –neighborjoining if you prefer, but note that this is substantially slower than UPGMA for large numbers of sequences, and is also slightly less accurate. See discussion of –usetree above.

2.13 Specifying a substitution matrix
You can specify your own substitution matrix by using the -matrix option. This reads a protein substitution matrix in NCBI or WU-BLAST format. The alphabet is assumed to be amino acid, and sum-of-pairs scoring is used. The ­-gapopen, -gapextend and -center parameters should be specified; normally you will specify a zero value for the center. Note that gap penalties MUST be negative. The environment variable MUSCLE_MXPATH can be used to specify a path where the matrices are stored. For example,

 

muscle -in seqs.fa -out seqs.afa -matrix blosum62 -gapopen -12.0

    -gapextend -1.0 -center 0.0

 

You can hack a nucleotide matrix by pretending that AGCT are amino acids and making a 20x20 matrix out of the original 4x4 matrix. Let me know if this isn't clear, I can help you through it.

2.14 Refining a long alignment
A long alignment can be refined using the –refinew option, which is primarily designed for refining whole-genome nucleotide alignments. Usage is:

 

muscle -in input.afa -out output.afa

 

MUSCLE divides the input alignment into non-overlapping windows and re-aligns each window from scratch, i.e. all gap characters are discarded. The –refinewindow option may be used to change the window length, which is 200 columns by default.2.1 Installation
Copy the muscle binary file to a directory that is accessible from your computer. That's it—there are no configuration files, libraries, environment variables or other settings to worry about. If you are using Windows, then the binary file is named muscle.exe. From now on muscle should be understood to mean "muscle if you are using Linux or Unix, muscle.exe if you are using Windows".

2.2 Making an alignment
Make a FASTA file containing some sequences. (If you are not familiar with FASTA format, it is described in detail later in this Guide.) For now, just to make things fast, limit the number of sequence in the file to no more than 50 and the sequence length to be no more than 500. Call the input file seqs.fa. (An example file named seqs.fa is distributed with the standard MUSCLE package). Make sure the directory containing the muscle binary is in your path. (If it isn't, you can run it by typing the full path name, and the following example command lines must be changed accordingly). Now type:

 

muscle -in seqs.fa -out seqs.afa

 

You should see some progress messages. If muscle completes successfully, it will create a file seqs.afa containing the alignment. By default, output is created in "aligned FASTA" format (hence the .afa extension). This is just like regular FASTA except that gaps are added in order to align the sequences. This is a nice format for computers but not very readable for people, so to look at the alignment you will want an alignment viewer such as Belvu, or a script that converts FASTA to a more readable format. You can also use the –clw command-line option to request output in CLUSTALW format, which is easier to understand for people. If muscle gives an error message and you don't know how to fix it, please read the Troubleshooting section.

 

The default settings are designed to give the best accuracy, so this may be all you need to know.

2.3 Large alignments
If you have a large number of sequences (a few thousand), or they are very long, then the default settings of may be too slow for practical use. A good compromise between speed and accuracy is to run just the first two iterations of the algorithm. On average, this gives accuracy comparable to T-Coffee and speeds much faster than CLUSTALW. This is done by the option –maxiters 2, as in the following example.

 

muscle -in seqs.fa -out seqs.afa -maxiters 2

2.4 Faster speed
The –diags option enables an optimization for speed by finding common words (6-mers in a compressed amino acid alphabet) between the two sequences as seeds for diagonals. This is related to optimizations in programs such as BLAST and FASTA: you get faster speed, but sometimes lower average accuracy. For large numbers of closely related sequences, this option works very well.

 

If you want the fastest possible speed, then the following example shows the applicable options for proteins.

 

muscle -in seqs.fa -out seqs.afa -maxiters 1 -diags -sv -distance1 kbit20_3

 

For nucleotides, use:

 

muscle -in seqs.fa -out seqs.afa -maxiters 1 -diags

 

At the time of writing, muscle with these options is faster than any other multiple sequence alignment program that I have tested. The alignments are not bad, especially when the sequences are closely related. However, as you might expect, this blazing speed comes at the cost of the lowest average accuracy of the options that muscle provides.

2.5 Huge alignments
If you have a very large number of sequences (several thousand), or they are very long, then the kbit20_3 option may cause problems because it needs a relatively large amount of memory. Better is to use the default distance measure, which is roughly 2× or 3× slower but needs less memory, like this:

 

muscle -in seqs.fa -out seqs.afa -maxiters 1 -diags1 -sv

2.6 Accuracy: caveat emptor
Why do I keep using the clumsy phrase "average accuracy" instead of just saying "accuracy"? That's because the quality of alignments produced by MUSCLE varies, as do those produced other programs such as CLUSTALW and T-Coffee. The state of the art leaves plenty of room for improvement. Sometimes the fastest speed options to muscle give alignments that are better than T-Coffee, though the reverse will more often be the case. With challenging sets of sequences, it is a good idea to make several different alignments using different muscle options and to try other programs too. Regions where different alignments agree are more believable than regions where they disagree.

2.7 Pipelining
Input can be taken from standard input, and output can be written to standard output. This is the default, so our first example would also work like this:

 

muscle < seqs.fa > seqs.afa

2.8 Refining an existing alignment
You can ask muscle to try to improve an existing alignment by using the –refine option. The input file must then be a FASTA file containing an alignment. All sequences must be of equal length, gaps can be specified using dots "." or dashes "–". For example:

 

muscle -in seqs.afa -out refined.afa -refine

2.9 Using a pre-computed guide tree
The –usetree option allows you to provide your own guide tree. For example,

 

muscle -in seqs.fa -out seqs.afa -usetree mytree.phy

 

The tree must by in Newick format, as used by the Phylip package (hence the .phy extension). The Newick format is described here:

 

        http://evolution.genetics.washington.edu/phylip/newicktree.html

 

WARNING. Do not use this option just because you believe that you have an accurate evolutionary tree for your sequences. The best guide tree for multiple alignment is not in general the correct evolutionary tree. This can be understood by the following argument. Alignment accuracy decreases with lower sequence identity. It follows that given a set of profiles, the two that can be aligned most accurately will tend to be the pair with the highest identity, i.e. at the shortest evolutionary distance. This is exactly the pair selected by the nearest-neighbor criterion which MUSCLE uses by default. When mutation rates are variable, the evolutionary neighbor may not be the nearest neighbor. This explains why a nearest-neighbor tree may be superior to the true evolutionary tree for guiding a progressive alignment.

 

You will get a warning if you use the –usetree option. To disable the warning, use ­–usetree_nowarn instead,

e.g.:

 

muscle -in seqs.fa -out seqs.afa -usetree_nowarn mytree.phy

2.10 Profile-profile alignment
A fundamental step in the MUSCLE algorithm is aligning two multiple sequence alignments. This operation is sometimes called "profile-profile alignment". If you have two existing alignments of related sequences you can use the –profile option of MUSCLE to align those two sequences. Typical usage is:

 

muscle -profile -in1 one.afa -in2 two.afa -out both.afa

 

The alignments in one.afa and two.afa, which must be in aligned FASTA format, are aligned to each other, keeping input columns intact and inserting columns of gaps where needed. Output is stored in both.afa.

 

MUSCLE does not compute a similarity measure or measure of statistical significance (such as an E-value), so this option is not useful for discriminating homologs from unrelated sequences. For this task, I recommend Sadreyev & Grishin's COMPASS program.

2.11 Adding sequences to an existing alignment
To add a sequence to an existing alignment that you wish to keep intact, use profile-profile alignment with the new sequence as a profile. For example, if you have an existing alignment existing_aln.afa and want to add a new sequence in new_seq.fa, use the following commands:

 

muscle -profile -in1 existing_aln.afa -in2 new_seq.fa -out combined.afa

 

If you have more than one new sequences, you can align them first then add them, for example:

 

muscle -in new_seqs.fa -out new_seqs.afa

muscle -profile -in1 existing_aln.afa -in2 new_seqs.fa -out combined.afas

2.12 Sequence clustering
The first stage in MUSCLE is a fast clustering algorithm. This may be of use in other applications. Typical usage is:

 

muscle -cluster -in seqs.fa -tree1 tree.phy -maxiters 1

 

The sequences will be clustered, and a tree written to tree.phy. Options –weight1, –distance1, –cluster1 and –root1 can be applied if desired. Note that by default, UPGMA clustering is used. You can use

 –neighborjoining if you prefer, but note that this is substantially slower than UPGMA for large numbers of sequences, and is also slightly less accurate. See discussion of –usetree above.

2.13 Specifying a substitution matrix
You can specify your own substitution matrix by using the -matrix option. This reads a protein substitution matrix in NCBI or WU-BLAST format. The alphabet is assumed to be amino acid, and sum-of-pairs scoring is used. The ­-gapopen, -gapextend and -center parameters should be specified; normally you will specify a zero value for the center. Note that gap penalties MUST be negative. The environment variable MUSCLE_MXPATH can be used to specify a path where the matrices are stored. For example,

 

muscle -in seqs.fa -out seqs.afa -matrix blosum62 -gapopen -12.0

    -gapextend -1.0 -center 0.0

 

You can hack a nucleotide matrix by pretending that AGCT are amino acids and making a 20x20 matrix out of the original 4x4 matrix. Let me know if this isn't clear, I can help you through it.

2.14 Refining a long alignment
A long alignment can be refined using the –refinew option, which is primarily designed for refining whole-genome nucleotide alignments. Usage is:

 

muscle -in input.afa -out output.afa

 

MUSCLE divides the input alignment into non-overlapping windows and re-aligns each window from scratch, i.e. all gap characters are discarded. The –refinewindow option may be used to change the window length, which is 200 columns by default.
