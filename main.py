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
from langchain.document_loaders import S3FileLoader

import os

from flask import Flask, request
app = Flask(__name__)

headers = {
    'Access-Control-Allow-Methods': 'POST',
    'Content-Type': 'application/json'
}
@app.route("/", methods=['GET', 'POST'])
def hello_world():
    """Example Hello World route."""
    data = request.get_json(silent=True) or request.args

    if not data:
        print("❗️ Missing parameters")
        return 'Error: Missing parameters', 400
    
    required_fields = ['file_key', 'bucket']

    for field in required_fields:
        if not data.get(field) or not isinstance(data[field], (str)):
            print(f"❗️ Missing/Invalid {field} parameter")
            return f'Error: Missing/Invalid parameter', 400

    file_key = data['file_key']
    bucket = data['bucket']
    

    print(
        {
            "🪣 bucket": bucket,
            "📁 file_key": file_key,
        }
    )

    return get_document(file_key, bucket)

def get_document(file_key, bucket):
    print("📂 Loading document from S3")
    try:
        loader = S3FileLoader(bucket, file_key)
        documents = loader.load()
    except Exception as e:
        print(f"An error occurred loading S3 document: {e}")
        return {"error": str(e)}, 500, headers
    return {"metadata": documents[0].metadata, "pageContent": documents[0].pageContent}, 200, headers


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
# [END run_helloworld_service]
# [END cloudrun_helloworld_service]