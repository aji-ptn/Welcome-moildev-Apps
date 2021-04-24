# Welcome-moildev-Apps
# **Create new application** for Moildev Plug-in

Here is the tutorial to create the application plugin that can connect to the moildev application. You have to install a Qt Designer to design the GUI (graphical user interface) if you don’t have. For windows, you can be following [this tutorial](https://build-system.fman.io/qt-designer-download). 

## 1. Open the Qt Designer app

![image](https://user-images.githubusercontent.com/58238736/115769782-7ff8a180-a3de-11eb-8e16-365d641083cc.png)

## 2. Create a new project

![image](https://user-images.githubusercontent.com/58238736/115769806-8be46380-a3de-11eb-83c4-d31bd344bfce.png)

- Select main windows

![image](https://user-images.githubusercontent.com/58238736/115769858-9bfc4300-a3de-11eb-81a1-a0f69af9e29a.png)

## 3. Start to design the GUI 

For example, I create the UI with the name test application and the design of the form can be seen in the figure below this. Object name of Home push button was “home” lower case (red color). This button has a function if we want to go back to Moildev Apps. 

![image](https://user-images.githubusercontent.com/58238736/115769891-a6b6d800-a3de-11eb-8641-2caf85fc4e6e.png)

## 4. Save the file and convert it to file .py 

- Create the folder to store our project file. 

After you save the file, then you can convert it to file .py from the terminal in PyCharm IDE or command from. The command is the same. Here I give example in terminal Pycharm IDE with the named file was “MainWindow”.

![image](https://user-images.githubusercontent.com/58238736/115769957-b7ffe480-a3de-11eb-8c00-129bbd70919c.png)

- To change the format file from the design PyQt format, you need some command in your PyCharam terminal by using this command. 

```bash
pyuic5 -x “name_program".ui -o “name_program".py
```

- “name_program” can be anything depends on what name program you made. Because I using “test_application” the command will become: 

```bash
pyuic5 -x MainWindows.ui -o MainWindows.py
```

- Then it will generate the MainWindows.py file 

![image](https://user-images.githubusercontent.com/58238736/115770007-c2ba7980-a3de-11eb-9d47-94b9d952ae6d.png)

## 5. create a python file to control the UI

This step was very important because if we want to change the UI for the future the code will affect test_application.ui and we need to convert again and the code will change also. If we made this file, our main program will not change. 

- For example, create the file controller.py 

![image](https://user-images.githubusercontent.com/58238736/115770067-cf3ed200-a3de-11eb-92bf-8527f051de97.png)

- Import MainWindows.py 

```bash
from .MainWindow import * 
```

- Made class of controller and make home button have ObjectName “home” can give even back to Moil-dev Apps (Step 3). 

```bash
from .MainWindow import * 

class Controller(QtWidgets.QMainWindow): 
    def __init__(self, parent): 
        super(Controller,self).__init__() 
        print("etste") 
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self) 
        self.old = parent 
        self.ui.home.clicked.connect(self.home) 
 
    def home(self): 
        self.old.show() 
        self.close() 
```

## 6. Create main.py file 

We need to make this application connect to Moilde_apps by made new code “main.py” and type this code: 

![image](https://user-images.githubusercontent.com/58238736/115770100-d82fa380-a3de-11eb-8933-1f2a59cf2c10.png)

- Import package and file Controller.py 

```bash
import base_plugin 
from .Controller import * from .MainWindow import * 
```

- Make the class Welcome. This word will be the name of your program. 

```bash
class Welcome(base_plugin.Plugin): 
    def __init__(self): 
        super(Welcome, self).__init__() 
        self.description = "Welcome Apps" 
 
    def perform_operation(self, argument): 
        self.w = Controller(argument) 
        self.w.show() 
```

## 7. Import welcome program to Moil-dev Apps 

- Before import the program you need to delete “venv” folder. 

![image](https://user-images.githubusercontent.com/58238736/115770140-e1b90b80-a3de-11eb-8ea4-03a452cd6c6f.png)

Note: After you delete “venv” folder, your program no have Virtual Environment but you can make it again just like make a new environment. 

## 8. Import Program to Moildev Apps

- Select "Add" button to import program 

![image](https://user-images.githubusercontent.com/58238736/115770157-e8478300-a3de-11eb-92f5-b621a0f4a443.png)

- Select file from directory

![image](https://user-images.githubusercontent.com/58238736/115770193-f2698180-a3de-11eb-88ef-8ce850de7cb7.png)

## 9. Open test application by click on Open Button 

![image](https://user-images.githubusercontent.com/58238736/115770209-fac1bc80-a3de-11eb-894d-bbd51cbef283.png)

- Select open

![image](https://user-images.githubusercontent.com/58238736/115770238-03b28e00-a3df-11eb-98de-54e9ee3f55ea.png)
