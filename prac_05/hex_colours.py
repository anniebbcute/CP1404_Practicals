
HEX_COLOURS = {"CornflowerBlue": "#6495ed", "DarkOrchid": "#9932cc", "DodgerBlue3": "#1874cd", "gainsboro": "#dcdcdc",
               "GreenYellow": "#adff2f", "IndianRed": "#cd5c5c", "LightGoldenrodYellow": "#fafad2",
               "MediumOrchid": "#ba55d3", "moccasin": "#ffe4b5", "PapayaWhip": "#ffefd5"}

hex = input("Enter colour name: ")
while hex != "":
    if hex in HEX_COLOURS:
        print(hex, "is", HEX_COLOURS[hex])
    else:
        print("Invalid colour name.")
    hex = input("Enter colour name: ")