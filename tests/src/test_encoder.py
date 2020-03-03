# from unittest import TestCase, mock
# from unittest.mock import MagicMock
# from unittest.mock import patch

# import json

# import warnings

# warnings.filterwarnings('ignore', category=DeprecationWarning)
# warnings.filterwarnings('ignore', category=FutureWarning)

# from gpt_2_simple.src import encoder
    
# class TestEncoder(TestCase):
#     def test_init(self):
  
#         mockjson = '{ "name":"test"}'
#         encitems = json.loads(mockjson)
#         bpe_merges = ''
#         errors='replace'
#         result = encoder.Encoder(encitems, bpe_merges, errors)

#     def test_bytes_to_unicode(self):
#         result = encoder.bytes_to_unicode()
    
#     def test_get_pairs(self):
#         word = 'test','123'
#         result = encoder.get_pairs(word)

#     def test_bpe(self):
#         mockjson = '{ "name":"test"}'
#         encitems = json.loads(mockjson)
#         bpe_merges = ''
#         errors='replace'
#         enc = encoder.Encoder(encitems, bpe_merges, errors)

#         token =  'test','123'
#         result = enc.bpe(token)

#     def test_encode(self):
#         mockjson = '{ "name":"test"}'
#         encitems = json.loads(mockjson)
#         bpe_merges = ''
#         errors='replace'
#         enc = encoder.Encoder(encitems, bpe_merges, errors)

#         text =  'test def','abc 123'
#         result = enc.encode(text)

#     def test_decode(self):
#         mockjson = '{ "name":"test"}'
#         encitems = json.loads(mockjson)
#         bpe_merges = ''
#         errors='replace'
#         enc = encoder.Encoder(encitems, bpe_merges, errors)

#         tokens =  'test','123'
#         result = enc.decode(tokens)
 
#     def test_get_encoder(self):
#         checkpoint_path = "./tests/"
#         with patch('os.open', mock.mock_open(read_data='encodertest.json')) as m:
#             result = encoder.get_encoder(checkpoint_path)

