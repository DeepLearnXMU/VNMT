#! /usr/bin/python

'''
python sample.py --state search_state.pkl --beam-search --beam-size 10 --ignore-unk --source nist05.src.sen  --trans nist05.trans --verbose ./search_model.npz
 python evaluate.py ~/.pro/.cps/nist_test/nist05/src.sgm ~/.pro/.cps/nist_test/nist05/ref.sgm ./nist05.trans
'''

import sys
import os
from os import system as run

from evaluate import eval_trans

path = os.path.dirname(os.path.realpath(__file__))
def save_valid_model(state):
    prefix = state['prefix'][:-1]

    run('cp {0}_state.pkl best_{0}_state.pkl'.format(prefix))
    run('cp {0}_model.npz best_{0}_model.npz'.format(prefix))
    run('cp {0}_timing.npz best_{0}_timing.npz'.format(prefix))

    run('cp {0}_{1} best_dev_{0}_{1}'.format(prefix, state['dev_trs']))
    run('cp {0}_{1}.sgm best_dev_{0}_{1}.sgm'.format(prefix, state['dev_trs']))
    run('cp {0}_{1}.eval.nmt best_dev_{0}_{1}.eval.nmt'.format(prefix, state['dev_trs']))

def validate_translation(state):
    ### 0. model parameters
    prefix = state['prefix'][:-1]
    beam_size  = state['beam_size']
    ignore_unk = state['ignore_unk']

    sample_cmd = '--state {prefix}_state.pkl --verbose --beam-search --beam-size {beam_size}'.format(prefix=prefix, beam_size=beam_size)
    if ignore_unk:
        sample_cmd += ' --ignore-unk'

    ### 1. validate development sets
    dev_src = state['dev_src']
    dev_tgt = state['dev_tgt']
    dev_trs = state['dev_trs']

    cmd = 'python %s/sample.py %s --source %s.plain --trans %s_%s %s_model.npz' % (path, sample_cmd, dev_src, prefix, dev_trs, prefix)
    print cmd
    run(cmd)
    dev_bleu = eval_trans(dev_src + ".sgm", dev_tgt, prefix + '_' + dev_trs)
    print "development set bleu:\t", dev_bleu
    run('echo "Step:%s Development set bleu:%s" | cat >> %s_%s' % (state['step'], dev_bleu, prefix, state['dev_record']))

    ### 3. decide for save
    if not 'dev_score' in state:
        state['dev_score'] = -1.
    if dev_bleu > state['dev_score']:
        state['dev_score'] = dev_bleu
        save_valid_model(state)
        print "the best model is updated"
