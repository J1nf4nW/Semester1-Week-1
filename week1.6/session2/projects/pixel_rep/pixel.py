# Week 1.6, Session 2
class Image:
    def _write_pgm(self, filename):
        """
        writes the Image to the specific PGM file
        """
        with open( filename, "wt") as imgfile:
            self._write_header(imgfile)
            self._write_pixels(imgfile)

    def _write_header(self, imgfile):
        print("P2", file=imgfile)
        print(self.width, self.height, file=imgfile)
        print(self.max_value, file=imgfile)

    def _write_pixels(self, imgfile):
        print(f"rows, {self.width}")
        print(f"columns, {self.height}")
        for row in range (0, self.height):
            for col in range (0, self.width):
                print(f"col{col}")
                print(f"{self.pixels[row][col]}",end = "", file = imgfile)
            print(file=imgfile)