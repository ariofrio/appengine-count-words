from google.appengine.ext import blobstore
from google.appengine.ext import db

from model import WordCount

def count_words(blob_key):
    # TODO: Make this indepotent.
    blob_reader = blobstore.BlobReader(blob_key)
    word_counts = {}
    for line in blob_reader:
        for word in line.split():
            word = word.decode("utf-8")
            def txn():
                entity = WordCount.get_by_key_name(word)
                if entity is None:
                    entity = WordCount(key_name=word, count=1)
                else:
                    entity.count += 1
                entity.put()
            db.run_in_transaction(txn)
