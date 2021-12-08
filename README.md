# BART (BAR-darT)
Record and display dart scores

![Logo](art/bart.png)

## Build instruction
Create a virtual environnement :

    `python3 -m venv env`
    `source env/bin/activate` or `env\Scripts\activate.bat`

Pip install the following libs :

- wxPython
- pytest
    
### Linux ###

For linux, it is possible to install a specific version from: https://extras.wxpython.org/wxPython4/extras/linux/gtk3/

      pip install -U -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-20.04/ wxPython

## Run

1. Create the Version : 
   
        cd bart
        python createversion.py version.py

2. Run the program

        python -m bart

3. Run the tests

        pytest test