Pre-requisite:
1. Install docker (https://docs.docker.com/install)
2. Install goss
# Install latest version to /usr/local/bin
curl -fsSL https://goss.rocks/install | sh
chmod +rx /usr/local/bin/goss
chmod +rx /usr/local/bin/dgoss
3. Extract simplehttpserver.zip on machine (say at /)


Part1: 
- Develop simplehttpserver
- Build and start simplehttpserver container

$ pwd
/simplehttpserver
$ ls
Dockerfile goss.yaml Readme.txt simplehttpserver.py 
$ docker build -t simplehttpserver .
$ docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
simplehttpserver    latest              9056dfea5853        8 hours ago         679MB
python              2.7                 ce24966d2075        2 days ago          679MB
hello-world         latest              e38bc07ac18e        2 weeks ago         1.85kB
$ docker run -d -p 8080:8080 simplehttpserver
$ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
9870a7b2ed3e        simplehttpserver    "python simplehttpse…"   About an hour ago   Up About an hour    0.0.0.0:8080->8080/tcp   practical_kepler





Part2: 
- Run the integration test (using goss)

$ pwd
/simplehttpserver
$ ls
Dockerfile goss.yaml Readme.txt simplehttpserver.py

// Run all test define in goss.yaml
```
$ goss validate
/hello
127.0.0.1 - - [29/Apr/2018 18:16:20] "GET /hello HTTP/1.1" 200 -
/?uppercase
127.0.0.1 - - [29/Apr/2018 18:16:20] "GET /?uppercase HTTP/1.1" 200 -
../?reversed
127.0.0.1 - - [29/Apr/2018 18:16:20] "GET /?reversed HTTP/1.1" 200 -
/hello?reversed
127.0.0.1 - - [29/Apr/2018 18:16:20] "GET /hello?reversed HTTP/1.1" 200 -
/world?reversed
127.0.0.1 - - [29/Apr/2018 18:16:20] "GET /world?reversed HTTP/1.1" 200 -
/
127.0.0.1 - - [29/Apr/2018 18:16:20] "GET / HTTP/1.1" 200 -
./world?uppercase
127.0.0.1 - - [29/Apr/2018 18:16:20] "GET /world?uppercase HTTP/1.1" 200 -
............./hello?uppercase
127.0.0.1 - - [29/Apr/2018 18:16:20] "GET /hello?uppercase HTTP/1.1" 200 -
../world
127.0.0.1 - - [29/Apr/2018 18:16:20] "GET /world HTTP/1.1" 200 -
..

Total Duration: 0.017s
Count: 20, Failed: 0, Skipped: 0

```


Part3: CI integration

// Download docker-compose
sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
// Download fly - copy to /usr/local/bin/.
https://concourse-ci.org/download.html


$ docker-compose up -d
$ fly --target testserver login --concourse-url http://127.0.0.1:8081
$ fly --target testserver execute -c httpserver_run.yml
$ fly --target testserver execute -c test_run.yml

