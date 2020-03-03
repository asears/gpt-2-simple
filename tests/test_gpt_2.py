import os

from unittest import TestCase, mock
from unittest.mock import patch

import pytest
import requests

# Tensorflow warings will kill test discovery and throw spurious errors with py.test, suppress them
# This shows up as error Error: 2020-03-01 15:43:56.145370: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cudart64_101.dll
# Disable tensorflow DeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses

import warnings

warnings.filterwarnings('ignore', category=DeprecationWarning)
warnings.filterwarnings('ignore', category=FutureWarning)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

from gpt_2_simple import gpt_2

# TODO Mock tensorflow, external dependencies
class Object(object):
    pass

class TestGpt_2(TestCase):

    def test_init(self):
        pass
    
    @mock.patch("requests.get")
    @mock.patch("builtins.open")
    def test_download_file_with_progress(self, requests_mock, builtin_opens_mock):
        url_base = ""
        sub_dir = ""
        model_name = ""
        file_name = ""

        result = gpt_2.download_file_with_progress(
            url_base, sub_dir, model_name, file_name)

    @mock.patch("gpt_2_simple.gpt_2.download_file_with_progress")
    @mock.patch("builtins.open")
    @mock.patch("os.makedirs")
    def test_download_gpt2(self, requests_mock, builtin_opens_mock, os_makedirs_mock):
        model_dir = ""
        model_name = ""

        result = gpt_2.download_gpt2(model_dir, model_name)



    @mock.patch("tensorflow.compat.v1.ConfigProto")
    @mock.patch("tensorflow.compat.v1.Session")
    def test_start_tf_sess(self, tf_configproto_mock, tf_session_mock):
        threads = 0
        server = Object()
        server.target = ""

        result = gpt_2.start_tf_sess(threads, server)

    # start_tf_sess
    # reset_session
    # get_available_gpus
    # finetune
    # load_gpt2
    # generate
    # generate_to_file
    # mount_gdrive
    # is_mounted
    # get_tarfile_name
    # copy_checkpoint_to_gdrive
    # copy_checkpoint_from_gdrive
    # copy_file_to_gdrive
    # copy_file_from_gdrive
    # is_gpt2_downloaded
    # encode_csv
    # encode_dataset
    # cmd
    # cmd_finetune
    # cmd_generate
