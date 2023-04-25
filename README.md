# Final project - IT Factory - Python Course
### Project name: Planets-fact-site
###

- Step 1 - 
Install [Google Chrome](https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwiZpqDwjsX-AhWngFAGHSVwBVQYABAAGgJkZw&ohost=www.google.com&cid=CAESauD20c82cYwEF5faNLs1iPVZ02CcZob1yckwyCQ1CLZiKtYYSy5O5Q0bwcP85HMSC3BuOTmK3XPGAnHcvH2ykzFJGACu-FFvZjhrzJnZypgUCCzD_eAy_VdwfaIrHUck9YQOfegpYD2c8Yg&sig=AOD64_3hl9ERHq5kI30h4gtxs2cKNUFE6w&q&adurl&ved=2ahUKEwjRjZfwjsX-AhWOg_0HHWw-BPcQ0Qx6BAgHEAE)
###


- Step 2 - 
Install python 3
###

- Step 3 - 
Install PyCharm Community Edition\
(https://www.jetbrains.com/pycharm/download/#section=windows)<br/>
- I used: PyCharm 2021.3.2 (Community Edition)

###

- Step 4 - 
Install Git\
(https://git-scm.com/downloads)<br/>
###

- Step 5 - Create a new folder and GitBash into it\
  Right-click in a local folder where you want to clone the project
  and click on **GitBash Here**:<br><br>
  ![gitbash here](https://i.stack.imgur.com/7BI04.png)<br><br>
  Then in your terminal run the following commands:\
  `git clone https://github.com/SimaElisabeta/Planets-fact-site.git` <br><br>
###

- Step 6 - Once you've cloned the repository, open Pycharm<br>
  Click File -> Open... , navigate to the folder where you cloned the project, press **OK**
  and click **Trust Project**.
###

- Step 7 - Create a virtual environment\
In PyCharm navigate to File->Settings...->Project->Python Interpreter\
Click on Add Interpreter-> Add Local Interpreter and click **OK**.
###

- Step 8 - Navigate into the project in PyCharm terminal\
Go to Terminal(bottom side), click on the down arrow and click on `Command Prompt`\
Change the directory to plantes_fact_site app <br>
`cd plantes_fact_site`
###

- Step 9 - Install the following project's packages\
Instal Django package - `pip install django`<br>
Instal Pillow package - `pip install Pillow`
###

- Step 10 - The comparison page uses public REST API call. <br>
You must create an account at https://api-ninjas.com/register  <br>
After registration you can find your API key by going to https://api-ninjas.com/profile and clicking on `Show API Key` <br>
Copy the key and replace the contents of `plantes_fact_site/static/secrets/api_key.txt` with this key
###

- Step 11 - Run the project\
If there are no hitches here you should now be able to open the server by running:\
`cd plantes_fact_site` <br>
`python manage.py runserver`
###

- Step 12 - Open the localhost link (http://127.0.0.1:8000/) and enjoy!
