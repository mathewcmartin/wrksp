# A module's __name__

# Every module has a name and statements in a module can find out the name of its module. This is especially handy in one particular situation - As mentioned previously, when a module is imported for the first time, the main block in that module is run. What if we want to run the block only if the program was used by itself and not when it was imported from another module? This can be achieved using the __name__ attribute of the module.

'''\
    Example:
        #!/usr/bin/python
        # Filename: using_name.py

        if __name__ == '__main__':
        	print('This program is being run by itself')
        else:
        	print('I am being imported from another module')
'''

#!/usr/bin python

if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print ('I am being imported from another module')

# Every Python module has it's __name__ defined and if this is '__main__', it implies that the module is being run standalone by the user and we can do corresponding appropriate actions.
