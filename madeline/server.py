import logging
import os
import subprocess
import uuid
import time

import flask
import jinja2

def cli(cmd_args, timeout=None):
    result = {}
    decode_method = 'utf-8'
    logging.info('cli.cmd_args: %s' % cmd_args)

    try:
        output = subprocess.check_output(cmd_args, stderr=subprocess.STDOUT, timeout=timeout)
        result['status'] = 'success'
        result['output'] = output.decode(decode_method)

    except subprocess.CalledProcessError as e:
        result['status'] = 'error'
        result['output'] = e.output.decode(decode_method)
        result['data'] = 'returncode: {rc}'.format(rc=e.output.returncode)

    except subprocess.TimeoutExpired as e:
        message = 'subprocess.check_output({cmd_args}, timeout={timeout}) threw exception TimeoutExpired'
        result['status'] = 'error'
        result['output'] = e.output.decode(decode_method)
        result['data'] = 'timeout ({timeout}) expired'.format(timeout=timeout)

    except Exception as e:
        result['status'] = 'error'
        result['output'] = str(e)

    logging.info('cli.result: %s' % result)

    return result

#-------------------------------------------------------------------------
# main
#-------------------------------------------------------------------------

logging.basicConfig(level=logging.INFO)

app =  flask.Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route("/", methods=['GET'])
def route_route():
    with open('templates/index.html.j2') as f:
        template = jinja2.Template(f.read())
    return template.render()

@app.route("/version", methods=['GET'])
def route_version():
    return cli(['cat', 'madeline-version.txt'])['output']

@app.route("/submit", methods=['POST'])
def route_run():
    job_id = str(uuid.uuid4())

    work_dir = 'tmp/{job_id}'.format(job_id=job_id)
    data_file = os.path.join(work_dir,'input.txt')
    output_prefix = os.path.join(work_dir, 'output')

    os.makedirs(work_dir)

    json_data = flask.request.get_json(force=True)

    with open(data_file, 'w') as f:
        f.write(json_data.get('data', ''))

    args = json_data.get('args', [])

    if len(args) > 1:
        command = ['madeline2', *args, '--outputprefix', output_prefix, data_file]
    else:
        command = ['madeline2', '--outputprefix', output_prefix, data_file]

    result = cli(command, timeout=30)

    result['command'] = command

    if result['status'] == 'success' and os.path.isfile(output_prefix + '.svg'):
        with open(output_prefix + '.svg') as f:
            result['data'] = f.read()
    else:
        result['status'] = 'error'
        result['data'] = result.get('data', '')

    return flask.jsonify(result)

@app.route("/help", methods=['GET'])
def route_help():
    with open('templates/help.html.j2') as f:
        template = jinja2.Template(f.read())

    help_message  = cli(['madeline2', '--help'])['output']

    return template.render(help_message=help_message)

if __name__ == "__main__":
    app.run(host=os.environ.get('APP_HOST', '0.0.0.0'),
            port=os.environ.get('APP_PORT', '5000'))

