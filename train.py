import matplotlib.pyplot as plt


def visuals_bonus(kms, prices, T0, T1, min_km, max_km) -> None:
    try:
        # All values
        plt.scatter(kms, prices, color='dodgerblue', label='Données')

        # Draw a line
        price_at_min = T0 + (T1 * 0.0)
        price_at_max = T0 + (T1 * 1.0)
        plt.plot([min_km, max_km], [price_at_min, price_at_max],
                 color='orchid', linewidth=2, label='Prédiction')

        # Setup graph
        plt.title('Car Prices vs Mileage')
        plt.xlabel('Mileage (km)')
        plt.ylabel('Price ($)')
        plt.legend()
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


def accuracy_bonus(T0, T1, kms_norm, prices, m) -> None:
    average_price = sum(prices) / len(prices)

    # R² = 1 - (Somme des résidus au carré / Somme totale au carré)
    s_res = 0.0
    s_total = 0.0

    for i in range(m):
        prediction = T0 + (T1 * kms_norm[i])
        s_res += (prices[i] - prediction) ** 2
        s_total += (prices[i] - average_price) ** 2

    r2 = 1 - (s_res / s_total)

    print(f'Program accuracy: {r2 * 100:.0f}%')


def readCSV():
    kms = []
    prices = []

    try:
        with open('data.csv', 'r') as file:
            next(file)
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    kms.append(float(parts[0]))
                    prices.append(float(parts[1]))
        return kms, prices

    except Exception as e:
        print(f"Error reading csv: {e}")
        return [], []


def main():
    try:
        kms, prices = readCSV()
        if not kms or not prices:
            print("Error: No data to train on.")
            return

        # Normalisation
        min_km = min(kms)
        max_km = max(kms)
        kms_norm = [(x - min_km) / (max_km - min_km) for x in kms]

        # Settings
        T0, T1 = 0.0, 0.0
        learningRate = 0.1
        iterations = 1000
        m = len(kms_norm)

        # Algo
        for _ in range(iterations):
            sum_error0 = 0.0
            sum_error1 = 0.0

            for i in range(m):
                prediction = T0 + (T1 * kms_norm[i])
                error = prediction - prices[i]
                sum_error0 += error
                sum_error1 += error * kms_norm[i]

            T0 -= (learningRate / m) * sum_error0
            T1 -= (learningRate / m) * sum_error1

        # Save values
        with open('var.txt', 'w') as f:
            f.write(f"T0 = {T0}\n")
            f.write(f"T1 = {T1}\n")
            f.write(f"min_km = {min_km}\n")
            f.write(f"max_km = {max_km}\n")

        # Bonus
        accuracy_bonus(T0, T1, kms_norm, prices, m)
        visuals_bonus(kms, prices, T0, T1, min_km, max_km)

    except Exception as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    main()
