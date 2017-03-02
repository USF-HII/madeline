# Madeline Pedigree Drawing Engine Web Service

Web service to generate pedigree diagrams utilizing the
Madeline 2.0 Pedigree Drawing Engine (http://madeline.med.umich.edu/madeline).

## API

### Version

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

#### Examples

    $ curl http://<app>/version

    https://github.com/piratical/Madeline_2.0_PDE/tree/8ab82ad - 2016-12-21 00:38:52 -0500

---

### Submit

Submit data and command line arguments to render a pedigree diagram

#### URL

    http://<app>/submit

#### Methods

##### POST

JSON Parameters:

    {
      'data': <text>,            # Tab-separated/XML data
      'args': [<arg>, <arg...>]  # Madeline PDE command line arguments
    }

Response (Success):

    {
      'status': 'success',
      'data': <svg_xml>,
      'command': <command>,
      'command_output': <command_output>
    }

Response (Error):

    {
      'status': 'error',
      'data': <error_information>,
      'command': <command>,
      'command_output': <command_output>
    }

#### Examples

*Note: Test data available at:* http://madeline.med.umich.edu/madeline/testdata/

    $ cat madeline/data/cs_001.data

    Individualid	Familyid	Gender	Mother	Father
    m100	cs_001	m	.	.
    m101	cs_001	f	.	.
    m102	cs_001	m	m101	m100
    m103	cs_001	f	m101	m100
    m104	cs_001	m	.	.
    m105	cs_001	f	m101	m100
    m106	cs_001	m	.	.
    m107	cs_001	m	m101	m100
    m109	cs_001	m	m103	m104
    m108	cs_001	m	m103	m104
    m110	cs_001	m	m114	m108
    m111	cs_001	m	m114	m108
    m114	cs_001	f	m105	m106
    m112	cs_001	m	m105	m106

    $ cat madeline/data/request-with-tsv.json
    {
      "args": [ "--color", "--noiconlabels" ],
      "data": "Individualid\tFamilyid\tGender\tMother\tFather\nm100\tcs_001\tm\t.\t.\nm101\tcs_001\tf\t...etc."
    }

    $ curl -X POST -d @madeline/data/request-with-tsv.json http://localhost:5000/submit
    {
      "status": "success",
      "svg": "<?xml version=\"1.0\" standalone=\"no\"?>\n <svg version=\"1.1\"  id=\"svgDC\" xmlns=...etc.",
      "command": [
        "madeline2",
        "--color",
        "--noiconlabels",
        "--outputprefix",
        "tmp/2ff66bac-07d8-41d2-a7c2-ae3d194840f6/output",
        "tmp/2ff66bac-07d8-41d2-a7c2-ae3d194840f6/2ff66bac-07d8-41d2-a7c2-ae3d194840f6.txt"
      ],
      "command_output": "┌─────────────────────────────┐\n│ Welcome to Madeline 2.0 PDE │\n└──────────────────...etc."
    }

