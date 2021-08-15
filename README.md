# Practical-Project

For my project I have decided to create a D&D app that generates a random character (class and race) and automatically gives the base points based on the two.

The requirements of my project, set by QA Academy are as follows:

* An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
* An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
* If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
* The project must follow the Service-oriented architecture that has been asked for.
* The project must be deployed using containerisation and an orchestration tool.
* As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
* The project must make use of a reverse proxy to make your application accessible to the user.

# Proposal
I've decided to develop a simple D&D Character Generator application which generates character's race, class and ability points. I will explain how I structured my services below:
* Service 1 is a front end application that gathers the information generated by the other services.
* Service 2 generates a character's race using the random python module from a given list.
* Service 3 generaters a character's class using the same method as the application above.
* Service 4 gathers the information given by Service 2 and 3 and generates ability points based on Service 2 and 3 using a dictionary and requests.

## Architecture
# Risk Assessment
The risk assessment below highlights the potential risks that would prevent me from completing the project. I find it extremely important to have a plan when dealing with difficult situations and luckily - none of the risks were something I've been dealing with by the end of the project. I always like to think about the technical risks as well as enviromental ones.
![](https://i.imgur.com/J3qj9yQ.png)

# Planning Board (Trello)
Can be seen here: https://trello.com/b/A7OrSxv2/project2
I've chosen Trello because it's very quick and easy to use.

# Testing
I've managed to achieve 98% coverage using pytest for unit testing and all of my tests were ran by Jenkins.
The test in Service 1 is a mock test that inputs variables that would have been generated by service 2, 3 and 4 together.
The rest tests whether correct things have been generated and the status codes of the server.

## Infrastructure

* Jenkins
I've used Jenkins to automate my deployment and therefore reduce the time it takes from development to actually deploying the application. Whenever a push is made to my Dev branch on github, Jenkins runs the whole job for me and quickly updates the page of my application using a webhook.

The Jenkins pipeline is as follows:
* Installing Dependencies.
* Tests using Pytest together with detailed logs.
* Build images using Docker-compose while handing the DockerHub credentials.
* VM configuration - Ansible - Setting up the swarm by generating the join tokens on manager VM for the worker VM, and also setting up my NGINX as the load balancer.
* Deployment using docker-compose.yaml

![](https://i.imgur.com/kPRMgqJ.png)

# Database
I've used a simple model of a single table database and described the exact structure of it in the diagram below:
![](https://i.imgur.com/Zsfy29h.png)

# Interactions
![](https://i.imgur.com/88EDeGm.png)
I've orchestrated a network of virtual machines using docker swarm that are all able to communicate with each other.
The list of virtual machiens:
* Load Balancer
* Manager
* Worker
I've also had a Jenkins VM that was communicating with my Github using a webhook and a Development VM where I've made all the pushes from therefore sending my code to Jenkins and triggering a build.

# Refactoring
I refactored my testing by using the Cobertura Plugin via Jenkins to show me my exact coverage and some extra information that speeded up making sure that the tests are effecient in all areas.

## Application
# Front-End
When navigating to the load balancer IP on port 80, your character will be generated as mentioned above.
I've used HTML and a CSS bootstrap to display the returned outcome of my applications together.

* ![](https://i.imgur.com/8SnSkZz.png)


## Future Improvements
* I would really like my application to generate factual points as per D&D book for base points of every class.
* I would also like my application to display previously generated characters.
* Improving the tests to include Integration testing.

# Acknowledgements
I would like to say thank you to the amazing Oliver Nichols and Ryan Wright for guiding me through this project as well as every single person from my class.
