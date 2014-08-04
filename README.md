gunicorn-issue
==============

Please test by deploying this app to Heroku, and then use curl to post data:

    curl --data "username=foo&password=bar" http://hidden-citadel-3540.herokuapp.com/test1
  
Our test deployment is at hidden-citadel-3540.herokuapp.com.

`/test1` fails with an H18 error in Heroku's router. `/test2` always works.


Alternatively, try switching the Procfile out for Procfile.alternative, which uses an alternative server (waitress). Using waitress, both work.
