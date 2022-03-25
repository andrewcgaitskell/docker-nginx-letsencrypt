c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'
c.Application.log_format = '[%(name)s]%(highlevel)s %(message)s'
c.Application.log_level = 30

c.JupyterHub.authenticator_class = 'jupyterhub.auth.PAMAuthenticator'

c.JupyterHub.base_url = '/dev/'
c.JupyterHub.bind_url = 'http://127.0.0.1:5050'

## match to /etc/nginx/conf.d/default.conf

#  If set to 0, no limit is enforced.
#  Default: 100
# c.JupyterHub.concurrent_spawn_limit = 100

## The config file to load
#  Default: 'jupyterhub_config.py'
c.JupyterHub.config_file = 'jupyterhub_config.py'

## Number of days for a login cookie to be valid.
#          Default is two weeks.
#  Default: 14
c.JupyterHub.cookie_max_age_days = 14

## The cookie secret to use to encrypt cookies.
#  
#          Loaded from the JPY_COOKIE_SECRET env variable by default.
#  
#          Should be exactly 256 bits (32 bytes).
#  Default: traitlets.Undefined
# c.JupyterHub.cookie_secret = traitlets.Undefined

## File in which to store the cookie secret.
#  Default: 'jupyterhub_cookie_secret'
c.JupyterHub.cookie_secret_file = 'jupyterhub_cookie_secret'

## The location of jupyterhub data files (e.g. /usr/local/share/jupyterhub)
#  Default: '/home/andrew_gaitskell/jupyterhub/env/share/jupyterhub'

c.JupyterHub.data_files_path = '/home/andrew_gaitskell/jupyterhub/env/share/jupyterhub'

## Include any kwargs to pass to the database connection.
#          See sqlalchemy.create_engine for details.
#  Default: {}
# c.JupyterHub.db_kwargs = {}

## url for the database. e.g. `sqlite:///jupyterhub.sqlite`
#  Default: 'sqlite:///jupyterhub.sqlite'
c.JupyterHub.db_url = 'sqlite:///jupyterhub.sqlite'

## log all database transactions. This has A LOT of output
#  Default: False
c.JupyterHub.debug_db = False

## The default URL for users when they arrive (e.g. when user directs to "/")
#  
#  By default, redirects users to their own server.
#  
#  Can be a Unicode string (e.g. '/hub/home') or a callable based on the handler
#  object:
#  
#  ::
#  
#def default_url_fn(handler):
#    user = handler.current_user
#    if user and user.admin:
#        return '/hub/admin'
#    return '/hub/home'

#c.JupyterHub.default_url = default_url_fn

#  Default: traitlets.Undefined
# c.JupyterHub.default_url = traitlets.Undefined


## The URL on which the Hub will listen. This is a private URL for internal
#  communication. Typically set in combination with hub_connect_url. If a unix
#  socket, hub_connect_url **must** also be set.
#  
#  For example:
#  
#      "http://127.0.0.1:8081"
#      "unix+http://%2Fsrv%2Fjupyterhub%2Fjupyterhub.sock"
#  
#  .. versionadded:: 0.9
#  Default: ''
# c.JupyterHub.hub_bind_url = ''

## The ip or hostname for proxies and spawners to use
#          for connecting to the Hub.
#  
#          Use when the bind address (`hub_ip`) is 0.0.0.0, :: or otherwise different
#          from the connect address.
#  
#          Default: when `hub_ip` is 0.0.0.0 or ::, use `socket.gethostname()`,
#  otherwise use `hub_ip`.
#  
#          Note: Some spawners or proxy implementations might not support hostnames. Check your
#          spawner or proxy documentation to see if they have extra requirements.
#  
#          .. versionadded:: 0.8
#  Default: ''
# c.JupyterHub.hub_connect_ip = ''


