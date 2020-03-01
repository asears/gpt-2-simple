import os

from unittest import TestCase, mock
from unittest.mock import MagicMock
from unittest.mock import patch

import json

import warnings

warnings.filterwarnings('ignore', category=DeprecationWarning)
warnings.filterwarnings('ignore', category=FutureWarning)

from gpt_2_simple.src import model

# Disable tensorflow DeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import tensorflow as tf

class TestModel(TestCase):
    def test_init(self):
        hyper_params = model.HParams(
            n_vocab=0,
            n_ctx=1024,
            n_embd=768,
            n_head=12,
            n_layer=12,
        )

    def test_override_from_dict(self):
        hyper_params = model.HParams(
            n_vocab=0,
            n_ctx=1024,
            n_embd=768,
            n_head=12,
            n_layer=12,
        )
        param_dict = ""

        result = hyper_params.override_from_dict(param_dict)
    
    def test_default_hparams(self):
        hyper_params = model.HParams(
            n_vocab=0,
            n_ctx=1024,
            n_embd=768,
            n_head=12,
            n_layer=12,
        )

        hyper_params.default_hparams()
    
    def test_shape_list(self):
        x = ""
        result = model.shape_list(x)

    def test_softmax(self):
        x = ""
        axis = ""
        result = model.softmax(x, axis)

    def test_gelu(self):
        x = ""
        result = model.gelu(x)

    def test_norm(self):
        x = ""
        result = model.norm(x)

    def test_split_states(self):
        x = ""
        n = ""
        result = model.split_states(x, n)

    @patch('gpt_2_simple.src.model.shape_list')        
    def test_merge_states(self, mock):
        
        x = [[1, 2, 3], 
      [4, 5, 6]] 
        result = model.merge_states(x)

    def test_conv1d(self):
        x = ""
        scope = ""
        nf = ""
        w_init_stdev = 0
        result = model.conv1d(x, scope, nf, "123", w_init_stdev)

    def test_attention_mask(self):
        nd = ""
        ns = ""
        dtype = ""
        result = model.attention_mask(nd, ns, dtype=dtype)

    def test_attn(self):
        x = ""
        scope = ""
        n_state = ""
        past = ""
        hparams = ""
        result = model.attn(x, scope, n_state)#, "123", past, hparams)

    def test_mlp(self):
        x = ""
        scope = ""
        n_state = ""
        past = ""
        hparams = ""
        result = model.mlp(x, scope, n_state, "123", hparams)

    def test_block(self):
        x = ""
        scope = ""
        past = ""
        hparams = ""
        result = model.block(x, scope, "123", past, hparams)

    def test_past_shape(self):
        sequence = ""
        batch_size = ""
        hparams = ""
        result = model.past_shape("123", hparams, batch_size, sequence)

    def test_expand_tile(self):
        value = ""
        size = ""
        result = model.expand_tile(value, size)

    def test_positions_for(self):
        tokens = ""
        past_length = ""
        result = model.positions_for(tokens, past_length)

    def test_model(self):
        hparams = ""
        X = ""
        past = ""
        scope = ""
        gpus = []
        reuse = ""

        result = model.model(hparams, X, past, scope, gpus, reuse)