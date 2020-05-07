# darknet2onnx
将常见的darknet模型转成通用的ONNX格式, 以方便后续转TensorRT进行加速.

> NVIDIA官方给的脚本是Python2的, 不支持Python3. 我把代码修改成支持Python3. onnx的版本必须是1.4.1, 其他的会有问题.

主要转了3个模型:

- yolov3: 主要操作有convolutional、shortcut、route、upsample;

- yolov3-tiny: 主要操作有convolutional、shortcut、route、upsample、maxpool;

- platedetection(yolo-dense): 主要操作有convolutional、shortcut、route、upsample、maxpool;

yolo-dense的输入大小是(325, 325), 标准的应该是(320, 320). 这么做的主要原因是当时在将darknet成TensorFlow pb文件的时候发现当padding为奇数时,
比如说padding为5, TensorFlow的做法是左边2, 右边3; 而darknet的做法是左边3, 右边2. 所以当时做了个简单处理, 先手动按照TensorFlow的padding方式
给图片加上padding, 然后把原先的第一个卷积层的padding去掉. 不过我发现onnx的卷积操作是支持选中padding模式的, 具体可以参考[这里](https://github.com/onnx/onnx/blob/f2daca5e9b9315a2034da61c662d2a7ac28a9488/docs/Operators.md#Conv). 因此直接用标准的(320, 320)大小的yolo-dense网络去转onnx是完全没问题的.


第一层卷积操作是不加padding的, 这个与官方的稍有区别. 因此解析cfg的时候需要先解析出pad参数, 根据pad是否为1决定卷积的auto_pad模式.

生成onnx模型文件:

- 进入models/yolov3/目录下, 执行python3 -B onnx\_inference.py命令;

- 进入models/yolov3-tiny/目录下, 执行python3 -B onnx\_inference.py命令;

- 进入models/plate_detection(yolo-dense)/目录下, 执行python3 -B onnx\_inference.py命令;

由于yolov3.weights文件很大, github不支持上传. 有需要的可自行前往[darknet官网](https://pjreddie.com/media/files/yolov3.weights)下载.

onnx\_inference.py 文件是直接对onnx文件进行推理.

onnx2trt\_yolov3tiny.py 文件是将yolov3-tiny网络的onnx文件转成trt文件并进行推理加速. 我在Jetson Tx2平台上是测试成功的.
