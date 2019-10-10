from align_sequence import indexed_alignment, global_alignment
from read_fasta import read_file
import time

import os
import psutil

# pid = os.getpid()
# py = psutil.Process(pid)

queries = read_file("HW3_Queries.fna")
reference = "".join(read_file("HW3_References.fna"))
#print(len(queries),len(reference))
indexed_timing = []
global_timing = []
for query in queries:
    print("Index alignemnt for ", query)
    start = time.time()
    indexed_alignment(query,reference)
    end = time.time()
    indexed_timing.append(end-start)
    start = time.time()
    global_alignment(query,reference)
    end = time.time
    global_timing.append(end-start)

print("Average time for indexed alignment:", sum(indexed_timing)/len(indexed_timing))
print("Average time for global alignment:", sum(global_timing)/len(global_timing))