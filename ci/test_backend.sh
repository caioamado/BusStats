#!/bin/bash
export COMPOSE_PROJECT_NAME=BusStats_${CI_COMMIT_SHA}
docker-compose -f docker/compose/test.yml run BusStats unittests.sh
exitcode=$?
docker-compose -f docker/compose/test.yml down
exit $exitcode
