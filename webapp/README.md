PHP website that allows researchers to view their publications, citations and other metrics. Researchers login with their unique researcher ID and a password is given at the setup phase to allow people to login.

# Views

* Index Page, which is also the login page
* Researchers page, where users can see their papers. Researchers can verify that their  that are correct.

# Setup

* Set the ```DOCUMENT_ROOT``` of the Apache server to the ```public_html/``` directory, and make sure PHP is enabled. 
* Setup the MySQL database required by running the commands in ```private/db/db_setup.sql``` in the MySQL terminal. Also, edit the file ```private/db/config_demo.ini``` - add the host, username, server password, and database name. (leave database name set to default). Once you're done editing rename the file to ```config.ini```.

# Features to Add

1. **Duplicate Papers View**: Users can see potential duplicate papers and be able to merge the papers.