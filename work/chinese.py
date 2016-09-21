dict(
    target = ["/home/bzhang/.pro/.lib/neumt/github/nmt-master/nmt/works/step_-1_prepare_datas/binarized_text.en.shuf.h5"],
    source = ["/home/bzhang/.pro/.lib/neumt/github/nmt-master/nmt/works/step_-1_prepare_datas/binarized_text.zh.shuf.h5"],
    indx_word = "/home/bzhang/.pro/.lib/neumt/github/nmt-master/nmt/works/step_-1_prepare_datas/ivocab.zh.pkl",
    indx_word_target = "/home/bzhang/.pro/.lib/neumt/github/nmt-master/nmt/works/step_-1_prepare_datas/ivocab.en.pkl",
    word_indx = "/home/bzhang/.pro/.lib/neumt/github/nmt-master/nmt/works/step_-1_prepare_datas/vocab.zh.pkl",
    word_indx_trgt = "/home/bzhang/.pro/.lib/neumt/github/nmt-master/nmt/works/step_-1_prepare_datas/vocab.en.pkl",
    seqlen = 50,
    sort_k_batches = 20,

    null_sym_source = 30000,
    null_sym_target = 30000,
    n_sym_source = 30001,
    n_sym_target = 30001,

    timeStop = 24*60*31,
    loopIters = 36250*12*3,
    hookFreq = 4000,

    ### for validation
    beam_size = 10,
    ignore_unk = False,
    maxsamp = 10,

    ### variational
    v_dim = 2000,

    ### dev setting
    validFreq = 20,
    dev_record = "bleu.curve.record",
    dev_src = "/home/bzhang/.pro/.cps/nist_test/nist05/src",
    dev_tgt = "/home/bzhang/.pro/.cps/nist_test/nist05/ref.sgm",
    dev_trs = "nist05.nmt.trs",
)
