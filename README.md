# Demo
![image](https://github.com/xianyuntang/snapnews/blob/master/demo/1568101923597.jpg)
![image](https://github.com/xianyuntang/snapnews/blob/master/demo/1567759244991.jpg)

# Download

````
$ docker pull xt1800i/snapnews-web
````

# Deploying Steps 

### Step 1: install docker
Please refer to  [this link](https://www.linode.com/docs/applications/containers/install-docker-ce-ubuntu-1804/)

### Step 2: pull docker image
````
$ docker pull xt1800i/snapnews-web
````

### Step 3: run docker container
*make sure docker volume is mounted*
````
$ docker run -itd -p 80:80 -v /media/storage/images:/media/storage/images --restart=always  xt1800i/snapnews
````

## If you want to create a new database 

### Step 1: open docker bash 
````
$ docker exec -it 'your docker container name' bash
````

### Step 2: edit /app/SnapNewsWeb/settings.py to your database*
Only mysql was recommended. **DO NOT USE OTHER DATABASE** 
````
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'host',
        'PORT': 'port'
    }
}
````
### Step 3: migrate database 
````
# python3 manager.py makemigrations
# python3 manager.py migrate
````
### Step 4: restart container 
````
$ docker restart 'your docker container name'
````
## note
1. make sure the image directory '/media/storage/images' exists 

