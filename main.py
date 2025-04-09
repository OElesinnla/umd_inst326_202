import model, view

def main():
    adder = model.Adder()
    val = 0

    while True:
        view.render(val)
        adder.prompt()
        val = adder.get_sum()

if __name__ == '__main__':
    main()