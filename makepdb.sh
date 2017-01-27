#!/bin/bash
FILES=domain_files/*
for f in $FILES
do
mv -- "$f" "${f%.ent.text}.pdb"
done