## The URL for connecting to the Hub. Spawners, services, and the proxy will use
#  this URL to talk to the Hub.
#  
#  Only needs to be specified if the default hub URL is not connectable (e.g.
#  using a unix+http:// bind url).
#  
#  .. seealso::
#      JupyterHub.hub_connect_ip
#      JupyterHub.hub_bind_url
#  
#  .. versionadded:: 0.9
#  Default: ''
# c.JupyterHub.hub_connect_url = ''

## The ip address for the Hub process to *bind* to.
#  
#          By default, the hub listens on localhost only. This address must be accessible from
#          the proxy and user servers. You may need to set this to a public ip or '' for all
#          interfaces if the proxy or user servers are in containers or on a different host.
#  
#          See `hub_connect_ip` for cases where the bind and connect address should differ,
#          or `hub_bind_url` for setting the full bind URL.
#  Default: '127.0.0.1'
c.JupyterHub.hub_ip = '127.0.0.1'

## The internal port for the Hub process.
#  
#          This is the internal port of the hub itself. It should never be accessed directly.
#          See JupyterHub.port for the public port to use when accessing jupyterhub.
#          It is rare that this port should be set except in cases of port conflict.
#  
#          See also `hub_ip` for the ip and `hub_bind_url` for setting the full
#  bind URL.
#  Default: 8081
#c.JupyterHub.hub_port = 8081

## The routing prefix for the Hub itself.
#  
#  Override to send only a subset of traffic to the Hub. Default is to use the
#  Hub as the default route for all requests.
#  
#  This is necessary for normal jupyterhub operation, as the Hub must receive
#  requests for e.g. `/user/:name` when the user's server is not running.
#  
#  However, some deployments using only the JupyterHub API may want to handle
#  these events themselves, in which case they can register their own default
#  target with the proxy and set e.g. `hub_routespec = /hub/` to serve only the
#  hub's own pages, or even `/hub/api/` for api-only operation.
#  
#  Note: hub_routespec must include the base_url, if any.
#  
#  .. versionadded:: 1.4
#  Default: '/'
# c.JupyterHub.hub_routespec = '/'

## Trigger implicit spawns after this many seconds.
#  
#          When a user visits a URL for a server that's not running,
#          they are shown a page indicating that the requested server
#          is not running with a button to spawn the server.
#  
#          Setting this to a positive value will redirect the user
#          after this many seconds, effectively clicking this button
#          automatically for the users,
#          automatically beginning the spawn process.
#  
#          Warning: this can result in errors and surprising behavior
#          when sharing access URLs to actual servers,
#          since the wrong server is likely to be started.
#  Default: 0
# c.JupyterHub.implicit_spawn_seconds = 0

## Timeout (in seconds) to wait for spawners to initialize
#  
#  Checking if spawners are healthy can take a long time if many spawners are
#  active at hub start time.
#  
#  If it takes longer than this timeout to check, init_spawner will be left to
#  complete in the background and the http server is allowed to start.
#  
#  A timeout of -1 means wait forever, which can mean a slow startup of the Hub
#  but ensures that the Hub is fully consistent by the time it starts responding
#  to requests. This matches the behavior of jupyterhub 1.0.
#  
#  .. versionadded: 1.1.0
#  Default: 10
# c.JupyterHub.init_spawners_timeout = 10

## The location to store certificates automatically created by
#          JupyterHub.
#  
#          Use with internal_ssl
#  Default: 'internal-ssl'
# c.JupyterHub.internal_certs_location = 'internal-ssl'


## Dict of 'group': ['usernames'] to load at startup.
#  
#          This strictly *adds* groups and users to groups.
#  
#          Loading one set of groups, then starting JupyterHub again with a different
#          set will not remove users or groups from previous launches.
#          That must be done through the API.
#  Default: {}
# c.JupyterHub.load_groups = {}

