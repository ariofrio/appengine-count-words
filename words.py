# vim: shiftwidth=4 softtabstop=4:
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import deferred

from countwords import count_words
from model import WordCount

class WordCounts(webapp.RequestHandler):
    def get(self):
        self.response.out.write(
             template.render('word_counts.html', {
                "upload_url": blobstore.create_upload_url('/upload'),
                "word_counts": WordCount.all().order('-count').fetch(30)
             }
        ))

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        upload_files = self.get_uploads('file')
        blob_info = upload_files[0]
        deferred.defer(count_words, blob_info.key())
        self.redirect('/')
    

def main():
    run_wsgi_app(webapp.WSGIApplication([
        ('/', WordCounts),
        ('/upload', UploadHandler),
    ]))

if __name__ == '__main__':
    main()

