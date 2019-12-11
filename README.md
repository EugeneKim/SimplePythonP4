# SimplePythonP4
This short Python script shows how to use Python P4 library (p4python) from https://www.perforce.com/.

## Where and How to download
### Where
https://pypi.org/project/p4python/
### How
`pip install p4python`

## How to use
p4python provides a simple interface from Python wrapping the Perforce C++ API to gain performance and ease of coding.
### Import the modules
`from P4 import P4, P4Exception`

### Instantiate P4
`p4 = P4()`

### Config connection settings
```
p4.port = 'p4server:1666'
p4.user = 'joe'
p4.password = 'joe_password'
```

### Connect
`p4.connect()`
 
### Login
`p4.run_login()`

### Use P4 
*See the document or sample code*

### Logout
`p4.run("logout")`

### Disconnect
`p4.disconnect()`

## Error handling
P4Exception will be thrown and contains all details of the exception, if an error occurs.
There are two types of list, *exceptions* and *warnings*. The former contains exception details of error-level and the latter contains exception details of warning-level. An error must not be ignored in any case, but warning could be. 
For instance if there is no resource found in the repository, that doesn't necessarily mean a critical one.

