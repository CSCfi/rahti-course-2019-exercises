# 6. OOM killer

Create pod yaml-spec that runs the image
`docker-registry.default.svc:5000/rahti-course-2019/oom-killer:1`. That image
contains a python code, listed in `app/app.py` file, that reserves 10MB more memory
every second.

Make sure that the container gets killed when it reserves over 50MB of memory.

