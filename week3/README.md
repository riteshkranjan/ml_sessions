# Launch server
* pip install -r requirement.txt
* python app.py


# To use sqlite database instead of postgre
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.sqlite3'

## Create virtual environment for python
* pip install virtualenv
* python -m virtualenv env
* source env/bin/activate  (.\env\Scripts\activate for windows)
* deactivate


## Create virtual environment in anaconda
* conda create -n env python=x.x anaconda
* source activate env
* source deactivate


# deploy in apache
* login to virtualenv 
* set MOD_WSGI_APACHE_ROOTDIR=D:\Apache24
* pip install mod_wsgi  (if some apache's .h libraries are missing copy manually to apache include folder)
* mod_wsgi-express module-config
* it will print 3 lines (LoadFile, load module and wsgipythonhome) copy all the lines and copy at the end of apache httpd file as it is. 

```
LoadFile "C:/Program Files/Python36/python36.dll"   
LoadModule wsgi_module "d:/workspace_python/machine_learning_sessions/week3/env/lib/site-packages/mod_wsgi/server/mod_wsgi.cp36-win_amd64.pyd"   
WSGIPythonHome "d:/workspace_python/machine_learning_sessions/week3/env"
```
* Finally add below entry for virtual host 
```
<VirtualHost *>    
        ServerName example.com       
        WSGIScriptAlias / D:\workspace_python\machine_learning_sessions\week3\web.wsgi      
        <Directory D:\workspace_python\machine_learning_sessions\week3>      
            Require all granted     
        </Directory>     
</VirtualHost>     
```

# Some basic postgre commands
```
login to postgre console using : psql -U postgres
list all dbs : \l 
create database <dbname>;
connect to a db : \c <db name>  
show tables : \td
select * from <tablename>;
quit : \q

```