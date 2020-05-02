# darknet2onnx
将常见的darknet模型转成通用的ONNX格式, 以方便后续转TensorRT进行加速.

> NVIDIA官方给的脚本是Python2的, 不支持Python3. 我把代码修改成支持Python3. onnx的版本必须是1.4.1, 其他的会有问题.

主要转了3个模型:

- yolov3: 没有maxpool操作

- yolov3-tiny: 有maxpool操作

- platedetection: 有maxpool操作

生成onnx模型文件:

- python3 -B yolov3\_onnx.py

- python3 -B yolov3tiny\_onnx.py

- python3 -B platedetection\_onnx.py

由于yolov3.weights文件很大, github不支持上传. 有需要的可自行前往[darknet官网](https://pjreddie.com/media/files/yolov3.weights)下载.

onnx\_inference.py 文件是直接对onnx文件进行推理.

onnx2trt\_yolov3tiny.py 文件是将yolov3-tiny网络的onnx文件转成trt文件并进行推理加速. 我在Jetson Tx2平台上是测试成功的.
