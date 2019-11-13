# 7. Hello world web server with DeploymentConfig

Pre-requisites: *Exercise 1*

In this exercise, write (or copy-paste from slides) all the API objects in YAML
plaintext and submit them with `oc create -f ...`. 

## DeploymentConfig

* Create a DeploymentConfig that will spawn a pod running image
  `openshift/hello-openshift`. Name it `hello-openshift` and label it `app:
  hello-openshift`. Apply the same label `app: hello-openshift` to the pods to
  be spawned as well.
  * What is the name of the pod that appeared? *Hint: `oc get pod -l
    app=hello-openshift`*.
  * Delete the pod. 
  * What is the name of the pod that appeared?
* List all objects that have metadata label `app: hello-openshift`. What
  *Kinds* of objects are listed?

## Service

* Create a Service object that will redirect traffic internally to the pod.

## Route

* Expose the Service to internet at 'hello-rahti-##.rahtiapp.fi', where ## is
  the number of the training account you are holding.
  * Secure the route with TLS edge termination policy and redirect
    insecure traffic to the secure one.

## Cleanup: DeploymentConfig

* If you remove DeploymentConfig, what will happen to the corresponding ReplicationController and Pods?
* Remove DeploymentConfigs. Did you guess correctly?
* *Bonus*: Why did it happen?

## Cleanup: The rest

* Remove the Route and the Service objects.

