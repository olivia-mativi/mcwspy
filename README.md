# mcwspy
MasterControl WebServices API Abstraction Module in Python

## Enabling the module
Simply download mcwspy.py and place in your workspace directory, then
```python
>> import mcwspy as mc
```
## Starting a new ws session
Ensure that you have a .env in your workspace directory with the variables:
```
API_KEY=<your API key here>
SITE_URL=<your site URL to ws json bridge>
```

Then you can start a new session:
```python
>> s = mc.Session()
```

## Using the session
It's as simple as accessing the instance methods of Session, e.g.:
```python
>> print(s.get_all_users(99999, False).json())
```
