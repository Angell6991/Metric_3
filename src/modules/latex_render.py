import matplotlib.pyplot as plt

###-----------------def_function------------------###
def LaTeX(text_latex, dir_save, color):
    
    plt.rcParams['mathtext.fontset'] = 'cm'
    fig, ax = plt.subplots(figsize=(6,3))
    ax.text(
        0.5, 
        0.5, 
        f"${text_latex}$", 
        fontsize=200, 
        ha='center', 
        va='center', 
        color=color
    )
    ax.axis('off')

    plt.savefig(f"{dir_save}.png", dpi=600, bbox_inches='tight', transparent=True)
    plt.close()

###--------------texting_function-----------------###
# LaTeX("g_{\\alpha \\mu}", "save", "#000000")
