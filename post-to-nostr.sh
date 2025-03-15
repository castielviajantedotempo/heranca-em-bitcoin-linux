#!/bin/bash

export GOROOT=/usr/local/go/bin
export GOPATH=$HOME/go

$GOPATH/bin/noscl publish "$1"
