# 10. BuildConfigs and Triggers

Pre-requisites: *Exercise 1*.

## Inlining Dockerfiles for the base image

Create a BuildConfig inlining the following `Dockerfile` (don't be tempted to
uncomment the `#RUN ...` lines yet)
```Dockerfile
FROM nginx:mainline-alpine

#RUN chmod g+rwX /var/cache/nginx /var/run /var/log/nginx
#RUN chgrp -R root /var/cache/nginx

COPY cfg/default.conf /etc/nginx/conf.d/default.conf
COPY cfg/nginx.conf /etc/nginx/nginx.conf
COPY cfg/index.html /usr/share/nginx/html/index.html
#RUN chmod -R g+rX /etc/nginx/

RUN chmod -R g+rX /usr/share/nginx/html
EXPOSE 8080
```

* Use the ConfigMap listed in file `nginx-config.yaml` to provide the files
`cfg/default.conf`, `cfg/nginx.conf` and `cfg/index.html` to the build context.
  * **Bonus**: Create the nginx-config.yaml file by yourself from files under
    `cfg/` directory. 
    * ***Tip #1***: `oc create configmap <name> --from-file=<file1>
      --from-file=<file2> ... --dry-run -o yaml`
* Create an ImageStream object named `my-openshift-nginx` and set the output of
your BuildConfig to ImageStreamTag `my-openshift-nginx:latest`.

* ***Tip #2***: Create skeleton code of the objects with `oc new-build my-bc
--dry-run -o yaml --allow-missing-images -D - > bcs.yaml` and copy-paste the
Dockerfile above and press Control-D.

## Actual website from Github

Fork `github.com/cscfi/rahti-httpd-ex` in GitHub. Add the following Dockerfile 
to your fork:

```Dockerfile
FROM my-openshift-nginx:latest
COPY ./ /usr/share/nginx/html/
RUN rm /usr/share/nginx/html/Dockerfile
RUN chmod -R g+rX /usr/share/nginx/html
```

Create a scaffolding for a new application with the following command
```bash
$ oc --name new-app my-static-home https://github.com/<youraccount>/rahti-httpd-ex \
    --dry-run -o yaml > scaffolding.yaml
```

The file `scaffolding.yaml` will now contain multiple API objects in a *List*
object.

The container `my-static-home` should be in a crash-loop right now. The lines
starting with `#RUN ...` in the first Dockerfile should not have be commented
out in the first place after all―the correct Dockerfile looks like be:

```Dockerfile
FROM nginx:mainline-alpine

RUN chmod g+rwX /var/cache/nginx /var/run /var/log/nginx
RUN chgrp -R root /var/cache/nginx

COPY cfg/default.conf /etc/nginx/conf.d/default.conf
COPY cfg/nginx.conf /etc/nginx/nginx.conf
COPY cfg/index.html /usr/share/nginx/html/index.html
RUN chmod -R g+rX /etc/nginx/

RUN chmod -R g+rX /usr/share/nginx/html
EXPOSE 8080
```

Modify the BuildConfig housing Dockerfile defined in the first part in and
rebuild the image in ImageStreamTag `my-openshift-nginx:latest`. ***Tip #3***:
You can modify the Dockerfile directly from the web console: Locate the
BuildConfig and click Actions → Edit.

Once build has been completed, the final application should work and you can
make a Route to it.

