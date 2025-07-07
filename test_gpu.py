from RealtimeSTT import AudioToTextRecorder

# 使用GPU配置
recorder = AudioToTextRecorder(
    model="base",  # 或更大的模型
    device="cuda",  # 指定使用CUDA
    gpu_device_index=0,  # GPU设备索引
    compute_type="float16"  # 使用半精度提升性能
)