# 2024-01-21T14:34:49.594542400
import vitis

client = vitis.create_client()
client.set_workspace(path="C:/Users/xjh/WorkSpace/CoDesign")

platform = client.create_platform_component(name = "platform",hw = "C:/Users/xjh/WorkSpace/CoDesign/hardware/design_1_wrapper.xsa",os = "standalone",cpu = "microblaze_0")

platform = client.get_platform_component(name="platform")
status = platform.build()

comp = client.get_component(name="xgpio_example")
comp.build()

comp.build()

