#from flask_cicd.apps.homes.tests.controls import app


def test_home_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/home' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/home')
        print("test_home_route__status_code__%s" % res.status_code)

def test_logout_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/logout' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/logout')
        print("test_logout_route__status_code__%s" % res.status_code)

