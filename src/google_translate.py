""" Usage:
    <file-name> --in=IN_FILE --src=SOURCE_LANGUAGE --tgt=TARGET_LANGUAGE --out=OUT_FILE [--debug]
"""
# External imports
import logging
import pdb
from pprint import pprint
from pprint import pformat
from docopt import docopt
from collections import defaultdict
from operator import itemgetter
from tqdm import tqdm
# from google.cloud import translate_v2 as translate
import html
from googletrans import Translator

# Local imports

#=-----

# GOOGLE_TRANSLATE_CLIENT = translate.Client()
translator = Translator()

def google_translate(sents, target_language, source_language = None):
    """
    Run google translate on a batch of sentences.
    """
    if source_language is None:
        # Detected input language
        # TODO: it's possible that this is redundant and not needed
        trans = translator.translate(sents,
                                                  target_language = target_language)
    else:
        trans = translator.translate(sents,
                                                  source_language = source_language,
                                                  target_language = target_language)

    for out_dict in trans:
        out_dict["translatedText"] = html.unescape(out_dict["translatedText"])
    return trans
