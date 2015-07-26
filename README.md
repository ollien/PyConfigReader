PyConfigReader
==============

A very basic config reader for all of your needs in python.

Example of use

```py
import configReader
reader = configReader.ConfigReader(name="myConfig.txt") #You can set the name to be whatever you like, but leaving it without will default to myConfig.txt
reader.readKeys() #This will read from the file and allow you to export them into a dictionary (This will be automatically done by getKeys if the read flag is set to True, which it is by default)
keys = reader.getKeys() #This will be a dictionary for you to read at your pleasure (run reader.getKeys(read=False) in order for it to not re-read the file.
myConfigCode = keys['myKey']
```

and an example of the config.txt this would be reading

```
#Just a simple example key
myKey = key.example
moreKeys = examples!
```
