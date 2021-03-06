from setuptools import setup, find_packages

setup(
    name="jhub-nginx",
    packages=find_packages(),
    version="0.1",
    description="Manage virtual hosts entries for proxying from nginx to JupyterHub",
    long_description='''
Automates exposing jupyterhub instances to the web in a safe manner.

1. Get free SSL certificate from letsencrypt
2. Configure Nginx to forward https to jupyterhub running locally or behind a firewall or in container
3. Optionally updates DNS (for providers supported by apache-libcloud, also for duckdns.org)
    ''',
    author="Kirill Kouzoubov",
    author_email="Kirill888@gmail.com",
    url="https://github.com/Kirill888/jhub-nginx",
    license="MIT",
    keywords=["jupyterhub", "jupyter", "nginx"],
    install_requires=[
        "jinja2",
        "requests >= 2.18.0",
        "pydash",
        "pyyaml",
        "click",
    ],
    extras_require=dict(
        dns=['apache-libcloud'],
        ec2=['apache-libcloud', 'boto3'],
    ),
    entry_points={
        "console_scripts": [
            "jhub-vhost = jhubnginx.app:cli"
        ]
    }
)
