T0 = 0.0
T1 = 0.0
min_km = 0.0
max_km = 0.0


def manageFile() -> None:
    global T0, T1, min_km, max_km
    try:
        with open('var.txt', 'r') as file:
            lines = file.readlines()
            data = {}
            for line in lines:
                key, val = line.split('=')
                data[key.strip()] = float(val.strip())

            T0 = data.get('T0', 0.0)
            T1 = data.get('T1', 0.0)
            min_km = data.get('min_km', 0.0)
            max_km = data.get('max_km', 0.0)

    except Exception as e:
        print(f'Error: {e}')
        T0, T1, min_km, max_km = 0.0, 0.0, 0.0, 0.0


def mileageInput() -> float:
    while True:
        try:
            line = input("Enter a mileage: ")
            mileage = float(line)
            if mileage < 0:
                print("Error: mileage cannot be negative.")
                continue
            return mileage
        except ValueError:
            print("Error: please enter a valid number.")


def main():
    try:
        manageFile()
        mileage = mileageInput()

        if max_km != min_km:
            mileage_norm = (mileage - min_km) / (max_km - min_km)
        else:
            mileage_norm = 0.0

        estimatePrice = T0 + (T1 * mileage_norm)

        if estimatePrice < 0:
            estimatePrice = 0.0
        print(f'Estimate price: {estimatePrice:.2f}$')

    except Exception as e:
        print(f'Error: {e}')
        return 1

    return 0


if __name__ == "__main__":
    main()
