import os

from flask import Flask, jsonify, request, abort, redirect, make_response, current_app, Response, stream_with_context

# Initialize the Flask app.
app = Flask(__name__)

# Setting this to False prevents the Flask jsonify() function from printing line breaks and
# indentation. All of the api return values pass through the jsonify() function.
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

###################################################################################################
#                                            Routes                                               #
###################################################################################################

@app.route('/')
def index():
    return Response("x" * 12, mimetype="application/json")

@app.route('/test1')
def test1():
    return Response("x" * 13082, mimetype="application/json")


@app.route('/test2')
def test2():
    return Response("x" * 12900, mimetype="application/json")


def configure_error_handlers(app):

    @app.errorhandler(403)
    def forbidden_page(error):
        """
        The server understood the request, but is refusing to fulfill it.
        Authorization will not help and the request SHOULD NOT be repeated.
        If the request method was not HEAD and the server wishes to make public
        why the request has not been fulfilled, it SHOULD describe the reason for
        the refusal in the entity. If the server does not wish to make this
        information available to the client, the status code 404 (Not Found)
        can be used instead.
        """
        resp = jsonify(responseCode=403, error="Invalid login")
        resp.status_code = 403
        return resp


configure_error_handlers(app)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