## List of predefined role dictionaries to load at startup.
#  
#          For instance::
#  
#              load_roles = [
#                              {
#                                  'name': 'teacher',
#                                  'description': 'Access to users' information and group membership',
#                                  'scopes': ['users', 'groups'],
#                                  'users': ['cyclops', 'gandalf'],
#                                  'services': [],
#                                  'groups': []
#                              }
#                          ]
#  
#          All keys apart from 'name' are optional.
#          See all the available scopes in the JupyterHub REST API documentation.
#  
#          Default roles are defined in roles.py.
#  Default: []
# c.JupyterHub.load_roles = []

## The date format used by logging formatters for %(asctime)s
#  See also: Application.log_datefmt
# c.JupyterHub.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#  See also: Application.log_format
# c.JupyterHub.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#  See also: Application.log_level
# c.JupyterHub.log_level = 30

## Specify path to a logo image to override the Jupyter logo in the banner.
#  Default: ''
# c.JupyterHub.logo_file = ''

## Maximum number of concurrent named servers that can be created by a user at a
#  time.
#  
#  Setting this can limit the total resources a user can consume.
#  
#  If set to 0, no limit is enforced.
#  Default: 0
# c.JupyterHub.named_server_limit_per_user = 0

## Expiry (in seconds) of OAuth access tokens.
#  
#          The default is to expire when the cookie storing them expires,
#          according to `cookie_max_age_days` config.
#  
#          These are the tokens stored in cookies when you visit
#          a single-user server or service.
#          When they expire, you must re-authenticate with the Hub,
#          even if your Hub authentication is still valid.
#          If your Hub authentication is valid,
#          logging in may be a transparent redirect as you refresh the page.
#  
#          This does not affect JupyterHub API tokens in general,
#          which do not expire by default.
#          Only tokens issued during the oauth flow
#          accessing services and single-user servers are affected.
#  
#          .. versionadded:: 1.4
#              OAuth token expires_in was not previously configurable.
#          .. versionchanged:: 1.4
#              Default now uses cookie_max_age_days so that oauth tokens
#              which are generally stored in cookies,
#              expire when the cookies storing them expire.
#              Previously, it was one hour.
#  Default: 0
# c.JupyterHub.oauth_token_expires_in = 0

## File to write PID
#          Useful for daemonizing JupyterHub.
#  Default: ''
# c.JupyterHub.pid_file = ''

## The URL the single-user server should start in.
#  
#  `{username}` will be expanded to the user's username
#  
#  Example uses:
#  
#  - You can set `notebook_dir` to `/` and `default_url` to `/tree/home/{username}` to allow people to
#    navigate the whole filesystem from their notebook server, but still start in their home directory.
#  - Start with `/notebooks` instead of `/tree` if `default_url` points to a notebook instead of a directory.
#  - You can set this to `/lab` to have JupyterLab start by default, rather than Jupyter Notebook.
#  Default: ''
#c.notebook_dir = '/'
#c.Spawner.default_url = '/tree/home/{username}'
#c.Spawner.default_url = '/lab/home/{username}'

## Disable per-user configuration of single-user servers.
#  
#  When starting the user's single-user server, any config file found in the
#  user's $HOME directory will be ignored.
#  
#  Note: a user could circumvent this if the user modifies their Python
#  environment, such as when they have their own conda environments / virtualenvs
#  / containers.
#  Default: False
# c.Spawner.disable_user_config = False

## List of environment variables for the single-user server to inherit from the
#  JupyterHub process.
#  
#  This list is used to ensure that sensitive information in the JupyterHub
#  process's environment (such as `CONFIGPROXY_AUTH_TOKEN`) is not passed to the
#  single-user server's process.
#  Default: ['PATH', 'PYTHONPATH', 'CONDA_ROOT', 'CONDA_DEFAULT_ENV', 'VIRTUAL_ENV', 'LANG', 'LC_ALL', 'JUPYTERHUB_SINGLEUSER_APP']
# c.Spawner.env_keep = ['PATH', 'PYTHONPATH', 'CONDA_ROOT', 'CONDA_DEFAULT_ENV', 'VIRTUAL_ENV', 'LANG', 'LC_ALL', 'JUPYTERHUB_SINGLEUSER_APP']

