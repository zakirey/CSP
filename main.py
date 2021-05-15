from Map import map_coloring_csp
from Zebra import zebra_problem_csp
from tkinter import *
from Heuristics import mrv, first_unassigned_variable, lcv, unordered_domain_values
from Inference import no_inference, forward_checking, ac3_caller

if __name__ == '__main__':
    root = Tk()
    root.geometry('270x480')
    root.title('CSP')

    methods = {"var_heuristics": first_unassigned_variable,
               "val_heuristics": unordered_domain_values,
               "inference": no_inference}

    var = IntVar()
    var.set(1)

    val = IntVar()
    val.set(3)

    inf = IntVar()
    inf.set(5)

    variable_heuristics = [("No Var Heuristics", 1),
                           ("Mrv", 2)]

    value_heuristics = [("No Val Heuristics", 3),
                        ("Lcv", 4)]

    inference_list = [("No Inference", 5),
                      ("Forward Checking", 6),
                      ("AC3", 7)]


    def change_choice():
        if var.get() == 1:
            methods["var_heuristics"] = first_unassigned_variable
        if var.get() == 2:
            methods["var_heuristics"] = mrv
        if val.get() == 3:
            methods["val_heuristics"] = unordered_domain_values
        if val.get() == 4:
            methods["val_heuristics"] = lcv
        if inf.get() == 5:
            methods["inference"] = no_inference
        if inf.get() == 6:
            methods["inference"] = forward_checking
        if inf.get() == 7:
            methods["inference"] = ac3_caller


    Label(root, text="""Choose Variable Heuristics""").pack()

    for heuristic, v in variable_heuristics:
        Radiobutton(root,
                    text=heuristic,
                    variable=var,
                    command=change_choice,
                    value=v).pack()

    Label(root, text="""Choose Value Heuristics""").pack()

    for heuristic, v in value_heuristics:
        Radiobutton(root,
                    text=heuristic,
                    variable=val,
                    command=change_choice,
                    value=v).pack()

    Label(root, text="""Choose Inference""").pack()

    for method, v in inference_list:
        Radiobutton(root,
                    text=method,
                    variable=inf,
                    command=change_choice,
                    value=v).pack()

    number_of_points = Label(root, text="Enter Number of points")
    number_of_points.pack()

    number_input = IntVar()
    number_input_entry = Entry(root, textvariable=number_input)
    number_input_entry.pack()

    width = Label(root, text="Enter Grid X", padx=20)
    width.pack()

    width_input = IntVar()
    width_input_entry = Entry(root, textvariable=width_input)
    width_input_entry.pack()

    height = Label(root, text="Enter Grid Y")
    height.pack()

    height_input = IntVar()
    height_input_entry = Entry(root, textvariable=height_input)
    height_input_entry.pack()

    line_distance = Label(root, text="Enter Distance")
    line_distance.pack()

    distance_input = IntVar()
    distance_input_entry = Entry(root, textvariable=distance_input)
    distance_input_entry.pack()

    button_label = Label(root).pack(side=BOTTOM)


    def map_button():
        print(methods["var_heuristics"])
        print(methods["val_heuristics"])
        print(methods["inference"])
        map_coloring_csp(number_input.get(), width_input.get(),
                         height_input.get(), distance_input.get(), var_heuristics=methods["var_heuristics"],
                         val_heuristics=methods["val_heuristics"],
                         inference=methods["inference"])


    map_start_button = Button(button_label, text="Start Map Coloring", command=map_button)
    map_start_button.pack()


    def zebra_button():
        print(methods["var_heuristics"])
        print(methods["val_heuristics"])
        print(methods["inference"])
        zebra_problem_csp(var_heuristics=methods["var_heuristics"],
                          val_heuristics=methods["val_heuristics"],
                          inference=methods["inference"])


    zebra_start_button = Button(button_label, text="Start Zebra Problem", command=zebra_button)
    zebra_start_button.pack()

    root.mainloop()
