# 神经网络产品工作流

本文主要记载，对于一个基于神经网络模型的产品，它在研发阶段的工作流程应该是怎么样的。大致的流程简化成下面的样子。

__产品端__ -----(图片/视频流地址)-----> __模型端__ -----(模型推理结果)-----> __产品端__

由此我们可以概括出两个部分需要实现的功能。

### 功能描述
__1. 产品端__
发布接口，主要包括图片/视频流地址，模型参数。

回调接口，接受模型的推理结果，然后再反馈给具体的任务端。

__2. 模型端__
接受到产品端的发布接口，开始进行模型推理。然后根据回调接口返回结果。

### 实现流程
- __模型封装__
方法1： `uvicorn server:app --reload`
server.py，app是fastapi对象
方法2： `python server.py`
server.py运行一个while True
```python
task_info_url = "http://192.168.xx.xx:8000/mock"
response = requests.get(task_info_url)
response_json = json.loads(response.content) # 将字节数据解析为字典或者列表
data = response_json.get("data", {})
run(task_info=data) # while true循环
```

- __构造视频流__
`mediamtx` : 启动流服务的平台MediaMTX。
在我们的任务中，它将ffempeg转换的流发布为可访问的 RTSP 服务，支持多人访问/协议转换。使用方法：`mediamtx`
`ffmpeg-builds`: 作者创建了一个工作流，每天自动编译ffmpeg的各种版本形成可执行文件。这样就能直接使用
在我们的任务中，它将视频转换为一个循环播放的rtsp流，从而模拟真实的摄像头。使用方法：
```bash
.\ffmpeg.exe -re -stream_loop -1 -i .\v_HangingBox_g01_c0006.mp4 -c copy -f rtsp rtsp://127.0.0.1:8554/stream
```


- __客户端封装__
```python
app = FastAPI()
@app.get("/mock")   # 模拟任务信息，主要是提供视频流地址
@app.post("/callback")  # 回调接口，用于接收模型结果
uvicorn.run(app, host="0.0.0.0", port=8000)
```


- __大致流程__
总的来说，首先我们通过ffmpeg、mediatx将视频流转换为可访问的RTSP服务。然后启动客户端，服务端。服务端首先向/mock接口请求任务信息，然后启动模型推理。然后通过/callback接口将模型结果返回给服务端。最后，客户端进行后续处理，例如显示图片/打印结果等。
