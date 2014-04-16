PyConfigReader
==============

A very basic config reader for all of your needs in python.

Example of use

```
import configReader
reader=configReader.ConfigReader()
reader.readKeys() #This will read from the file and allow you to export them into a dictionary
keys=reader.readKeys() #This will be a dictionary for you to read at your pleasure
myConfigCode=keys['myKey']
```

and an example of the config this would be reading

```
#Just a simple example key
myKey=key.example
moreKeys=examples!
