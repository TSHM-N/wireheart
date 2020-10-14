import random
from string import ascii_letters
from collections import deque
from copy import deepcopy
from math import ceil

ALPHABET_ASCII = [char for char in ascii_letters]
ALPHABET_ASCII.extend([" ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
ALPHABET_ASCII = deque(ALPHABET_ASCII)
ALPHABET_WIREHEART = deque(["ˤ", "‽", "ӻ", "ȣ", "฿", "΅", "ē", "⫌", "Ⴤ", "ϫ", "ȵ", "α", "β", "δ", "ɲ", "ʬ", "⤭",
							"Ք", "ʩ", "∝", "ಸ", "æ", "ɨ", "ъ", "מ", "ཪ", "λ", "ֆ", "ͼ", "˥", "ȿ", "ɏ", "ɂ", "⤽",
							"Ѷ", "ԙ", "ҽ", "ϻ", "ˢ", "ϗ", "ǝ", "ץ", "⪓", "҂", "ी", "৬", "౫", "໑", "༅", "໒", "⦼",
							"æ", "↊", "⧥", "༒", "༬", "࿐", "ᄋ", "ኦ", "᎙", "Ꭿ", "Ω", "θ", "σ", "ρ", "τ", "χ",
							"ι", "π", "ς", "ʨ", "⧤", "⧎", "⥈", "∳", "փ", "ʭ"])


def encrypt(message: str):
	encrypted_message_raw = []
	wire = (random.randint(0, 9), random.randint(0, 9))

	wire_split = []
	for num in wire:
		wire_split.extend([int(x) for x in str(num)])
	print(wire)

	wire_string = ""
	for digit in wire_split:
		wire_string += "".join([ALPHABET_WIREHEART[ALPHABET_ASCII.index(str(digit))]])

	shift_value = wire[0] * wire[1]
	shifted_alphabet = deepcopy(ALPHABET_WIREHEART)
	shifted_alphabet.rotate(shift_value)

	for letter in message:
		try:
			encrypted_message_raw.append(shifted_alphabet[ALPHABET_ASCII.index(letter)])
		except ValueError:
			encrypted_message_raw.append(letter)

	encrypted_message_raw = [item for sublist in encrypted_message_raw for item in sublist]
	encrypted_message_raw.insert(ceil(len(encrypted_message_raw) / 2), wire_string)
	encrypted_message = "".join(encrypted_message_raw)

	return encrypted_message


def decrypt(message: str):
	encrypted_wire = (message[ceil(len(message) / 2) - 1], message[ceil(len(message) / 2)])
	wire = ()
	for letter in encrypted_wire:
		wire += tuple(ALPHABET_ASCII[ALPHABET_WIREHEART.index(letter)])
	wireless_message = message[0:ceil(len(message) / 2) - 1:] + message[ceil(len(message) / 2) + 1::]

	shift_value = int(wire[0]) * int(wire[1])
	temp = deepcopy(ALPHABET_WIREHEART)
	temp.rotate(shift_value)
	shifted_alphabet = temp

	decrypted_message = ""

	for letter in wireless_message:
		try:
			decrypted_message += ALPHABET_ASCII[shifted_alphabet.index(letter)]
		except ValueError:
			decrypted_message += letter
	return decrypted_message


if __name__ == "__main__":
	while True:
		enc = encrypt(input())
		print(enc)
		print(decrypt(enc))
