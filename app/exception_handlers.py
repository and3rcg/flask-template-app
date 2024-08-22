from flask import render_template, jsonify

import werkzeug.exceptions

def register_exception_handlers(app):
    @app.errorhandler(werkzeug.exceptions.NotFound)
    def not_found_error(error):
        return render_template("404.html"), 404

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        response = {
            "error": str(error),
            "message": "An unexpected error occurred. Please try again later."
        }
        return jsonify(response), 500
