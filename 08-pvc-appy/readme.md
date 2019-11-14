# 8. Application data on persistent volume

Pre-requisites: *Exercise 4*

In the following exercises you are expected to modify the YAML specification
directly with the Rahti Application Console. At the Application Console page,
the specification can be found by clicking "Applications → Deployments", then
the name of the Deployment and finally clicking the upper right corner "Actions
→ Edit YAML".

This exercise comprises of three parts:

1.  Create and mount a persistent volume with the picture
    [https://rahti-course-nov-2019.a3s.fi/kitten.jpg](https://rahti-course-nov-2019.a3s.fi/kitten.jpg) 
    to the application `hello-flask-#` made in exercise 4 at
    `/opt/app-root/src/static`.

    Navigate to `http://hello-flask-#-course-training-#.rahtiapp.fi/kitten` and
    you should see a kitten.

    *Note*: It doesn't matter in which order you mount and copy, as long as you
    end up with pods with the file `/opt/app-root/src/static/kitten.jpg`.

    *Tip #1*: Storage can be added and mounted to the DeploymentConfig with the
    web console.

    *Tip #2*: `oc cp kitten.jpg <podname>:...` or `oc rsh dc/hello-flask-#` and `curl -L -O <url>`

2.  Create a configmap from file `custom.json` with the following contents:
    ```json
    {
     "greeting": "Custom Hello from custom.json"
    }

    *Tip #3*: `oc create configmap ...`
    ```
    Place the custom.json file visible in `/opt/app-root/src/config`.

3.  Create a secret and use that secret to bring environment variable
    "PASSWORD=secretPassword" to the application.

    You may change the password above to your liking.

    *Tip #4*: `oc create secret generic ...`

Loading urls http://hello-flask-#-course-training-#.rahtiapp.fi/kitten/ and
http://hello-flask-#-course-training-#.rahtiapp.fi/secret-kitten/secretPassword
(with # being the training account number entered earlier) should now display
kittens.

