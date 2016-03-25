from flask import Flask, render_template
import json

app = Flask(__name__)
app.debug = False
resume_path = 'data/resume.json'


def read_resume(resume_path=resume_path):
    return json.load(open(resume_path))


@app.route('/')
def show_resume():
    return render_template('compact.html', r=read_resume())


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-d', '--debug', default=False, action='store_true',
                        help='Start flask app in debug mode. Default false.')
    parser.add_argument('-p', '--port', default=5000, type=int,
                        help="Port to run app on. Default 5000.")
    parser.add_argument('-H', '--host', default='127.0.0.1',
                        help='Set the flask app\'s "host" parameter. Default '
                        '127.0.0.1 answers requests only on localhost. '
                        '0.0.0.0 answers requests from any host. Use with '
                        'caution, especially in conjunction with --debug!')
    parser.add_argument('-r', '--resume-path', default='data/resume.json',
                        help='Set the (relative) path of JSON file containing '
                        'resume data. Default "data/resume.json".')
    args = parser.parse_args()

    resume_path = args.resume_path

    app.run(host=args.host, port=args.port, debug=args.debug)
