#!/bin/bash

python server.py &

python server.py -p 11111 &

python server.py -p 12389 &
python server.py -p 12287 &
python server.py -p 12346 &
python server.py -p 12347 &
python server.py -p 14431 &

