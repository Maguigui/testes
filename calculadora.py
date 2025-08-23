import pyautogui

pyautogui.hotkey("win","r")
pyautogui.sleep(1)

pyautogui.write("calc", interval=0.1)
pyautogui.press("enter")
pyautogui.sleep(1)

pyautogui.write("20", interval=0.2)
pyautogui.press("+")
pyautogui.write("20", interval=0.2)
pyautogui.press("enter")

pyautogui.alert("Operação concluída! Verifique o resultado na calculadora.")