## Extra environment variables to set for the single-user server's process.
#  
#  Environment variables that end up in the single-user server's process come from 3 sources:
#    - This `environment` configurable
#    - The JupyterHub process' environment variables that are listed in `env_keep`
#    - Variables to establish contact between the single-user notebook and the hub (such as JUPYTERHUB_API_TOKEN)
#  
#  The `environment` configurable should be set by JupyterHub administrators to
#  add installation specific environment variables. It is a dict where the key is
#  the name of the environment variable, and the value can be a string or a
#  callable. If it is a callable, it will be called with one parameter (the
#  spawner instance), and should return a string fairly quickly (no blocking
#  operations please!).
#  
#  Note that the spawner class' interface is not guaranteed to be exactly same
#  across upgrades, so if you are using the callable take care to verify it
#  continues to work after upgrades!
#  
#  .. versionchanged:: 1.2
#      environment from this configuration has highest priority,
#      allowing override of 'default' env variables,
#      such as JUPYTERHUB_API_URL.
#  Default: {}
# c.Spawner.environment = {}

## Timeout (in seconds) before giving up on a spawned HTTP server
#  
#  Once a server has successfully been spawned, this is the amount of time we
#  wait before assuming that the server is unable to accept connections.
#  Default: 30
# c.Spawner.http_timeout = 30

## The URL the single-user server should connect to the Hub.
#  
#  If the Hub URL set in your JupyterHub config is not reachable from spawned
#  notebooks, you can set differnt URL by this config.
#  
#  Is None if you don't need to change the URL.
#  Default: None
# c.Spawner.hub_connect_url = None

## The IP address (or hostname) the single-user server should listen on.
#  
#  Usually either '127.0.0.1' (default) or '0.0.0.0'.
#  
#  The JupyterHub proxy implementation should be able to send packets to this
#  interface.
#  
#  Subclasses which launch remotely or in containers should override the default
#  to '0.0.0.0'.
#  
#  .. versionchanged:: 2.0
#      Default changed to '127.0.0.1', from ''.
#      In most cases, this does not result in a change in behavior,
#      as '' was interpreted as 'unspecified',
#      which used the subprocesses' own default, itself usually '127.0.0.1'.
#  Default: '127.0.0.1'
# c.Spawner.ip = '127.0.0.1'

## Minimum number of bytes a single-user notebook server is guaranteed to have
#  available.
#  
#  Allows the following suffixes:
#    - K -> Kilobytes
#    - M -> Megabytes
#    - G -> Gigabytes
#    - T -> Terabytes
#  
#  **This is a configuration setting. Your spawner must implement support for the
#  limit to work.** The default spawner, `LocalProcessSpawner`, does **not**
#  implement this support. A custom spawner **must** add support for this setting
#  for it to be enforced.
#  Default: None
# c.Spawner.mem_guarantee = None

## Maximum number of bytes a single-user notebook server is allowed to use.
#  
#  Allows the following suffixes:
#    - K -> Kilobytes
#    - M -> Megabytes
#    - G -> Gigabytes
#    - T -> Terabytes
#  
#  If the single user server tries to allocate more memory than this, it will
#  fail. There is no guarantee that the single-user notebook server will be able
#  to allocate this much memory - only that it can not allocate more than this.
#  
#  **This is a configuration setting. Your spawner must implement support for the
#  limit to work.** The default spawner, `LocalProcessSpawner`, does **not**
#  implement this support. A custom spawner **must** add support for this setting
#  for it to be enforced.
#  Default: None
# c.Spawner.mem_limit = None

## Path to the notebook directory for the single-user server.
#  
#  The user sees a file listing of this directory when the notebook interface is
#  started. The current interface does not easily allow browsing beyond the
#  subdirectories in this directory's tree.
#  
#  `~` will be expanded to the home directory of the user, and {username} will be
#  replaced with the name of the user.
#  
#  Note that this does *not* prevent users from accessing files outside of this
#  path! They can do so with many other means.
#  Default: ''
# c.Spawner.notebook_dir = ''

