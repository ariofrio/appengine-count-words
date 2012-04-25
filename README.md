# Count words demo application

This Google AppEngine application allows you to upload text files and it 
will keep a count of the words it encounters, displaying the top 30 words.

It uses the [deferred][] library so that file processing is done in the 
background (in a queue, by workers, etc).

  [deferred]: https://developers.google.com/appengine/articles/deferred
