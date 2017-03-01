# Madeline Pedigree Drawing Engine Web Service

Web service to generate pedigree diagrams utilizing the
Madeline 2.0 Pedigree Drawing Engine (http://madeline.med.umich.edu/madeline).

## API

---

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

Example:

    $ curl http://<app>/version

    https://github.com/piratical/Madeline_2.0_PDE/tree/8ab82ad - 2016-12-21 00:38:52 -0500

---

### Submit

Submit data and command line arguments to render a pedigree diagram

#### URL

    http://<app>/submit

#### Methods

##### POST

Parameters:

- `data` - The text or XML for madeline to use as input to render the diagram

- `args` - List of command line arguments to pass to the madeline PDE binary

Response (Success):

    {
      'status': 'success',
      'svg': <svg_data>,
      'command': <command>,
      'command_output': <command_output>
    }

Response (Error):

    {
      'status': 'error',
      'reason': <reason_code>,
      'command': <command>,
      'command_output': <command_output>
    }

Example:

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
      "data": "Individualid\tFamilyid\tGender\tMother\tFather\nm100\tcs_001\tm\t.\t.\nm101\tcs_001\tf\t.\t.\nm102\tcs_001\tm\tm101\tm100\nm103\tcs_001\tf\tm101\tm100\n"
    }


    $ curl -X POST -d @madeline/data/request-with-tsv.json http://localhost:5000/submit
    {
      "command": [
        "madeline2",
        "--color",
        "--noiconlabels",
        "--outputprefix",
        "tmp/2ff66bac-07d8-41d2-a7c2-ae3d194840f6/output",
        "tmp/2ff66bac-07d8-41d2-a7c2-ae3d194840f6/2ff66bac-07d8-41d2-a7c2-ae3d194840f6.txt"
      ],
      "message": "",
      "output": "┌─────────────────────────────┐\n│ Welcome to Madeline 2.0 PDE │\n└─────────────────────────────┘\n--------------------------------------------\n LABELS                          TOTAL: 0\n--------------------------------------------\n--------------------------------------------\nParser::readFile(): Opening a(n) UTF-8 file ...\nReading file data in Madeline-XML format ...\nThere is 1 table\nEnd of Parser::_readXML() method.\nTable 1 is a pedigree table.\n┏ Start of    addPedigreesFromDataTable ┓\nDefault ordering of siblings.\n┗ End of      addPedigreesFromDataTable ┛\n┏ Start of    draw                      ┓\nPedigree output file is “tmp/2ff66bac-07d8-41d2-a7c2-ae3d194840f6/output.svg”\n┗ End of      draw                      ┛\n",
      "status": "success",
      "svg": "<?xml version=\"1.0\" standalone=\"no\"?>\n <svg version=\"1.1\"  id=\"svgDC\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\"  width=\"189\" height=\"266\"  viewBox=\"0 0 189 266\"  onload=\"init()\" >\n <defs>\n  <style type=\"text/css\"><![CDATA[\n\nline{\n\tstroke:#000;\n\tstroke-width:0.5mm;\n\tstroke-linejoin:miter;\n\tstroke-linecap:square;\n}\n\nrect{\n\tstroke:#000;\n\tstroke-width:0.5mm;\n\tstroke-linejoin:miter;\n\tstroke-linecap:square;\n}\n\nellipse{\n\tstroke: #000;\n    fill: #fff;\n\tstroke-width:0.25mm;\n}\n\ntext{\n\tfont-family:\"DejaVu Sans\",sans-serif;\n\tfont-size:12px;\n}\n\n.smallText{\n\tfont-family:\"DejaVu Sans\",sans-serif;\n\tfont-size:9px;\n\tfill:#444;\n}\n\n.layer text{\n\tfill:#930;\n}\n\n.layer line{\n\tstroke:#000;\n}\n\n.birthOrder,.unknownTwins{\n\tfont-size: 8px;\n}\n\n.header{\n\tfont-size:18px;\n\tfont-weight:bold;\n}\n\n.keyBox{\n\tfill:#e5e5e5;\n\tstroke:#000;\n\tstroke-width:0.5mm;\n\tstroke-linejoin:miter;\n\tstroke-linecap:square;\n}\n\n.mating:hover{\n\tstroke-width:1mm;\n\tstroke:#d56300;\n}\n\n.selectedIndividual{\n\tstroke-width:1mm;\n\tstroke-linecap:square;\n\tstroke-linejoin:miter;\n\tstroke:#d00;\n    fill:none;\n}\n\n.selectedIndividual:hover{\n\tstroke:#d00;\n\tfill:#ffbbbb;\n\tfill-opacity:0.70;\n}\n\n.solid{\n\tstroke-width:0.5mm;\n\tstroke-linecap:square;\n\tstroke-linejoin:miter;\n\tstroke:#000;\n\tfill:none;\n}\n\n.dashed{\n\tstroke-width:0.5mm;\n\tstroke-linecap:square;\n\tstroke-linejoin:miter;\n\tstroke:#98afc7;\n\tstroke-dasharray:2mm,1mm;\n\tstroke-dashoffset:1.0mm;\n\tfill:none;\n}\n\n.solid:hover{\n\tfill:#ffb787;\n\tfill-opacity:0.70;\n\tstroke:#d56300;\n\tstroke-width:1mm;\n}\n\n.dashed:hover{\n\tfill:#ffb787;\n\tfill-opacity:0.70;\n\tstroke:#d56300;\n\tstroke-width:1mm;\n}\n\n.filled{\n\tstroke-width:0.5mm;\n\tstroke-linecap:square;\n\tstroke-linejoin:miter;\n\tstroke:#000;\n\tfill:#000;\n}\n\n.specialIcons{\n\tstroke-width:0.25mm;\n\tstroke-linecap:round;\n\tstroke-linejoin:miter;\n\tstroke:#000;\n\tfill:#fff;\n}\n\n.specialLines{\n\tstroke-linecap:square;\n\tstroke-linejoin:miter;\n\tstroke:#000;\n\tstroke-width:0.5mm;\n\tfill:none;\n}\n\n.thinLine{\n\tfill:none;\n\tstroke: #000;\n\tstroke-width:0.25mm;\n}\n\n.curvedConnector{\n\tstroke-linecap:square;\n\tstroke-linejoin:miter;\n\tstroke:#98afc7;\n\tstroke-width:0.5mm;\n\tstroke-dasharray:2mm,1mm;\n\tstroke-dashoffset:1.0mm;\n\tfill:none;\n}\n\n.curvedConnector:hover{\n\tstroke:#d56300;\n}\n\n.whiteInkLetter_1{\n\tfont-size: 12px;\n\tfill: #fff;\n}\n\n.whiteInkLetter_2{\n\tfont-size: 10px;\n\tfill: #fff;\n}\n\n.whiteInkLetter_3{\n\tfont-size: 8px;\n\tfill: #fff;\n}\n\n.whiteInkLetter{\n\tfont-size: 8px;\n\tfill: #fff;\n}\n\n.blackInkLetter_1{\n\tfont-size: 12px;\n}\n\n.blackInkLetter_2{\n\tfont-size: 10px;\n}\n\n.blackInkLetter_3{\n\tfont-size: 8px;\n}\n\n.blackInkLetter{\n\tfont-size: 8px;\n\tfill: #000;\n}\n\n.blackInk{\n\tfill: #000;\n}\n\n.whiteInk{\n\tfill: #fff;\n}\n\n.counter{\n\tfont-size: 14px;\n\tfill: #000;\n}\n\n.counterFill{\n\tfill: #fff;\n}\n\n.sampleLevel{\n\tstroke:none;\n\tfill:#f99;\n}\n\n]]></style>\n <script type=\"text/javascript\" xlink:href=\"javascript/madeline.js\"></script>\n <marker id=\"endArrow\" viewBox=\"0 0 10 10\" refX=\"1\" refY=\"5\" markerUnits=\"strokeWidth\" orient=\"auto\" markerWidth=\"5\" markerHeight=\"4\">  <polyline points=\"0,0 10,5 0,10 1,5\" fill=\"#000\" /> </marker>\n </defs>\n <g class=\"pedigree\" transform=\"translate(-462.86)\">\n\n <g id=\"bottomLayer\" class=\"layer\" >\n\n </g>\n <g id=\"layer0\" class=\"layer\" >\n </g>\n\n  <g class=\"drawing\">\n  <text x=\"557.36\" y=\"30\" text-anchor=\"middle\"  class=\"header\" >cs_001</text>\n  <rect x=\"500.66\" y=\"38.66\" width=\"22.68\" height=\"22.68\" id=\"m100\" class=\"solid\">\n\t<title>m100</title>\n</rect>\n  <text x=\"512\" y=\"92.5845\" text-anchor=\"middle\" >m100</text>\n  <line x1=\"523.34\" y1=\"50\" x2=\"591.38\" y2=\"50\" />\n<circle cx=\"602.72\" cy=\"50\" r=\"11.34\" id=\"m101\" class=\"solid\">\n\t<title>m101</title>\n</circle>\n  <text x=\"602.72\" y=\"92.5845\" text-anchor=\"middle\" >m101</text>\n  <line class=\"mating\" id=\"m101:m100\" x1=\"557.36\" y1=\"50\" x2=\"557.36\" y2=\"123.907\" />\n  <line class=\"solid\" x1=\"512\" y1=\"123.907\" x2=\"512\" y2=\"152.257\" />\n  <rect x=\"500.66\" y=\"152.257\" width=\"22.68\" height=\"22.68\" id=\"m102\" class=\"solid\">\n\t<title>m102</title>\n</rect>\n  <text x=\"512\" y=\"206.181\" text-anchor=\"middle\" >m102</text>\n  <line class=\"solid\" x1=\"602.72\" y1=\"123.907\" x2=\"602.72\" y2=\"152.257\" />\n<circle cx=\"602.72\" cy=\"163.597\" r=\"11.34\" id=\"m103\" class=\"solid\">\n\t<title>m103</title>\n</circle>\n  <text x=\"602.72\" y=\"206.181\" text-anchor=\"middle\" >m103</text>\n  <line x1=\"512\" y1=\"123.907\" x2=\"602.72\" y2=\"123.907\" />\n  </g>\n\n </g>\n </svg>\n\n"
    }
