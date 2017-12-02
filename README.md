# VNMT

*Current implementation for VNMT only support 1 layer NMT! Deep layers are meaningless.*

Source code for variational neural machine translation, we will make it available soon!

If you use this code, please cite <a href="http://www.aclweb.org/anthology/D/D16/D16-1050.pdf">our paper</a>:
```
@InProceedings{zhang-EtAl:2016:EMNLP20162,
  author    = {Zhang, Biao  and  Xiong, Deyi  and  su, jinsong  and  Duan, Hong  and  Zhang, Min},
  title     = {Variational Neural Machine Translation},
  booktitle = {Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing},
  month     = {November},
  year      = {2016},
  address   = {Austin, Texas},
  publisher = {Association for Computational Linguistics},
  pages     = {521--530},
  url       = {https://aclweb.org/anthology/D16-1050}
}
```

## Basic Requirement

Our source is based on the <a href="https://github.com/lisa-groundhog/GroundHog">GroundHog</a>. Before use our code, please install it.

## How to Run?

To train a good VNMT model, you need follow two steps.

###  Step 1. Pretraining

Pretrain a base model using the GroundHog.

### Step 2. Retraining

Go to the `work` directory, and put the pretrained model to this directory, i.e. use the pretrained model to initialize the parameters of VNMT.

Simply Run (Clearly, before that you need re-config the `chinese.py` file to your own dataset :))
```
run.sh
```
That's it!

*Notice that our test and deveopment set is the NIST dataset, which follow the `sgm` format! Please see the `work/data/dev` for example.*

For any comments or questions, please email <a href="mailto:zb@stu.xmu.edu.cn">Biao Zhang</a>.
