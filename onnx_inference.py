import time
import onnx
import numpy as np
import onnxruntime


sess = onnxruntime.InferenceSession('onnx/yolov3-tiny.onnx')
first_input_name = sess.get_inputs()[0].name
first_output_name = sess.get_outputs()[0].name
second_output_name = sess.get_outputs()[1].name

input_tensor = np.random.rand(1, 3, 416, 416).astype(np.float32)
for i in range(100):
    t1 = time.time()
    results = sess.run([first_output_name, second_output_name], {first_input_name: input_tensor})
    t2 = time.time()
    print('inference cost: ', (t2-t1)*1000, 'ms')

print(results[0].shape)
print(results[1].shape)
