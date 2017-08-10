#! usr/bin/python
# #coding=utf-8
import json
import sys

import time
import requests
from requests.auth import HTTPBasicAuth


class JsonSerializableObj:
    def __init__(self):
        pass

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class JobStep(JsonSerializableObj):
    def __init__(self):
        JsonSerializableObj.__init__(self)

        self.name = None
        self.sequence_id = None
        self.exec_cmd = None
        self.interrupt_cmd = None
        self.exec_start_time = None
        self.exec_end_time = None
        self.exec_wait_time = None
        self.step_status = None
        self.cmd_type = None
        self.info = None
        self.run_async = None

    @staticmethod
    def from_json(json_dict):
        if not json_dict or type(json_dict) != dict: return None

        js = JobStep()

        js.name = json_dict.get('name')
        js.sequence_id = json_dict.get('sequence_id')
        js.exec_cmd = json_dict.get('exec_cmd')
        js.interrupt_cmd = json_dict.get('interrupt_cmd')
        js.exec_start_time = json_dict.get('exec_start_time')
        js.exec_end_time = json_dict.get('exec_end_time')
        js.exec_wait_time = json_dict.get('exec_wait_time')
        js.step_status = json_dict.get('step_status')
        js.cmd_type = json_dict.get('cmd_type')
        js.info = json_dict.get('info')
        js.run_async = json_dict.get('run_async')

        return js


class JobBuildRequest(JsonSerializableObj):
    """
    python class mapping to org.apache.kylin.rest.request.JobBuildRequest
    """

    def __init__(self):
        JsonSerializableObj.__init__(self)

        self.startTime = None
        self.endTime = None
        self.buildType = JobBuildRequest.BUILD

    def __init__(self, a, b, c):
        JsonSerializableObj.__init__(self)

        self.startTime = a
        self.endTime = b
        self.buildType = c


class JobScheduleRequest(JsonSerializableObj):
    def __init__(self):
        JsonSerializableObj.__init__(self)

        self.triggerTime = None
        self.startTime = None
        self.repeatCount = '1'
        self.repeatInterval = '0'
        self.partitionInterval = '10'

    def __init__(self, a, b, c, d, e):
        JsonSerializableObj.__init__(self)
        self.triggerTime = a
        self.startTime = b
        self.repeatCount = c
        self.repeatInterval = d
        self.partitionInterval = e


class JobInstance(JsonSerializableObj):
    def __init__(self):
        JsonSerializableObj.__init__(self)

        self.uuid = None
        self.last_modified = None
        self.name = None
        self.type = None
        self.duration = None
        self.related_cube = None
        self.related_segment = None
        self.exec_start_time = None
        self.exec_end_time = None
        self.mr_waiting = None
        self.steps = None
        self.submitter = None

    @staticmethod
    def from_json(json_dict):
        if not json_dict or type(json_dict) != dict: return None

        ji = JobInstance()

        ji.uuid = json_dict.get('uuid')
        ji.last_modified = json_dict.get('last_modified')
        ji.name = json_dict.get('name')
        ji.type = json_dict.get('type')
        ji.duration = json_dict.get('duration')
        ji.related_cube = json_dict.get('related_cube')
        ji.related_segment = json_dict.get('related_segment')
        ji.exec_start_time = json_dict.get('exec_start_time')
        ji.exec_end_time = json_dict.get('exec_end_time')
        ji.mr_waiting = json_dict.get('mr_waiting')
        # deserialize json for steps
        if json_dict.get('steps') and type(json_dict.get('steps')) == list:
            step_list = json_dict.get('steps')
            ji.steps = [JobStep.from_json(step) for step in step_list]
        ji.submitter = json_dict.get('submitter')

        return ji

    def get_status(self):
        if not self.steps:
            return 'ERROR'

        for job_step in self.steps:
            if job_step.step_status in 'ERROR':
                return 'ERROR'
            if job_step.step_status in 'DISCARD':
                return 'DISCARD'

        # check the last step
        job_step = self.steps[-1]
        if job_step.step_status not in 'FINISHED':
            return 'RUNNING'

        return 'FINISHED'

    def get_current_step(self):
        if not self.steps:
            return 0

        step_id = 1
        for job_step in self.steps:
            if job_step.step_status not in 'FINISHED':
                return step_id
            step_id += 1

        return len(self.steps)


class JobSchedulerInstance(JsonSerializableObj):
    def __init__(self):
        JsonSerializableObj.__init__(self)

        self.name = None
        self.project = None
        self.related_cube = None
        self.partition_start_time = None
        self.scheduled_run_time = None
        self.repeat_count = None
        self.cur_repeat_count = None
        self.repeat_interval = None
        self.partition_interval = None

    @staticmethod
    def from_json(json_dict):
        if not json_dict or type(json_dict) != dict: return None

        ji = JobSchedulerInstance()

        ji.uuid = json_dict.get('name')
        ji.project = json_dict.get('project')
        ji.related_cube = json_dict.get('related_cube')
        ji.partition_start_time = json_dict.get('partition_start_time')
        ji.scheduled_run_time = json_dict.get('scheduled_run_time')
        ji.repeat_count = json_dict.get('repeat_count')
        ji.cur_repeat_count = json_dict.get('cur_repeat_count')
        ji.repeat_interval = json_dict.get('repeat_interval')
        ji.partition_interval = json_dict.get('partition_interval')

        return ji

    def get_status(self):
        if not self.steps:
            return 'ERROR'

        for job_step in self.steps:
            if job_step.step_status in 'ERROR':
                return 'ERROR'
            if job_step.step_status in 'DISCARD':
                return 'DISCARD'

        # check the last step
        job_step = self.steps[-1]
        if job_step.step_status not in 'FINISHED':
            return 'RUNNING'

        return 'FINISHED'

    def get_current_step(self):
        if not self.steps:
            return 0

        step_id = 1
        for job_step in self.steps:
            if job_step.step_status not in 'FINISHED':
                return step_id
            step_id += 1

        return len(self.steps)


