from kps_tehdas import KPSTehdas


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        if vastaus in ["a", "b", "c"]:
            peli = KPSTehdas.luo_peli(vastaus)
            peli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
