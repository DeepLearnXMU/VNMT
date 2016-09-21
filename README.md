# VNMT

Source code for variational neural machine translation, we will make it available soon!

If you use this code, please cite our paper:
```
@InProceedings{Zhang:EMNLP:2016:VNMT,
  author    = {Biao Zhang, Deyi Xiong, Jinsong Su, Hong Duan and Min Zhang},
  title     = {Variational Neural Machine Translation},
  booktitle = {Proc. of EMNLP},
  year      = {2016},
}
```

## Basic Requirement

Our source is based on the <a href="https://github.com/lisa-groundhog/GroundHog">GroundHog</a>. Before use our code, please install it.

## How to Run?

To train a good VNMT model, you need follow two steps.

###  Step 1. Pretraining

Pretrain a good base model using the GroundHog.

### Step 2. Retraining

Go to the `work` directory, and put the pretrained model to this directory.

Simply Run (Clearly, before that you need re-config the `chinese.py` file to your own dataset :))
```
run.sh
```
That's it!

*Notice that our test and deveopment set is the NIST dataset, which follow the `sgm` format!*

For any comments or questions, please email <a href="mailto:zb@stu.xmu.edu.cn">Biao Zhang</a>.
