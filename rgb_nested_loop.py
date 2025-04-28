#!/usr/bin/env python3
# Created by: Xiaohan
# Created on: Apr 23, 2025
# This program uses a nested loop to print out the RGB color values


def main():
    for red in range(0, 256, 15):
        for green in range(0, 256, 15):
            for blue in range(0, 256, 15):
                print(
                    "\033[38;2;{};{};{}mRGB({}, {}, {})\033[38;2;255;255;255m".format(
                        red, green, blue, red, green, blue
                    )
                )

    print("Thanks for using this program!")


if __name__ == "__main__":
    main()
