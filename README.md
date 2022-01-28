# Hello-world-app

The blog for this repository is available [here](https://deepnote.com/@tathagata-raha/hello-world-app-dH5kv5SnTgeTTBCBtf-tSQ). In order to run the code, you need to clone the repository. Clone the repository by entering the following command:

`git clone https://github.com/tathagata-raha/hello-world-app`

Instructions to run each technology are in the following sections.


## Flask

  

### Introduction
Flask is a web development framework developed in Python. It is classified as a microframework because it does not require particular tools or libraries[1]. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. It was created by Armin Ronacher of Pocoo, an international group of Python enthusiasts formed in 2004[2]. Some of the features of Flask are:

- Development server and debugger
- Integrated support for unit testing
- RESTful request dispatching
- Uses Jinja templating
- Support for secure cookies (client side sessions)
- 100% WSGI 1.0 compliant
- Unicode-based

### Application description
With Flask, I have built a simple calculator that can perform addition, subtraction, multiplication and division using port forwarding. Suppose if your application is running at `localhost:5000` , then you can go at `http://localhost:5000/addition/x/y` to get the sum of `x` and `y` where `x` and `y` are integers. I have also taken cares of error handling. For example x and y have to be integers and y cannot be 0 while performing division. More instructions can be found on the index page.

### How to run?

Follow the instructions below to run the Flask app:

 `cd flask`

`pip install -r requirements.txt` : Installs the libraries in requirements.py

`python app.py`: Starts the flask app

Your Flask app will be running at port 5000. Open `localhost:5000` to access your app.

### Comparision
Below, I have given the comparision of Flask with other contemporary Python web development frameworks:


| | | Flask | | Django | | web2py |
| -- |-- | -- | -- | -- | -- | -- |
| **Dynamic HTML** | | No | | Yes | | Yes |
| **MVC framework** | | No | | Yes | | Yes |
| **Best for**| | Simple applications | | Big projects | | Small projects |
| **Main feature** | | Very simple and lightweight | | Small projects | |Old, not used a lot |
  

### Resources
Below, I have listed some of the best resources for learning Flask:
- [Digitalocean](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3): For a very quick introduction to Flask, you can follow this Digitalocean tutorial which teaches you to build a starter application for Flask in less than 30mins.
- [Tutorialspoint](https://www.tutorialspoint.com/flask/index.htm): For a more deeper understanding of Flask, you can check out Tutorialspoint which covers most of the concepts of Flask.
- [Cheatsheet](https://s3.us-east-2.amazonaws.com/prettyprinted/flask_cheatsheet.pdf): For a quick revision of the Flask concepts, you can check the cheatsheet which lists all the important concepts. However, it is recommended that you are comfortable with the concepts of Flask.
- [Official](https://flask.palletsprojects.com/en/2.0.x/): You can checkout the official documentation of Flask. It lists all the concepts of Flask.
- [FreeCodeCamp video](https://www.youtube.com/watch?v=Qr4QMBUPxWo): If you are a fan of video tutorials and want to learn flask by building a simple application, this is a very good resource. This 6 hour tutorial teaches you all the concepts of Flask by building your own e-commerce website with its own authentication system. 


  

## ExpressJS

### Introduction

Express is a minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications[6]. It has been called the de facto standard server framework for Node.js. It was founded by TJ Holowaychuk on 22nd of May, 2010. Later, it was put under the stewardship of the Node.js Foundation incubator.[7] Some of the features of ExpressJS are as follows:
  

- Faster Server side development

-   Robust routing
- Templating
- Concentrate on high-performance

  

### Application description

Similar to the Flask application, I have built a simple calculator that can perform addition, subtraction, multiplication and division using port forwarding. Suppose if your application is running at `localhost:5000` , then you can go at `http://localhost:5000/addition/x/y` to get the sum of `x` and `y` where `x` and `y` are integers. More instructions can be found on the index page.

  

### How to run?

  

Follow the instructions below to run the Flask app:

  

`cd express-js`

  

`npm install --save express`: Install express-js in the node modules directory

  

`npm install -g nodemon`: Install nodemon globally so that it can accessed from anywhere through terminal

`nodemon index.js`: Run the index.js through nodemon server

Your Express app will be running at port 3000.

  

### Comparision

Below, I have given the comparision of Express-js with other contemporary Javascript web development frameworks:

| | | Express-js | | Node-js| | Angular.js |
| -- |-- | -- | -- | -- | -- | -- |
| **Backend or frontend?** | |  backend  | | both backend and frontend | | backend |
| **What is it?** | | framework for node-js | | developed on Google's V8 Javascript engine | | web app dev framework developed by google |
| **Built using**| | Javascript	 | | Javscript, C, C++ | | Javascript |
| **Used for** | | small project| | small projects | |highly interactive web projects |

  

### Resources

Below, I have listed some of the best resources for learning Express:

- [Digitalocean](https://www.digitalocean.com/community/tutorials/nodejs-express-basics): For a very quick introduction to Express-js and Node, you can follow this Digitalocean tutorial which teaches you to build a starter application for Flask in less than 30mins. It can be a nice starting guide for beginners.

- [Tutorialspoint](https://www.tutorialspoint.com/expressjs/index.htm): For a more deeper understanding of Express, you can check out Tutorialspoint which covers most of the concepts of Express.

- [Cheatsheet](https://devhints.io/express): For a quick revision of the Express concepts, you can check the cheatsheet which lists all the important concepts. However, it is recommended that you are comfortable with the concepts of Express.

- [Official](https://expressjs.com/): You can checkout the official documentation of Express. It lists all the concepts of Express.

- [FreeCodeCamp video](https://www.youtube.com/watch?v=Oe421EPjeBE): If you are a fan of video tutorials and want to learn Node and Express by building a simple application, this is a very good resource. This 8 hour tutorial teaches you all the concepts of Express by building a simple MERN application.


## MongoDB

  

### Introduction
MongoDB is an open-source document database and leading NoSQL database. It is classified as a NoSQL database because it uses JSON-like documents with optional schemas. 10gen software company began developing MongoDB in 2007 as a component of a planned platform as a service product. In 2009, the company shifted to an open-source development model, with the company offering commercial support and other services. In 2013, 10gen changed its name to MongoDB Inc.[3] Some of the features of MongoDB are as follows:

 - Ad-hoc queries for optimized, real-time analytics
 - Indexing appropriately for better query executions
 - Replication for better data availability and stability
 - Sharding
 - Load balancing

### Application description
With the help of pymongo library, I have built a simple Python application that inserts and queries a MongoDB database. The MongoDB database is hosted at MongoDB Atlas which is online cloud database service built that hosts MongoDB databases and allows us to access MongoDB without the need of any installation. pymongo is a wrapper that allowes us to connect and perform queries to a MongoDB dataset from Python. Our application contains two scripts:
- `insert.py`: This scripts inserts into a MongoDB dataset from a json file.
- `query.py`: This script performs different queries to the MongoDB database.

### How to run?

Follow the instructions below to run the MongoDB app:

 `cd mongo-db`
 
`pip install -r requirements.txt` : Install the libraries in `requirements.txt`

`python insert.py`: Inserts into MongoDB database

`python query.py`: Queries from MongoDB database

### Comparision
Below, I have given the comparision of MongoDB with other contemporary database systems:
| | | MongoDB | | Cassandra| | MySQL |
| -- |-- | -- | -- | -- | -- | -- |
| **Description** | |  One of the most popular document stores available both as a fully managed cloud service and for deployment on self-managed infrastructure  | | Wide-column store based on ideas of BigTable and DynamoDB | | Widely used open source RDBMS |
| **Primary database model** | | Document store | | Wide column store | | Relational DBMS |
| **Developer**| | MongoDB, Inc	 | | Apache Software Foundation | | Oracle |
| **Implementation language** | | C++| | Java | |C and C++ |
| **Data scheme** | | No | | No | |Yes |
| **Foreign keys** | | No | | No | |Yes |
| **Advantages** | | High Availability, High Fault Tolerance | | Flexible document schemas,Change-friendly design, Powerful querying and analytics  | |On-Demand Scalability, Round-the-clock Uptime |			
  

### Resources
Below, I have listed some of the best resources for learning MongoDB:
- [Studio3t](https://studio3t.com/knowledge-base/articles/mongodb-getting-started/): This article provides a gentle introduction to MongoDB and NoSQL databases. It can be considered as a good starting point for the beginners.
- [Tutorialspoint](https://www.tutorialspoint.com/mongodb/index.htm): For a more deeper understanding of MongoDB, you can check out Tutorialspoint which covers most of the concepts of MongoDB.
- [Cheatsheet](https://www.mongodb.com/developer/quickstart/cheat-sheet/): For a quick refresher of the MongoDB concepts, you can check the cheatsheet which lists all the important concepts. However, it is recommended that you are comfortable with the concepts of MongoDB.
- [Official](https://docs.mongodb.com/): You can checkout the official documentation of MongoDB. It lists all the concepts of MongoDB.
- [FreeCodeCamp video](https://www.youtube.com/watch?v=4yqu8YF29cU): If you are a fan of video tutorials and want to learn MongoDB by building a simple application, this is a very good resource. This 1.2 hour tutorial teaches you the concepts of MongoDB and Mongoose by building a simple Node application.


## Docker
  

### Introduction
Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels. It enables developers to easily pack, ship, and run any application as a lightweight, portable, self-sufficient container, which can run virtually anywhere. The Docker software as a service offering consists of three components:
- **Software**: The Docker daemon, called dockerd, is a persistent process that manages Docker containers and handles container objects. The daemon listens for requests sent via the Docker Engine API. The Docker client program, called docker, provides a command-line interface (CLI), that allows users to interact with Docker daemons.
- **Objects:** Docker objects are various entities used to assemble an application in Docker. The main classes of Docker objects are images, containers, and services.
- **Registries:** A Docker registry is a repository for Docker images. Docker clients connect to registries to download ("pull") images for use or upload ("push") images that they have built. Registries can be public or private. Two main public registries are Docker Hub and Docker Cloud.
Docker Inc. was founded by Kamel Founadi, Solomon Hykes, and Sebastien Pahl[4] during the Y Combinator Summer 2010 startup incubator group and launched in 2011. Hykes started the Docker project in France as an internal project within dotCloud, a platform-as-a-service company. It was released as open-source in 2013.[5]

Some of the major features of Docker are as follows:

-   Faster and easier configuration.
-   Application isolation.
-   Rapid scaling of Systems.
-   Swarm.
-   Increase in productivity.

### Application description
For the assignment, I have built a simple Docker container that bundles the Flask calculator app that we have previously built. On building the container, it installs all the requirements and creates an image. On running it, it starts running the application at the default port or a desired port passed as argument.

### How to run?

Before running the docker application, make sure docker is installed. You can check if Docker is installed by entering `docker --version` in terminal. It shows the version of Docker that is installed. If Docker is not installed, follow the instructions [here](https://docs.docker.com/engine/install/) to install Docker.

Follow the instructions below to run the Docker app:

 `cd docker`
 
`docker build . -t flask-app` : Build the Docker image with the name 'flask-app'

`docker run -p 5000:5000 flask-app`: Run the Docker image. map port 5000 of the host to port 5000 in the container

Open `localhost:5000` in your browser

### Comparision
Below, I have given the comparision of Docker with Kubernates:

| | | Docker | | Kubernates |
| -- |-- | -- | -- | -- |
| **Description** | |  open-source lightweight containerization technology  | | open-source container management software  | 
| **Developer**| | Docker Inc.	 | | Google |
| **Implementation language** | | Go | | Go |
| **Auto-scaling** | | No | | Yes |
| **Number of nodes** | | supports up to 2000 nodes | | supports upto 5000 nodes | |
| **Customization** | | more comprehensive and highly customizable | | less extensive and customizable  |  |
| **Fault tolerance** | | high fault tolerance | | low fault tolerance  |  |
| **Advantages** | | Offers an efficient and easier initial set up, Ensures that application is isolated | | Easy organization of service with pods, Adheres to the principals of immutable infrastructure  |  |



  

### Resources
Below, I have listed some of the best resources for learning Docker:
- [DigtalOcean](https://www.digitalocean.com/community/tutorials/getting-started-with-docker): This article provides a gentle introduction to Docker and containers. It can be considered as a good starting point for the beginners.
- [Tutorialspoint](https://www.tutorialspoint.com/docker/index.htm): For a more deeper understanding of Docker, you can check out Tutorialspoint which covers most of the concepts of Docker.
- [Cheatsheet](https://www.docker.com/sites/default/files/d8/2019-09/docker-cheat-sheet.pdf): For a quick refresher of the Docker concepts, you can check the official cheatsheet which lists all the important concepts. However, it is recommended that you are comfortable with the concepts of Docker.
- [Official](https://docs.docker.com/): You can checkout the official documentation of Docker. It lists all the concepts of Docker.
- [FreeCodeCamp video](https://www.youtube.com/watch?v=fqMOX6JJhGo): If you are a fan of video tutorials and want to learn Docker through a series of lectures that use animation, illustration and some fun analogies that simplifies complex concepts, this is a very good resource. This 2 hour tutorial teaches you the concepts of Docker and containers through demos and hands-on-lab that one can access right in the browser.


## scikit-learn
  

### Introduction
Scikit-learn is a free software machine learning library for the Python programming language. It features various classification, regression and clustering algorithms including support-vector machines, random forests, gradient boosting, k-means and DBSCAN, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy. Scikit-learn is a NumFOCUS fiscally sponsored project. The scikit-learn project started as scikits.learn, a Google Summer of Code project by French data scientist David Cournapeau and the first public release was made on February the 1st 2010.[8] Some of the major featuresof scikit-learn are as follows:
- **Datasets**: Scikit-learn contains several inbuilt datasets which are easy to understand and you can directly implement ML models on them. These datasets are good for beginners.
- **Models**: Contains different supervised and unsupervised models like Linear Regression, Logistic Regression, Decision Trees, Random Forests, Ada Boost and support vector machines. 
- **Metrics**: After building a model, it is possible to analyze the predictions of the algorithms with different metrics like classification, accuracy, f1 score, MSE, etc.

### Application description
For the assignment, I have considered a dataset that contains real and fake news about COVID-19. This dataset was published at the CONSTRAINT-2020 shared task(co-located with AAAI) where the aim was classify better fake and real news.[9] We have used scikit-learn library to extract tf-idf features from the news text and build different classification models using naive-bayes, logistic regression, random forests, xgboost and support vector machines.

### How to run?

Before running the application, make sure Jupyter is installed. The python code is written in the jupyter notebook. You can check if Jupyter is installed by entering `jupyter --version` in terminal. It shows the version of Jupyter that is installed. If Jupyter is not installed, follow the instructions [here](https://jupyter.org/install) to install Jupyter.

Follow the instructions below to run the Docker app:

 `cd scikit-learn`
 
`pip install -r requirements.txt` : Build the Docker image with the name 'flask-app'

Open the `covidBaseLinesModel.ipynb`in Jupyter and run through the cells to run the models

### Comparision
Below, I have given the comparision of scikit-learn with other contemporary Python data science frameworks:

| | | scikit-learn | | pytorch | | tensorflow |
| -- |-- | -- | -- | -- | -- | -- |
| **Description** | |  open-source package for creating and evaluating machine learning models of all flavors  | | open-source framework with a primary focus on neural networks  | | open-source framework with a primary focus on neural networks |
| **Developer**| | Numfocus	 | | Facebook | | Google |
| **Implementation language** | | Python, ‎Cython‎, ‎C‎ and ‎C++ | | Python; ‎C++‎; ‎CUDA | | C++ and CUDA |
| **GPU access** | | No | | Yes | |Yes |
| **TPU access** | | No | | Partial | |Yes |
| **Used for** | | building simple machine learning models including Support Vector Machines, Random Forests, K-means clustering | | building neural networks with a special focus on research purposes  | |building neural networks with a special focus on deploying and production |		
  

### Resources
Below, I have listed some of the best resources for learning scikit-learn:
- [Paperspace](https://blog.paperspace.com/getting-started-with-scikit-learn/): This article provides a gentle introduction to scikit-learn and containers. It can be considered as a good starting point for the beginners. This blog teaches to build a simple classfication model on the iris dataset.
- [Tutorialspoint](https://www.tutorialspoint.com/scikit_learn/index.htm): For a more deeper understanding of scikit-learn, you can check out Tutorialspoint which covers most of the concepts of scikit-learn.
- [Cheatsheet](https://www.datacamp.com/community/blog/scikit-learn-cheat-sheet): For a quick refresher of the scikit-learn concepts, you can check the official cheatsheet which lists all the important concepts. However, it is recommended that you are comfortable with the concepts of scikit-learn.
- [Official](https://scikit-learn.org/stable/): You can checkout the official documentation of scikit-learn. It lists all the concepts of scikit-learn.
- [FreeCodeCamp video](https://www.youtube.com/watch?v=pqNCD_5r0IU): If you are a fan of video tutorials and want to learn scikit-learn through a series of lectures that use animation, illustration and some fun analogies that simplifies complex concepts, this is a very good resource. This 3 hour tutorial teaches you the concepts of scikit-learn through demos and hands-on-lab.

## References 
[1]

Flask, “Foreword — Flask Documentation (0.10),” _web.archive.org_, Nov. 17, 2017. https://web.archive.org/web/20171117015927/http://flask.pocoo.org/docs/0.10/foreword (accessed Jan. 28, 2022).

[2]

“Pocoo Team — Pocoo,” _web.archive.org_, Mar. 15, 2018. https://web.archive.org/web/20180315200205/http://www.pocoo.org/team/ (accessed Jan. 28, 2022).

[3]

D. Harris, “10gen embraces what it created, becomes MongoDB Inc.,” _Gigaom_, Aug. 27, 2013. http://gigaom.com/2013/08/27/10gen-embraces-what-it-created-becomes-mongodb-inc/ (accessed Jan. 28, 2022).

[4]

Docker, “Au revoir,” _Docker Blog_, Mar. 28, 2018. https://www.docker.com/blog/au-revoir/ (accessed Jan. 28, 2022).

[5]

A. Avram, “Docker: Automated and Consistent Software Deployments,” _InfoQ_, Mar. 27, 2013. http://www.infoq.com/news/2013/03/Docker.

[6]

OpenJS Foundation, “Express - Node.js web application framework,” _Expressjs.com_, 2017. https://expressjs.com/.

[7]

P. Krill, “Node.js Foundation to shepherd Express Web framework,” _InfoWorld_, Feb. 10, 2016. http://www.infoworld.com/article/3031686/javascript/nodejs-foundation-to-shepherd-express-web-framework.html (accessed Jan. 28, 2022).

[8]

D. Cournapeau, “About us — scikit-learn 0.23.2 documentation,” _scikit-learn.org_, Feb. 01, 2010. https://scikit-learn.org/stable/about.html#history.

[9]

P. Patwa _et al._, “Fighting an Infodemic: COVID-19 Fake News Dataset,” _arXiv:2011.03327 [cs]_, vol. 1402, pp. 21–29, 2021, doi: 10.1007/978-3-030-73696-5_3.