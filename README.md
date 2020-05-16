# CovidMailTracker

This is a simple Python CLI tool that will send you regular emails regarding the coronavirus statistics in your country. The data is provided from [worldometers.info](https://www.worldometers.info/coronavirus/). So make sure your country is listed there and have a seprate page like that of [Italy](https://www.worldometers.info/coronavirus/country/italy/). Windows Scheduler is also required to schedule the taks on a daily or weekly basis.

## How To Use

#### 1. Setup Google Mail App:

  - You need to have a working google account. If you have disabled 2 factor authentication, then head onto [this link](https://myaccount.google.com/lesssecureapps), else if you have it enable the go to [this link](https://myaccount.google.com/apppasswords).<br />
  - From the  ***Select App*** dropdown select ***Mail*** and from the ***Select device*** select ***Other**** and name it anything you would like. Click on ***Generate*** and store the password that is displayed, you will need it later. That's it for the App Setup.

#### 2. Execute the code:

  - Clone this repository
  ```
  git clone https://github.com/anubhavvs/CovidMailTracker.git
  ```
  - Download the dependencies
  ```
  cd CovidMailTracker/
  pip install -r requirements.txt
  ```
  - In the folder you will see two python files. Keep ***emailscript.py*** intact as it is. Open the ***script.py*** file and make the following changes to the code:
    * Provide the country name as the ***country*** variable.
    * Provide your google mail id as the ***SENDER*** variable.
    * Provide the mail app password that you stored in the first step as ***GOOGLE_PASS*** variable.
    * For this code, the sender and the reciever is the same, that is you. But if you want to send the mail to someone else, provide their email in the ***reciever*** variable.
    
  - Execute the script for atleast once. If it runs successfully follow the next steps.
  ```
  python script.py
  ```
#### 2. Schedule the script:

  - Open Task Scheduler in Windows Opeartion System.
  - Under ***Actions*** tab, select select ***Create Task...*** option.
  - Provide a name of your choice.
  - Under the ***Action*** Tab in the popup, create a new action.
  - Provide the full path to the ***python.exe*** on your machine in the ***Program/Script*** option. You can get this by executing the following in your CMD
    ```
    where python
    ````
  - In the ***Add arguments*** option, type the filename. Here ***script.py***.
  - In the ***Start in*** option, provide the full path to the ***script.py*** file and click OK For example: **D:\Python_Proramming\CovidMailTracker\**
  - Under the ***Triggers*** tab in the popup, create a new trigger.
  - Select the ***Daily*** radiobox if you want to get the mail on a daily basis. Also provide the time you want to run the script daily.
  - All done.
## Built With

  * [python](https://docs.python.org/3/) - Programming Language
  * [requests](https://requests.readthedocs.io/en/master/) - Requests to the website
  * [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Web Scrapping
  * [datetime](https://docs.python.org/3/library/datetime.html) - Date time manupluation

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
