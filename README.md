# Docking Simulation Helpers

Local network application for molecular docking and molecular dynamics simulations built for the Research Lab. 

The goal is to keep it super simple and maximize abstraction for our wet-lab biologists. Anything requiring significant installation receives a docker container. This adds tons of overhead, as well as having redundant packages, but we do not care. 

Requirements: 
  - pipx: A tool to install and run Python applications in isolated environments.
  - docker: Enables containerization, allowing applications to run consistently across environments. 

Services: 
- DeepGlycanSite: Carbohydrate-binding site predictions through a geometry-based graphical neural network.
  * [Research Article](https://www.nature.com/articles/s41467-024-49516-2)
  * [GitHub](https://github.com/xichengeva/DeepGlycanSite)


Notes: 

- In the repository, there is a docker-compose.yml that ships with the python package that establishes the services to be included in the application. That is how we can ship a large amount of application in a one-step python package. 