## Allowed roles for oauth tokens.
#  
#          This sets the maximum and default roles
#          assigned to oauth tokens issued by a single-user server's
#          oauth client (i.e. tokens stored in browsers after authenticating with the server),
#          defining what actions the server can take on behalf of logged-in users.
#  
#          Default is an empty list, meaning minimal permissions to identify users,
#          no actions can be taken on their behalf.
#  Default: traitlets.Undefined
# c.Spawner.oauth_roles = traitlets.Undefined

## An HTML form for options a user can specify on launching their server.
#  
#  The surrounding `<form>` element and the submit button are already provided.
#  
#  For example:
#  
#  .. code:: html
#  
#      Set your key:
#      <input name="key" val="default_key"></input>
#      <br>
#      Choose a letter:
#      <select name="letter" multiple="true">
#        <option value="A">The letter A</option>
#        <option value="B">The letter B</option>
#      </select>
#  
#  The data from this form submission will be passed on to your spawner in
#  `self.user_options`
#  
#  Instead of a form snippet string, this could also be a callable that takes as
#  one parameter the current spawner instance and returns a string. The callable
#  will be called asynchronously if it returns a future, rather than a str. Note
#  that the interface of the spawner class is not deemed stable across versions,
#  so using this functionality might cause your JupyterHub upgrades to break.
#  Default: traitlets.Undefined
# c.Spawner.options_form = traitlets.Undefined

## Interpret HTTP form data
#  
#  Form data will always arrive as a dict of lists of strings. Override this
#  function to understand single-values, numbers, etc.
#  
#  This should coerce form data into the structure expected by self.user_options,
#  which must be a dict, and should be JSON-serializeable, though it can contain
#  bytes in addition to standard JSON data types.
#  
#  This method should not have any side effects. Any handling of `user_options`
#  should be done in `.start()` to ensure consistent behavior across servers
#  spawned via the API and form submission page.
#  
#  Instances will receive this data on self.user_options, after passing through
#  this function, prior to `Spawner.start`.
#  
#  .. versionchanged:: 1.0
#      user_options are persisted in the JupyterHub database to be reused
#      on subsequent spawns if no options are given.
#      user_options is serialized to JSON as part of this persistence
#      (with additional support for bytes in case of uploaded file data),
#      and any non-bytes non-jsonable values will be replaced with None
#      if the user_options are re-used.
#  Default: traitlets.Undefined
# c.Spawner.options_from_form = traitlets.Undefined

## Interval (in seconds) on which to poll the spawner for single-user server's
#  status.
#  
#  At every poll interval, each spawner's `.poll` method is called, which checks
#  if the single-user server is still running. If it isn't running, then
#  JupyterHub modifies its own state accordingly and removes appropriate routes
#  from the configurable proxy.
#  Default: 30
# c.Spawner.poll_interval = 30

## The port for single-user servers to listen on.
#  
#  Defaults to `0`, which uses a randomly allocated port number each time.
#  
#  If set to a non-zero value, all Spawners will use the same port, which only
#  makes sense if each server is on a different address, e.g. in containers.
#  
#  New in version 0.7.
#  Default: 0
# c.Spawner.port = 0

## An optional hook function that you can implement to do work after the spawner
#  stops.
#  
#  This can be set independent of any concrete spawner implementation.
#  Default: None
# c.Spawner.post_stop_hook = None

## An optional hook function that you can implement to do some bootstrapping work
#  before the spawner starts. For example, create a directory for your user or
#  load initial content.
#  
#  This can be set independent of any concrete spawner implementation.
#  
#  This maybe a coroutine.
#  
#  Example::
#  
#      from subprocess import check_call
#      def my_hook(spawner):
#          username = spawner.user.name
#          check_call(['./examples/bootstrap-script/bootstrap.sh', username])
#  
#      c.Spawner.pre_spawn_hook = my_hook
#  Default: None
# c.Spawner.pre_spawn_hook = None

## List of SSL alt names
#  
#          May be set in config if all spawners should have the same value(s),
#          or set at runtime by Spawner that know their names.
#  Default: []
# c.Spawner.ssl_alt_names = []

## Whether to include DNS:localhost, IP:127.0.0.1 in alt names
#  Default: True
# c.Spawner.ssl_alt_names_include_local = True

## Timeout (in seconds) before giving up on starting of single-user server.
#  
#  This is the timeout for start to return, not the timeout for the server to
#  respond. Callers of spawner.start will assume that startup has failed if it
#  takes longer than this. start should return when the server process is started
#  and its location is known.
#  Default: 60
# c.Spawner.start_timeout = 60

#------------------------------------------------------------------------------
# Authenticator(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
## Base class for implementing an authentication provider for JupyterHub

## Set of users that will have admin rights on this JupyterHub.
#  
#  Note: As of JupyterHub 2.0, full admin rights should not be required, and more
#  precise permissions can be managed via roles.
#  
#  Admin users have extra privileges:
#   - Use the admin panel to see list of users logged in
#   - Add / remove users in some authenticators
#   - Restart / halt the hub
#   - Start / stop users' single-user servers
#   - Can access each individual users' single-user server (if configured)
#  
#  Admin access should be treated the same way root access is.
#  
#  Defaults to an empty set, in which case no user has admin access.
#  Default: set()
# c.Authenticator.admin_users = set()

## Set of usernames that are allowed to log in.
#  
#  Use this with supported authenticators to restrict which users can log in.
#  This is an additional list that further restricts users, beyond whatever
#  restrictions the authenticator has in place. Any user in this list is granted
#  the 'user' role on hub startup.
#  
#  If empty, does not perform any additional restriction.
#  
#  .. versionchanged:: 1.2
#      `Authenticator.whitelist` renamed to `allowed_users`
#  Default: set()
# c.Authenticator.allowed_users = set()

## The max age (in seconds) of authentication info
#          before forcing a refresh of user auth info.
#  
#          Refreshing auth info allows, e.g. requesting/re-validating auth
#  tokens.
#  
#          See :meth:`.refresh_user` for what happens when user auth info is refreshed
#          (nothing by default).
#  Default: 300
# c.Authenticator.auth_refresh_age = 300

## Automatically begin the login process
#  
#          rather than starting with a "Login with..." link at `/hub/login`
#  
#          To work, `.login_url()` must give a URL other than the default `/hub/login`,
#          such as an oauth handler or another automatic login handler,
#          registered with `.get_handlers()`.
#  
#          .. versionadded:: 0.8
#  Default: False
# c.Authenticator.auto_login = False

## Automatically begin login process for OAuth2 authorization requests
#  
#  When another application is using JupyterHub as OAuth2 provider, it sends
#  users to `/hub/api/oauth2/authorize`. If the user isn't logged in already, and
#  auto_login is not set, the user will be dumped on the hub's home page, without
#  any context on what to do next.
#  
#  Setting this to true will automatically redirect users to login if they aren't
#  logged in *only* on the `/hub/api/oauth2/authorize` endpoint.
#  
#  .. versionadded:: 1.5
#  Default: False
# c.Authenticator.auto_login_oauth2_authorize = False

## Set of usernames that are not allowed to log in.
#  
#  Use this with supported authenticators to restrict which users can not log in.
#  This is an additional block list that further restricts users, beyond whatever
#  restrictions the authenticator has in place.
#  
#  If empty, does not perform any additional restriction.
#  
#  .. versionadded: 0.9
#  
#  .. versionchanged:: 1.2
#      `Authenticator.blacklist` renamed to `blocked_users`
#  Default: set()
# c.Authenticator.blocked_users = set()

