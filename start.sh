#!/bin/bash -e

function cleanup {
	echo "Fechando o programa."
	pkill -f "python3 serve.py"
	pkill -f "python3 update.py"
}

trap cleanup EXIT
python3 serve.py &
python3 update.py &
tail -f /dev/null
