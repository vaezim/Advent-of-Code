from string import ascii_lowercase as letters

def RoomChecker(room: str):
    tokens = room.split('-')
    checksum = tokens[-1][tokens[-1].index('[')+1:-1]
    room_id = int(tokens[-1][:tokens[-1].index('[')])
    IS_NORTHPOLE = False

    alpha_stats = {}
    for t in tokens[:-1]:
        for c in t:
            if alpha_stats.get(c) == None:
                alpha_stats[c] = 0
            alpha_stats[c] += 1

    top_alphas = list(alpha_stats.keys())
    top_alphas.sort() # alphabetically
    top_alphas.sort(key=lambda x: alpha_stats[x], reverse=True) # repetition

    calc_checksum = ''.join(top_alphas[:5])
    deciphered = ShiftCipher('-'.join(tokens[:-1]), room_id)

    if (deciphered == "northpole object storage"):
        IS_NORTHPOLE = True

    return (calc_checksum == checksum) * room_id, IS_NORTHPOLE

def ShiftCipher(room: str, room_id: int):
    deciphered = list(room)
    room_id = room_id % 26
    for i in range(len(deciphered)):
        if deciphered[i] == '-':
            deciphered[i] = ' '
            continue
        deciphered[i] = letters[(letters.index(deciphered[i]) + room_id) % 26]
    return ''.join(deciphered)

if __name__ == "__main__":
    room = "not-a-real-room-404[oarel]"
    print(RoomChecker(room))
    print(ShiftCipher("qzmt-zixmtkozy-ivhz", 343))
    