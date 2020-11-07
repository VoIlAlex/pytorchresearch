# PTR Project Structure

## Running

Running of the project is done with `manage.py` file
from the root of the project.

// TODO: add details about `manage.py`, its arguments or link to the documents

## Development

Development involves writing configuration files
in `confing/` folder. To see details about writing 
configuration files see **<a href="#config">config</a>** 
section in this document.


## File system

#### /

Here `manage.py` file reside. This is the file to use
for running a PTR project.

#### /config <a name="config">

Collection of configurations for research.
Configuration files should have names ending with "config.py".

Configuration file should contain an object called RESEARCH_SESSION_CONFIG
with the following structure:
```json

```

#### /backbone