#!/usr/bin/env python
#-*-*- encoding: utf-8 -*-*-
#
# Copyright (C) 2012 onwards University of Deusto
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#
# This software consists of contributions made by many individuals,
# listed below:
#
# Author: Luis Rodriguez Gil <luis.rodriguezgil@deusto.es>
#
from flask import make_response, request
from weblab.core.wl import weblab_api

import uuid
import json
import requests

# # PROTOCOL
#
# ## ACTION: Create a new job
# METHOD: POST to /compiserv/queue/armc
# PARAMETERS: Can receive the file as a multipart file, or as raw data.
#
# RETURNS:
# A JSON object:
# { result: <result>, // <result> is 'accepted' or 'denied'
#   uid: <uid>, // only if result is 'accepted'
# }
#
#
# ## ACTION: Check the state of a job
# METHOD: GET to /compiserv/queue/<uid>
# PARAMETERS: The <uid>
#
# RETURNS:
# A JSON object:
# { state: <state>, // <state> is 'finished' if the task is done or failed, 'unfinished' if it is reportedly in progress or
#                      in queue, and 'not_found' if it could not be found.
#
# }
#

JOBS = {}
BASE_URL = "http://llcompilerservice.azurewebsites.net/CompilerGeneratorService.svc"
POST_URL = BASE_URL + "/PutCompilerTask/uvision"
GET_URL = BASE_URL + "/GetCompilerTask/uvision/{0}/{1}"


@weblab_api.route_web('/compiserv/')
def compiserve():
    msg = "Welcome to the Compiler Service. This is not yet implemented."
    data = {"msg": msg}
    contents = json.dumps(data, indent = 4)
    response = make_response(contents)
    response.content_type = 'application/json'
    return response


@weblab_api.route_web('/compiserv/queue/armc', methods=["POST"])
def compiserve_queue_armc_post():
    """
    Enqueues an ARMC synthesization job. This can be done by any client.
    :return:
    """

    response = {
        "result": ""  # accepted or denied
    }

    file_contents = None

    if request.data is not None:
        file_contents = request.data
    elif request.files is not None and len(request.files) > 0:
        file_contents = request.files['file']
        # TO-DO

    if file_contents is None:
        response['result'] = 'denied'
        response['reason'] = 'no_file_sent'

    else:
        # Send to AZURE SERVICE
        resp = requests.post(POST_URL, file_contents)
        json_resp = resp.json()
        generated_date = json_resp["GeneratedDate"]
        id = json_resp["ID"]
        token = json_resp["TokenID"]

        response['result'] = 'accepted'
        uid = "{0}+{1}".format(id, token)
        response['uid'] = uid

        # Store the JOB in the queue.
        JOBS[uid] = {'state': 'queued'}

    contents = json.dumps(response, indent=4)
    response = make_response(contents)
    response.content_type = 'application/json'
    return response


@weblab_api.route_web('/compiserv/queue/<uid>', methods=["GET"])
def compiserve_queue_get(uid):
    """
    Enquiries about the status of a specific job. This can be done by any client.
    :return:
    """

    result = {
        "state": ""
    }

    if uid not in JOBS:
        result['state'] = 'not_found'

    job = JOBS[uid]

    # Split the UID into its components.
    id, tokenid = uid.split("+", 1)

    # Retrieve the state of the remote JOB
    resp = requests.get(GET_URL.format(id, tokenid))
    jsresp = resp.json()

    # BinaryFile, CompletedDate, LogFile, State
    state = jsresp['State'].lower()

    if state == 'finished':
        binary_file = jsresp['BinaryFile']
        completed_date = jsresp['CompletedDate']
        log_file = jsresp['LogFile']

        # Store the files internally. TODO: DO THIS PROPERLY. For now we store them in memory.
        job["binary_file"] = binary_file
        job["completed_date"] = completed_date
        job["log_file"] = log_file

        result['state'] = 'done'

    elif state.startswith('unfinished'):
        splits = state.split(":")
        number = int(splits[1].strip())
        result['state'] = 'queued'
        result['position'] = number

    # TODO: How are failures reported?

    else:
        raise Exception("Unrecognized job state: " + state)

    contents = json.dumps(result, indent=4)
    response = make_response(contents)
    response.content_type = 'application/json'
    return response


@weblab_api.route_web('/compiserv/result/<uid>/outputfile', methods=["GET"])
def compiserve_result_outputfile(uid):
    """
    Requests the result (outputfile) of a job. This is only to be called INTERNALLY by the Experiment Servers
    and is protected by a token.
    :return:
    """

    if uid not in JOBS:
        result = {
            'result': 'error',
            'msg': "job not found"
        }
        result = json.dumps(result, indent=4)
        response = make_response(result)
        response.headers["Content-Type"] = "application/json"
        return response

    # Find the job
    job = JOBS[uid]

    if "binary_file" in job:  # TODO: IF FILE IS INDEED READY
        file_contents = job["binary_file"]
        response = make_response(file_contents)
        response.headers["Content-Disposition"] = "attachment; filename=result.bin"
        response.headers["Content-Type"] = "application/octet-stream"
    else:  #
        result = {
            'result': 'error',
            'msg': 'result not found'
        }
        result = json.dumps(result, indent=4)
        response = make_response(result)
        response.headers["Content-Type"] = "application/json"

    return response

@weblab_api.route_web('/compiserv/result/<uid>/logfile', methods=["GET"])
def compiserve_result_logfile(uid):
    """
    Requests the result (logfile) of a job. This is only to be called INTERNALLY by the Experiment Servers
    and is protected by a token.
    :param uid:
    :return:
    """

    if uid not in JOBS:
        result = {
            'result': 'error',
            'msg': "job not found"
        }
        result = json.dumps(result, indent=4)
        response = make_response(result)
        response.headers["Content-Type"] = "application/json"
        return response

    # Find the job
    job = JOBS[uid]

    if "log_file" in job:  # TODO: IF FILE IS INDEED READY
        # TODO: Check the state of the job. Do not assume it is finished.
        file_contents = job["log_file"]
        response = make_response(file_contents)
        response.headers["Content-Disposition"] = "attachment; filename=logfile.bin"
        response.headers["Content-Type"] = "application/octet-stream"
    else:  #
        result = {
            'result': 'error',
            'msg': 'result not found'
        }
        result = json.dumps(result, indent=4)
        response = make_response(result)
        response.headers["Content-Type"] = "application/json"

    return response
