# Copyright 2020 Google, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START cloudrun_helloworld_service]
# [START run_helloworld_service]
import os
from langchain_community.document_loaders import UnstructuredFileLoader

from flask import Flask, request
app = Flask(__name__)

headers = {
    'Access-Control-Allow-Methods': 'POST'
}


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    try:
        #  More about this function: https://python.langchain.com/docs/integrations/document_loaders/unstructured_file
        loader = UnstructuredFileLoader("./test.txt")
        documents = loader.load()
        print(f"📂 documents = {documents}")
    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}, 500, headers

    return {"metadata": documents[0].metadata, "pageContent": documents[0].pageContent}, 200, headers


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
# [END run_helloworld_service]
# [END cloudrun_helloworld_service]
