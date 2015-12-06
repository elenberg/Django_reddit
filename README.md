# Django Scaffold

Good starting point for a modern Django web application. Comes with support for a quick and easy development workflow with Docker containers! (Requires OSX) Here are the steps to get started:

**One time setup**:  
* Download [Kitematic](https://kitematic.com/), [Docker Compose](https://docs.docker.com/compose/install/) (easiest way is ```sudo pip install -U docker-compose```), and optionally [Ngrok](https://ngrok.com/) if you want to be able to expose your project with a public url for testing.
* Once those packages are installed on your Mac open Kitematic. (This will install Docker and Virtual Box and start the Docker VM. This first time it will take a while longer and ask for your password)
* Kitematic will show you some recommended containers to build from [docker hub](https://hub.docker.com/account/signup/). Click create hello-world-nginx example in the top left. Once this builds this will create a folder in your home directory: ```~/Kitematic```
* Feel free to try out the nginx server and see how docker and Kitematic work and when your ready to move on...
* ```cd``` into the Kitematic folder and clone the django-scaffold by running ```git clone https://github.com/lightningkite/django-scaffold```

**Basic development workflow**:

* Once you've completed the one time setup getting up and running is a piece of cake.
* Open Kitematic and click on the little whale in the bottom left corner of the window ![screen shot 2015-04-23 at 10 27 19 pm](https://cloud.githubusercontent.com/assets/2521298/7312459/009723bc-ea08-11e4-8f4a-73f1c5a0d9be.png) This will open up a terminal session within the context of docker so that you can run ```docker-compose``` commands.
* Next ```cd``` into the recently cloned django-scaffold folder and run: ```docker-compose up``` that will fire up your db server and the python container and run the runserver command for you. The first time you run the command there will be some more output and it will take a minute or two but after you build it once it will be almost instant to get up and running. You will see in Kitematic that your two containers (web and db) are up and running. Your shell will look something like this: ![screen shot 2015-04-23 at 8 56 48 pm](https://cloud.githubusercontent.com/assets/2521298/7311784/0b454f64-e9fe-11e4-8a36-19e9237ce5f1.png) This is your docker container that automatically runs the ```runserver``` command. You can shut down your docker container/dev environment at any time with ```ctrl + c``` in this terminal window. This one command, ```docker-compose up``` is basically the entire workflow to get up and running with the django scaffold docker dev environment! However there are a few other things you should know...
* Kitematic will show that your db server and and your web server are running. To view the home page of your django site make sure the web container is selected and click the view button at the top and that will open your browser to the containers ip:
![screen shot 2015-04-23 at 9 28 36 pm](https://cloud.githubusercontent.com/assets/2521298/7311920/44fd71e4-ea00-11e4-8190-3795aff62e1e.png)
* If you need to open up a shell in the context of the environment just click the terminal button to the right of the restart button: ![screen shot 2015-04-23 at 9 35 40 pm](https://cloud.githubusercontent.com/assets/2521298/7311961/d88f70ba-ea00-11e4-93cf-4a2c9ddac1c7.png) Within this terminal window you can run things like ```python manage.py migrate``` and any other management commands you may need.
* From here just open up your project directory in your favorite text editor and start coding!
* Last but not least if you want to expose your app publicly thats where ngrok comes in, just run ```./ngrok http [ip_of_container:port]```
