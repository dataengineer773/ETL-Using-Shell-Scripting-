# Extracting data using 'cut' command
# The filter command cut helps us extract selected characters or fields from a line of text.
# Extracting characters, The command below shows how to extract the first four characters:
echo "database" | cut -c1-4


# The command below shows how to extract 5th to 8th characters :
echo "database" | cut -c5-8

# The command below shows how to extract the 1st and 5th characters:
echo "database" | cut -c1,5

# Extracting fields/columns :
# We can extract a specific column/field from a delimited text file, by mentioning
# the delimiter using the -d option, or
# the field number using the -f option.
# The /etc/passwd is a “:” delimited file.
# The command below extracts usernames (the first field) from /etc/passwd:
cut -d":" -f1 /etc/passwd

# The command below extracts multiple fields 1st, 3rd, and 6th (username, userid, and home directory) from /etc/passwd:
cut -d":" -f1,3,6 /etc/passwd

# The command below extracts a range of fields 3rd to 6th (userid, groupid, user description and home directory) from /etc/passwd:
cut -d":" -f3-6 /etc/passwd

# Transforming data using 'tr' :
# tr is a filter command used to translate, squeeze, and/or delete characters.
# Translate from one character set to another
# The command below translates all lower case alphabets to upper case:
echo "Shell Scripting" | tr "[a-z]" "[A-Z]"

# You could also use the pre-defined character sets also for this purpose:
echo "Shell Scripting" | tr "[:lower:]" "[:upper:]"

# The command below translates all upper case alphabets to lower case:
echo "Shell Scripting" | tr  "[A-Z]" "[a-z]"

# Squeeze repeating occurrences of characters
# The -s option replaces a sequence of a repeated characters with a single occurrence of that character.
# The command below replaces repeat occurrences of ‘space’ in the output of ps command with one ‘space’.:
ps | tr -s " "

# In the above example, the space character within quotes can be replaced with the following : "[\:space\:]".
# Delete characters
# We can delete specified characters using the -d  option.
# The command below deletes all digi :
echo "My login pin is 5634" | tr -d "[:digit:]"

#  Create a table In PostgraSQL:
# The table users will have the following columns:
# uname
# uid
# home
# You will connect to template1 database which is already available by default. To connect to this database, run the following command at the ‘postgres=#’ :
\c template1


# Run the following statement at the ‘template1=#’ prompt to create the table:
create table users(username varchar(50),userid int,homedirectory varchar(100));


# save the code for script and extract and transform and load in the csv file :
# Run the script:
bash csv2db.sh

# Verify that the output contains the three fields, that you extracted.
# Change the script to redirect the extracted data into a file named extracted-data.txt
# Replace the cut command at end of the script with the following command:
cut -d":" -f1,3,6 /etc/passwd > extracted-data.txt


# Run the script :
bash csv2db.sh

# Run the command below to verify that the file extracted-data.txt is created, and has the conten:
cat extracted-data.txt

# Run the script :
bash csv2db.sh

# Run the command below to verify that the file transformed-data.csv is created, and has the content :
cat transformed-data.csv

# To load data from a shell script, you will use the psql client utility in a non-interactive manner. This is done by sending the database commands through a command # pipeline to psql with the help of echo command.
# PostgreSQL command to copy data from a CSV file to a table is COPY:
# Run the script :
bash csv2db.sh


# Go to Postgres SQL CLI that you used in the Run the command below to verify that the table users is populated with the data:
echo '\c template1; \\SELECT * from users;' | psql --username=postgres --host=localhost
