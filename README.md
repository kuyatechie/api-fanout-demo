# api-fanout-demo
This project is to demonstrate simple URL fanout API

## Prerequisite
Linux Environment
Python 3.10+
Docker
Docker Compose

### Install Python libraries
Using Ubuntu
```
$ apt install python3-pip
$ pip install -r requirements.txt
$ apt-get install docker docker-compose
```

## How to use
The app directory is in app folder
```
$ cd app
```

### Migrate database
Note: There is no actual model in this project. Migrating database doesn't affect the functionality but is done to reduce runtime warnings. You can skip this part as well.
```
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, constance, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying constance.0001_initial... OK
  Applying constance.0002_migrate_from_old_table... OK
  Applying constance.0003_drop_pickle... OK
  Applying sessions.0001_initial... OK
```

### Using help tool
Run help to see available commands. Notice that port number is an optional argument and message is a positional argument.
Default message is "Hello World!"
Default port is 8000
```
$ python manage.py runserver --help
usage: manage.py runserver [-h] [--addrport ADDRPORT] [--ipv6] [--nothreading] [--noreload] [--version]
                           [--settings SETTINGS] [--pythonpath PYTHONPATH] [--no-color] [--force-color]
                           [--skip-checks]
                           message [message ...]

Starts a lightweight web server for development.

positional arguments:
  message               Message to return response from index.

options:
  -h, --help            show this help message and exit
  --addrport ADDRPORT   Optional port number, or ipaddr:port
  --ipv6, -6            Tells Django to use an IPv6 address.
  --nothreading         Tells Django to NOT use threading.
  --noreload            Tells Django to NOT use the auto-reloader.
  --version             Show program's version number and exit.
  --settings SETTINGS   The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided,
                        the DJANGO_SETTINGS_MODULE environment variable will be used.
  --pythonpath PYTHONPATH
                        A directory to add to the Python path, e.g. "/home/djangoprojects/myproject".
  --no-color            Don't colorize the command output.
  --force-color         Force colorization of the command output.
  --skip-checks         Skip system checks.
```

### Running the app
#### To run the app
```
$ python manage.py runserver --addrport 5000 -- Hello!
Setting up the return response to Hello!
Setting up the return response to Hello!
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 20, 2024 - 10:38:22
Django version 5.1.1, using settings 'app.settings'
Starting development server at http://0.0.0.0:5000/
Quit the server with CONTROL-C.
```

#### On another terminal
```
$ curl localhost:5000
Hello!
```

## Dockerizing the application
All docker commands should be ran from the workdir.
```
$ cd ..
$ pwd
/home/arvin/workspace/api-fanout-demo
```

### Build docker image
```
$ docker build --tag api-fanout-demo .
[+] Building 13.8s (10/10) FINISHED                                                                      docker:default
 => [internal] load build definition from Dockerfile                                                               0.0s
 => => transferring dockerfile: 381B                                                                               0.0s
 => [internal] load metadata for docker.io/library/python:bookworm                                                 0.5s
 => [internal] load .dockerignore                                                                                  0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [1/5] FROM docker.io/library/python:bookworm@sha256:096c49cf57695962d6d5e2998d0d23640b4234dfffcd8472d48adceb5  0.0s
 => [internal] load build context                                                                                  0.0s
 => => transferring context: 1.69kB                                                                                0.0s
 => CACHED [2/5] ADD app /app                                                                                      0.0s
 => [3/5] COPY requirements.txt /app/requirements.txt                                                              0.0s
 => [4/5] WORKDIR /app                                                                                             0.0s
 => [5/5] RUN apt-get update &&     apt-get install python3-pip -y &&     pip3 install -r /app/requirements.txt   12.5s
 => exporting to image                                                                                             0.7s
 => => exporting layers                                                                                            0.7s
 => => writing image sha256:9972e34e28fe2746fcc16be21eef2df7c139deb150768e5cb2493ce46801968a                       0.0s
 => => naming to docker.io/library/api-fanout-demo                                                                 0.0s
```

### Run app via Docker container
#### Run docker container
```
$ docker run -p 5000:5000 api-fanout-demo --addrport 5000 Hello World!
Setting up the return response to Hello World!
Setting up the return response to Hello World!
Performing system checks...

System check identified no issues (0 silenced).
September 20, 2024 - 19:58:59
Django version 5.1.1, using settings 'app.settings'
Starting development server at http://0.0.0.0:5000/
Quit the server with CONTROL-C.
```
#### On another terminal
```
$ curl localhost:5000
Hello World!
```

