import logging
import os
import subprocess
import uuid

import flask

def cli(cmd_args, timeout=None):
    result = {}
    decode_method = 'utf-8'
    logging.info('cli.cmd_args: %s' % cmd_args)

    try:
        output = subprocess.check_output(cmd_args, stderr=subprocess.STDOUT, timeout=timeout)
        result['status'] = 'success'
        result['message'] = ''
        result['output'] = output.decode(decode_method)

    except subprocess.CalledProcessError as e:
        result['status'] = 'error'
        result['message'] = str(e)
        result['output'] = e.output.decode(decode_method)

    except subprocess.TimeoutExpired as e:
        message = 'subprocess.check_output({cmd_args}, timeout={timeout}) threw exception TimeoutExpired'
        result['status'] = 'error'
        result['message'] = message.format(cmd_args=cmd_args, timeout=timeout)
        result['output'] = e.output.decode(decode_method)

    logging.info('cli.result: %s' % result)

    return result

#-------------------------------------------------------------------------
# main
#-------------------------------------------------------------------------

logging.basicConfig(level=logging.INFO)

app =  flask.Flask(__name__)

app.config['JSON_AS_ASCII'] = True

@app.route("/", methods=['GET'])
def route_route():
    return "Coming soon"

@app.route("/version", methods=['GET'])
def route_version():
    return cli(['cat', 'madeline-version.txt'])['output']

@app.route("/run", methods=['POST'])
def route_run():
    job_id = str(uuid.uuid4())

    work_dir = 'tmp/{job_id}'.format(job_id=job_id)
    data_file = os.path.join(work_dir, job_id + '.txt')

    os.makedirs(work_dir)

    with open(data_file, 'w') as f:
        f.write(flask.request.form['data'])

    result = cli(['madeline2', data_file], timeout=30)

    return flask.jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000')

