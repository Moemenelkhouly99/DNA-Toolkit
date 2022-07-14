Nucleotide = ['A','T','C','G']
def validating_seq(seq):
    '''Function validate that DNA seq is upper case and consists of 4 nucleotide'''
    tmp_seq = seq.upper()
    for nuc in Nucleotide:
        if nuc not in tmp_seq:
            return False
    return tmp_seq
dic = {'A':0,'T':0,'C':0,'G':0}
def counting_seq(seq):
    '''Counting nucleotides'''
    for nuc in seq:
        dic[nuc]+=1
    return dic

def Transcription(seq):
    '''Allow the transcription of DNA into mRNA'''
    return seq.replace('T','U')
def DNA_complement(seq):
    return ''.join([reverse_complement_seq[nun]for nun in seq])

reverse_complement_seq = {'A':'T','T':'A','C':'G','G':'C'}
def Reverse_complement(seq):
    '''Finding the reverse complement of DNA sequence'''
    return ''.join([reverse_complement_seq[nun] for nun in seq])[::-1]

def GC_content(seq):
    return round((seq.count('C')+seq.count('G'))/len(seq)*100)

def GC_content_subseq(seq,k):
    '''Function return GC content for subsequent sequence'''
    result = []
    for i in range(0,len(seq)-k+1,k):
        subseq = seq[i:i+k]
        result.append(GC_content(subseq))
    return result

from Bio import SeqIO

def read_fasta(x):
    for seq_record in SeqIO.parse(x,'fasta'):

        return seq_record

