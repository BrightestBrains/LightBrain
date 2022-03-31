### Micropython

Over time, I have chosen for myself the best way to use micropython. It may not seem very convenient, but it is by far the most stable and consistent way to check code, to write a simple program.

I'm choosing [UPIOT](https://github.com/gepd/uPiotMicroPythonTool), Sublime plugin to develop with micropython. For all the details and more precise instructions, see the add-on's github.

MICROPYTHON INSTRUCTION:

1. Sublime — Package Package Control > Add Repository
2. Add Repository: https://rawgit.com/gepd/uPiot-MicroPython-Tool/master/repository.json
3. Package Control: Install Package > UPIOT
4. UPIOT: Download Firmware > esp32 > Put path to bin file and make sure that the link contains "http", not "https" (!)
5. UPIOT: Burn Firmware > esp32 > *.bin
6. It is better to erase the memory, respectively "press buttons" (EN + BOOT) - esptool will be waiting
7. UPIOT: Open Console (or in any other terminal)
8. UPIOT: Put Current File — main.py will start immediately after a reboot

Tips:
CTRL+SHIFT+P — fast menu for sublime.\
See the [Micropython](https://docs.micropython.org/en) documentation for more details. 