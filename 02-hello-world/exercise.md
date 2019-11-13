# 2. Execute a container in a pod

Pre-requisites: *Exercise 1*

## The Docker's hello-world

* Run container image [`hello-world`](https://hub.docker.com/_/hello-world) in
  a pod called hello-pod.
* Get the standard output of the container. 
* Verify that the container is crash-looping. Fix it so that it isn't. Replace
  the container with fixed pod specification.

## Custom "Hello, world"

* Run command `echo Hello, world!` inside container from image `alpine:edge`.
  Name the pod as `custom-hello-pod`.

* Verify that the standard output of the container really is "Hello, world!".

## Sleeping pod

* Create a pod based on `alpine:edge` image that sleeps for 7200 seconds and
  then exits. Name it `sleeping-pod`.

## Cleanup

* Remove the pods named `hello-pod` and `custom-hello-pod`. Let the sleeping pod sleep.

