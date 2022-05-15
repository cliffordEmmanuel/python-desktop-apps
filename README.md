# Motivation

Improve my python scripts skills by learning about creating desktop apps with PyQt.
I'll be updating as I learn newer techniques.

### 1. Setup:

In order to get started I needed to install a GUI library, and I went with PyQT well for no particular reason.

- I created a new virtual environment: `conda create -n desktop-app python==3.8`
- Then installed the pyqt5 package: `pip3 install pyqt5`
- Then installed the pyqt5-tools to get the QT designer: `pip3 install pyqt5-tools`

_Quick side note I run into some dependency error issues using the latest python version with installing the pyqt5 packages, consider using a lower python version say 3.8_

### 2. The QT designer:

I think I should state that I'm using linux, so the setup is a bit different. Anyways to launch the Qt designer you need to do some digging inside where your virtual environment was installed, 
So in my case: `~/envs/desktop-app/lib/python3.8/site-packages/qt5_applications/Qt/bin/designer`



### Sources:

- Setup and basic GUI app: [TechWithTim](https://www.youtube.com/watch?v=Vde5SH8e1OQ&ab_channel=TechWithTim)
- Installing guide (linux and windows): [Real Python](https://realpython.com/qt-designer-python/#:~:text=Installing%20and%20Running%20Qt%20Designer,-There%20are%20several&text=pyqt5%20installs%20PyQt%20and%20a,lib%2Fpython3.)