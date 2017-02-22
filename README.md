# Madeline Pedigree Drawing Engine Service

## API

- `http://<app>/version`
  - GET: Return version (Github Commit SHA and Date) of compiled madeline PDE binary

- `http://<app>/submit`
  - POST: Submit data and command line arguments to render a pedigree diagram
    - fields:
      - `data` - the text or XML for madeline to use as input to render the diagram
      - `args` - Command line arguments to pass to the madeline PDE binary
    - response: ```
      { 'status':
        'message':
        'output':

- `http://<app>/get/<jobid>`
  - GET:
