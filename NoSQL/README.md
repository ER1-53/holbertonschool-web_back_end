# NoSQL

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/0HR2bZ3XFJzkttuEVF5Rug" title="NoSQL Databases Explained" target="_blank">NoSQL Databases Explained</a> </li>
<li><a href="/rltoken/JGxz6PJsAN9cjBBT_WVCAg" title="What is NoSQL ?" target="_blank">What is NoSQL ?</a> </li>
<li><a href="/rltoken/PkdXgnfXUfJIk5iqf9Wp4A" title="MongoDB with Python Crash Course - Tutorial for Beginners" target="_blank">MongoDB with Python Crash Course - Tutorial for Beginners</a> </li>
<li><a href="/rltoken/y6ncfHy0Hn7uqaIyitWQRg" title="MongoDB Tutorial 2 : Insert, Update, Remove, Query" target="_blank">MongoDB Tutorial 2 : Insert, Update, Remove, Query</a> </li>
<li><a href="/rltoken/sIORcQADQT2Wf2opdMu30Q" title="Aggregation" target="_blank">Aggregation</a> </li>
<li><a href="/rltoken/BLt93wwWTkVQWVlSDerI1g" title="Introduction to MongoDB and Python" target="_blank">Introduction to MongoDB and Python</a> </li>
<li><a href="/rltoken/q-RfEFpmN-fGiX-SvmQjHA" title="mongo Shell Methods" target="_blank">mongo Shell Methods</a> </li>
<li><a href="/rltoken/fmrWM3wzfC2d2-WHqzzPBQ" title="The mongo Shell" target="_blank">The mongo Shell</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/2Kw4G-iwbeaF3gBMQiUZJg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What NoSQL means</li>
<li>What is difference between SQL and NoSQL</li>
<li>What is ACID</li>
<li>What is a document storage</li>
<li>What are NoSQL types</li>
<li>What are benefits of a NoSQL database</li>
<li>How to query information from a NoSQL database</li>
<li>How to insert/update/delete information from a NoSQL database</li>
<li>How to use MongoDB</li>
</ul>

<h2>Requirements</h2>

<h3>MongoDB Command File</h3>

<ul>
<li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>MongoDB</code> (version 4.2)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be a comment: <code>// my comment</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h3>Python Scripts</h3>

<ul>
<li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7) and <code>PyMongo</code> (version 3.10)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.5.*)</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your functions should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code></li>
<li>Your code should not be executed when imported (by using <code>if __name__ == &quot;__main__&quot;</code>:)</li>
</ul>

<h2>More Info</h2>

<h3>Install MongoDB 4.2 in Ubuntu 18.04</h3>

<p><a href="/rltoken/mchw-5H4h95lL3Au_ETh_Q" title="Official installation guide" target="_blank">Official installation guide</a></p>

<pre><code>$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo &quot;deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse&quot; &gt; /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
...
$  sudo service mongod status
mongod start/running, process 3627
$ mongo --version
MongoDB shell version v4.2.8
git version: 43d25964249164d76d5e04dd6cf38f6111e21f5f
OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
allocator: tcmalloc
modules: none
build environment:
distmod: ubuntu1804
distarch: x86_64
target_arch: x86_64
$
$ pip3 install pymongo
$ python3
&gt;&gt;&gt; import pymongo
&gt;&gt;&gt; pymongo.__version__
&#39;3.10.1&#39;
</code></pre>

<p>Potential issue if documents creation doesn&rsquo;t work or this error: <code>Data directory /data/db not found., terminating</code> (<a href="/rltoken/Mpe5zmt_IlIraIzmQtfAIw" title="source" target="_blank">source</a> and <a href="/rltoken/omWrxp3WcrtN9SL1Mb-MCg" title="source" target="_blank">source</a>)</p>

<pre><code>$ sudo mkdir -p /data/db
</code></pre>

<p>Or if <code>/etc/init.d/mongod</code> is missing, please find here an example of the file:</p>

<details>
<summary>Click to expand/hide file contents</summary>
<pre><code>
#!/bin/sh
### BEGIN INIT INFO
# Provides:          mongod
# Required-Start:    $network $local_fs $remote_fs
# Required-Stop:     $network $local_fs $remote_fs
# Should-Start:      $named
# Should-Stop:
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: An object/document-oriented database
# Description:       MongoDB is a high-performance, open source, schema-free
#                    document-oriented data store that's easy to deploy, manage
#                    and use. It's network accessible, written in C++ and offers
#                    the following features:
#
#                       * Collection oriented storage - easy storage of object-
#                         style data
#                       * Full index support, including on inner objects
#                       * Query profiling
#                       * Replication and fail-over support
#                       * Efficient storage of binary data including large
#                         objects (e.g. videos)
#                       * Automatic partitioning for cloud-level scalability
#
#                    High performance, scalability, and reasonable depth of
#                    functionality are the goals for the project.
### END INIT INFO

PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
DAEMON=/usr/bin/mongod
DESC=database

NAME=mongod
# Defaults.  Can be overridden by the /etc/default/$NAME
# Other configuration options are located in $CONF file. See here for more:
# http://dochub.mongodb.org/core/configurationoptions
CONF=/etc/mongod.conf
PIDFILE=/var/run/$NAME.pid
ENABLE_MONGOD=yes

# Include mongodb defaults if available.
# All variables set before this point can be overridden by users, by
# setting them directly in the defaults file. Use this to explicitly
# override these values, at your own risk.
if [ -f /etc/default/$NAME ] ; then
. /etc/default/$NAME
fi

# Handle NUMA access to CPUs (SERVER-3574)
# This verifies the existence of numactl as well as testing that the command works
NUMACTL_ARGS="--interleave=all"
if which numactl >/dev/null 2>/dev/null && numactl $NUMACTL_ARGS ls / >/dev/null 2>/dev/null
then
NUMACTL="`which numactl` -- $NUMACTL_ARGS"
DAEMON_OPTS=${DAEMON_OPTS:-"--config $CONF"}
else
NUMACTL=""
DAEMON_OPTS="-- "${DAEMON_OPTS:-"--config $CONF"}
fi


if test ! -x $DAEMON; then
echo "Could not find $DAEMON"
exit 0
fi

if test "x$ENABLE_MONGOD" != "xyes"; then
exit 0
fi

. /lib/lsb/init-functions

STARTTIME=1
DIETIME=10                  # Time to wait for the server to die, in seconds
# If this value is set too low you might not
# let some servers to die gracefully and
# 'restart' will not work

DAEMONUSER=${DAEMONUSER:-mongodb}
DAEMONGROUP=${DAEMONGROUP:-mongodb}

set -e

running_pid() {
# Check if a given process pid's cmdline matches a given name
pid=$1
name=$2
[ -z "$pid" ] && return 1
[ ! -d /proc/$pid ] &&  return 1
cmd=`cat /proc/$pid/cmdline | tr "\000" "\n"|head -n 1 |cut -d : -f 1`
# Is this the expected server
[ "$cmd" != "$name" ] &&  return 1
return 0
}

running() {
# Check if the process is running looking at /proc
# (works for all users)

# No pidfile, probably no daemon present
[ ! -f "$PIDFILE" ] && return 1
pid=`cat $PIDFILE`
running_pid $pid $DAEMON || return 1
return 0
}

start_server() {
# Start the process using the wrapper
start-stop-daemon --background --start --quiet --pidfile $PIDFILE \
--make-pidfile --chuid $DAEMONUSER:$DAEMONGROUP \
--exec $NUMACTL $DAEMON $DAEMON_OPTS
errcode=$?
return $errcode
}

stop_server() {
# Stop the process using the wrapper
start-stop-daemon --stop --quiet --pidfile $PIDFILE \
--retry 300 \
--user $DAEMONUSER \
--exec $DAEMON
errcode=$?
return $errcode
}

force_stop() {
# Force the process to die killing it manually
[ ! -e "$PIDFILE" ] && return
if running ; then
kill -15 $pid
# Is it really dead?
sleep "$DIETIME"s
if running ; then
kill -9 $pid
sleep "$DIETIME"s
if running ; then
echo "Cannot kill $NAME (pid=$pid)!"
exit 1
fi
fi
fi
rm -f $PIDFILE
}


case "$1" in
start)
log_daemon_msg "Starting $DESC" "$NAME"
# Check if it's running first
if running ;  then
log_progress_msg "apparently already running"
log_end_msg 0
exit 0
fi
if start_server ; then
# NOTE: Some servers might die some time after they start,
# this code will detect this issue if STARTTIME is set
# to a reasonable value
[ -n "$STARTTIME" ] && sleep $STARTTIME # Wait some time
if  running ;  then
# It's ok, the server started and is running
log_end_msg 0
else
# It is not running after we did start
log_end_msg 1
fi
else
# Either we could not start it
log_end_msg 1
fi
;;
stop)
log_daemon_msg "Stopping $DESC" "$NAME"
if running ; then
# Only stop the server if we see it running
errcode=0
stop_server || errcode=$?
log_end_msg $errcode
else
# If it's not running don't do anything
log_progress_msg "apparently not running"
log_end_msg 0
exit 0
fi
;;
force-stop)
# First try to stop gracefully the program
$0 stop
if running; then
# If it's still running try to kill it more forcefully
log_daemon_msg "Stopping (force) $DESC" "$NAME"
errcode=0
force_stop || errcode=$?
log_end_msg $errcode
fi
;;
restart|force-reload)
log_daemon_msg "Restarting $DESC" "$NAME"
errcode=0
stop_server || errcode=$?
# Wait some sensible amount, some server need this
[ -n "$DIETIME" ] && sleep $DIETIME
start_server || errcode=$?
[ -n "$STARTTIME" ] && sleep $STARTTIME
running || errcode=$?
log_end_msg $errcode
;;
status)

log_daemon_msg "Checking status of $DESC" "$NAME"
if running ;  then
log_progress_msg "running"
log_end_msg 0
else
log_progress_msg "apparently not running"
log_end_msg 1
exit 1
fi
;;
# MongoDB can't reload its configuration.
reload)
log_warning_msg "Reloading $NAME daemon: not implemented, as the daemon"
log_warning_msg "cannot re-read the config file (use restart)."
;;

*)
N=/etc/init.d/$NAME
echo "Usage: $N {start|stop|force-stop|restart|force-reload|status}" >&2
exit 1
;;
esac

exit 0
</code></pre>
</details>

<h3>Use &ldquo;container-on-demand&rdquo; to run MongoDB</h3>

<ul>
<li>Ask for container <code>Ubuntu 18.04 - MongoDB</code></li>
<li>Connect via SSH</li>
<li>Or via the WebTerminal</li>
<li>In the container, you should start MongoDB before playing with it:</li>
</ul>

<pre><code>$ service mongod start
* Starting database mongod                                              [ OK ]
$
$ cat 0-list_databases | mongo
MongoDB shell version v4.2.8
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&amp;gssapiServiceName=mongodb
Implicit session: session { &quot;id&quot; : UUID(&quot;70f14b38-6d0b-48e1-a9a4-0534bcf15301&quot;) }
MongoDB server version: 4.2.8
admin   0.000GB
config  0.000GB
local   0.000GB
bye
$
</code></pre>


<details>
<summary>Click to see: Tasks</summary>

<h3 class="panel-title">
0. List all databases
</h3>

Write a script that lists all databases in MongoDB.</p>

<pre><code>guillaume@ubuntu:~/$ cat 0-list_databases | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
admin        0.000GB
config       0.000GB
local        0.000GB
logs         0.005GB
bye
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>NoSQL</code></li>
<li>File: <code>0-list_databases</code></li>
</ul>
</div>

<h3 class="panel-title">
1. Create a database
</h3>

Write a script that creates or uses the database <code>my_db</code>:</p>

<pre><code>guillaume@ubuntu:~/$ cat 0-list_databases | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
admin        0.000GB
config       0.000GB
local        0.000GB
logs         0.005GB
bye
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ cat 1-use_or_create_database | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db my_db
bye
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>NoSQL</code></li>
<li>File: <code>1-use_or_create_database</code></li>
</ul>
</div>

<h3 class="panel-title">
2. Insert document
</h3>

Write a script that inserts a document in the collection <code>school</code>:</p>

<ul>
<li>The document must have one attribute <code>name</code> with value &ldquo;Holberton school&rdquo;</li>
<li>The database name will be passed as option of <code>mongo</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 2-insert | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
WriteResult({ &quot;nInserted&quot; : 1 })
bye
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>NoSQL</code></li>
<li>File: <code>2-insert</code></li>
</ul>
</div>

<h3 class="panel-title">
3. All documents
</h3>

Write a script that lists all documents in the collection <code>school</code>:</p>

<ul>
<li>The database name will be passed as option of <code>mongo</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 3-all | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ &quot;_id&quot; : ObjectId(&quot;5a8fad532b69437b63252406&quot;), &quot;name&quot; : &quot;Holberton school&quot; }
bye
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>NoSQL</code></li>
<li>File: <code>3-all</code></li>
</ul>
</div>

<h3 class="panel-title">
4. All matches
</h3>

Write a script that lists all documents with <code>name=&quot;Holberton school&quot;</code> in the collection <code>school</code>:</p>

<ul>
<li>The database name will be passed as option of <code>mongo</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 4-match | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ &quot;_id&quot; : ObjectId(&quot;5a8fad532b69437b63252406&quot;), &quot;name&quot; : &quot;Holberton school&quot; }
bye
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>NoSQL</code></li>
<li>File: <code>4-match</code></li>
</ul>
</div>

<h3 class="panel-title">
5. Count
</h3>

Write a script that displays the number of documents in the collection <code>school</code>:</p>

<ul>
<li>The database name will be passed as option of <code>mongo</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 5-count | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
1
bye
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>NoSQL</code></li>
<li>File: <code>5-count</code></li>
</ul>
</div>

<h3 class="panel-title">
6. Update
</h3>

Write a script that adds a new attribute to a document in the collection <code>school</code>:</p>

<ul>
<li>The script should update only document with <code>name=&quot;Holberton school&quot;</code> (all of them)</li>
<li>The update should add the attribute <code>address</code> with the value &ldquo;972 Mission street&rdquo;</li>
<li>The database name will be passed as option of <code>mongo</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 6-update | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
WriteResult({ &quot;nMatched&quot; : 1, &quot;nUpserted&quot; : 0, &quot;nModified&quot; : 1 })
bye
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ cat 4-match | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ &quot;_id&quot; : ObjectId(&quot;5a8fad532b69437b63252406&quot;), &quot;name&quot; : &quot;Holberton school&quot;, &quot;address&quot; : &quot;972 Mission street&quot; }
bye
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>NoSQL</code></li>
<li>File: <code>6-update</code></li>
</ul>
</div>

<h3 class="panel-title">
7. Delete by match
</h3>

Write a script that deletes all documents with <code>name=&quot;Holberton school&quot;</code> in the collection <code>school</code>:</p>

<ul>
<li>The database name will be passed as option of <code>mongo</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 7-delete | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ &quot;acknowledged&quot; : true, &quot;deletedCount&quot; : 1 }
bye
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ cat 4-match | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
bye
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>NoSQL</code></li>
<li>File: <code>7-delete</code></li>
</ul>
</div>

<h3 class="panel-title">
8. List all documents in Python
</h3>

Write a Python function that lists all documents in a collection:</p>

<ul>
<li>Prototype: <code>def list_all(mongo_collection):</code></li>
<li>Return an empty list if no document in the collection</li>
<li><code>mongo_collection</code> will be the <code>pymongo</code> collection object</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/env python3
&quot;&quot;&quot; 8-main &quot;&quot;&quot;
from pymongo import MongoClient
list_all = __import__(&#39;8-all&#39;).list_all

if __name__ == &quot;__main__&quot;:
client = MongoClient(&#39;mongodb://127.0.0.1:27017&#39;)
school_collection = client.my_db.school
schools = list_all(school_collection)
for school in schools:
print(&quot;[{}] {}&quot;.format(school.get(&#39;_id&#39;), school.get(&#39;name&#39;)))

guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ ./8-main.py
[5a8f60cfd4321e1403ba7ab9] Holberton school
[5a8f60cfd4321e1403ba7aba] UCSD
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>NoSQL</code></li>
<li>File: <code>8-all.py</code></li>
</ul>
</div>

<h3 class="panel-title">
9. Insert a document in Python
</h3>

Write a Python function that inserts a new document in a collection based on <code>kwargs</code>:</p>

<ul>
<li>Prototype: <code>def insert_school(mongo_collection, **kwargs):</code></li>
<li><code>mongo_collection</code> will be the <code>pymongo</code> collection object</li>
<li>Returns the new <code>_id</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 9-main.py
#!/usr/bin/env python3
&quot;&quot;&quot; 9-main &quot;&quot;&quot;
from pymongo import MongoClient
list_all = __import__(&#39;8-all&#39;).list_all
insert_school = __import__(&#39;9-insert_school&#39;).insert_school

if __name__ == &quot;__main__&quot;:
client = MongoClient(&#39;mongodb://127.0.0.1:27017&#39;)
school_collection = client.my_db.school
new_school_id = insert_school(school_collection, name=&quot;UCSF&quot;, address=&quot;505 Parnassus Ave&quot;)
print(&quot;New school created: {}&quot;.format(new_school_id))

schools = list_all(school_collection)
for school in schools:
print(&quot;[{}] {} {}&quot;.format(school.get(&#39;_id&#39;), school.get(&#39;name&#39;), school.get(&#39;address&#39;, &quot;&quot;)))

guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ ./9-main.py
New school created: 5a8f60cfd4321e1403ba7abb
[5a8f60cfd4321e1403ba7ab9] Holberton school
[5a8f60cfd4321e1403ba7aba] UCSD
[5a8f60cfd4321e1403ba7abb] UCSF 505 Parnassus Ave
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>NoSQL</code></li>
<li>File: <code>9-insert_school.py</code></li>
</ul>
</div>

<h3 class="panel-title">
10. Change school topics
</h3>

Write a Python function that changes all topics of a school document based on the name:</p>

<ul>
<li>Prototype: <code>def update_topics(mongo_collection, name, topics):</code></li>
<li><code>mongo_collection</code> will be the <code>pymongo</code> collection object</li>
<li><code>name</code> (string) will be the school name to update</li>
<li><code>topics</code> (list of strings) will be the list of topics approached in the school</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 10-main.py
#!/usr/bin/env python3
&quot;&quot;&quot; 10-main &quot;&quot;&quot;
from pymongo import MongoClient
list_all = __import__(&#39;8-all&#39;).list_all
update_topics = __import__(&#39;10-update_topics&#39;).update_topics

if __name__ == &quot;__main__&quot;:
client = MongoClient(&#39;mongodb://127.0.0.1:27017&#39;)
school_collection = client.my_db.school
update_topics(school_collection, &quot;Holberton school&quot;, [&quot;Sys admin&quot;, &quot;AI&quot;, &quot;Algorithm&quot;])

schools = list_all(school_collection)
for school in schools:
print(&quot;[{}] {} {}&quot;.format(school.get(&#39;_id&#39;), school.get(&#39;name&#39;), school.get(&#39;topics&#39;, &quot;&quot;)))

update_topics(school_collection, &quot;Holberton school&quot;, [&quot;iOS&quot;])

schools = list_all(school_collection)
for school in schools:
print(&quot;[{}] {} {}&quot;.format(school.get(&#39;_id&#39;), school.get(&#39;name&#39;), school.get(&#39;topics&#39;, &quot;&quot;)))

guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ ./10-main.py
[5a8f60cfd4321e1403ba7abb] UCSF
[5a8f60cfd4321e1403ba7aba] UCSD
[5a8f60cfd4321e1403ba7ab9] Holberton school [&#39;Sys admin&#39;, &#39;AI&#39;, &#39;Algorithm&#39;]
[5a8f60cfd4321e1403ba7abb] UCSF
[5a8f60cfd4321e1403ba7aba] UCSD
[5a8f60cfd4321e1403ba7ab9] Holberton school [&#39;iOS&#39;]
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>NoSQL</code></li>
<li>File: <code>10-update_topics.py</code></li>
</ul>
</div>

<h3 class="panel-title">
11. Where can I learn Python?
</h3>

Write a Python function that returns the list of school having a specific topic:</p>

<ul>
<li>Prototype: <code>def schools_by_topic(mongo_collection, topic):</code></li>
<li><code>mongo_collection</code> will be the <code>pymongo</code> collection object</li>
<li><code>topic</code> (string) will be topic searched</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 11-main.py
#!/usr/bin/env python3
&quot;&quot;&quot; 11-main &quot;&quot;&quot;
from pymongo import MongoClient
list_all = __import__(&#39;8-all&#39;).list_all
insert_school = __import__(&#39;9-insert_school&#39;).insert_school
schools_by_topic = __import__(&#39;11-schools_by_topic&#39;).schools_by_topic

if __name__ == &quot;__main__&quot;:
client = MongoClient(&#39;mongodb://127.0.0.1:27017&#39;)
school_collection = client.my_db.school

j_schools = [
{ &#39;name&#39;: &quot;Holberton school&quot;, &#39;topics&#39;: [&quot;Algo&quot;, &quot;C&quot;, &quot;Python&quot;, &quot;React&quot;]},
{ &#39;name&#39;: &quot;UCSF&quot;, &#39;topics&#39;: [&quot;Algo&quot;, &quot;MongoDB&quot;]},
{ &#39;name&#39;: &quot;UCLA&quot;, &#39;topics&#39;: [&quot;C&quot;, &quot;Python&quot;]},
{ &#39;name&#39;: &quot;UCSD&quot;, &#39;topics&#39;: [&quot;Cassandra&quot;]},
{ &#39;name&#39;: &quot;Stanford&quot;, &#39;topics&#39;: [&quot;C&quot;, &quot;React&quot;, &quot;Javascript&quot;]}
]
for j_school in j_schools:
insert_school(school_collection, **j_school)

schools = schools_by_topic(school_collection, &quot;Python&quot;)
for school in schools:
print(&quot;[{}] {} {}&quot;.format(school.get(&#39;_id&#39;), school.get(&#39;name&#39;), school.get(&#39;topics&#39;, &quot;&quot;)))

guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ ./11-main.py
[5a90731fd4321e1e5a3f53e3] Holberton school [&#39;Algo&#39;, &#39;C&#39;, &#39;Python&#39;, &#39;React&#39;]
[5a90731fd4321e1e5a3f53e5] UCLA [&#39;C&#39;, &#39;Python&#39;]
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>NoSQL</code></li>
<li>File: <code>11-schools_by_topic.py</code></li>
</ul>
</div>

<h3 class="panel-title">
12. Log stats
</h3>

Write a Python script that provides some stats about Nginx logs stored in MongoDB:</p>

<ul>
<li>Database: <code>logs</code></li>
<li>Collection: <code>nginx</code></li>
<li>Display (same as the example):

<ul>
<li>first line: <code>x logs</code> where <code>x</code> is the number of documents in this collection</li>
<li>second line: <code>Methods:</code></li>
<li>5 lines with the number of documents with the <code>method</code> = <code>[&quot;GET&quot;, &quot;POST&quot;, &quot;PUT&quot;, &quot;PATCH&quot;, &quot;DELETE&quot;]</code> in this order (see example below - warning: it&rsquo;s a tabulation before each line) </li>
<li>one line with the number of documents with:

<ul>
<li><code>method=GET</code></li>
<li><code>path=/status</code></li>
</ul></li>
</ul></li>
</ul>

<p>You can use this dump as data sample: <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/6/645541f867bb79ae47b7a80922e9a48604a569b9.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240108%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240108T081043Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=dd684bf25184deab91fb789868d84727d24eda461f24ad84903f6216a745b067" title="dump.zip" target="_blank">dump.zip</a> </p>

<p>The output of your script <strong>must be exactly the same as the example</strong></p>

<pre><code>guillaume@ubuntu:~/$ curl -o dump.zip -s &quot;https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-webstack/411/dump.zip&quot;
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ unzip dump.zip
Archive:  dump.zip
creating: dump/
creating: dump/logs/
inflating: dump/logs/nginx.metadata.json
inflating: dump/logs/nginx.bson
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ mongorestore dump
2018-02-23T20:12:37.807+0000    preparing collections to restore from
2018-02-23T20:12:37.816+0000    reading metadata for logs.nginx from dump/logs/nginx.metadata.json
2018-02-23T20:12:37.825+0000    restoring logs.nginx from dump/logs/nginx.bson
2018-02-23T20:12:40.804+0000    [##......................]  logs.nginx  1.21MB/13.4MB  (9.0%)
2018-02-23T20:12:43.803+0000    [#####...................]  logs.nginx  2.88MB/13.4MB  (21.4%)
2018-02-23T20:12:46.803+0000    [#######.................]  logs.nginx  4.22MB/13.4MB  (31.4%)
2018-02-23T20:12:49.803+0000    [##########..............]  logs.nginx  5.73MB/13.4MB  (42.7%)
2018-02-23T20:12:52.803+0000    [############............]  logs.nginx  7.23MB/13.4MB  (53.8%)
2018-02-23T20:12:55.803+0000    [###############.........]  logs.nginx  8.53MB/13.4MB  (63.5%)
2018-02-23T20:12:58.803+0000    [#################.......]  logs.nginx  10.1MB/13.4MB  (74.9%)
2018-02-23T20:13:01.803+0000    [####################....]  logs.nginx  11.3MB/13.4MB  (83.9%)
2018-02-23T20:13:04.803+0000    [######################..]  logs.nginx  12.8MB/13.4MB  (94.9%)
2018-02-23T20:13:06.228+0000    [########################]  logs.nginx  13.4MB/13.4MB  (100.0%)
2018-02-23T20:13:06.230+0000    no indexes to restore
2018-02-23T20:13:06.231+0000    finished restoring logs.nginx (94778 documents)
2018-02-23T20:13:06.232+0000    done
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ ./12-log_stats.py
94778 logs
Methods:
method GET: 93842
method POST: 229
method PUT: 0
method PATCH: 0
method DELETE: 0
47415 status check
guillaume@ubuntu:~/$
</code></pre>

</div>

<div class="list-group">
<!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
<li>Directory: <code>NoSQL</code></li>
<li>File: <code>12-log_stats.py</code></li>
</ul>
</div>

</details>
