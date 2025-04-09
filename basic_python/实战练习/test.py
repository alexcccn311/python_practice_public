# 作者：Alex
# 2024/10/26 06:51
import fluidsynth

try:
    fs = fluidsynth.Synth()
    fs.start(driver="dsound")  # 替换为你系统支持的驱动程序
    print("FluidSynth 启动成功")
except Exception as e:
    print(f"FluidSynth 启动失败: {e}")