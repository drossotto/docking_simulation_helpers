# Docking Simulation Helpers

Local network application for molecular docking and molecular dynamics simulations built for the Research Lab. 

The goal is to keep it super simple and maximize abstraction for our wet-lab biologists. Anything requiring significant installation receives a docker container. This adds tons of overhead, as well as having redundant packages, but we do not care. 

Services: 
- DeepGlycanSite: Carbohydrate-binding site predictions through a geometry-based graphical neural network.
  * [Paper Source](https://www.nature.com/articles/s41467-024-49516-2)
  * [GitHub](https://github.com/xichengeva/DeepGlycanSite)
