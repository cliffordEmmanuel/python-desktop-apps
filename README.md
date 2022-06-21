# Motivation

Improve my python scripts skills by learning about creating desktop apps with PyQt.
I'll be updating as I learn newer techniques.

## 1. Setup

In order to get started I needed to install a GUI library, and I went with PyQT, for no particular reason.

- I created a new virtual environment: `conda create -n desktop-app python==3.8`
- Then installed the pyqt5 package: `pip3 install pyqt5`
- Then installed the pyqt5-tools to get the QT designer: `pip3 install pyqt5-tools`

_Quick side note I run into some dependency error issues using the latest python version with installing the pyqt5 packages, consider using a lower python version say 3.8 ._

### 2. The QT designer

I think I should state that I'm using linux, so the setup is a bit different. Anyways to launch the Qt designer you need to do some digging inside where your virtual environment was installed,
So in my case: `~/envs/desktop-app/lib/python3.8/site-packages/qt5_applications/Qt/bin/designer`

The drag and drop tool is really cool to use. After a quick design you can save the file in any location you want. The file is saved with a .ui extension.

Which brings us to the awesome part: creating a python version of the design so you can edit as you see fit.

type this code snippet via the terminal: `pyuic5 -x <name of file>.ui -o <name of file>.py`
_this assumes the terminal is pointing to the exact location of the file otherwise provide the paths as needed._

## Learning insights

It seems as if PyQt can be understood as 2 major parts:

1. Placing elements within a window and defining their attributes
2. Attaching actions that are triggered when the elements are interacted with.

In order words, I create sources of signals ie elements, and then i define what should happen when a signal is triggered or an event occurs, ie functions that handle the events.

On one hand, I cannot know all the elements and their attributes but I can focus on learning these patterns:

1. How to setup the basic window, including the most basic characteristics
2. How to create an element
3. How to define a events for the element
4. How to create functions that responds to an event on the element.

## Making a linux python installer for the PyQt app

[Pyinstaller](https://pyinstaller.org/en/stable/) is according to the docs the library used to bundle a Python application and its dependencies into a single package.

The following steps outlines how to make a linux installer out of the pyqt application:

- Step 1: install PyInstaller
  `pip3 install PyInstaller preferably into a virtual environment`
- Step 2: building the app
  `pyinstaller app.py`
  - make sure you navigate to the folder where the application exists.
  The result of this is you'll have 2 folders created: **dist** and **build**.

  - The _build_ folder is used by pyinstaller to collect and prepare the files for bundling. You can  largely ignore this unless you're trying to debug)

  - The _dist_ folder contains the files to be distributed, includes your application bundled as an executable file, together with the libraries and binary .so files.
  
  - Also created is a **.spec** file.
  This spec file contains the build configuration and instructions used by PyInstaller to package the application. It is generated the first time pyinstaller command is ran for the application script.
  
- Step: Tweaking your build:

  To rebuild your application you only need to pass the corresponding .spec file to the pysintaller command: `pyinstaller app.spec`

## Sources

- Setup and basic GUI app: [TechWithTim](https://www.youtube.com/watch?v=Vde5SH8e1OQ&ab_channel=TechWithTim)
- Text-based Tutorials on building a PyQt app: [TechWithTim](https://www.techwithtim.net/tutorials/pyqt5-tutorial/basic-gui-application/)
- Installing guide (linux and windows): [Real Python](https://realpython.com/qt-designer-python/#:~:text=Installing%20and%20Running%20Qt%20Designer,-There%20are%20several&text=pyqt5%20installs%20PyQt%20and%20a,lib%2Fpython3.)
