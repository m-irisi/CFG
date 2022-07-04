import requests
import tkinter as tk
import webbrowser  # opens the link on internet

# functions:
def callback(url):
    webbrowser.open_new_tab(url)

def get_recipes():
    ingredient = searchbox.get()
    app_id = 'dd0a9504'
    app_key = '03de3442e25326b7910a0458023088ca'
    look_up = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)
    )

    data = look_up.json()
    results = data['hits']

    for result in results:
        recipe = result['recipe']
        recipe_name = recipe['label']
        recipe_link = recipe['uri']
        results_box.insert('1.0', "{} \n {} \n \n ".format(recipe_name, recipe_link))


# form and appearance:
form = tk.Tk()  # create the form
form.configure(bg='#bde7ff')    # colour of form
form.title("Recipe search: ")

# elements of form:
label = tk.Label(form, text="Enter ingredient or recipe name: ")
searchbox = tk.Entry(form, relief="flat")
searchbutton = tk.Button(form, text="search", command=get_recipes)
results_box = tk.Text(form)

c1 = tk.Checkbutton(form, text="Vegetarian")
c2 = tk.Checkbutton(form, text="Vegan")
c3 = tk.Checkbutton(form, text="Gluten free")

# layout of form:
c1.grid(row=1, column=0)
c2.grid(row=1, column=1)
c3.grid(row=1, column=2)

label.grid(row=2, column=0, padx=15, pady=15)
searchbox.grid(row=2, column=1, columnspan=5, padx=15, pady=15)
searchbutton.grid(row=2, column=6, padx=15, pady=15)
results_box.grid(row=3, column=1, padx=15, pady=15)

form.mainloop()  # keeps the form from disappearing
