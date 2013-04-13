# flajt

Work in progress renderer/viewer of data from the [FlySight GPS](http://www.flysight.ca/).

To use it simply

    $ flajt --data <flysight data directory>

Then point your web browser to [http://localhost:8000/](http://localhost:8000/) (default).

# Work in progress screenshot

![Screenshot](https://raw.github.com/bjornedstrom/flajt/master/doc/shot.jpg "Screenshot")

# Security Warning

Because of ease of development, this program will fire up a local web
server. There are important security considerations of this design. By default, the web server will only accept connections from localhost. Do not change this! The program can read arbitrary files on disk.

# About & License

This software is written by Björn Edström 2013. See LICENSE for details.

This project uses the Google Maps Javascript API, jQuery (MIT License) and Mustache (MIT License).
