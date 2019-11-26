
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](http://opensource.org/licenses/MIT)   
#### Author
> Machel Nyanumba.

## Description
Awwards is an application that allows users to post projects that they have created and get it reviewed by their peers.

A project can be rated based on 3 different criteria

* Design
* Usability
* Content
## Setup Instructions:
### Requirements
##### 1. Clone the repository
Clone the the repository by running 

   ```bash
   git clone https://github.com/Machel54/Awards.git
   ```
 or download a zip file of the project from github
 

Navigate to the project directory
```bash
cd Awwards
```

##### 2. Create a virtual environment
 Install `Virtualenv` 

   ```prettier
   pip install virtualenv
   ```

To create a virtual environment named `virtual`, run

   ```prettier
   virtualenv virtual
   ```
To activate the virtual environment we just created, run

   ```bash
   source virtual/bin/activate
   ```

##### 3. Create a database
You'll need to create a new postgress database, Type the following command to access postgress
   ```bash
    $ psql
   ```
   Then run the following query to create a new database named ```Awards``` 
   ```prettier
   # create database Awards
   ```


#####  4.Install dependencies
To install the requirements from `requirements.txt` file,

   ```prettier
   pip install -r requirements.txt
   ```

#####  5.Create Database migrations
Making migrations on postgres using django

```prettier
python3 manage.py makemigrations awards
```

 
then run the command below;

 ```bash
 python3 manage.py migrate
 ```

##### 6.Run the app
To run the application on your development machine, 

    python3 manage.py runserver

### Running Tests
>To run tests;

    python3 manage.py test

## Technologies Used
* Django
* Python
* Html
* Css
* Javascript
* Bootstrap


## User stories
>As a user of the application I should be able to:

- [X] View posted projects and their details
- [X] Post a project to be rated/reviewed
- [X] Rate/ review other users' projects
- [X] Search for projects 
- [X] View projects overall score
- [X] View my profile page


## Bugs
There are no know bugs at the moment

## License
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](http://opensource.org/licenses/MIT)
>MIT license &copy;  2019 Machel
 
## Collaboration Information
* Clone the repository
* Make changes and write tests
* Push changes to github
* Create a pull request

## Contacts
Reach me on:
>Email:  machelnyanumba14@gmail.com