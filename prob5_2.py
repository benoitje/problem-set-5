#! /usr/bin/env python

import ipdb
from collections import Counter
#from _future_ import print_function
from collections import defaultdict
bedfile ='/Users/jeanne/Desktop/molb7621/data-sets/bed/lamina.bed'
# for x in y, get a line back for each line in file
# for loop will run everything tabbed in (indented)

#starts = {}
data = defaultdict(list)
#starts = dict()
chrom_counts = Counter()

start_big = 0
chrom_big = 0

for line in open(bedfile):
    if line.startswith('#'):
        continue

    fields = line.strip().split('\t')

    chrom = fields[0]
    start = int(fields[1])
    end = int(fields[2])
    value = float(fields[3])

    if start > start_big:
        start_big = start
        chrom_big = chrom

print "answer-1:  %s:%s" % (chrom_big,start_big)

Y_end = 0
for line in open(bedfile):
    if line.startswith('#'):
        continue
    field = line.strip().split('\t')

    chrom = fields[0]
    start = int(fields[1])
    end = int(fields[2])
    value = float(fields[3])

    if chrom == "chrY":
        if end > Y_end:
            Y_end = end
            Y_start = start

print "answer-2:  %s:%s-%s" % (chrom,Y_start,Y_end)

filename = '/Users/jeanne/Desktop/molb7621/data-sets/fastq/SP1.fq'

line_num = 0
num_records = 0


def reverse_complement(seq):
    comps = []
    empty = ''
    for char in seq:
        if char == 'A':
            comps.append('T')
        if char == 'T':
            comps.append('A')
        if char == 'G':
            comps.append('C')
        if char == 'C':
            comps.append('G')
        if char == 'U':
            comps.append('A')
    rev_com = ''.join(reversed(comps))
    return rev_com

def sum_quals(qual):
    #val = sum (ord(i) for i in char)
    sum = 0
    for char in qual:
        sum += ord(char)
    return sum

def parse_fastq(filename):
    line_num = 0

    for line in open(filename):
        line_type = line_num % 4

        if line_type == 0:
            name = line.strip()
        elif line_type == 1:
            seq = line.strip ()
        elif line_type == 3:
            quals = line.strip ()
        #    quals_sum = sum_quals(quals)

            yield name,seq,quals

        line_num += 1

num_rec = 0
maxC = 0
#max_name 
for name, seq, quals in parse_fastq(filename):
    #ipdb.set_trace()
    #fancy stuff here

#    print seq
    counts = Counter(seq)
#     print counts['C']
    r = counts['C']
    if r > maxC:
        maxC = r
        max_name = name
       # print max_name, counts['C']
    num_rec += 1

    if num_rec > 9:
        break

print "answer-3: ",name, maxC
#print ("answer-3: ", name, maxC, file=answer.yml)

large_qual = 0
number_count = 0
for name, seq, quals in parse_fastq(filename):
    #print sum_quals(quals)

    if sum_quals(quals) > large_qual:
        large_qual = sum_quals(quals)
    number_count += 1

print "answer-4: ",large_qual

num_rec = 0
for name, seq, quals in parse_fastq(filename):
    if num_rec < 10:
 #       print seq
        rv = reverse_complement(seq)
        print "answer-5: ",rv
    num_rec += 1

