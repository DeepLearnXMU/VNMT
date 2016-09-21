#! /bin/bash

THEANO_FLAGS='floatX=float32,device=gpu0,nvcc.fastmath=True'  python train.py --proto=prototype_search_state --state chinese.py
