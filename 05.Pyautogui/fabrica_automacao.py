import pyautogui

pyautogui.press("win")
pyautogui.sleep(0.5)
pyautogui.write("Google Chrome", interval=0.1)
pyautogui.press("enter")
pyautogui.sleep(2)

pyautogui.write("https://prefeitura.santanadeparnaiba.sp.gov.br/Plataforma/smti/fabrica-de-programadores")
pyautogui.press("enter") 
pyautogui.sleep(1)

pyautogui.press("printscreen")
pyautogui.sleep(1)
pyautogui.mouseDown(10, 10)
pyautogui.moveTo(1910, 1070, duration=1)
pyautogui.mouseUp()