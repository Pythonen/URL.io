# URL.io
URL-shortener made with [Flask](https://flask.palletsprojects.com/en/1.1.x/)🤩

This is just a **_proof-of-concept_**. Since I don't own any short domain, it doesn't quite shorten the URL.

If you have any ideas about how to improve it [Fork project](https://github.com/Pythonen/URL.io/fork) and send me a pull request.



How to get it working locally
======


To get started clone this repository
```
$ mkdir Project
$ cd Project
$ git clone https://github.com/Pythonen/URL.io.git
```

I suggest you to make virtual environment to install all dependencies as if you have your own projects with same dependencies but different versions,
it might break them.

Once thats done, in the project root type:
```
pip3 install -r requirements.txt
```

After that head to [MongoDB](https://www.mongodb.com) and make your own database. Once that is done, copy the MONGO_URI and paste it to .env file as shown in example.

Now you should be good to go! In terminal type 
```
python3 app.py
```
Open http://127.0.0.1:5000/, customize project files and have fun.

Requirements
-----------
You need to have Python **3.6** or above


