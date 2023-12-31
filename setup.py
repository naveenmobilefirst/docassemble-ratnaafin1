import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.ratnaafin1',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description='# docassemble.ratnaafin1\r\n\r\nA docassemble extension.\r\n\r\n## Author\r\n\r\nNaveen Boddeda, naveen.mobilefirst@gmail.com\r\n\r\n',
      long_description_content_type='text/markdown',
      author='Naveen Boddeda',
      author_email='naveen.mobilefirst@gmail.com',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=['3to2>=1.1.1', 'Babel>=2.13.0', 'CairoSVG>=2.7.0', 'ConfigArgParse>=1.7', 'Deprecated>=1.2.14', 'Docassemble-Flask-User>=0.6.29', 'Docassemble-Pattern>=3.6.7', 'Flask>=2.3.2', 'Flask-Cors>=4.0.0', 'Flask-Login>=0.6.2', 'Flask-Mail>=0.9.1', 'Flask-SQLAlchemy>=3.1.1', 'Flask-SocketIO>=5.3.6', 'Flask-WTF>=1.2.1', 'Hyphenate>=1.1.0', 'Jinja2>=3.1.2', 'Mako>=1.2.4', 'Markdown>=3.4.3', 'MarkupSafe>=2.1.3', 'Pillow>=10.0.1', 'PyJWT>=2.8.0', 'PyLaTeX>=1.4.1', 'PyNaCl>=1.5.0', 'PySocks>=1.7.1', 'PyYAML>=6.0.1', 'Pygments>=2.15.1', 'SQLAlchemy>=2.0.22', 'SecretStorage>=3.3.3', 'SocksiPy-branch>=1.01', 'TatSu>=5.8.3', 'WTForms>=3.1.0', 'Werkzeug>=2.3.6', 'XlsxWriter>=3.1.7', 'acme>=2.7.1', 'aiohttp>=3.8.5', 'aiohttp-retry>=2.8.3', 'aiosignal>=1.3.1', 'airtable-python-wrapper>=0.15.3', 'alembic>=1.11.1', 'amqp>=5.1.1', 'anyio>=3.7.1', 'arrow>=1.3.0', 'asn1crypto>=1.5.1', 'astunparse>=1.6.3', 'async-generator>=1.10', 'async-timeout>=4.0.2', 'atomicwrites>=1.4.1', 'attrs>=23.1.0', 'azure-common>=1.1.28', 'azure-core>=1.28.0', 'azure-identity>=1.13.0', 'azure-keyvault-secrets>=4.7.0', 'azure-nspkg>=3.0.2', 'azure-storage-blob>=12.17.0', 'bcrypt>=4.0.1', 'beautifulsoup4>=4.12.2', 'behave>=1.2.6', 'bidict>=0.22.1', 'billiard>=4.1.0', 'bleach>=6.0.0', 'blinker>=1.6.2', 'boto>=0.8c', 'boto3>=1.28.63', 'botocore>=1.31.63', 'cachetools>=5.3.1', 'cairocffi>=1.6.0', 'celery>=5.3.1', 'certbot>=2.7.1', 'certbot-apache>=2.7.1', 'certbot-nginx>=2.7.1', 'certifi>=2023.7.22', 'cffi>=1.16.0', 'chardet>=5.1.0', 'charset-normalizer>=3.3.0', 'click>=8.1.6', 'click-didyoumean>=0.3.0', 'click-plugins>=1.1.1', 'click-repl>=0.3.0', 'clicksend-client>=5.0.72', 'colorama>=0.4.6', 'commonmark>=0.9.1', 'configobj>=5.0.8', 'configparser>=6.0.0', 'contourpy>=1.1.1', 'convertapi>=1.7.0', 'crayons>=0.4.0', 'cryptography>=41.0.4', 'cssselect2>=0.7.0', 'cycler>=0.12.1', 'defusedxml>=0.7.1', 'deprecation>=2.1.0', 'distro>=1.8.0', 'dnspython>=2.4.0', 'docassemble-backports>=1.0', 'docassemble-textstat>=0.7.2', 'docassemble.demo>=1.4.82', 'docassemble.ratnaafin1', 'docassemblekvsession>=0.7', 'docopt>=0.6.2', 'docutils>=0.20.1', 'docxcompose>=1.4.0', 'docxtpl>=0.16.7', 'email-validator>=2.0.0.post2', 'et-xmlfile>=1.1.0', 'eventlet>=0.33.3', 'exceptiongroup>=1.1.2', 'flask-babel>=4.0.0', 'fonttools>=4.43.1', 'frozenlist>=1.4.0', 'future>=0.18.3', 'gcs-oauth2-boto-plugin>=3.0', 'geographiclib>=2.0', 'geopy>=2.3.0', 'google-api-core>=2.12.0', 'google-api-python-client>=1.0', 'google-auth>=2.23.3', 'google-auth-httplib2>=0.1.1', 'google-auth-oauthlib>=1.1.0', 'google-cloud-core>=2.3.3', 'google-cloud-storage>=2.12.0', 'google-cloud-translate>=3.12.0', 'google-cloud-vision>=3.4.4', 'google-crc32c>=1.5.0', 'google-i18n-address>=3.1.0', 'google-reauth>=0.1.1', 'google-resumable-media>=2.6.0', 'googleapis-common-protos>=1.61.0', 'googledrivedownloader>=0.4', 'greenlet>=2.0.2', 'grpcio>=1.56.2', 'grpcio-status>=1.56.2', 'gspread>=5.10.0', 'guess-language-spirit>=0.5.3', 'h11>=0.14.0', 'httpcore>=0.17.3', 'httplib2>=0.22.0', 'humanize>=4.7.0', 'ics>=0.7.2', 'idna>=3.4', 'img2pdf>=0.4.4', 'importlib-metadata>=6.8.0', 'importlib-resources>=6.0.0', 'iniconfig>=2.0.0', 'iso8601>=2.0.0', 'isodate>=0.6.1', 'itsdangerous>=2.1.2', 'jaraco.classes>=3.3.0', 'jdcal>=1.4.1', 'jeepney>=0.8.0', 'jellyfish>=0.11.2', 'jmespath>=1.0.1', 'joblib>=0.17.0', 'josepy>=1.13.0', 'keyring>=24.2.0', 'kiwisolver>=1.4.5', 'kombu>=5.3.1', 'libcst>=1.0.1', 'links-from-link-header>=0.1.0', 'lxml>=4.9.3', 'markdown-it-py>=3.0.0', 'matplotlib>=3.8.0', 'mdurl>=0.1.2', 'minio>=7.1.15', 'mod-wsgi>=4.9.4', 'monotonic>=1.6', 'more-itertools>=9.1.0', 'msal>=1.23.0', 'msal-extensions>=1.0.0', 'msrest>=0.7.1', 'multidict>=6.0.4', 'mypy-extensions>=1.0.0', 'namedentities>=1.5.2', 'netifaces>=0.11.0', 'nltk>=2.0.1', 'num2words>=0.5.12', 'numpy>=1.25.1', 'oauth2client>=1.0', 'oauthlib>=3.2.2', 'openpyxl>=3.1.2', 'ordered-set>=4.1.0', 'outcome>=1.2.0', 'packaging>=23.1', 'pandas>=2.0.3', 'parse>=1.19.1', 'parse-type>=0.6.2', 'parsedatetime>=2.6', 'passlib>=1.7.4', 'pdfminer.six>=20221105', 'phonenumbers>=8.13.17', 'pikepdf>=8.2.0', 'pip>=23.2.1', 'pkginfo>=1.9.6', 'pluggy>=1.2.0', 'ply>=3.11', 'portalocker>=2.7.0', 'prompt-toolkit>=3.0.39', 'proto-plus>=1.22.3', 'protobuf>=4.23.4', 'psutil>=5.9.5', 'psycopg2-binary>=2.9.6', 'pyOpenSSL>=23.2.0', 'pyRFC3339>=1.1', 'pyasn1>=0.5.0', 'pyasn1-modules>=0.3.0', 'pycountry>=22.3.5', 'pycparser>=2.21', 'pycryptodome>=3.18.0', 'pycryptodomex>=3.18.0', 'pycurl>=7.45.2', 'pyotp>=2.8.0', 'pyparsing>=3.1.1', 'pypng>=0.20220715.0', 'pytest>=7.4.0', 'python-augeas>=1.1.0', 'python-dateutil>=2.8.2', 'python-docx>=1.0.1', 'python-dotenv>=1.0.0', 'python-editor>=1.0.4', 'python-engineio>=4.5.1', 'python-http-client>=3.3.7', 'python-ldap>=3.4.3', 'python-socketio>=5.8.0', 'pytz>=2004b.2', 'pytz-deprecation-shim>=0.1.0.post0', 'pyu2f>=0.1.5', 'pyzbar>=0.1.9', 'qrcode>=7.4.2', 'rauth>=0.7.3', 'readme-renderer>=40.0', 'redis>=4.6.0', 'regex>=0.1.20130125', 'reportlab>=4.0.4', 'repoze.lru>=0.7', 'requests>=2.31.0', 'requests-oauthlib>=1.3.1', 'requests-toolbelt>=1.0.0', 'retry-decorator>=1.1.1', 'rfc3339>=6.2', 'rfc3986>=2.0.0', 'rich>=13.4.2', 'rsa>=4.7.2', 'ruamel.yaml>=0.17.32', 'ruamel.yaml.clib>=0.2.7', 's3transfer>=0.7.0', 's4cmd>=2.1.0', 'scikit-learn>=1.3.0', 'scipy>=1.11.1', 'selenium>=4.10.0', 'sendgrid>=6.10.0', 'setuptools>=59.6.0', 'simplekv>=0.14.1', 'six>=1.16.0', 'sniffio>=1.3.0', 'sortedcontainers>=2.4.0', 'soupsieve>=2.4.1', 'starkbank-ecdsa>=2.2.0', 'tailer>=0.4.1', 'telnyx>=2.0.0', 'threadpoolctl>=3.2.0', 'tinycss2>=1.2.1', 'titlecase>=2.4', 'toml>=0.10.2', 'tomli>=2.0.1', 'tqdm>=4.65.0', 'trio>=0.22.2', 'trio-websocket>=0.10.3', 'twilio>=8.9.1', 'twine>=4.0.2', 'types-python-dateutil>=2.8.19.14', 'typing-inspect>=0.9.0', 'typing_extensions>=4.7.1', 'tzdata>=2023.3', 'tzlocal>=5.1', 'uWSGI>=2.0.22', 'ua-parser>=0.18.0', 'uritemplate>=4.1.1', 'urllib3>=2.0.6', 'us>=3.1.1', 'user-agents>=2.2.0', 'vine>=5.0.0', 'wcwidth>=0.2.6', 'webdriver-manager>=4.0.0', 'webencodings>=0.5.1', 'wheel>=0.41.0', 'wrapt>=1.15.0', 'wsproto>=1.2.0', 'xfdfgen>=0.4', 'xlrd>=2.0.1', 'xlwt>=1.3.0', 'yarl>=1.9.2', 'zipp>=3.16.2'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/ratnaafin1/', package='docassemble.ratnaafin1'),
     )

