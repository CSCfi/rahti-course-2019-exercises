# Execute a container in a pod

## The Docker's hello-world

* Run container image `hello-world` in a pod called hello-pod:

  *`pod.yaml`*:

  ```yaml
  kind: Pod
  apiVersion: v1
  metadata:
    name: hello-pod
  spec:
    containers:
    - name: hello-container
      image: hello-world
  ```
  ```bash
  oc create -f pod.yaml
  ```
  
* Get the standard output of the container. 

  ```bash
  oc logs hello-pod
  ```

* Verify that the container is crash-looping.
  
  ```bash
  $ oc status
  In project course-rahti-demo on server https://rahti.csc.fi:8443

  pod/hello-pod runs hello-world

  Errors:
    * pod/hello-pod is crash-looping

  1 error, 1 info identified, use 'oc status --suggest' to see details.
  ```

  Fix it so that it isn't. Replace the container with fixed pod specification:

  *`pod-fixed.yaml`*:
  ```yaml
  kind: Pod
  apiVersion: v1
  metadata:
    name: hello-pod
  spec:
    containers:
    - name: hello-container
      image: hello-world
    restartPolicy: OnFailure
  ```

## Custom "Hello, world"

* Run command `echo Hello, world!` inside container from image `alpine:edge`. Name the pod as `custom-hello-pod`:

  `pod-custom.yaml`:
  ```yaml

  kind: Pod
  apiVersion: v1
  metadata:
    name: custom-hello-pod
  spec:
    containers:
    - name: custom-hello
      image: alpine:edge
      command: ["echo", "Hello, world!"]
    restartPolicy: OnFailure
  ```

* Verify that the standard output of the container really is "Hello, world!":

  ```bash
  $ oc logs custom-hello-pod
  Hello, world!
  ```

    Or from the web console: Applications → Pods, custom-hello-pod, Logs
## Cleanup

* Remove the pods named `hello-pod` and `custom-hello-pod`:

  ```bash
  $ oc delete pod hello-pod custom-hello-pod
  pod "hello-pod" deleted
  pod "custom-hello-pod" deleted
  ```
