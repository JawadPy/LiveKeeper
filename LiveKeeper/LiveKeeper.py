class LiveKeeper:
    def LiveKeeper() -> None:
        from flask import Flask, abort

        app = Flask(__name__)

        @app.before_request
        def deny_all():
            abort(403)
        
        app.run(
            debug=False,
            host='0.0.0.0',
            port=80
        )

    @staticmethod
    def run():
        from threading import Thread
        Thread(target=LiveKeeper.LiveKeeper).start()
