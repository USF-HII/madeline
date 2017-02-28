# Madeline Pedigree Drawing Engine Service

## API

### Version (GET)

Returns version (Github Commit SHA and Date) of compiled madeline PDE binary.

The madeline PDE binary is compiled from the Madeline PDE source code
located at https://github.com/piratical/Madeline_2.0_PDE.

#### URL

`http://<app>/version`

#### Methods

##### GET

Parameters:

    None

Response:

    <git_url> - <datestamp_of_commit>

Example:

    $ curl http://<app>/version

    https://github.com/piratical/Madeline_2.0_PDE/tree/8ab82ad - 2016-12-21 00:38:52 -0500

---

### Submit (POST)

Submit data and command line arguments to render a pedigree diagram

#### URL

http://<app>/submit

#### Methods

##### POST

Parameters:

    data - The text or XML for madeline to use as input to render the diagram

    args - Command line arguments to pass to the madeline PDE binary

Response (Success):

    {
      'status': 'success',
      'output': <cli_output>,
      'svg': <svg_data>
    }

Response (Error):

    {
      'status': 'error',
      'output': <cli_output>,
      'reason': error|timeout
    }

### Get Madeline PDE Job Results

- `http://<app>/get/<job_id>`
  - GET