## Delete any users from the database that do not pass validation
#  
#          When JupyterHub starts, `.add_user` will be called
#          on each user in the database to verify that all users are still valid.
#  
#          If `delete_invalid_users` is True,
#          any users that do not pass validation will be deleted from the database.
#          Use this if users might be deleted from an external system,
#          such as local user accounts.
#  
#          If False (default), invalid users remain in the Hub's database
#          and a warning will be issued.
#          This is the default to avoid data loss due to config changes.
#  Default: False
# c.Authenticator.delete_invalid_users = False

## Enable persisting auth_state (if available).
#  
#          auth_state will be encrypted and stored in the Hub's database.
#          This can include things like authentication tokens, etc.
#          to be passed to Spawners as environment variables.
#  
#          Encrypting auth_state requires the cryptography package.
#  
#          Additionally, the JUPYTERHUB_CRYPT_KEY environment variable must
#          contain one (or more, separated by ;) 32B encryption keys.
#          These can be either base64 or hex-encoded.
#  
#          If encryption is unavailable, auth_state cannot be persisted.
#  
#          New in JupyterHub 0.8
#  Default: False
# c.Authenticator.enable_auth_state = False

## Let authenticator manage user groups
#  
#          If True, Authenticator.authenticate and/or .refresh_user
#          may return a list of group names in the 'groups' field,
#          which will be assigned to the user.
#  
#          All group-assignment APIs are disabled if this is True.
#  Default: False
# c.Authenticator.manage_groups = False

## An optional hook function that you can implement to do some bootstrapping work
#  during authentication. For example, loading user account details from an
#  external system.
#  
#  This function is called after the user has passed all authentication checks
#  and is ready to successfully authenticate. This function must return the
#  authentication dict reguardless of changes to it.
#  
#  This maybe a coroutine.
#  
#  .. versionadded: 1.0
#  
#  Example::
#  
#      import os, pwd
#      def my_hook(authenticator, handler, authentication):
#          user_data = pwd.getpwnam(authentication['name'])
#          spawn_data = {
#              'pw_data': user_data
#              'gid_list': os.getgrouplist(authentication['name'], user_data.pw_gid)
#          }
#  
#          if authentication['auth_state'] is None:
#              authentication['auth_state'] = {}
#          authentication['auth_state']['spawn_data'] = spawn_data
#  
#          return authentication
#  
#      c.Authenticator.post_auth_hook = my_hook
#  Default: None
# c.Authenticator.post_auth_hook = None

## Force refresh of auth prior to spawn.
#  
#          This forces :meth:`.refresh_user` to be called prior to launching
#          a server, to ensure that auth state is up-to-date.
#  
#          This can be important when e.g. auth tokens that may have expired
#          are passed to the spawner via environment variables from auth_state.
#  
#          If refresh_user cannot refresh the user auth data,
#          launch will fail until the user logs in again.
#  Default: False
# c.Authenticator.refresh_pre_spawn = False

## Dictionary mapping authenticator usernames to JupyterHub users.
#  
#          Primarily used to normalize OAuth user names to local users.
#  Default: {}
# c.Authenticator.username_map = {}

## Regular expression pattern that all valid usernames must match.
#  
#  If a username does not match the pattern specified here, authentication will
#  not be attempted.
#  
#  If not set, allow any username.
#  Default: ''
# c.Authenticator.username_pattern = ''

## Deprecated, use `Authenticator.allowed_users`
#  Default: set()
# c.Authenticator.whitelist = set()

#------------------------------------------------------------------------------
# CryptKeeper(SingletonConfigurable) configuration
#------------------------------------------------------------------------------
## Encapsulate encryption configuration
#  
#      Use via the encryption_config singleton below.

#  Default: []
# c.CryptKeeper.keys = []

## The number of threads to allocate for encryption
#  Default: 2
# c.CryptKeeper.n_threads = 2
