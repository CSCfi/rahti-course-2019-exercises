# 5. Liveness and Readiness probes

Pre-requisites: *Exercise 1*

The following pod waits for 30 seconds, then creates the file `/tmp/alive`
inside the container, then waits again for 30 seconds and deletes the file.

* Edit the specification so that the container is "ready" and "live" only if
  the file `/tmp/alive` exists.
* Wait for 30 seconds before starting to check if the container is live. 
* Try what happens if the liveness probing starts immediately when the container is started?
* **Cleanup**: Delete the pod from the cluster afterwards with `oc delete pod probe-tests`.

*Tip #1*: Go to Monitoring page on the Application Console to see the status of
your pod.

*Tip #2*: You can monitor the pod with `watch oc describe pod probe-tests` or
`watch oc get pod probe-tests`

*Tip #3*: The GNU coreutils tool *`cat <filename>`* returns 0 if the
<filename> exists and everything went fine.

```yaml
kind: Pod
apiVersion: v1
metadata:
  name: probe-tests
spec:
  containers:
  - name: probe-test-container
    image: centos:7
    command:
    - sh
    - -c
    - >
      echo "Waiting for 30 seconds to go live" && 
      for i in {1..30}; do echo "."; sleep 1; done && 
      touch /tmp/alive && 
      echo "Now waiting for 30 seconds to go die" && 
      for i in {1..30}; do echo "."; sleep 1; done && 
      rm /tmp/alive && 
      echo "Going to sleep mode" && 
      sleep inf
```
