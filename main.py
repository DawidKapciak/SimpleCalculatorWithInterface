import PySimpleGUI as Sg


class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def add(__num1: float, __num2: float):
        return __num1 + __num2

    @staticmethod
    def multiply(__num1: float, __num2: float):
        return __num1 * __num2

    @staticmethod
    def subtraction(__num1: float, __num2: float):
        return __num1 - __num2

    @staticmethod
    def divide(__num1: float, __num2: float):
        return __num1 / __num2

    @staticmethod
    def operations(window_gui: Sg.Window):
        sign = ''
        num1 = None
        num2 = None
        first_iteration = True
        ready_to_calculate = False
        result = ''
        while True:
            event, values = window_gui.read()
            if event == Sg.WIN_CLOSED:
                break
            else:
                if event in ["+", "-", "/", "×"]:
                    if values['-input-'] != '':
                        num1 = float(values['-input-'])
                    else:
                        num1 = 0
                    result = ''
                    first_iteration = False

                elif event == "C":
                    result = ''
                    first_iteration = True

                elif event == "=":
                    if ready_to_calculate:
                        if sign == "+":
                            result = str(calc.add(float(num1), float(num2)))

                        if sign == "/":
                            if num2 == 0:
                                result = "Divided by 0"
                            else:
                                result = str(calc.divide(float(num1), float(num2)))
                        if sign == "-":
                            result = str(calc.subtraction(float(num1), float(num2)))
                        if sign == "×":
                            result = str(calc.multiply(float(num1), float(num2)))

                else:
                    if values['-input-'] in ["0", ''] and event == "0":
                        result = ''
                    else:
                        result = values['-input-'] + str(event)
                        if not first_iteration:
                            num2 = float(result)
                            ready_to_calculate = True

            if event in ["+", "-", "/", "×"] and num1 is not None:
                sign = event
            window_gui['-input-'].update(result)


class Window:

    def __init__(self):
        Sg.theme('Dark Amber')
        font = ("Arial", 40)
        size = (3, 1)
        col_interior = [

            [Sg.Input(size=(100, 100), font=font, key='-input-', do_not_clear=False)],

            [Sg.Push(), Sg.Button("7", font=font, size=size),
             Sg.Button("8", font=font, size=size),
             Sg.Button("9", font=font, size=size),
             Sg.Button("+", font=font, size=size)],

            [Sg.Push(), Sg.Button("4", font=font, size=size),
             Sg.Button("5", font=font, size=size),
             Sg.Button("6", font=font, size=size),
             Sg.Button("×", font=font, size=size)],

            [Sg.Push(), Sg.Button("1", font=font, size=size),
             Sg.Button("2", font=font, size=size),
             Sg.Button("3", font=font, size=size),
             Sg.Button("-", font=font, size=size)],

            [Sg.Push(), Sg.Button("C", font=font, size=size),
             Sg.Button("0", font=font, size=size),
             Sg.Button("=", font=font, size=size, button_color="Red"),
             Sg.Button("/", font=font, size=size)],

        ]

        window_gui = Sg.Window("Calculator", col_interior, size=(475, 525), resizable=True, finalize=True)
        Calculator.operations(window_gui)
        window_gui.close()


if __name__ == '__main__':
    calc = Calculator()
    window = Window()