## Using Docker Compose
### Build the images
```
$ docker compose build
[+] Building 1.0s (17/21)                                                                                docker:default
 => [webapp_b internal] load build definition from Dockerfile                                                      0.0s
 => => transferring dockerfile: 314B                                                                               0.0s
 => [webapp_a internal] load build definition from Dockerfile                                                      0.0s
 => => transferring dockerfile: 314B                                                                               0.0s
 => [webapp_a internal] load metadata for docker.io/library/python:bookworm                                        0.9s
 => [webapp_b auth] library/python:pull token for registry-1.docker.io                                             0.0s
 => [webapp_b internal] load .dockerignore                                                                         0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [webapp_a internal] load .dockerignore                                                                         0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [webapp_a 1/5] FROM docker.io/library/python:bookworm@sha256:096c49cf57695962d6d5e2998d0d23640b4234dfffcd8472  0.0s
 => [webapp_b internal] load build context                                                                         0.0s
 => => transferring context: 1.64kB                                                                                0.0s
 => [webapp_a internal] load build context                                                                         0.0s
 => => transferring context: 8.18kB                                                                                0.0s
 => CACHED [webapp_b 2/5] COPY requirements.txt /app/requirements.txt                                              0.0s
 => CACHED [webapp_b 3/5] RUN apt-get update &&     apt-get install python3-pip -y &&     pip3 install -r /app/re  0.0s
 => CACHED [webapp_b 4/5] ADD app /app                                                                             0.0s
 => CACHED [webapp_a 5/5] WORKDIR /app                                                                             0.0s
 => [webapp_b] exporting to image                                                                                  0.0s
 => => exporting layers                                                                                            0.0s
 => => writing image sha256:736b251c1e0bc23e11af6d3355ea54e88b475b5980565e4c7aa796f03cfb94be                       0.0s
 => => naming to docker.io/library/api-fanout-demo-webapp_b                                                        0.0s
 => [webapp_a] exporting to image                                                                                  0.0s
 => => exporting layers                                                                                            0.0s
 => => writing image sha256:f733affc9e962f8eb1290a94e924687a68646531ef005c56345d06d55fb90f8b                       0.0s
 => => naming to docker.io/library/api-fanout-demo-webapp_a                                                        0.0s
 => [webapp_a] resolving provenance for metadata file                                                              0.0s
 => [webapp_b] resolving provenance for metadata file                                                              0.0s
```

### Run docker compose up
#### Run command
```
$ docker compose up
[+] Running 4/4
 ✔ Network api-fanout-demo_default       Created                                                                   0.0s
 ✔ Container api-fanout-demo-webapp_a-1  Created                                                                   0.0s
 ✔ Container api-fanout-demo-webapp_b-1  Created                                                                   0.0s
 ✔ Container api-fanout-demo-router-1    Created                                                                   0.0s
Attaching to router-1, webapp_a-1, webapp_b-1
router-1    | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
router-1    | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
router-1    | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
router-1    | 10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
router-1    | 10-listen-on-ipv6-by-default.sh: info: /etc/nginx/conf.d/default.conf differs from the packaged version
router-1    | /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
router-1    | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
router-1    | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
router-1    | /docker-entrypoint.sh: Configuration complete; ready for start up
router-1    | 2024/09/20 20:03:50 [notice] 1#1: using the "epoll" event method
router-1    | 2024/09/20 20:03:50 [notice] 1#1: nginx/1.27.1
router-1    | 2024/09/20 20:03:50 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14)
router-1    | 2024/09/20 20:03:50 [notice] 1#1: OS: Linux 5.15.153.1-microsoft-standard-WSL2
router-1    | 2024/09/20 20:03:50 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
router-1    | 2024/09/20 20:03:50 [notice] 1#1: start worker processes
router-1    | 2024/09/20 20:03:50 [notice] 1#1: start worker process 28
router-1    | 2024/09/20 20:03:50 [notice] 1#1: start worker process 29
router-1    | 2024/09/20 20:03:50 [notice] 1#1: start worker process 30
router-1    | 2024/09/20 20:03:50 [notice] 1#1: start worker process 31
router-1    | 2024/09/20 20:03:50 [notice] 1#1: start worker process 32
router-1    | 2024/09/20 20:03:50 [notice] 1#1: start worker process 33
router-1    | 2024/09/20 20:03:50 [notice] 1#1: start worker process 34
router-1    | 2024/09/20 20:03:50 [notice] 1#1: start worker process 35
router-1    | 2024/09/20 20:03:50 [notice] 1#1: start worker process 36
router-1    | 2024/09/20 20:03:50 [notice] 1#1: start worker process 37
router-1    | 2024/09/20 20:03:50 [notice] 1#1: start worker process 38
router-1    | 2024/09/20 20:03:50 [notice] 1#1: start worker process 39
router-1    | 2024/09/20 20:03:50 [notice] 1#1: start worker process 40
webapp_a-1  | Setting up the return response to Hello from a
webapp_b-1  | Setting up the return response to Hello from b
router-1    | 2024/09/20 20:03:50 [notice] 1#1: start worker process 41
router-1    | 2024/09/20 20:03:50 [notice] 1#1: start worker process 42
router-1    | 2024/09/20 20:03:50 [notice] 1#1: start worker process 43
webapp_a-1  | Setting up the return response to Hello from a
webapp_b-1  | Setting up the return response to Hello from b
webapp_a-1  | Performing system checks...
webapp_b-1  | Performing system checks...
webapp_a-1  |
webapp_b-1  |
webapp_b-1  | System check identified no issues (0 silenced).
webapp_a-1  | System check identified no issues (0 silenced).
webapp_b-1  | September 20, 2024 - 20:03:50
webapp_b-1  | Django version 5.1.1, using settings 'app.settings'
webapp_b-1  | Starting development server at http://0.0.0.0:8001/
webapp_b-1  | Quit the server with CONTROL-C.
webapp_b-1  |
webapp_a-1  | September 20, 2024 - 20:03:50
webapp_a-1  | Django version 5.1.1, using settings 'app.settings'
webapp_a-1  | Starting development server at http://0.0.0.0:8000/
webapp_a-1  | Quit the server with CONTROL-C.
webapp_a-1  |
```

#### Check HTTP response
On another terminal
```
$ curl localhost:1234/a
"Hello from a"

$ curl localhost:1234/b
"Hello from b"

```
