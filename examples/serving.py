# coding=utf-8
# Copyright 2023  The AIWaves Inc. team.

#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
example code for serving an autonomous agents with Flask/FastAPI backend
"""

from flask import Flask,request
from gevent import pywsgi
<<<<<<< HEAD
import sys
sys.path.append("/home/aiwaves/longli/agents/src/agents")
from sop import SOP
from agent import Agent
=======
from src.agents.sop import SOP
from src.agents.agent import Agent

>>>>>>> 6630d40fb43c2d4e5e5e021b943c0668ed10fa3b
if __name__ == "__name__":
    app = Flask(__name__)
    sop = SOP("customer_service.json")
    agent = Agent(sop.get_root())
    @app.route('/api/v1/ask/',methods=['post'])
    def reply():
        query = request.json.get('query')
        response = agent.reply(query)
        return response
    app.run(debug=True,host='0.0.0.0', port=7820)
    server = pywsgi.WSGIServer(('0.0.0.0', 7820), app)
    server.serve_forever()