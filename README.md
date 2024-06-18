## Generate SSL Certificates

To create new SSL certificates, run the following from the root directory and provide the necessary information on the command line:

```bash
openssl req -x509 -newkey rsa:4096 -nodes -out app/ssl/cert.pem -keyout app/ssl/key.pem -days 365
```

## Run Locally

To run the application locally, execute the following from the `app` directory:

```bash
flask --app app.py run
```

To make the server publicly available, add `--host=0.0.0.0` to listen on all public IPs:

```bash
flask --app app.py run --host=0.0.0.0
```

You may also optionally specify a port for the application to run on with the `--port=` argument:

```bash
flask --app app.py run --host=0.0.0.0 --port=5050
```

The application can be run over HTTPS without requiring the creation of certificates by leveraging the `--cert=adhoc` argument:

```bash
flask --app app.py run --cert=adhoc
```

Alternatively, if you want to run the application with SSL certificates that you have created in the `ssl/` directory, use the following:

```bash
flask --app app.py run --cert=ssl/cert.pem --key=ssl/key.pem
```

## Sources & References

- [Flask Tutorial in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-flask)
- [Running Your Flask Application Over HTTPS](https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https)
