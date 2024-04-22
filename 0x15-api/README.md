# 0x15. API

## Python

## Scripting

## Back-end

## API

## Background Context

- Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.

- One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.

- This is a perfect example of a task that is not suited for Bash scripting, so let’s build Python scripts.

## Resources

- Read or watch:

	- [Friends don’t let friends program in shell script](#friends-don't-let-friends-program-in-shell-script)
	- [What is an API](#what-is-an-API)
	- [What is an API? In English, please](#what-is-an-api?-in-english-,-please)
	- [What is a REST API](#what-is-a-rest-api)
	- [What are microservices](#what-are-microservices)
	- [PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry](#pep8-python-style-having-a-clean-code-respecting-style-guide-is-really-appreciated-in-the-industry)

## Requirements

## General

	- Allowed editors: vi, vim, emacs
	- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
	- All your files should end with a new line
	- The first line of all your files should be exactly #!/usr/bin/python3
	- Libraries imported in your Python files must be organized in alphabetical order
	- A README.md file, at the root of the folder of the project, is mandatory
	- Your code should use the pycodestyle (version 2.8.*)
	- All your files must be executable
	- The length of your files will be tested using wc
	- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
	- You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
	- Your code should not be executed when imported (by using if __name__ == "__main__":)

## Tasks

## 0. Gather data from an API
mandatory
Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.

Requirements:

- You must use urllib or requests module
- The script must accept an integer as a parameter, which is the employee ID
- The script must display on the standard output the employee TODO list progress in this exact format:
First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
	- EMPLOYEE_NAME: name of the employee
	- NUMBER_OF_DONE_TASKS: number of completed tasks
	- TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
	- Second and N next lines display the title of completed tasks: TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
Example:

sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 2

Employee Ervin Howell is done with tasks(8/20):

     distinctio vitae autem nihil ut molestias quo

     voluptas quo tenetur perspiciatis explicabo natus

     aliquam aut quasi

     veritatis pariatur delectus

     nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis

     repellendus veritatis molestias dicta incidunt

     excepturi deleniti adipisci voluptatem et neque optio illum ad

     totam atque quo nesciunt
sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 4

Employee Patricia Lebsack is done with tasks(6/20):

     odit optio omnis qui sunt

     doloremque aut dolores quidem fuga qui nulla

     sint amet quia totam corporis qui exercitationem commodi

     sequi dolorem sed

     eum ipsa maxime ut

     tempore molestias dolores rerum sequi voluptates ipsum consequatur

sylvain@ubuntu$

sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 4 | tr " " "S" | tr "\t" "T" 

EmployeeSPatriciaSLebsackSisSdoneSwithStasks(6/20):

TSoditSoptioSomnisSquiSsunt

TSdoloremqueSautSdoloresSquidemSfugaSquiSnulla

TSsintSametSquiaStotamScorporisSquiSexercitationemScommodi

TSsequiSdoloremSsed

TSeumSipsaSmaximeSut

TStemporeSmolestiasSdoloresSrerumSsequiSvoluptatesSipsumSconsequatur

sylvain@ubuntu$

Repo:

	- GitHub repository: alx-system_engineering-devops
	- Directory: 0x15-api
	- File: 0-gather_data_from_an_API.py

## 1. Export to CSV

mandatory

Using what you did in the task #0, extend your Python script to export data in the CSV format.

Requirements:

- Records all tasks that are owned by this employee
- Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name must be: USER_ID.csv

Example:

sylvain@ubuntu$ python3 1-export_to_CSV.py 2

sylvain@ubuntu$ cat 2.csv

"2","Antonette","False","suscipit repellat esse quibusdam voluptatem incidunt"

"2","Antonette","True","distinctio vitae autem nihil ut molestias quo"

"2","Antonette","False","et itaque necessitatibus maxime molestiae qui quas velit"

"2","Antonette","False","adipisci non ad dicta qui amet quaerat doloribus ea"

"2","Antonette","True","voluptas quo tenetur perspiciatis explicabo natus"

"2","Antonette","True","aliquam aut quasi"

"2","Antonette","True","veritatis pariatur delectus"

"2","Antonette","False","nesciunt totam sit blanditiis sit"

"2","Antonette","False","laborum aut in quam"

"2","Antonette","True","nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis"

"2","Antonette","False","repudiandae totam in est sint facere fuga"

"2","Antonette","False","earum doloribus ea doloremque quis"

"2","Antonette","False","sint sit aut vero"

"2","Antonette","False","porro aut necessitatibus eaque distinctio"

"2","Antonette","True","repellendus veritatis molestias dicta incidunt"

"2","Antonette","True","excepturi deleniti adipisci voluptatem et neque optio illum ad"

"2","Antonette","False","sunt cum tempora"

"2","Antonette","False","totam quia non"

"2","Antonette","False","doloremque quibusdam asperiores libero corrupti illum qui omnis"

"2","Antonette","True","totam atque quo nesciunt"

sylvain@ubuntu$

Repo:

	- GitHub repository: alx-system_engineering-devops
	- Directory: 0x15-api
	- File: 1-export_to_CSV.py

## 2. Export to JSON

mandatory

Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

- Records all tasks that are owned by this employee
- Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
- File name must be: USER_ID.json

Example:

sylvain@ubuntu$ python3 2-export_to_JSON.py 2
sylvain@ubuntu$ cat 2.json
{"2": [{"task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": false, "username": "Antonette"}, {"task": "distinctio vitae autem nihil ut molestias quo", "completed": true, "username": "Antonette"}, {"task": "et itaque necessitatibus maxime molestiae qui quas velit", "completed": false, "username": "Antonette"}, {"task": "adipisci non ad dicta qui amet quaerat doloribus ea", "completed": false, "username": "Antonette"}, {"task": "voluptas quo tenetur perspiciatis explicabo natus", "completed": true, "username": "Antonette"}, {"task": "aliquam aut quasi", "completed": true, "username": "Antonette"}, {"task": "veritatis pariatur delectus", "completed": true, "username": "Antonette"}, {"task": "nesciunt totam sit blanditiis sit", "completed": false, "username": "Antonette"}, {"task": "laborum aut in quam", "completed": false, "username": "Antonette"}, {"task": "nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis", "completed": true, "username": "Antonette"}, {"task": "repudiandae totam in est sint facere fuga", "completed": false, "username": "Antonette"}, {"task": "earum doloribus ea doloremque quis", "completed": false, "username": "Antonette"}, {"task": "sint sit aut vero", "completed": false, "username": "Antonette"}, {"task": "porro aut necessitatibus eaque distinctio", "completed": false, "username": "Antonette"}, {"task": "repellendus veritatis molestias dicta incidunt", "completed": true, "username": "Antonette"}, {"task": "excepturi deleniti adipisci voluptatem et neque optio illum ad", "completed": true, "username": "Antonette"}, {"task": "sunt cum tempora", "completed": false, "username": "Antonette"}, {"task": "totam quia non", "completed": false, "username": "Antonette"}, {"task": "doloremque quibusdam asperiores libero corrupti illum qui omnis", "completed": false, "username": "Antonette"}, {"task": "totam atque quo nesciunt", "completed": true, "username": "Antonette"}]}sylvain@ubuntu$

Repo:

	- GitHub repository: alx-system_engineering-devops
	- Directory: 0x15-api
	- File: 2-export_to_JSON.py

## 3. Dictionary of list of dictionaries

mandatory

Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

- Records all tasks from all employees
- Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
- File name must be: todo_all_employees.json

