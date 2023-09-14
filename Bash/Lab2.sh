~
#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
NEGATIVE=$(echo $DATA | jq '.[0].negative')
PENDING=$(echo $DATA | jq '.[0].pending')
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalized')
DEATH=$(echo $DATA | jq '.[0].death')
echo "On $TODAY, there were $POSITIVE positive COVID cases and $NEGATIVE negative COVID cases. There are also $PENDING pending tests. Currently the hospitals report a total number of $HOSPITALIZED admitted patients, of which $DEATH were reported deceased."
