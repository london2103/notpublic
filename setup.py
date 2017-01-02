from setuptools import setup

setup(
    name="electrum-server",
    version="0.9",
    scripts=['run_electrum_server.py','electrum-server'],
    install_requires=['plyvel','jsonrpclib', 'irc >= 11'],
    package_dir={
        'electrumserver':'src'
        },
    py_modules=[
        'electrumserver.__init__',
        'electrumserver.utils',
        'electrumserver.storage',
        'electrumserver.deserialize',
        'electrumserver.networks',
        'electrumserver.blockchain_processor',
        'electrumserver.server_processor',
        'electrumserver.processor',
        'electrumserver.version',
        'electrumserver.ircthread',
        'electrumserver.stratum_tcp',
        'electrumserver.stratum_http'

    ],
    description="CloakCoin Electrum Server",
    author="Thomas Voegtlin & vuksa2103",
    author_email="thomasv@electrum.org",
    license="MIT Licence",
    url="https://github.com/spesmilo/electrum-server/",
    long_description="""Server for the Electrum Lightweight CloakCoin Wallet"""
)
