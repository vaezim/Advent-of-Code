
class Decompressor:

    def Decompress(self, text):
        i = 0
        decompressed_text = ""
        while i < len(text):
            if text[i] == '(':
                marker = ""
                i += 1
                while text[i] != ')':
                    marker += text[i]
                    i += 1
                i += 1  # character after the ')'
                length, repeats = int(marker.split('x')[0]), int(marker.split('x')[1])
                decompressed_text += (text[i:i+length] * repeats)
                i += length
            else:
                decompressed_text += text[i]
                i += 1
        return decompressed_text

    def Decompress2Len(self, text):
        i = 0
        total_len = 0
        while i < len(text):
            if text[i] == '(':
                j = i
                while text[j] != ')':
                    j += 1
                length, repeats = int(text[i+1:j].split('x')[0]), int(text[i+1:j].split('x')[1])
                total_len += repeats * self.Decompress2Len(text[j+1:j+length+1])
                i = (j + length+1)
            else:
                total_len += 1
                i += 1
        return total_len


if __name__ == "__main__":
    decomp = Decompressor()
    print(decomp.Decompress2Len("(3x3)XYZ"))
    print(decomp.Decompress2Len("X(8x2)(3x3)ABCY"))
    print(decomp.Decompress2Len("(27x12)(20x12)(13x14)(7x10)(1x12)A"))
    print(decomp.Decompress2Len("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"))
