#! /usr/bin/python

'''
    Evaluate the translation result from Neural Machine Translation
'''

import sys
import os
import re
import time
import string

run = os.system
path = os.path.dirname(os.path.realpath(__file__))

def split_seg(line):
    p1 = line.find(">")+1
    p2 = line.rfind("<")
    return [ line[:p1], line[p1:p2], line[p2:] ]

def plain2sgm(trg_plain, src_sgm, trg_sgm):
    "Converse plain format to sgm format"
    fin_trg_plain = file(trg_plain , "r")
    fin_src_sgm = file(src_sgm, "r")
    fout = file(trg_sgm, "w")

    #head
    doc_head = fin_src_sgm.readline().rstrip().replace("srcset", "tstset")
    if doc_head.find("trglang") == -1 :
        doc_head = doc_head.replace(">", " trglang=\"en\">")
    print >> fout, doc_head

    for line in fin_src_sgm:
        line = line.rstrip()
        #process doc tag
        if "<doc" in line or "<Doc" in line or "<DOC" in line:
            p1 = line.find('"')
            p2 = line.find('"' , p1+1)
            id = line[p1+1 : p2]
            print >> fout, '''<doc docid="%s" sysid="hiero">''' %id
        elif line.startswith("<seg"):
            head, body , tail  = split_seg(line)
            print >> fout, head, fin_trg_plain.readline().rstrip(), tail
        elif line.strip() == "</srcset>":
            print >> fout, "</tstset>"
        else:
            print >> fout, line

    fout.close()
    fin_src_sgm.close()

def get_bleu(fe):
    "Get the bleu score from result file printed by mteval"

    c = file(fe, "rU").read()
    reg = re.compile(r"BLEU score =\s+(.*?)\s+")
    r = reg.findall(c)
    assert len(r) == 1
    return float(r[0])

def eval_trans(src_sgm, ref_sgm, trs_plain):

    plain2sgm(trs_plain, src_sgm, "result.sgm")
    run("%s/mteval-v11b.pl -s %s -r %s -t result.sgm > %s.eval.nmt" \
            %(path, src_sgm, ref_sgm, trs_plain))
    eval_nmt = ''.join(file('%s.eval.nmt' % trs_plain, 'rU').readlines())
    print >> file('%s.eval.nmt' % trs_plain, 'w'), eval_nmt.replace('hiero', 'Nerual Machine Translation')
    run('mv result.sgm %s.sgm' % trs_plain)

    return get_bleu('%s.eval.nmt' % trs_plain)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print '%s src_sgm, ref_sgm, trs_plain' % sys.argv[0]
        sys.exit(0)

    src_sgm = sys.argv[1]
    ref_sgm = sys.argv[2]
    trs_plain = sys.argv[3]

    eval_trans(src_sgm, ref_sgm, trs_plain)
