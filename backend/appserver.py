"""
appserver.py  
- creates an application instance and runs the dev server
"""

if __name__ == '__main__':  
    from give_me_eat.application import create_app
    app = create_app()
    #app.run()
    app.run(host="0.0.0.0", port=8080)
