# TP Multithreading
## Introduction
Developed in Python, this framework is designed for the efficient execution of distributed tasks using parallel processing. It features a Master-Slave architecture, where the Master delegates tasks and the Slave nodes execute them. Leveraging Python's multiprocessing library, it facilitates simultaneous processing of tasks, offering an intuitive approach to managing workload distribution across multiple processors. This repository contains the code for the SRI UPSSITECH 3rd year (M2 equivalent) course on multithreading. The course and TP statements are available on the following GitHub: https://gitlab.laas.fr/gsaurel/teach/-/tree/main/2023-2024/3A_SRI?ref_type=heads

## Main Features
Master-Slave Structure: Optimized for distributing tasks in a parallel computing environment.
Parallel Processing: Employs Python's multiprocessing features for simultaneous task processing.
Task Handling: Includes classes for task assignment, result aggregation, and inter-node communication.
Sample Code: Comes with sample code for Master, Slave, and Task classes.

## License 
This software is supplied under the MIT license.

## Installation guide
### Requirements
Python 3
### Installation
To install, you need to run the venv_install.sh script in the directory where the project is located, with the line :
``./setup/venv_install.sh``
### Uninstall
To uninstall the project, you need to run the venv_uninstall.sh script from the project directory with the following line of code:
``./setup/venv_uninstall.sh``

