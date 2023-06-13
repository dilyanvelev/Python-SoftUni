from math import ceil


class PhotoAlbum:
    PHOTOS_ON_A_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / PhotoAlbum.PHOTOS_ON_A_PAGE))

    def add_photo(self, label):
        for page in range(len(self.photos)):
            if len(self.photos[page]) < PhotoAlbum.PHOTOS_ON_A_PAGE:
                self.photos[page].append(label)

                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"
        return "No more free slots"

    def display(self):
        result = ["-" * 11]

        for page in self.photos:
            result.append(("[] " * len(page)).rstrip())
            result.append("-" * 11)

            return "\n".join(result)