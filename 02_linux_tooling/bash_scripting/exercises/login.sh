#!/bin/bash

case ${1,,} in
	herbert | administrator)
		echo "Hello, you're the boss here!"
		;;
	hel)
		echo "Just enter your username!"
		;;
	*)
		echo "Hello there, you're not the boss of me. Enter a valid username!"
esac