class KylinRestApi:
    cookies = None
    host = 'http://localhost'
    port = '7070'
    user = 'ADMIN'
    password = 'KYLIN'
    rest_path_prefix = '/kylin/api'

    def __init__(self):
        if not KylinRestApi.cookies:
            KylinRestApi.cooikes = KylinRestApi.login()

        if not KylinRestApi.cooikes:
            print "can't set cookies, exiting..."
            sys.exit(1)

    def __init__(self, host, port, user, password):
        KylinRestApi.host = host
        KylinRestApi.port = port
        KylinRestApi.user = user
        KylinRestApi.password = password
        if not KylinRestApi.cookies:
            KylinRestApi.cooikes = KylinRestApi.login()

        if not KylinRestApi.cooikes:
            print "can't set cookies, exiting..."
            sys.exit(1)

    @staticmethod
    def is_response_ok(response):
        return response.ok

    @staticmethod
    def get_api_url(uri, query_string):
        return KylinRestApi.host + ':' + str(KylinRestApi.port) + KylinRestApi.rest_path_prefix \
               + '/' + uri + '?' + query_string

    @staticmethod
    def http_get(uri, query_string, headers=None):
        api_url = KylinRestApi.get_api_url(uri, query_string)

        headers = headers if headers and type(headers) == dict else {}
        headers['content-type'] = 'application/json'

        req_response = requests.get(api_url, headers=headers, cookies=KylinRestApi.cooikes)

        return req_response

    @staticmethod
    def http_post(uri, query_string, headers=None, payload=None):
        api_url = KylinRestApi.get_api_url(uri, query_string)

        headers = headers if headers and type(headers) == dict else {}
        headers['content-type'] = 'application/json'

        if payload:
            data = payload if type(payload) == str else json.dumps(payload)
            req_response = requests.post(api_url, data=data, headers=headers, cookies=KylinRestApi.cooikes)
        else:
            req_response = requests.post(api_url, headers=headers, cookies=KylinRestApi.cooikes)

        return req_response

    @staticmethod
    def http_put(uri, query_string, headers=None, payload=None):
        api_url = KylinRestApi.get_api_url(uri, query_string)

        headers = headers if headers and type(headers) == dict else {}
        headers['content-type'] = 'application/json'

        if payload:
            data = payload if type(payload) == str else json.dumps(payload)
            req_response = requests.put(api_url, data=data, headers=headers, cookies=KylinRestApi.cooikes)
        else:
            req_response = requests.put(api_url, headers=headers, cookies=KylinRestApi.cooikes)

        return req_response

    @staticmethod
    def http_delete(uri, query_string, headers=None, payload=None):
        api_url = KylinRestApi.get_api_url(uri, query_string)

        headers = headers if headers and type(headers) == dict else {}
        headers['content-type'] = 'application/json'

        # print payload

        if payload:
            data = payload if type(payload) == str else json.dumps(payload)
            req_response = requests.delete(api_url, data=data, headers=headers, cookies=KylinRestApi.cooikes)
        else:
            req_response = requests.delete(api_url, headers=headers, cookies=KylinRestApi.cooikes)

        # print str(req_response.json())

        return req_response

    @staticmethod
    def login():
        if KylinRestApi.user and KylinRestApi.password:
            # auth and get back cookies
            headers = {"Content-Type": "application/json", "Accept": "application/json, text/javascript, */*; q=0.01"}
            req_response = requests.post(KylinRestApi.get_api_url('user/authentication', ''),
                                         auth=HTTPBasicAuth(KylinRestApi.user, KylinRestApi.password))
            return req_response.cookies

        return None

    @staticmethod
    def rebuild_cube(cube_name, job_build_request):
        job_instance = None

        try:
            response = KylinRestApi.http_put('cubes/' + cube_name + '/rebuild', '',
                                             payload=job_build_request.to_json())

            if KylinRestApi.is_response_ok(response):
                job_instance = JobInstance.from_json(response.json())
            else:
                print response.json()
        except Exception, ex:
            print ex

        return job_instance

    @staticmethod
    def cancel_job(job_id):

        try:
            response = KylinRestApi.http_put('jobs/' + job_id + '/cancel', '', '')

            if KylinRestApi.is_response_ok(response):
                print 'canceled'
            else:
                print response.json()
        except Exception, ex:
            print ex

        return job_instance


if __name__ == '__main__':
    bb = sys.argv
    if bb.__len__() != 8:
        print 'Illegal input arguments!'
        print 'Run with: ' + 'python client.py {host} {port} {user} {password} {cube name} {start time} {end time}'
        exit()

    rest = KylinRestApi(bb[1], bb[2], bb[3], bb[4])
    req = JobBuildRequest(bb[6], bb[7], 'BUILD')

    job_instance = KylinRestApi.rebuild_cube(bb[5], req)

    if job_instance is not None:
        print "Job submitted success"
    else:
        print "Job submitted failed"
