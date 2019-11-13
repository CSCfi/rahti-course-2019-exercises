# 9. Webhook to hello-flask 

Pre-requisites: *Exercise 4*.

You can now configure GitHub webhook for your hello-flask application, this
will trigger your application builds automatically when there are push events
in your GitHub code.

Configure a GitHub webhook to the fork repository of rahti-flask-hello you made
earlier in Exercise 4.

* To find out the secret in the webhook payload look at the BuildConfig
  of the application: `oc get bc hello-flask-# -o yaml` and look for element
  `github.secret` in the array `spec.triggers`, where `#` is your training
  account number. 
* ***Tip #1***: Get the payload URI w/o the secret with `oc describe bc
  rahti-flask-#`.
* Edit app.py: Change line 6 to `DefaultTitle="Application from Student
  #"` where # is your training account number.
* Commit changes, verify that new build for your application is triggered in
  Rahti. 

